#include "windsonic.h"
#include "esphome/core/log.h"

namespace esphome {
namespace windsonic {

static const char *TAG = "windsonic";

void WindsonicComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "Windsonic:");
  LOG_SENSOR("  ", "Wind Speed", wind_speed_sensor_);
  LOG_SENSOR("  ", "Wind Direction Degrees", wind_direction_degrees_sensor_);
  
  LOG_TEXT_SENSOR("  ", "NMEA Text", nmea_text_sensor_);
  check_uart_settings(19200);
}

void WindsonicComponent::loop() {
 while (this->available()) {
    uint8_t c;
    this->read_byte(&c);
    this->handle_value_(c);
  }
}


void WindsonicComponent::handle_value_(uint8_t c) {
 if (c == '\r')
    return;
  if (c == '\n') {
    std::string s(this->rx_message_.begin(), this->rx_message_.end());
    std::string r = s.substr(7, 10);
    std::string a = s.substr(13, 19);
    float winddirection = std::stof(r);
    float windspeed = std::stof(a);
    wind_direction_degrees_sensor_->publish_state(winddirection);
    wind_speed_sensor_->publish_state(windspeed);
	nmea_text_sensor_->publish_state(s);
    this->rx_message_.clear();
	r = "";
    s = "";
    return;
  }
  this->rx_message_.push_back(c);

}

}  // namespace windsonic
}  // namespace esphome