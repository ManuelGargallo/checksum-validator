from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.core.luhn import validate_luhn, generate_luhn

app = FastAPI(title="Number Validator API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

from pydantic import BaseModel, Field, field_validator

class NumberPayload(BaseModel):
    """Payload for Luhn algorithm operations."""
    number: str = Field(
        ..., 
        description="The number to validate or use for generation. Can include spaces or hyphens.",
        examples=["79927398713", "123-456-789", "12 34 56"]
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
def validate_luhn_number(payload: NumberPayload):
    """Verify if a number is valid according to the Luhn algorithm."""
    is_valid = validate_luhn(payload.number)
    return {"number": payload.number, "valid": is_valid}

@app.post("/generate/luhn")
def generate_luhn_digit(payload: NumberPayload):
    """Generate the check digit for a given base number and return the full number."""
    added_digit = generate_luhn(payload.number)
    return {
        "new_number": payload.number + added_digit, 
        "added_digit": added_digit
    }
