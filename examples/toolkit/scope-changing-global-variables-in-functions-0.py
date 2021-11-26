def clicker():
    global count
    count += 1
    display.show(count)

count = 0
while True:
    if button_a.was_pressed():
        clicker()