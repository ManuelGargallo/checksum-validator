from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.core.luhn import validate_luhn

app = FastAPI(title="Number Validator API")

class NumberPayload(BaseModel):
    number: str

@app.post("/validate/luhn")
def check_luhn(payload: NumberPayload):
    # Stripping spaces or dashes if users input them formatted
    clean_number = payload.number.replace(" ", "").replace("-", "")
    
    if not clean_number.isdigit():
        raise HTTPException(status_code=400, detail="Input must contain only digits.")
        
    is_valid = validate_luhn(clean_number)
    return {"number": payload.number, "valid": is_valid}
