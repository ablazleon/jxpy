#!/usr/bin/python

from http.server import BaseHTTPRequestHandler

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        output = 'v1 - This is Adrian'
        self.wfile.write(output.encode('utf-8'))
        return
