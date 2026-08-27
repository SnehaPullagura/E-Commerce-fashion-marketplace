from fastapi import APIRouter
from app.authentication.router import router as auth_router
from app.users.router import router as users_router
from app.categories.router import router as categories_router
from app.products.router import router as products_router
from app.search.router import router as search_router

api_router = APIRouter()

# Core Authentication & Users
api_router.include_router(auth_router)
api_router.include_router(users_router)

# Fashion Catalog
api_router.include_router(categories_router)
api_router.include_router(products_router)

# Discovery & Search
api_router.include_router(search_router)
