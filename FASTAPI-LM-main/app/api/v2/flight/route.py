from fastapi import APIRouter
from api.v2.flight.schema import FlightRequest
from api.v2.flight.service import predict_price
from api.v2.flight.train_flight_price import main as train_model

router = APIRouter()

@router.post('/predict', tags=['Flight Price Prediction'])
def get_flight_price_prediction(data: FlightRequest):
    prediction = predict_price(data)
    return prediction


@router.post('/train', tags=['Flight Price Prediction'])
def train_flight_price_model():
    """Train the flight price prediction model."""
    train_model()
    return {"message": "Flight price model trained successfully"}

