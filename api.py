from fastapi import FastAPI

app = FastAPI()

@app.get('/api/v1/hello')
def hello_world():
    return {'hello': 'world'}