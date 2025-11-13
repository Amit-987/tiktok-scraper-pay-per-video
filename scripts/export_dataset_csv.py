from pathlib import Path
import sys

# Make src importable when running this script directly
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from outputs.dataset_writer import DatasetWriter  # noqa: E402

def main() -> None:
    json_input = ROOT / "data" / "output.json"
    csv_output = ROOT / "data" / "output.csv"

    writer = DatasetWriter(output_path=json_input)
    writer.export_csv(csv_output)
    print(f"Exported CSV to {csv_output}")

if __name__ == "__main__":
    main()