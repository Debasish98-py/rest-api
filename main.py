from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_message():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": "Hi, This is Response"}
