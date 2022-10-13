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

## Licensing

These stubs are MIT or Apache 2.0 licensed depending on their origin (typeshed or MicroPython).
See [LICENSING.md](./LICENSING.md) for details.

## Scripts

`browser-package.py` packages the typeshed and a Pyright config file in a JSON format that can be consumed by the [Python Editor V3 project](https://github.com/microbit-foundation/python-editor-v3). A file is created per language.

## Testing

The stubs are tested against the code in the `examples/` folder using Pyright. To run the tests locally run `npm install` to install Pyright and then `npm test`.

## Code of Conduct

Trust, partnership, simplicity and passion are our core values we live and
breathe in our daily work life and within our projects. Our open-source
projects are no exception. We have an active community which spans the globe
and we welcome and encourage participation and contributions to our projects
by everyone. We work to foster a positive, open, inclusive and supportive
environment and trust that our community respects the micro:bit code of
conduct. Please see our [code of conduct](https://microbit.org/safeguarding/)
which outlines our expectations for all those that participate in our
community and details on how to report any concerns and what would happen
should breaches occur.
