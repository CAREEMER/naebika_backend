import uvicorn
from fastapi import FastAPI

from api import router
from core.config import app_config

app = FastAPI(
    title="BaseBackendTemplate",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(router.router)


def main():
    uvicorn.run(
        app="main:app",
        host=app_config.HOST,
        port=app_config.PORT,
        reload=app_config.ENV == "local",
        workers=1,
    )


if __name__ == "__main__":
    main()
