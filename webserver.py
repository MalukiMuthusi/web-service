# P15/81741/2017
from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import xml.etree.ElementTree as ET

"""
I am going to create an XML structure that has
    <root_xml>
        <num1></num1>
        <num2></num2>
        <sum></sum>
    </root_xml>
"""
root_xml = ET.Element('root_xml')
num1 = ET.SubElement(root_xml, 'addition')
num2 = ET.SubElement(root_xml, 'sum')
sum = ET.SubElement(root_xml, 'num')
num1.set('name','num1')
num2.set('name','num2')
sum.set('name','sum')

"""
Create a web service that listens at port 8080 on local host
"""
print("Listening at port :8080")
class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/xml')
        self.end_headers()
        gets = self.path
        first = re.findall('/?first=([0-9]+)', gets)
        second = re.findall('&second=([0-9]+)', gets)
        num1.text = first[0]
        num2.text = second[0]
        sum.text = str(int(first[0]) + int(second[0]))
        mydata = ET.tostring(root_xml)
        with open("addition.xml", "wb") as myfile:
            myfile.write(mydata)
        with open('addition.xml', 'r') as file: 
            self.wfile.write(file.read().encode('utf-8'))


myServer = HTTPServer(('localhost', 8080), MyServer)
myServer.serve_forever()
myServer.server_close()
