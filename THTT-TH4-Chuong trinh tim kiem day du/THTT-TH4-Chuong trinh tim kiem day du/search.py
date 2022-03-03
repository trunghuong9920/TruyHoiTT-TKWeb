from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
 
# Mở chỉ mục đã xây dựng trước đây
ix = open_dir('indexdir')

# Yêu cầu người dùng nhập vào xâu truy vấn
query_str = input('Enter a query string: ')

# Các văn bản được chấm điểm theo số lần xâu truy vấn xuất hiện
# trong mỗi văn bản.
with ix.searcher(weighting=scoring.Frequency) as searcher:
    # Tìm kiếm trong trường content
    query = QueryParser('content', ix.schema).parse(query_str)
    results = searcher.search(query)
    
    # Số kết quả trả về
    num_results = len(results)
    
    if (num_results == 0):
        print('No results')
    else:	
        # Hiện các kết quả, mỗi dòng gồm số thứ tự, tiêu đề, điểm số
        for i in range(len(results)):
            print(i, results[i]['title'], str(results[i].score))
        
        # Yêu cầu người dùng chọn kết quả muốn xem chi tiết
        k = int(input('Which result do you want to show? '))
        
        # Mở và hiển thị nội dung file tương ứng với kết quả đã chọn
        fp = open(results[k]['path'], 'r')
        print()
        print(fp.read())    
        fp.close()
