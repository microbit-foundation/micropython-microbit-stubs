# micro:bit MicroPython stubs for editor support

This project contains Python stub files for [MicroPython for micro:bit V2](https://github.com/microbit-foundation/micropython-microbit-v2).

The easiest way to try these type stubs is to use the online [micro:bit Python Editor](https://python.microbit.org) which uses them for its code intelligence features and the API documentation.

## Licensing

These stubs are MIT or Apache 2.0 licensed depending on their origin (typeshed or MicroPython).
See [LICENSE.md](./LICENSE.md) for details.

## Translations

We maintain translations of these files in the [micro:bit Crowdin project](https://crowdin.com/project/microbitorg) in [this file](https://crowdin.com/translate/microbitorg/6422). Only changes to the English source should be made in this repository.

The source content is in English in `lang/en`; translations sit beside it in `lang/<lang>`, named by Crowdin language id (`lang/zh-CN`). The translated directories are generated from `crowdin/translated/api.<lang>.json` and are committed so the diff of a sync is reviewable; do not edit them by hand.

The translated versions are periodically updated in this repository: `npm run i18n:download` (with a Crowdin personal access token in `CROWDIN_PERSONAL_TOKEN`) fetches the languages listed in `i18n.config.mjs` into `crowdin/translated/` using [`@microbit/i18n-tools`](https://github.com/microbit-foundation/ui/tree/main/packages/i18n-tools), then `scripts/build-translations.sh` converts them into `lang/<lang>/`. The translations-download workflow does both weekly and opens a pull request. `npm run i18n:upload` regenerates the English `crowdin/api.en.json` from the stubs and replaces it in Crowdin; the translations-upload workflow runs it from the Actions tab, with an option to keep translations for a correction translators need not revisit.

We translate:

- First lines of all docstrings
- First lines of parameter documentation in `:param name:`-style
- The API name, e.g. function name, with underscores replaced with spaces to make clear it's a hint not the actual name. This is displayed alongside the English API name.
- Parameter names (again with underscores replaced). These are displayed alongside the English parameter name.

## Releases and the Python Editor

`npm run build` runs `scripts/browser-package.py`, which packages each `lang/<lang>/typeshed` with the Pyright config in `config/` as `typeshed.<lang>.json` for the [Python Editor](https://github.com/microbit-foundation/python-editor-v3)'s browser Pyright.

Creating a GitHub release from a `vX.Y.Z` tag publishes those files to npm as [`@microbit/micropython-microbit-stubs`](https://www.npmjs.com/package/@microbit/micropython-microbit-stubs); the version is taken from the tag. The Python Editor depends on the package, so a release there is a Renovate pull request. Cut a release after merging a translation sync or a change to the English stubs that should reach the editor.

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
