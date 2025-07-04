from homeassistant.helpers.entity import Entity
from .const import DOMAIN
import logging

_LOGGER = logging.getLogger(__name__)

class MSpaEntity(Entity):
    def __init__(self, coordinator):
        self.coordinator = coordinator

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "mspa_hottub")},
            "name": "MSpa Hot Tub",
            "manufacturer": "MSpa",
            "model": getattr(self.coordinator, "product_id", None),
            "sw_version": "1.0.0",
        }