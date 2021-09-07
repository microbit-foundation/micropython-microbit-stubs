# Notes

These are working notes on discrepancies found when creating these stubs.

## Cross-cutting issues

Module docs throughout are a bit arbitrary and need review.

## Module-specific issues

## gc

isenabled is undocumented (not added).

## audio

AudioFrame.copyfrom is undocumented (not added).

AudioFrame implements some operations that aren't clearly documented (e.g. you can add them, multiple by an integer).

### uart

uart.readinto is misindented
there's a method documented as having been removed so I've omitted it from the stubs

### microbit

- image - type of buffer in second __init__ option
- text modified to split across __init__ definitions
- "Same as" language is unhelpful.
- __sub__ and __div__ added based on examples but not in docs.
- microphone - the doc style here is a bit different to elsewhere, might be less good in Pyright?

## micropython

- opt_level has @overload with split docs
- micropython.schedule is missing from our docs. Why? It is on the device (checked on V2).

## neopixel

Has long but important module docstring with important warnings for the user.
I've removed the images and reproduced it otherwise in full.

Some complication with write/show. Fine for stubs but will need revisiting for docs.

ws2812_write is undocumented (here and in microbit module)
ORDER is undocumented

### pins

get_analog_period_microseconds isn't documented

pin_logo isn't really a pin... it just has:
		CAPACITIVE
		RESISTIVE
		is_touched
		set_touch_mode
how to model this? currently incorrectly a touch pin.

pins need class docs

NO_PULL etc. aren't available on MicroBitDigitalPin. You need to use the instances
to access. Can/should we model this?

py:method::[a-z] shows broken docs where it's not rendered on readthedocs.

duplicate definition of MicroBitAnalogDigitalPin in the docs.

get_mode docs need fixing - I've done this for the stubs based on
https://github.com/microbit-foundation/micropython-microbit-v2/blob/eba8995843ebc7246765b364710543c9ffee344a/src/codal_port/microbit_pinmode.c#L97

### machine

	mem16
	mem32
	mem8
are undocumented

### micropython

schedule is undocumented

### os

ilistdir and stat are undocumented

### radio

In the docs and stubs but not on a V2 (V1 not checked):

>>> radio.RATE_250KBIT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'RATE_250KBIT'

## Example code failures

In waveforms.py

frames = [ None ] * 32

...is a problematic initialization pattern for arrays. Can we relax the rules?
Is the pattern widespread?