from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket
from starlette.responses import FileResponse
import random

# run this command: uvicorn main:app --reload

app = FastAPI()



@app.get("/")
async def get():
    return FileResponse('static/index.html')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        data = random.random()
        await websocket.send_text(f"Message text was: {data}")