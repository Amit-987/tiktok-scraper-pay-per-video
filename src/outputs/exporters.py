from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List, Any

def _load_json_array(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"JSON at {path} is not an array")
    return data

def json_to_csv(json_path: Path, csv_path: Path) -> None:
    """
    Convert a JSON array of flat objects into a CSV file.
    """
    records = _load_json_array(json_path)
    if not records:
        csv_path.write_text("", encoding="utf-8")
        return

    fieldnames = sorted({key for record in records for key in record.keys()})

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)