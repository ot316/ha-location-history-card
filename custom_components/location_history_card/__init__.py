"""Serve the Location History Card and maintain its Lovelace resource."""

from hashlib import sha256
from pathlib import Path

from homeassistant.components.http import StaticPathConfig
from homeassistant.components.lovelace import LOVELACE_DATA, MODE_STORAGE
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

_CARD_PATH = "/location_history_card/location-history-card.js"
_LEGACY_PATH = "/local/location-history-card.js"
_CARD_FILE = Path(__file__).parent / "frontend" / "location-history-card.js"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Register the bundled JavaScript once per HA process."""
    await hass.http.async_register_static_paths(
        [StaticPathConfig(_CARD_PATH, str(_CARD_FILE), cache_headers=True)]
    )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Create the module resource or migrate the original local card URL."""
    lovelace = hass.data[LOVELACE_DATA]
    if lovelace.resource_mode != MODE_STORAGE:
        raise ConfigEntryError(
            translation_domain=DOMAIN, translation_key="yaml_resources"
        )

    asset = await hass.async_add_executor_job(_CARD_FILE.read_bytes)
    url = f"{_CARD_PATH}?v={sha256(asset).hexdigest()[:12]}"
    resources = lovelace.resources
    await resources.async_get_info()
    items = {item["url"].partition("?")[0]: item for item in resources.async_items()}
    resource = items.get(_CARD_PATH)
    if resource is None:
        legacy = items.get(_LEGACY_PATH)
        if legacy is not None and legacy["type"] == "module":
            resource = legacy

    if resource is None:
        await resources.async_create_item({"res_type": "module", "url": url})
    elif resource["url"] != url or resource["type"] != "module":
        await resources.async_update_item(
            resource["id"], {"res_type": "module", "url": url}
        )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Keep the published resource available during an integration reload."""
    return True


async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Remove the integration's Lovelace module when uninstalled."""
    lovelace = hass.data[LOVELACE_DATA]
    if lovelace.resource_mode != MODE_STORAGE:
        return

    resources = lovelace.resources
    await resources.async_get_info()
    for item in list(resources.async_items()):
        if item["url"].partition("?")[0] == _CARD_PATH:
            await resources.async_delete_item(item["id"])
