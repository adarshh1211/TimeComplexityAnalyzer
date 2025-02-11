import http.server
import socketserver
import json
from complexity_analyzer import analyze_complexity, execute_code  

PORT = 8000 

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/analyze':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            code = data['code']

            complexity, explanation = analyze_complexity(code)
            execution_time = execute_code(code)

            response_data = {
                'complexity': complexity,
                'explanation': explanation,
                'execution_time': execution_time,
                'error': None 
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))


        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')


handler = MyHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()