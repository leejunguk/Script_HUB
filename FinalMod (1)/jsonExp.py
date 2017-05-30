from urllib.parse import urlparse

#? 뒤에 나오는 것들은 쿼리
url = "http://search.naver.com/search.naver?where=nexearch&query=python&sm=top_hty&fbm=1"
parts = urlparse(url)
print(parts)




