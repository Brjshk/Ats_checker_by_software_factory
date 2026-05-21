from fastapi import APIRouter

router = APIRouter()

@router.post('/api/analyze')
async def analyze(resumeId: str, jobId: str):
    return {'score': 85, 'feedback': 'Improve your skills in Python.'}

@router.get('/api/history')
async def history():
    return [{'id': '1', 'score': 85, 'feedback': 'Good match!'}]
