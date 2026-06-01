from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, Field, field_validator

from app.core.luhn import generate_luhn, validate_luhn

app = FastAPI(title="Number Validator API", version="1.0.0")
v1_router = APIRouter(prefix="/api/v1")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


def _clean_number(v: str) -> str:
    """Internal helper to clean and validate a single number string."""
    clean = v.replace(" ", "").replace("-", "")
    if not clean:
        raise ValueError("Input cannot be empty.")
    if not clean.isdigit():
        raise ValueError(f"Input must contain only digits, spaces, or hyphens: '{v}'")
    return clean


class NumberPayload(BaseModel):
    """Payload for Luhn algorithm operations."""

    number: str = Field(
        ...,
        description=(
            "The number to validate or use for generation. "
            "Can include spaces or hyphens."
        ),
        examples=["79927398713", "123-456-789"],
    )

    @field_validator("number")
    @classmethod
    def normalize_and_validate(cls, v: str) -> str:
        return _clean_number(v)


class BatchNumberPayload(BaseModel):
    """Payload for batch Luhn validation."""

    numbers: list[str] = Field(
        ...,
        description=(
            "A list of numbers to validate. Each can include spaces or hyphens."
        ),
        examples=[["79927398713", "7992-7398-714"]],
    )

    @field_validator("numbers")
    @classmethod
    def validate_numbers(cls, v: list[str]) -> list[str]:
        if not v:
            raise ValueError("The list of numbers cannot be empty.")
        return [_clean_number(s) for s in v]


@v1_router.post("/validate/luhn")
def validate_luhn_number(payload: NumberPayload) -> dict[str, str | bool]:
    """Verify if a number is valid according to the Luhn algorithm."""
    is_valid = validate_luhn(payload.number)
    return {"number": payload.number, "valid": is_valid}


@v1_router.post("/validate/luhn/batch")
def validate_luhn_batch(
    payload: BatchNumberPayload,
) -> dict[str, list[dict[str, str | bool]]]:
    """Verify multiple numbers in a single request for higher throughput."""
    return {
        "results": [
            {"number": num, "valid": validate_luhn(num)} for num in payload.numbers
        ]
    }


@v1_router.post("/generate/luhn")
def generate_luhn_digit(payload: NumberPayload) -> dict[str, str]:
    """Generate the check digit for a given base number and return the full number."""
    added_digit = generate_luhn(payload.number)
    return {"new_number": payload.number + added_digit, "added_digit": added_digit}


app.include_router(v1_router)
