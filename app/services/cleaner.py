import os
import pandas as pd
import uuid
from app.core.config import settings
from app.utils.logging import logger
from app.models.clean_schema import CleanReport, CleanResponse
from typing import Optional

def clean_dataset(dataset_id: str) -> Optional[CleanResponse]:

    src = os.path.join(settings.DATA_DIR, f"{dataset_id}.csv")
    if not os.path.exists(src):
        logger.error(f"Dataset not found: {src}")
        return None

    df = pd.read_csv(src)
    initial_count = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_count - len(df)

    filled = {}
    for col in df.columns:
        n_missing = df[col].isna().sum()
        if n_missing > 0:
            df[col].fillna(df[col].median() if df[col].dtype!=object else df[col].mode()[0], inplace=True)
            filled[col] = int(n_missing)

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    cleaned_id = uuid.uuid4().hex
    dest = os.path.join(settings.DATA_DIR, f"{cleaned_id}.csv")
    df.to_csv(dest, index=False)

    report = CleanReport(
        duplicates_removed=duplicates_removed,
        missing_values_filled=filled
    )
    return CleanResponse(
        dataset_id=dataset_id,
        cleaned_id=cleaned_id,
        report=report
    )