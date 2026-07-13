from homeassistant.helpers.update_coordinator import CoordinatorEntity


class PanelEntity(CoordinatorEntity):

    def __init__(self, coordinator):

        super().__init__(coordinator)

        self._attr_has_entity_name = True