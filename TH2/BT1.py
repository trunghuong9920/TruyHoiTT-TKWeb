from tkinter import Y
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.index import open_dir
import os.path
from whoosh.qparser import QueryParser
from whoosh.query import *
schema = Schema(title=TEXT(stored=True), path=ID(stored=True),

content=TEXT)
if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)
ix = open_dir("index")
writer = ix.writer()
writer.add_document(title="First document", path="/a",
content="This is the first document we've added!")
writer.add_document(title="Second document", path="/b",
content="The second one is the even more interesting!")
writer.commit()

def search(q):
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema)
        querystring = query.parse(q)
        # querystring = query.parse("first OR (content:one)")

        results = searcher.search(querystring)
        print(results[0:])
        print(results)
        print(len(results))

check = 'y'
while (check == 'y'):
    q = input("Từ cần tìm kiếm: ")
    search(q)
    check = input("Nhấn y tiếp tục: ")
