import lab2_hardware_light_sensor_emu.py

led = False

while True:
    sunlight = lab_2_hardware_light_sensor_emu.lightinput()
    if sunlight == False:
        led = True
    else:
        led = False
