# Usage Examples

All commands are assumed to be run from the repository root:

```bash
cd "TikTok Scraper (Pay per video)"

1. Basic SEARCH Run
bashpython src/main.py \
  --type SEARCH \
  --keyword "Cuocdoivandepsao" \
  --region "VN" \
  --max-items 10 \
  --output "data/output.search.json"

2. TREND Run for a Region
bashpython src/main.py \
  --type TREND \
  --region "US" \
  --max-items 50 \
  --output "data/output.trend.us.json"

3. HASHTAG Run
bashpython src/main.py \
  --type HASHTAG \
  --hashtag-url "https://www.tiktok.com/tag/cuocdoivandepsao" \
  --max-items 25 \
  --output "data/output.hashtag.json"

4. CSV Export
After running any mode, export the normalized JSON dataset to CSV: