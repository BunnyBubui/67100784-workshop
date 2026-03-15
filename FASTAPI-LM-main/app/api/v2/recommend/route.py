
from fastapi import APIRouter
from api.v2.recommend.schema import RecommendRequest
from api.v2.recommend.service import search_predict

router = APIRouter()

@router.post('/search', tags=['Recommendations'])
def get_recommendations(data: RecommendRequest):
    recommendations = search_predict(data.query, data.top_k, data.type)
    return recommendations