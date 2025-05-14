from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import urlparse, parse_qs

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_POST(self):
        # Handle form submission from the login page
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)

        # Check credentials (a basic example, replace with your authentication logic)
        if parsed_data.get('username', [''])[0] == 'user' and parsed_data.get('password', [''])[0] == 'password':
            self.send_response(302)
            self.send_header('Location', '/dashboard')
            self.end_headers()
        else:
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b'Invalid credentials')

if __name__ == "__main__":
    PORT = 8000
    with TCPServer(("127.0.0.1", PORT), MyHandler) as httpd:
        print(f"Serving at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
