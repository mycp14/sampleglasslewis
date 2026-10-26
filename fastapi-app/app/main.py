from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Sample Todo API")
app.include_router(router)


@app.get("/health", tags=["ops"])
def health() -> dict[str, str]:
    return {"status": "ok"}
