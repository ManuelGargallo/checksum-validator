from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.core.luhn import validate_luhn, generate_luhn

app = FastAPI(title="Number Validator API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

class NumberPayload(BaseModel):
    number: str

@app.post("/validate/luhn")
def validate_luhn_number(payload: NumberPayload):
    # Stripping spaces or dashes if users input them formatted
    clean_number = payload.number.replace(" ", "").replace("-", "")
    
    if not clean_number.isdigit():
        raise HTTPException(status_code=400, detail="Input must contain only digits.")
        
    is_valid = validate_luhn(clean_number)
    return {"number": payload.number, "valid": is_valid}

@app.post("/generate/luhn")
def generate_luhn_digit(payload: NumberPayload):
    # Stripping spaces or dashes if users input them formatted
    clean_number = payload.number.replace(" ", "").replace("-", "")
    
    if not clean_number.isdigit():
        raise HTTPException(status_code=400, detail="Input must contain only digits.")
        
    added_digit = generate_luhn(clean_number)
    return {"new_number": payload.number+added_digit, "added_digit": added_digit}
