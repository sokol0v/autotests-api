import grpc
import course_service_pb2
import course_service_pb2_grpc


def run():
    # Устанавливаем соединение с сервером
    with grpc.insecure_channel('localhost:50051') as channel:
        # Создаем "заглушку" (stub) клиента
        stub = course_service_pb2_grpc.CourseServiceStub(channel)

        # Формируем запрос
        request = course_service_pb2.GetCourseRequest(course_id="api-course")

        # Вызываем метод и получаем ответ
        response = stub.GetCourse(request)

        # Вывод результата
        print(response)


if __name__ == '__main__':
    run()