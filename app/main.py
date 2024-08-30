from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.brand_routes import router as brand_routes

app = FastAPI()

app.include_router(brand_routes, prefix="/api/v1")
origin = "http://localhost:3000"

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()
