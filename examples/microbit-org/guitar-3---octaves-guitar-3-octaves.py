from microbit import *
import music
F = 349
A = 440
C = 523
E = 659

while True:
    if pin1.is_touched():
        music.pitch(int(F), 500)
        music.pitch(int(A), 500)
        music.pitch(int(C), 500)
    if pin2.is_touched():
        music.pitch(int(A), 500)
        music.pitch(int(C), 500)
        music.pitch(int(E), 500)
    if button_a.was_pressed():
        F = F / 2
        A = A / 2
        C = C / 2
        E = E / 2
    if button_b.was_pressed():
        F = F * 2
        A = A * 2
        C = C * 2
        E = E * 2
        