from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

from utils.model import generate_summary, TextInput

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def root():
    return "Welcome to the model module!"


@app.post("/input", response_class=PlainTextResponse)
def get_summary(text_wrapper: TextInput):
    # TODO: send inference to database instead of user
    return generate_summary(text_wrapper.text)


if __name__ == "__main__":
    # Run uvicorn server from inside docker
    uvicorn.run(app, host="localhost", port=5000)
    # uvicorn.run(app)
