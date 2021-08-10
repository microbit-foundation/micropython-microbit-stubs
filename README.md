Temporary home for micro:bit MicroPython stubs.

These are incomplete and/or wrong and need careful review.

Standard library bits from https://github.com/cpwood/Pico-Stub
micro:bit specific stubs from https://github.com/vlasovskikh/intellij-micropython

At some point I replaced the stdlib bits with the ordinary Python typeshed but
not clear this was necessary. We could revert to the Pico ones if they have docs or are a better match to MicroPython.

All seem to be open source but obviously copied around a lot. It'd be good to
trace back with care and document.

See also https://github.com/Josverl/micropython-stubs/
