from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, VERSION
from .entity import PanelEntity


async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            PanelSensor(coordinator, entry),
        ]
    )


class PanelSensor(PanelEntity, SensorEntity):

    def __init__(self, coordinator, entry):

        super().__init__(coordinator)

        self._entry = entry

        self._attr_unique_id = entry.entry_id

        self._attr_name = entry.title

        self._attr_icon = "mdi:tablet-dashboard"

    @property
    def native_value(self):

        return "OK"

    @property
    def device_info(self):

        return DeviceInfo(
            identifiers={
                (DOMAIN, self._entry.entry_id)
            },
            name=self._entry.title,
            manufacturer="Panel Hub",
            model="ESP Panel",
            sw_version=VERSION,
        )

    @property
    def extra_state_attributes(self):

        return {
            "library_version": VERSION,
        }