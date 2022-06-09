# micro:bit MicroPython stubs for editor support

## Translations

We maintain translations of these files via Crowdin.

The source content is in English in `lang/en`.

The translated versions are periodically updated in this repository via a script.

We translate:

- First lines of all docstrings
- First lines of parameter documentation in `:param name:`-style
- The API name, e.g. function name, with underscores replaced with spaces to make clear it's a hint not the actual name
- Parameter names (again with underscores replaced)

## Credit and licensing

builtins and utility definitions are derived from [typeshed](https://github.com/python/typeshed). Further work is required to review these to ensure that we don't have stubs for definitions MicroPython does not support. These stubs don't provide documentation.

MicroPython and micro:bit stubs are based on the restructured text documentation for [micro:bit](https://github.com/bbcmicrobit/micropython/tree/v2-docs) and, where not otherwise covered in micro:bit-specific docs, [MicroPython](https://github.com/micropython/micropython/tree/master/docs/library). These stubs provide documentation.

Typeshed is Apache 2.0 licensed.

MicroPython is MIT Licensed and Copyright (c) 2013-2021 Damien P. George.
MicroPython for the micro:bit is MIT licensed and Copyright (c) 2013-2016 The MicroPython-on-micro:bit Developers (see [the authors file](https://github.com/bbcmicrobit/micropython/blob/v2-docs/AUTHORS)).

## Scripts

`browser-package.py` packages the typeshed and a Pyright config file in a JSON format that can be consumed by the [alpha Python editor project](https://github.com/microbit-foundation/python-editor-next). A file is created per language.

## Testing

The stubs are tested against the code in the `examples/` folder using Pyright. To run the tests locally run `npm install` to install Pyright and then `npm test`.