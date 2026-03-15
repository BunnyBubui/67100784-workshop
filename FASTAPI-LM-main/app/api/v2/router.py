from fastapi import APIRouter
from api.v2.recommend.route import router as recommend_router
from api.v2.flight.route import router as flight_router
from api.v2.depression.route import router as depression_router
from api.v2.animal.route import router as animal_router

app_router_v2 = APIRouter()

app_router_v2.include_router(
    recommend_router,
    prefix='/recommend',
    tags=['Recommendations']
)

app_router_v2.include_router(
    flight_router,
    prefix='/flight',
    tags=['Flight Price Prediction']
)

app_router_v2.include_router(
    depression_router,
    prefix='/depression',
    tags=['Depression Classification']
)

app_router_v2.include_router(
    animal_router,
    prefix='/animal',
    tags=['Animal Image Classification']
)




