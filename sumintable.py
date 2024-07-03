from bs4 import BeautifulSoup

with open ('D:/python/PyCharm/MyStudy/study2/3.html') as f:
    html = f.read()



soup = BeautifulSoup(html, 'html.parser')
print(sum(int(item.get_text()) for item in soup.find_all('td')))