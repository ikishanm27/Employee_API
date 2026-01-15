from fastapi import FastAPI
from app.routers.employee import router
from app.db import Base, engine
from app.routers.user import user




app = FastAPI(title="Employee API")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(user)
app.include_router(router)

@app.get("/")
def root():
    return{"messsage ":"employee crud api working successfully"}
