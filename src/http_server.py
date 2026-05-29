from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200) # Отправка кода ответа
        self.send_header('Content-type', 'text/html; charset=utf-8') # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа

        with open('static/contacts.html', "r", encoding="utf-8") as f:
            html = f.read()

        self.wfile.write(html.encode('utf-8'))  # Тело ответа
