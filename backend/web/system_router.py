from fastapi import APIRouter


system_router = APIRouter(tags=["system"])


@system_router.get("/")
def root():
    return {"status": "ok"}


@system_router.get("/health")
def health():
    return {"status": "healthy"}
