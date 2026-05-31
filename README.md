# Checksum Validator API

[![CI](https://github.com/ManuelGargallo/checksum-validator/actions/workflows/ci.yml/badge.svg)](https://github.com/ManuelGargallo/checksum-validator/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, production-ready validation API built with **FastAPI** to verify and generate numerical check digits using the **Luhn Algorithm**.

Designed with performance in mind, the core logic utilizes pre-computed lookup tables and zero-allocation summation to ensure minimal overhead.

## 🚀 Features

- **Luhn Validation**: Verify credit card numbers, IMEI numbers, and other ISO/IEC 7812 identifiers.
- **Check Digit Generation**: Generate the required check digit for any base number.
- **Robust Validation**: Automatic input cleaning (strips spaces and hyphens) via Pydantic.
- **High Performance**: Optimized core algorithm with lookup tables.
- **Developer Friendly**: Full OpenAPI (Swagger) documentation and type safety with MyPy.

## 🛠️ Installation

### Prerequisites
- Python 3.11+
- [Optional] `uv` or `pip` for dependency management.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ManuelGargallo/checksum-validator.git
   cd checksum-validator
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install .
   ```

3. Install development dependencies (optional):
   ```bash
   pip install ".[dev]"
   ```

## 🏃 Running the API

Start the server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## 🔌 API Usage

### Health Check
```bash
curl http://127.0.0.1:8000/health
```

### Validate a Number
```bash
curl -X POST http://127.0.0.1:8000/validate/luhn \
     -H "Content-Type: application/json" \
     -d '{"number": "7992-7398-713"}'
```

### Generate a Check Digit
```bash
curl -X POST http://127.0.0.1:8000/generate/luhn \
     -H "Content-Type: application/json" \
     -d '{"number": "7992739871"}'
```

## 🧪 Development

This project uses a modern toolstack to maintain high code quality:

- **Testing**: `pytest`
- **Linting & Formatting**: `ruff`
- **Type Checking**: `mypy`

Run the full suite:
```bash
# Run tests
pytest

# Lint and format check
ruff check .
ruff format --check .

# Type check
mypy app
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
