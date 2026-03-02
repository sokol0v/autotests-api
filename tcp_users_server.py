import socket


def run_server():
    # Создаем TCP-сокет (AF_INET - IPv4, SOCK_STREAM - TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к адресу и порту
    server_address = ('127.0.0.1', 12345)
    server_socket.bind(server_address)

    # Слушаем входящие соединения (очередь до 10 подключений)
    server_socket.listen(10)

    # Список для хранения истории сообщений
    all_messages = []

    print(f"Сервер запущен на {server_address[0]}:{server_address[1]}...")

    try:
        while True:
            # Принимаем новое подключение
            client_socket, client_address = server_socket.accept()
            print(f"Пользователь с адресом: {client_address} подключился к серверу")

            try:
                # Получаем данные от клиента (буфер 1024 байта)
                data = client_socket.recv(1024).decode('utf-8')

                if data:
                    print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

                    # Добавляем сообщение в историю
                    all_messages.append(data)

                    # Формируем ответ из всей истории, разделяя строки
                    response = '\n'.join(all_messages)

                    # Отправляем ответ клиенту
                    client_socket.send(response.encode('utf-8'))

            finally:
                # Закрываем соединение с текущим клиентом
                client_socket.close()

    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    run_server()