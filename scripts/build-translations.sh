#!/usr/bin/env bash
#
# Rebuild translations.
# Assumes it is run from the root of the project.

set -euxo pipefail

languages="ca de es-ES fr ga-IE ja ko nl pl zh-CN zh-TW lol"

for language in $languages; do
    lower="${language,,}"
    rm -rf "lang/${lower}"
    cp -r lang/en "lang/${lower}"
done
npm run i18n:typeshed-to-crowdin
npm run i18n:crowdin-to-typeshed
