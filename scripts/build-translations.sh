#!/usr/bin/env bash
#
# Rebuild translations from the Crowdin files in crowdin/translated/, as
# downloaded by `npm run i18n:download` (see i18n.config.mjs).
# Assumes it is run from the root of the project.

set -euxo pipefail

# Driven by the files on disk rather than i18n.config.mjs so a language whose
# download failed this week is rebuilt from last week's file.
for translated in crowdin/translated/api.*.json; do
    lang=$(basename "${translated}" .json)
    lang="${lang#api.}"
    rm -rf "lang/${lang}"
    cp -r lang/en "lang/${lang}"
done
npm run i18n:typeshed-to-crowdin
npm run i18n:crowdin-to-typeshed
