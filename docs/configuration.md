# Configuration Guide

This project ships with a small local runner that simulates a TikTok scraping
pipeline using a static JSON dataset. You can integrate it into your own
workflows by controlling it via CLI flags or environment variables.

## CLI Options

- `--type` – Scraping mode: `SEARCH`, `TREND`, `HASHTAG`, `USER`, `MUSIC`.
- `--keyword` – Keyword string for `SEARCH` mode.
- `--region` – Two-letter country code (used primarily by `TREND` and `SEARCH`).
- `--hashtag-url` – TikTok hashtag URL for `HASHTAG` mode.
- `--user-url` – TikTok profile URL for `USER` mode.
- `--music-url` – TikTok music track URL for `MUSIC` mode.
- `--max-items` – Soft limit on how many videos to collect.
- `--unlimited` – If set, attempts to return all matched records.
- `--input` – Path to the JSON file backing the demo client.
- `--output` – Path where normalized JSON output will be written.
- `--log-level` – Logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`).

## Environment Variables

You can also configure most fields via environment variables:

- `TTS_REGION`
- `TTS_KEYWORD`
- `TTS_HASHTAG_URL`
- `TTS_USER_URL`
- `TTS_MUSIC_URL`
- `TTS_MAX_ITEMS`
- `TTS_UNLIMITED`
- `TTS_INPUT_PATH`
- `TTS_OUTPUT_PATH`
- `TTS_LOG_LEVEL`

CLI flags always take precedence over environment variables.