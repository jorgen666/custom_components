#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace windsonic {

class WindsonicComponent : public uart::UARTDevice, public Component {
 public:
   void set_wind_speed_sensor(sensor::Sensor *wind_speed_sensor) { wind_speed_sensor_ = wind_speed_sensor; }
   void set_wind_direction_degrees_sensor(sensor::Sensor *wind_direction_degrees_sensor) { wind_direction_degrees_sensor_ = wind_direction_degrees_sensor; }
  
   void set_nmea_text_sensor(text_sensor::TextSensor *nmea_text_sensor) { nmea_text_sensor_ = nmea_text_sensor; }
  

  void dump_config() override;
  void loop() override;

  float get_setup_priority() const { return setup_priority::DATA; }

 protected:
  void handle_value_(uint8_t c);
  std::vector<uint8_t> rx_message_;

  sensor::Sensor *wind_speed_sensor_{nullptr};
  sensor::Sensor *wind_direction_degrees_sensor_{nullptr};
  

  text_sensor::TextSensor *nmea_text_sensor_{nullptr};
  

  int state_{0};
  std::string label_;
  std::string value_;
  uint32_t last_transmission_{0};
};

}  // namespace Windsonic
}  // namespace esphome