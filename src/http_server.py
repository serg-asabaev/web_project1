from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
from urllib.parse import parse_qs

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        if self.path == '/':
            self.send_response(200) # Отправка кода ответа
            self.send_header('Content-type', 'text/html; charset=utf-8') # Отправка типа данных, который будет передаваться
            self.end_headers() # Завершение формирования заголовков ответа

            with open('static/contacts.html', "r", encoding="utf-8") as f:
                html = f.read()

            self.wfile.write(html.encode('utf-8'))  # Тело ответа
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        # Получение длины контента
        content_length = int(self.headers.get('Content-Length', 0))

        # Чтение тела запроса
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Определение типа контента
        content_type = self.headers.get('Content-Type', '')

        if 'application/json' in content_type:
            # Обработка JSON
            try:
                data = json.loads(post_data)
                response = {'received': data, 'type': 'json'}
            except json.JSONDecodeError:
                response = {'error': 'Invalid JSON'}
                self.send_response(400)

        elif 'application/x-www-form-urlencoded' in content_type:
            # Обработка form-data
            data = parse_qs(post_data)
            response = {'received': data, 'type': 'form'}

        else:
            response = {'received': post_data, 'type': 'raw'}

        # Отправка ответа
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
