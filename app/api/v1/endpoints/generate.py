from fastapi import APIRouter, Request, HTTPException, Depends
from app.core.security import verify_shopify_signature
from app.services import ai_service
from app.schemas.generation import GenerationRequest

router = APIRouter()

async def validate_shopify_request(request: Request):
    """Dependency to validate Shopify Proxy Signature"""
    query_params = dict(request.query_params)
    if not verify_shopify_signature(query_params):
        raise HTTPException(status_code=403, detail="Invalid Shopify Signature")
    return True

@router.get("/test") 
async def test(request: Request, authorized: bool = Depends(validate_shopify_request)):
        return {"message": "Hello, World!"}