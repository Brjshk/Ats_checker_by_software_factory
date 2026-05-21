from fastapi import APIRouter

router = APIRouter()

@router.post('/api/register')
async def register(username: str, password: str):
    return {'message': 'User created'}

@router.post('/api/login')
async def login(username: str, password: str):
    return {'token': 'dummy_token'}
