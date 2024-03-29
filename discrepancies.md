# Notes

These are working notes on discrepancies found when creating these stubs.

## Cross-cutting issues

Module docs throughout are a bit arbitrary and need review.

Various docs don't line up exactly because @overload is the best way to represent their typings so requires docs to be customised for each scenario.

## Module-specific issues

### gc

isenabled is undocumented in MicroPython docs (not added).

### audio

[AudioFrame.copyfrom](https://github.com/microbit-foundation/micropython-microbit-v2/blob/bca4dc5690998e8e5de07019a44185fc9b9ea080/src/codal_port/modaudio.c#L301) is undocumented (not added).

AudioFrame implements some operations that aren't clearly documented (e.g. you can add them, multiple by an integer). I added stubs for these as they're used in examples.

### uart

uart.readinto is misindented in the docs (minor).
there's a method documented as having been removed so I've omitted it from the stubs

### microbit

- image - type of buffer in second __init__ option
- text modified to split across __init__ definitions
- "Same as" language is unhelpful.
- __sub__ and __div__ added based on examples but not in docs.
- microphone - the doc style here is a bit different to elsewhere, might be less good in Pyright?
- set\_volume has examples but no docs (added in stubs)

### micropython

- schedule is undocumented (I've not added it)
- micropython.schedule is missing from our docs. Why? It is on the device (checked on V2).

### neopixel

Has long but important module docstring with important warnings for the user.
I've removed the images and reproduced it otherwise in full.

Some complication with write/show. Fine for stubs but will need revisiting for docs.

ws2812_write is undocumented (here and in microbit module)
ORDER is undocumented

### pins (in microbit)

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

### machine

	mem16
	mem32
	mem8
are undocumented

### os

ilistdir and stat are undocumented (not added)

### radio

In the docs and stubs but not on a V2 (V1 not checked):

```
>>> radio.RATE_250KBIT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'RATE_250KBIT'
```

Raised https://github.com/microbit-foundation/micropython-microbit-v2/issues/87

### microphone

```python
>>> from microbit import *
>>> repr(microphone.current_event())
'None'
>>> repr(microphone.current_event())
"SoundEvent('loud')"
```

but [docs](https://microbit-micropython.readthedocs.io/en/v2-docs/microphone.html#microbit.microphone.current_event) (and for now stubs) claim it cannot return None

Raised https://github.com/microbit-foundation/micropython-microbit-v2/issues/86

## Interesting code failures

In waveforms.py

```python
frames = [ None ] * 32
```

...is a problematic initialization pattern for arrays. Can we relax the rules?
Is the pattern widespread? What options does Pyright have to relax behaviour around None?
