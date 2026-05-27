from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_get(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "application/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа

        with open('static/contacts.html', "r", encoding="utf-8") as f:
            html_page = f.read()

        self.wfile.write(bytes("{'message': 'OK'}", "utf-8")) # Тело ответа
