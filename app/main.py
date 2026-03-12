from fastapi import FastAPI
from .routers import user,auth,question

app = FastAPI()


@app.get("/health")
def health():
    return {"status" : "OK"}


#-------------------------Routers------------------


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(question.router)