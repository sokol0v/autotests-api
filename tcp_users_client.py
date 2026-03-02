import socket


def run_client():
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Адрес сервера
    server_address = ('127.0.0.1', 12345)

    try:
        # Подключаемся к серверу
        client_socket.connect(server_address)

        # Сообщение для отправки
        message = "Привет, сервер!"
        client_socket.send(message.encode('utf-8'))

        # Получаем ответ от сервера
        response = client_socket.recv(1024).decode('utf-8')

        # Выводим ответ в консоль
        print(response)

    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу. Убедитесь, что он запущен.")
    finally:
        # Закрываем соединение
        client_socket.close()


if __name__ == "__main__":
    run_client()