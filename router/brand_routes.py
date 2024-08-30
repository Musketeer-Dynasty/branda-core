import random
from fastapi import APIRouter
from pydantic import BaseModel
import requests

from config.langchain_helper import *


class BaseRequest(BaseModel):
    industry: str
    niche: str


router = APIRouter(prefix="/brand", tags=["brand"])


@router.get("/name")
async def get_brand_name(industry: str, niche: str):
    return generate_brand_name(industry, niche)


@router.get("/color")
async def get_brand_color(industry: str, niche: str):
    return generate_brand_color(industry, niche)


@router.get("/messaging")
async def get_brand_messaging(industry: str, niche: str):
    return generate_brand_messaging(industry, niche)


@router.get("/logo")
async def get_brand_logo(industry: str, niche: str):
    return generate_logo(industry, niche)


@router.get("/pattern")
async def get_brand_pattern(industry: str):
    return generate_pattern(industry)


@router.get("/photography")
async def get_brand_photography(industry: str):
    return generate_pics(industry)


@router.get("/strategy")
async def get_brand_strategy(industry: str, niche: str, country: str):
    return generate_business_strategy(industry, niche, country)


@router.get("/font")
async def get_font():
    return generate_fonts()
