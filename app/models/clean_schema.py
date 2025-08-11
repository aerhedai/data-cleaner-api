from pydantic import BaseModel
from typing import Dict

class CleanReport(BaseModel):
    duplicates_removed: int
    missing_values_filled: Dict[str, int]

class CleanResponse(BaseModel):
    dataset_id: str
    cleaned_id: str
    report: CleanReport