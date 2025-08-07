from fastapi import APIRouter
from app.services.example import get_message
from app.models.example_schema import ExampleResponse

router = APIRouter(prefix="/example", tags=["Example"])

@router.get("/", response_model = ExampleResponse)
async def read_example():
    return {"message": get_message()}
