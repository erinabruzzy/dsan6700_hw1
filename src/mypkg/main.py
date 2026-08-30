"""
Stand up a small FastAPI service skeleton. Your app does not have to do anything
interesting yet, but it must be a real web service:

❐ a FastAPI application with at least a /health endpoint that returns a small
typed response and lets a caller (or a container, or a grader) confirm the service
is up;
❐ at least one Pydantic request/response model so input is validated at the edge
and output is serialized predictably;
❐ a placeholder "predict"-style endpoint is welcome but optional this week.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from mypkg.config import settings

app = FastAPI(title=settings.app_name)


class HealthResponse(BaseModel):
    status: str
    environment: str


class PredictRequest(BaseModel):
    features: list[float]


class PredictResponse(BaseModel):
    prediction: float


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", environment=settings.environment)


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    result = sum(payload.features)
    return PredictResponse(prediction=result)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to Homework 1"}
