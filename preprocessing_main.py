from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

from utils.model import TextInput
from utils.preprocessing import preprocess_string, preprocessing_manager

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def root():
    return "Welcome to the preprocessing module!"


@app.post("/path", response_class=PlainTextResponse)
def get_summary(text_wrapper: TextInput):
    text = preprocessing_manager(text_wrapper.text)
    text = preprocess_string(text)
    return text


if __name__ == "__main__":
    # Run uvicorn server from inside docker
    uvicorn.run(app, host="localhost", port=7000)
