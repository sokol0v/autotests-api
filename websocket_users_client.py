import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        message_to_send = "Привет, сервер!"

        await websocket.send(message_to_send)
        print(f"Отправлено на сервер: {message_to_send}")

        for _ in range(5):
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(send_message())