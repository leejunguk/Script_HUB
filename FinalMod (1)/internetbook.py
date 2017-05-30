# -*- coding: cp949 -*-
#OpenAPI �� ���õ� �͵�
from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

#################�߰�
import os
import sys
import urllib.request



##global
conn = None
itemElements = None
#����api
regKey = 'XhKqnYiL44B3YdVVzKn2K2HUJ0tJJMUAAveunEp5YXfcfJhkpnUmo98E%2FlRE1X5CjqWTRCstJYzKwAHNCZ8lVQ%3D%3D'

# ���̹� OpenAPI ���� ���� information
#server = "openapi.naver.com"

# ���� OpenAPI ���� ���� information
server = "apis.data.go.kr"


# smtp ����
host = "smtp.gmail.com" # Gmail SMTP ���� �ּ�.
port = "587"

def userURIBuilder(server,**user):
    str = "https://" + server + "/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

#����κ� ����
def getBookDataFromName(name):

    global server, regKey, conn
    encText = urllib.parse.quote(name)
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, servicekey=regKey, QN=encText, numOfRows="1000")
    conn.request("GET", uri)

    # �Ľ� �߰��ڵ�
    # request = urllib.request.Request(uri)
    # response = urllib.request.urlopen(request)
    # rescode = response.getcode()

    req = conn.getresponse()

    print(req.status)
    if int(req.status) == 200:  # okay
        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def getBookDataFromISBN1(address):
    global server, regKey, conn

    encText = urllib.parse.quote(address)

    if conn == None :
        connectOpenAPIServer()
    #uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, servicekey=regKey, Q0 =  encText, numOfRows = "1000")
    conn.request("GET", uri)

    #�Ľ� �߰��ڵ�
    #request = urllib.request.Request(uri)
    #response = urllib.request.urlopen(request)
    #rescode = response.getcode()

    req = conn.getresponse()


    print (req.status)
    if int(req.status) == 200 : #okay
        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None

def getBookDataFromISBN(address,name):
    global server, regKey, conn

    encText = urllib.parse.quote(address)
    encText2 = urllib.parse.quote(name)

    if conn == None :
        connectOpenAPIServer()
    #uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, servicekey=regKey, Q0 =  encText, QN = encText2, numOfRows = "1000")
    conn.request("GET", uri)

    #�Ľ� �߰��ڵ�
    #request = urllib.request.Request(uri)
    #response = urllib.request.urlopen(request)
    #rescode = response.getcode()

    req = conn.getresponse()


    print (req.status)
    if int(req.status) == 200 : #okay
        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None


def SearchData(Addr):
    global server, regKey, conn
    if conn == None :
        connectOpenAPIServer()

    for i in range(69):
        #for j in range(1000):
        uri = userURIBuilder(server, servicekey = regKey, pageNo = str(i + 1), numOfRows = "1000")
        conn.request("GET", uri)
        req = conn.getresponse()

        if int(req.status) == 200:  # okay
            print("Book data downloading complete!")
            return  extractHospitalData(req.read(), Addr)
        else:
            print("OpenAPI request has been failed!! please retry")
            return None


def extractHospitalData(strXml,Addr):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    itemElements = tree.getiterator("item")



    for item in itemElements:
        ItemAddr = item.find("dutyAddr")
        str(ItemAddr).split()
    print(Addr)

    #for item in itemElements:
    #    if

def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print (strXml)
    #print("�����")
    # Book ������Ʈ�� �����ɴϴ�.

    global itemElements
    itemElements = tree.getiterator("item")  # return list type
    strXml.decode('utf-8')
    print(itemElements)
    cnt =0
    #������ 69000������ rum = 69���� ����
    for item in itemElements:
        BigAdress = item.find("dutyAddr")  # ��
        #SmallAdress = item.find("Q1")  # ��
        QZ = item.find("dutyName")  #  B : ���� C : �ǿ�
        QD = item.find("QD")  #  �𸣰�����
        Tel = item.find("dutyTel1")  # ���ϴ³�
        #HospitalName = item.find("QN")  # �����̸�


        weekdaySTime = item.find("dutyTime1s")    # ���� ���۽ð�
        weekdayETime = item.find("dutyTime1c")    # ���� �����½ð�

        weekendSTime = item.find("dutyTime6s")     # ����� ���� ���۽ð�
        weekendETime = item.find("dutyTime6c")     # ����� ���� �����½ð�

        weekendSTimeH = item.find("dutyTime7s")    # �Ͽ��� ���� ���۽ð�
        weekendETimeH = item.find("dutyTime7c")    # �Ͽ��� ���� �����½ð�

        HolidaySTime = item.find("dutyTime8s")    #������ ���� ���۽ð�
        HolidayETime = item.find("dutyTime8c")    #������ ���� �����½ð�

        #Num = item.find("rnum")

        print("�̸�:",QZ.text)
        print("�ּ�:",BigAdress.text)
        print("��ȭ��ȣ:",Tel.text)
        if weekdaySTime ==None or weekdayETime == None :
            pass
        else:
            print("���� ���� ���۽ð�:",weekdaySTime.text, "���� ���� ���� �ð� ",weekdayETime.text)

        if weekendSTime == None or weekendETime == None :
            pass
        else:
            print("����� ���� ���۽ð�:",weekendSTime.text, "����� ���� ���� �ð� ",weekendETime.text)
        if weekendSTimeH == None or weekendETimeH == None:
            pass
        else:
            print("�Ͽ��� ���� ���۽ð�:", weekendSTimeH.text, "�Ͽ��� ���� ���� �ð� ", weekendETimeH.text)
        if HolidaySTime==None or HolidayETime == None:
           pass
        else:
            print("�Ͽ��� ���� ���۽ð�:", HolidaySTime.text, "�Ͽ��� ���� ���� �ð� ", HolidayETime.text)
        cnt = cnt +1
        print(cnt)
        print(" ")


def sendMain():
    global host, port
    html = ""
    title = str(input ('Title :'))
    senderAddr = str(input ('sender email address :'))
    recipientAddr = str(input ('recipient email address :'))
    msgtext = str(input ('write message :'))
    passwd = str(input (' input your password of gmail account :'))
    msgtext = str(input ('Do you want to include book data (y/n):'))
    if msgtext == 'y' :
        keyword = str(input ('input keyword to search:'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
    
    import mysmtplib
    # MIMEMultipart�� MIME�� �����մϴ�.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    #Message container�� �����մϴ�.
    msg = MIMEMultipart('alternative')

    #set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset = 'UTF-8')
    
    # �޼����� ������ MIME ������ ÷���մϴ�.
    msg.attach(msgPart)
    msg.attach(bookPart)
    
    print ("connect smtp server ... ")
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)    # �α��� �մϴ�. 
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    
    print ("Mail sending complete!!!")

class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        from urllib.parse import urlparse
        import sys
      
        parts = urlparse(self.path)
        keyword, value = parts.query.split('=',1)

        if keyword == "title" :
            html = MakeHtmlDoc(SearchBookTitle(value)) # keyword�� �ش��ϴ� å�� �˻��ؼ� HTML�� ��ȯ�մϴ�.
            ##��� �κ��� �ۼ�.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8')) #  ����( body ) �κ��� ��� �մϴ�.
        else:
            self.send_error(400,' bad requst : please check the your url') # �� ���� ��û��� ������ �����Ѵ�.
        
def startWebService():
    try:
        server = HTTPServer( ('localhost',8080), MyHandler)
        print("started http server....")
        server.serve_forever()
        
    except KeyboardInterrupt:
        print ("shutdown web server")
        server.socket.close()  # server �����մϴ�.

def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True
