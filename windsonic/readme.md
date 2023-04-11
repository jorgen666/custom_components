a component to read Gill Instruments Windsonic sensor


```
YAML:

uart:
  id: wind
  tx_pin: 0
  rx_pin: 1
  baud_rate: 19200    


windsonic:
  uart_id: wind

sensor:
  - platform: windsonic
    wind_speed:
      id: ws
    wind_direction_degrees:
      id: wd
    nmea_text:
      id: nm
```
