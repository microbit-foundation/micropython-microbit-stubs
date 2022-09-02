from microbit import *

# Not the real CHIRP/WARBLE, just placeholders so we can
# maintain the test code below more or less as per the
# docs.
CHIRP = audio.SoundEffect(
    "110232570087411440044008880352005901003300010000000000000000010000000000"
)
WARBLE = audio.SoundEffect(
    "110232570087411440044008880352005901003300010000000000000000010000000000"
)
CLICK = audio.SoundEffect(
    "110232570087411440044008880352005901003300010000000000000000010000000000"
)

# Play a built in Sound Effect
audio.play(CHIRP)

# Create a Sound Effect and immediately play it
audio.play(
    audio.SoundEffect(
        freq_start=400,
        freq_end=2000,
        duration=500,
        vol_start=100,
        vol_end=255,
        wave=audio.SoundEffect.WAVE_TRIANGLE,
        fx=audio.SoundEffect.FX_VIBRATO,
        shape=audio.SoundEffect.SHAPE_LOG,
    )
)

# Play a Sound Effect instance, modify an attribute, and play it again
my_effect = audio.SoundEffect(
    preset=CHIRP,
    freq_start=400,
    freq_end=2000,
)
audio.play(my_effect)
my_effect.duration = 1000
audio.play(my_effect)

# You can also create a new effect based on an existing one, and modify
# any of its characteristics via arguments
audio.play(WARBLE)
my_modified_effect = audio.SoundEffect(WARBLE, duration=1000)
audio.play(my_modified_effect)

# Use sensor data to modify and play the existing Sound Effect instance
while True:
    my_effect.freq_start = accelerometer.get_x()
    my_effect.freq_end = accelerometer.get_y()
    audio.play(my_effect)

    if button_a.is_pressed():
        # On button A play an effect and once it's done show an image
        audio.play(CHIRP)
        display.show(Image.DUCK)
        sleep(500)
    elif button_b.is_pressed():
        # On button B play an effect while showing an image
        audio.play(CLICK, wait=False)
        display.show(Image.SQUARE)
        sleep(500)
