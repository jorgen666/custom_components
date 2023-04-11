import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, text_sensor, uart
from esphome.const import (CONF_ID,
        CONF_DIRECTION,
        ICON_WEATHER_WINDY,
        ICON_SIGN_DIRECTION,
        UNIT_DEGREES,
        DEVICE_CLASS_WIND_SPEED,
        DEVICE_CLASS_EMPTY
        )
from . import windsonic_ns, WindsonicComponent, CONF_WINDSONIC_ID

# sensors
CONF_WIND_SPEED = "wind_speed"
CONF_WIND_DIRECTION_DEGREES = "wind_direction_degrees"


# text sensors
CONF_NMEA_TEXT = "nmea_text"

UNIT_METER_PER_SECOND = "m/s"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_WINDSONIC_ID): cv.use_id(WindsonicComponent),
    cv.Optional(CONF_WIND_SPEED): sensor.sensor_schema(
        unit_of_measurement=UNIT_METER_PER_SECOND,
        icon=ICON_WEATHER_WINDY,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_WIND_SPEED
    ),
    cv.Optional(CONF_WIND_DIRECTION_DEGREES): sensor.sensor_schema(
        unit_of_measurement=UNIT_DEGREES,
        icon=ICON_SIGN_DIRECTION,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_EMPTY
    ),
    cv.Optional(CONF_NMEA_TEXT): text_sensor.TEXT_SENSOR_SCHEMA.extend({cv.GenerateID(): cv.declare_id(text_sensor.TextSensor)}),
})

async def to_code(config):
    windsonic = await cg.get_variable(config[CONF_WINDSONIC_ID])

    if CONF_WIND_SPEED in config:
        sens = await sensor.new_sensor(config[CONF_WIND_SPEED])
        cg.add(windsonic.set_wind_speed_sensor(sens))

    if CONF_WIND_DIRECTION_DEGREES in config:
        sens = await sensor.new_sensor(config[CONF_WIND_DIRECTION_DEGREES])
        cg.add(windsonic.set_wind_direction_degrees_sensor(sens))
      

    if CONF_NMEA_TEXT in config:
        conf = config[CONF_NMEA_TEXT]
        sens = cg.new_Pvariable(conf[CONF_ID])
        await text_sensor.register_text_sensor(sens, conf)
        cg.add(windsonic.set_nmea_text_sensor(sens))

    