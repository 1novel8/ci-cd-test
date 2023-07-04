from fastapi import FastAPI

from funcs.base_funcs import say_hello

app = FastAPI()


@app.get("/")
def hello():
    return {"message": say_hello()}



