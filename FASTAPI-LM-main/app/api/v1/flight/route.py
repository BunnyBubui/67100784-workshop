from fastapi import APIRouter
from api.v1.flight.schema import FlightRequest
from api.v1.flight.service import predict_price

router = APIRouter()

@router.post('/predict', tags=['Flight Price Prediction'])
def get_flight_price_prediction(data: FlightRequest):
    prediction = predict_price(data)
    return prediction