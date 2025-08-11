from fastapi import APIRouter, HTTPException
from app.services.cleaner import clean_dataset
from app.models.clean_schema import CleanResponse
from fastapi import Body

router = APIRouter()

@router.post("/clean", response_model=CleanResponse, summary="Clean uploaded dataset")
async def clean(dataset_id: str = Body(..., embed=True)):
    result = clean_dataset(dataset_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return result