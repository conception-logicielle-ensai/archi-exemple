from fastapi import FastAPI

from dao.configuration.database_connector import DatabaseConnector
from web.user_router import user_router
from config.app_config import add_cors_middleware

app = FastAPI()

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
