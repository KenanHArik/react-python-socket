from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket


app = FastAPI()

app.mount("./", StaticFiles(directory))

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")