from microbit import *

# function to read data file:
def get_nv_data(name):
    try:
        with open(name) as f:
            v = int(f.read())
    except OSError:
        v = temperature()
        try:
            with open(name, 'w') as f:
                f.write(str(v))
        except OSError:
            display.scroll('Cannot create file %s' % name)

    except ValueError:
        display.scroll('invalid data in file %s' % name)
        v = temperature()

    return v

# function to write data file:
def set_nv_data(name, value):
    try:
        with open(name, 'w') as f:
            f.write(str(value))
    except OSError:
        display.scroll('Cannot write to file %s' % name)

min = get_nv_data('min.txt')
max = get_nv_data('max.txt')

while True:
    currentTemp = temperature()
    if currentTemp < min:
        min = currentTemp
        set_nv_data('min.txt', min)
    if currentTemp > max:
        max = currentTemp
        set_nv_data('max.txt', max)
    if accelerometer.was_gesture('shake'):
        display.scroll(currentTemp)
    if button_a.was_pressed():
        display.scroll(get_nv_data('min.txt'))
    if button_b.was_pressed():
        display.scroll(get_nv_data('max.txt'))
    if pin2.is_touched():
        display.scroll('clearing data')
        set_nv_data('min.txt', currentTemp)
        set_nv_data('max.txt', currentTemp)
