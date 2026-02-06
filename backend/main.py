import os

from fastapi import FastAPI

from config.app_config import add_cors_middleware
from dao.configuration.database_connector import DatabaseConnector
from web.system_router import system_router
from web.user_router import user_router


app_title = os.getenv("APP_TITLE", "UserAPIEnsai")
app = FastAPI(title=app_title)


@app.on_event("startup")
def startup():
    database_connector = DatabaseConnector("sqlite", "default.db")
    database_connector.init_db()


@app.on_event("shutdown")
def shutdown():
    DatabaseConnector().close_connection()


app.include_router(user_router)
app.include_router(system_router)

# Configuration CORS
add_cors_middleware(app)

if __name__ == "__main__":
    import uvicorn

    # initialisation du connector
    database_connector = DatabaseConnector("sqlite", "default.db")
    # initialisation de la bdd : schema et donnees
    database_connector.init_db()
    # Run server
    uvicorn.run(app, host="0.0.0.0", port=8000)
