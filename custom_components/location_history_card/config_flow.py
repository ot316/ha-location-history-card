"""Config flow for the Location History Card integration."""

from typing import Any

from homeassistant.components.lovelace import LOVELACE_DATA, MODE_STORAGE
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN, NAME


class LocationHistoryCardConfigFlow(ConfigFlow, domain=DOMAIN):
    """Install the Lovelace resource from Devices & Services."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Confirm installation in a dashboard with storage-managed resources."""
        if self.hass.data[LOVELACE_DATA].resource_mode != MODE_STORAGE:
            return self.async_abort(reason="yaml_resources")
        if user_input is not None:
            return self.async_create_entry(title=NAME, data={})
        return self.async_show_form(step_id="user")
