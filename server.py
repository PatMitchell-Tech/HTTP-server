from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8000  # You can choose any port number (above 1024)

httpd = HTTPServer(("", PORT), CGIHTTPRequestHandler)
print(f"Serving at port {PORT}")
httpd.serve_forever()
