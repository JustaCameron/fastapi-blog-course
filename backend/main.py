from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base


from apis.base import api_router

def create_tables():
    Base.metadata.create_all(bind=engine) # Connects past API to database engine

def include_router(app):
    app.include_router(api_router)
    
def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    # app.include_router(router)
    return app


app = start_application()

@app.get("/")
def hello():
    return {"detail": "Hello FastAPI"}

