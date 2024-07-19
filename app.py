from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS to allow requests from web browsers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify allowed domains in production
    allow_methods=["*"],
    allow_headers=["*"],
)


class BMIOutput(BaseModel):
    bmi: float
    message: str
    image: str


@app.get("/")
def read_root():
    return {"message": "Hello, Python"}


@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float = Query(..., gt=20, lt=200,
                          description="Weight in kilograms"),
    height: float = Query(..., gt=1, lt=3, description="Height in meters")
):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = "You are underweight, eat more."
        image = "1"
    elif 18.5 <= bmi < 25:
        message = "You have a normal weight, keep it up."
        image = "2"
    elif 25 <= bmi < 30:
        message = "You are overweight, exercise more."
        image = "3"
    else:
        message = "You are obese, consult a doctor."
        image = "4"

    return BMIOutput(bmi=bmi, message=message, image=image)
