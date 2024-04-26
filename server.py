from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 80  #Choose your own port, just make sure not to choose a port that is currently running an active service

httpd = HTTPServer(("", PORT), CGIHTTPRequestHandler)
print(f"Your server is running on your localhost @: {PORT}")
httpd.serve_forever()#This runs the server
