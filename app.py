from fastapi import FastAPI
from helpers import predict_topic

app = FastAPI()


@app.get("/items/{text}")
def read_item(text):
    text_topic = predict_topic(text)
    return {"topic": text_topic}
