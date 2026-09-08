import { defineConfig } from "@microbit/i18n-tools";

// Languages the Python Editor ships API documentation in. The editor, the
// pyright fork and this repo list the same languages; add a new one to all
// three (see the editor's docs/tech-overview.md).
const languages = [
  "ca",
  "de",
  "es-ES",
  "fr",
  "ga-IE",
  "ja",
  "ko",
  "nl",
  "pl",
  "zh-CN",
  "zh-TW",
  "lol",
];

export default defineConfig({
  crowdin: {
    project: "microbitorg",
    branch: "new",
    directory: "apps/python-editor-v3",
  },
  languages,
  // api.en.json is generated from the stubs by `npm run i18n:typeshed-to-crowdin`
  // in Crowdin's message/description JSON, and the translations are converted
  // back into lang/<lang>/ by scripts/build-translations.sh, so the tool only
  // moves the files.
  files: [
    {
      crowdinFile: "api.en.json",
      local: "crowdin/translated/api.{lang}.json",
      source: "crowdin/api.en.json",
    },
  ],
});
