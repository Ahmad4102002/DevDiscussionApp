from fastapi import FastAPI
from .routers import user

app = FastAPI()


@app.get("/health")
def health():
    return {"status" : "OK"}


#-------------------------Routers------------------


app.include_router(user.router)