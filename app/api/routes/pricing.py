from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/pricing",
    tags=["Pricing"],
)


@router.post("/")
async def pricing():
    """
    Temporary endpoint to verify routing.
    """

    return {
        "message": "Pricing endpoint is working."
    }