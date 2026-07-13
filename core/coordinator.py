from datetime import timedelta

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class PanelCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, entry):

        super().__init__(
            hass,
            logger=None,
            name="panel_hub",
            update_interval=timedelta(seconds=5),
        )

        self.entry = entry

    async def _async_update_data(self):

        return {}