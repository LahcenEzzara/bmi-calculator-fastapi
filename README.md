# BMI Calculator FastAPI

This is a simple Body Mass Index (BMI) calculator API built with FastAPI. It calculates BMI based on user-provided weight and height, and returns a message and image indicating the BMI category.

## Features

- Calculate BMI using weight and height
- Return BMI value, message, and image representing the BMI category
- CORS setup to allow requests from web browsers

## Endpoints

- **GET /**: Returns a welcome message.
- **GET /calculate_bmi**: Calculates BMI based on query parameters `weight` and `height`.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LahcenEzzara/bmi-calculator-fastapi.git
    cd bmi-calculator-fastapi
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

### Running the Server

1. Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn app:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

### Usage

- **GET /**:
    ```bash
    curl -X 'GET' \
      'http://127.0.0.1:8000/' \
      -H 'accept: application/json'
    ```
    Response:
    ```json
    {
      "message": "Hello, Python"
    }
    ```

- **GET /calculate_bmi**:
    ```bash
    curl -X 'GET' \
      'http://127.0.0.1:8000/calculate_bmi?weight=70&height=1.75' \
      -H 'accept: application/json'
    ```
    Response:
    ```json
    {
      "bmi": 22.857142857142858,
      "message": "You have a normal weight, keep it up.",
      "image": "2"
    }
    ```

## Acknowledgements

- FastAPI
- Pydantic
- Uvicorn

## Copyright

This project is developed by Lahcen Ezzara and is protected under the MIT License. Please see the [LICENSE](LICENSE) file for more details.

**© 2024 Lahcen Ezzara. All rights reserved.**
