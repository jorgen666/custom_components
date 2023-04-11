import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.components import uart
#from esphome.components import text_sensor
from esphome.const import CONF_ID, CONF_STATE

DEPENDENCIES = ['uart']
AUTO_LOAD = ['sensor', 'text_sensor']

windsonic_ns = cg.esphome_ns.namespace('windsonic')
WindsonicComponent = windsonic_ns.class_('WindsonicComponent', uart.UARTDevice, cg.Component)

CONF_WINDSONIC_ID = "windsonic_id"


CONFIG_SCHEMA = uart.UART_DEVICE_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(WindsonicComponent),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
