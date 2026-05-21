from fastapi import APIRouter

router = APIRouter()

@router.post('/api/upload-resume')
async def upload_resume(file: bytes):
    return {'message': 'Resume uploaded'}

@router.post('/api/upload-job')
async def upload_job(file: bytes):
    return {'message': 'Job description uploaded'}
