import os

from config.app_config import add_cors_middleware
from dao.configuration.database_connector import DatabaseConnector
from fastapi import FastAPI
from web.user_router import user_router

app_title = os.getenv("APP_TITLE", "UserAPIEnsai")
app = FastAPI(title=app_title)

app.include_router(user_router)

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
