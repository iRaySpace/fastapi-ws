from fastapi import FastAPI, WebSocket

app = FastAPI(title="WebSocket Example")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("Accepting client connection...")
    await websocket.accept()
    value = 0
    while True:
        try:
            await websocket.receive_text()
            await websocket.send_json({"value": value})
            value = value + 1
        except Exception as e:
            print("Error:", e)
            break
    print("Bye...")
