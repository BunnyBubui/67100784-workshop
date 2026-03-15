from fastapi import APIRouter
from api.v1.recommend.schema import RecommendRequest
from api.v1.recommend.service import search_predict

router = APIRouter()

@router.post('/search', tags=['Recommendations'])
def get_recommendations(data: RecommendRequest):
    recommendations = search_predict(data.query, data.top_k, data.type)
    return recommendations

@router.get('/user')
def get_user_recommendations():
    return { "message": "User recommendations" }
