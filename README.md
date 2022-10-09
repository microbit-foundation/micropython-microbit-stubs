# micro:bit MicroPython stubs for editor support

The easiest way to try these type stubs is to use the online [micro:bit Python Editor](https://python.microbit.org) which bundles them.

## Translations

We maintain translations of these files in the [micro:bit Crowdin project](https://crowdin.com/project/microbitorg) in [this file](https://crowdin.com/translate/microbitorg/6422). Only changes to the English source should be made in this repository.

The source content is in English in `lang/en`.

The translated versions are periodically updated in this repository via a script.

We translate:

- First lines of all docstrings
- First lines of parameter documentation in `:param name:`-style
- The API name, e.g. function name, with underscores replaced with spaces to make clear it's a hint not the actual name. This is displayed alongside the English API name.
- Parameter names (again with underscores replaced). These are displayed alongside the English parameter name.

## Credit and licensing

builtins and utility definitions are derived from [typeshed](https://github.com/python/typeshed). These stubs don't provide documentation, though we'd love to add it in future.

MicroPython and micro:bit stubs are based on the restructured text documentation for [micro:bit](https://github.com/bbcmicrobit/micropython/tree/v2-docs) and, where not otherwise covered in micro:bit-specific docs, [MicroPython](https://github.com/micropython/micropython/tree/master/docs/library). These stubs provide documentation.

Typeshed is Apache 2.0 licensed.

MicroPython is MIT Licensed and Copyright (c) 2013-2021 Damien P. George.
MicroPython for the micro:bit is MIT licensed and Copyright (c) 2013-2016 The MicroPython-on-micro:bit Developers (see [the authors file](https://github.com/bbcmicrobit/micropython/blob/v2-docs/AUTHORS)).

## Scripts

`browser-package.py` packages the typeshed and a Pyright config file in a JSON format that can be consumed by the [Python Editor V3 project](https://github.com/microbit-foundation/python-editor-v3). A file is created per language.

## Testing

The stubs are tested against the code in the `examples/` folder using Pyright. To run the tests locally run `npm install` to install Pyright and then `npm test`.
