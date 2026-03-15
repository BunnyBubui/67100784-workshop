from fastapi import APIRouter
from api.v1.recommend.route import router as recommend_router
from api.v1.flight.route import router as flight_router
from api.v1.depression.route import router as depression_router

app_router = APIRouter()

app_router.include_router(
    recommend_router,
    prefix='/recommend',
    tags=['Recommendations']
)

app_router.include_router(
    depression_router,
    prefix='/depression',
    tags=['Depression']
)   

app_router.include_router(
    flight_router,
    prefix='/flight',
    tags=['Flight Price Prediction']
)