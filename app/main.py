from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

from app.core.luhn import generate_luhn, validate_luhn

app = FastAPI(title="Number Validator API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


class NumberPayload(BaseModel):
    """Payload for Luhn algorithm operations."""

    number: str = Field(
        ...,
        description=(
            "The number to validate or use for generation. "
            "Can include spaces or hyphens."
        ),
        examples=["79927398713", "123-456-789", "12 34 56"],
    )

    @field_validator("number")
    @classmethod
    def normalize_and_validate(cls, v: str) -> str:
        # Strip common formatting characters
        clean = v.replace(" ", "").replace("-", "")
        if not clean.isdigit():
            raise ValueError("Input must contain only digits, spaces, or hyphens.")
        if not clean:
            raise ValueError("Input cannot be empty.")
        return clean


@app.post("/validate/luhn")
def validate_luhn_number(payload: NumberPayload) -> dict[str, str | bool]:
    """Verify if a number is valid according to the Luhn algorithm."""
    is_valid = validate_luhn(payload.number)
    return {"number": payload.number, "valid": is_valid}


@app.post("/generate/luhn")
def generate_luhn_digit(payload: NumberPayload) -> dict[str, str]:
    """Generate the check digit for a given base number and return the full number."""
    added_digit = generate_luhn(payload.number)
    return {"new_number": payload.number + added_digit, "added_digit": added_digit}
