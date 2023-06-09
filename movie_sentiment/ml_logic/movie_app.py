#API
from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}


@app.get('/arc')
def arc():
    return {'the arc': 64}
