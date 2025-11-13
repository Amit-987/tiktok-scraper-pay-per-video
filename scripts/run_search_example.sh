set -euo pipefail

# Run a simple SEARCH example using the local sample dataset.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${PROJECT_ROOT}"
python src/main.py \
  --type SEARCH \
  --keyword "cuocdoivandepsao" \
  --region "VN" \
  --max-items 10 \
  --output "data/output.search.json"