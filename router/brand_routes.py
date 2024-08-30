from fastapi import APIRouter
from pydantic import BaseModel

from config.langchain_helper import *


class BaseRequest(BaseModel):
    industry: str
    niche: str


router = APIRouter(prefix="/brand", tags=["brand"])


@router.get("/name")
async def get_brand_name(industry: str, niche: str):
    return generate_brand_name(industry, niche)


@router.post("/color")
async def get_brand_color(industry: str, niche: str):
    return generate_brand_color(industry, niche)


@router.post("/messaging")
async def get_brand_messaging(industry: str, niche: str):
    return generate_brand_messaging(industry, niche)


@router.post("/font")
async def get_brand_font(industry: str, niche: str):
    return get_brand_font(industry, niche)


@router.post("/logo")
async def get_brand_logo(industry: str, niche: str):
    return generate_logo(industry, niche)


@router.post("/pattern")
async def get_brand_pattern(industry: str):
    return generate_pattern(industry)


@router.post("/photography")
async def get_brand_photography(industry: str):
    return generate_pics(industry)


@router.post("/strategy")
async def get_brand_strategy(industry: str, niche: str, country: str):
    return generate_business_strategy(industry, niche, country)
