from operator import le
from re import I
from tkinter import Y
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.index import open_dir
import os
from whoosh.qparser import QueryParser
from whoosh.query import *
schema = Schema(title=TEXT(stored=True), path=ID(stored=True),content=TEXT)         #Tạo lược đồ cho chỉ mục
if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)
ix = open_dir("index")

writer = ix.writer()
writer.add_document(title="First document", path="/a",
content="This is the first document we've added!")
writer.add_document(title="Second document", path="/b",
content="The second one is the even more interesting!")
writer.add_document(title="The Stilled Patter", path="/c",
content="George Washington was the father of his country.I am not George Washington. My name is Andrew Jones, and it is because of me there will be no more Joneses in the world. There will be, in fact, no more anybody.")
writer.commit()

def searchAnd(q):
    print("Câu truy vấn là: ",q)
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema)
        querystring = query.parse(q)

        results = searcher.search(querystring)
        print("Số lượng văn bản trả về: ",len(results))
        print("Các văn bản trả về: ",results[0:])
    
def searchOr(q):
    qr = ''
    for i in q.split():
        if(qr == ''):
            qr += i
        else:
            qr += ' OR' + ' ' + i
    print("Câu truy vấn là: ",qr)
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema)
        querystring = query.parse(qr)
        # querystring = query.parse("first OR (content:one)")

        results = searcher.search(querystring)
        print("Số lượng văn bản trả về: ",len(results))
        print("Các văn bản trả về: ",results[0:])
    
def searchNot(q):
    qr = ''
    if(len(q.split()) == 1):                    #Kiểm tra là 1 từ
        qr += 'NOT '+ q
    elif(len(q.split()) > 1):
        dem = 1;
        for i in q.split():
            if(dem < len(q.split())):           #kiểm tra là từ cuối cùng
                if(qr == ''):
                    qr += 'NOT ('  + i + ' OR '   
                else:
                    qr += i + ' OR '
            if(dem == len(q.split())):
                qr += i + ')'
            dem += 1
        
    print("Câu truy vấn là: ",qr)
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema)
        querystring = query.parse(qr)

        results = searcher.search(querystring)
        print("Số lượng văn bản trả về: ",len(results))
        print("Các văn bản trả về: ",results[0:])

check = 'y'
while (check == 'y'):
    print("Tìm các văn bản thỏa mãn. Lựa chọn:")
    print("'1' Chứa tất cả các từ.")
    print("'2' Chứa ít nhất một trong các từ.")
    print("'3' Không chứa các từ.")
    option = input("Nhập lựa chọn = ")
    if(option == '1'):
        q = input("Từ cần tìm kiếm: ")
        searchAnd(q)
    if(option == '2'):
        q = input("Từ cần tìm kiếm: ")
        searchOr(q)
    if(option == '3'):
        q = input("Từ cần tìm kiếm: ")
        searchNot(q)
    elif(option < '1' or option > '3'):
        print("Nhập sai lựa chọn!")
    check = input("Nhấn y tiếp tục: ")
