from fastapi import FastAPI
import backend
from fastapi.responses import Response

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Server is up and running!"}


@app.get("/attributes")
def get_attributes():
    response = backend.process_atributtes()
    return response


@app.get("/thumbnail")
def get_thumbnail():
    response = backend.process_thumbnail()
    return Response(content=response, media_type="image/png")


@app.get("/ndvi")
def get_ndvi():
    pass
