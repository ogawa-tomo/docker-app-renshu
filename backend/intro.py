from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def hello():
    return {"text": "hello, I am FastAPI!"}


@app.get('/get/{path}')
async def path(path: str):
    return {"text": f"hello, {path}"}
