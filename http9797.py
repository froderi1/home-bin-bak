#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os

#folgende Zeilen werden gebraucht wenn dir beiden dirs mittels tempfs im RAM gehalten werden
#os.system("sudo chmod 777 /var/www/upload")
#os.system("sudo chmod 777 /home/frank/www")
#os.system("sudo chown ftpuser:ftpuser /var/www/upload")
#os.system("sudo chown frank:frank /home/frank/www")
#os.system("sudo chmod +s /var/www/upload")
#os.system("sudo chmod +s /home/frank/www")
#os.system("sudo cp /home/frank/www_bak/index.html /home/frank/www")


os.chdir("/home/frank/www")

PORT = 9797
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()

