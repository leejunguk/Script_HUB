# -*- coding: cp949 -*-
loopFlag = 1
from internetbook import*
from tkinter import*
from tkinter import font


import tkinter.messagebox

RenderText = None

def InitTopText():

    TempFont = font.Font(g_Tk, size =20, weight = 'bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text = "[���� ���� ã�� ����]")
    MainText.pack()
    MainText.place(x=20)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',width=23, height=4, borderwidth=14, relief='ridge',yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(0, "��ġ��ݰ˻�")
    SearchListBox.insert(1, "�̸���ݰ˻�")
    SearchListBox.insert(2, "����+�̸���ݰ˻�")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=165)

def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=605, y=200)
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def SearchLibrary():
    pass
    #import http.client
    #from xml.dom.minidom import parse, parseString
    #conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    #conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    #req = conn.getresponse()
    #global DataList
    #DataList.clear()

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="�˻�", command=SearchButtonAction())




    SearchButton.pack()
    SearchButton.place(x=330, y=165)

def SearchButtonAction():
    global RenderText

    print(getBookDataFromName(str(InputLabel)))




#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)")
    print("========Menu==========")
    print("�ּҷ� ���� ã��!! : g")
    print("�̸����� ���� ã��!! : k")
    print("���� + �̸����� ���� ã��!! : s")
    print("========Menu==========")

    
def launcherFunction(menu):
    if menu ==  'l':
       pass
    elif menu == 'g': 
        address = str(input ('ã�� ���� ��ġ�� �Է����ּ���:'))
        ret = getBookDataFromISBN1(address)
    elif menu == 'k':
        name = str(input ('ã�� ������ �̸��� �Է����ּ���:'))
        ret = getBookDataFromName(name)
    elif menu == 's':
        address = str(input('ã�� ���� ��ġ�� �Է����ּ���:'))
        name = str(input('ã�� ������ �̸��� �Է����ּ���:'))
        ret = getBookDataFromISBN(address,name)
    else:
        print ("error : unknow menu key")


g_Tk = Tk()
g_Tk.geometry("400x600+750+200")
DataList = []
InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
g_Tk.mainloop()


def QuitBookMgr():

    global loopFlag
    loopFlag = 0
    BooksFree()
    
##### run #####
while(loopFlag > 0):

    printMenu()


    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)





else:
    print ("Thank you! Good Bye")



