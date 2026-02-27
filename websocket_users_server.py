import asyncio
import websockets

async def handle_connection(websocket):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Сервер WebSocket запущен на ws://localhost:8765")
        await asyncio.Future()  # Работает вечно

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСервер остановлен.")