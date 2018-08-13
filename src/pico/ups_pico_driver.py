import smbus
from time import sleep


pico = smbus.SMBus(1)

def bcd_word_to_dec(bcd_w):
  a = format(bcd_w, '016b')
  b = [int(a[i:i+4], 2) for i in range(0, len(a), 4)]
  return int("%d%d%d%d" % tuple(b))  

def trigger_hard_reset():
  pico.write_byte_data(0x6b, 0x05, 0x00)
  
def set_hard_reset_timer(secs):
  pico.write_byte_data(0x6b, 0x05, secs)
  
def get_hard_reset_timer():
  return pico.read_byte_data(0x6b, 0x05)
  
def disable_hard_reset_timer():
  pico.write_byte_data(0x6b, 0x05, 0xff)
    
def set_battery_timer(mins):
  pico.write_byte_data(0x6b, 0x01, mins)
  
def get_battery_timer():
  return pico.read_byte_data(0x6b, 0x01)
  
def disable_battery_timer():
  pico.write_byte_data(0x6b, 0x01, 0xff)

def disable_buzzer():
  pico.write_byte_data(0x6b, 0x6d, 0x00)
  
def enable_buzzer():
  pico.write_byte_data(0x6b, 0x6d, 0x01)

def set_buzzer_freq(freq):
  pico.write_byte_data(0x6b, 0x0e, freq)
  
def set_buzzer_duration(duration):
  pico.write_byte_data(0x6b, 0x10, duration)
  
def file_safe_shutdown():
  pico.write_byte_data(0x6b, 0x00, 0xcc)
  
def reset_factory_defaults():
  pico.write_byte_data(0x6b, 0x00, 0xdd)
  
def reset_pico_cpu():
  pico.write_byte_data(0x6b, 0x00, 0xee)
  
def reset_factory_defaults():
  pico.write_byte_data(0x6b, 0x00, 0xdd)

def get_temperature():
  return pico.read_byte_data(0x69, 0x1C)
  
def get_power_source():
  res = pico.read_byte_data(0x69, 0x00)
  return ("external" if res == 0x01 else "internal")  

def get_charger_status():
  res = pico.read_byte_data(0x69, 0x20)
  return res == 0x01
  #return ("charging" if res == 0x01 else "discharging")

def get_working_status():
  _a = pico.read_byte_data(0x69, 0x22)
  sleep(0.01)
  _b = pico.read_byte_data(0x69, 0x22)
  return ("working" if (_b > _a) else "crashed")

def set_orange_led(on):
  pico.write_byte_data(0x6b, 0x09, on)
  
def set_green_led(on):
  pico.write_byte_data(0x6b, 0x0A, on)
  
def set_blue_led(on):
  pico.write_byte_data(0x6b, 0x0B, on)

def get_ext_voltage():
  res = pico.read_word_data(0x69, 0x0c)
  return bcd_word_to_dec(res)/100.0
  
def get_bat_voltage():
  res = pico.read_word_data(0x69, 0x08)
  return bcd_word_to_dec(res)/100.0
  
def get_rpi_voltage():
  res = pico.read_word_data(0x69, 0x0a)
  return bcd_word_to_dec(res)/100.0


if __name__ == "__main__":
  print "Status: %s" % get_working_status()
  print "Temperature: %s" % get_temperature()
  print "Source: %s" % get_power_source()
  print "Charging: %s" % ("charging" if get_charger_status() else "discharging")
  print "External voltage: %.02f" % get_ext_voltage()
  print "Battery voltage: %.02f" % get_bat_voltage()
  print "Raspberry voltage: %.02f" % get_rpi_voltage()

  enable_buzzer()
  set_buzzer_freq(1000)
  #set_buzzer_duration(10)
  #print get_battery_timer()
  set_battery_timer(4)
