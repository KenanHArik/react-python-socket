from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket
from starlette.responses import FileResponse
import random
import asyncio


# run this command: uvicorn main:app --reload
async def infinite_random():
    while True:
        yield random.random()
        await asyncio.sleep(3)


def infinite_random2():
    while True:
        yield random.random()

app = FastAPI()


@app.get("/")
async def get():
    return FileResponse('static/index.html')


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # data = await websocket.receive_text()
        data = next(infinite_random2())
        # print(data)
        # data = random.random()
        await asyncio.sleep(1)
        await websocket.send_text(f"Random Number is : {data}")
