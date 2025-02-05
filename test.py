import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.algumon.com/category/2', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 모든 품목을 선택
items = soup.select('li[id^="post-"]')

product_list = []

for item in items:
    # 종료된 품목인지 확인
    end_tag = item.select_one('div.label-box > span.label.end')
    if end_tag:
        continue  # 종료된 품목은 건너뜀
    
    # 제품 이름 추출
    name_tag = item.select_one('span.primary-font.item-name a')
    product_name = name_tag.get_text(strip=True) if name_tag else 'N/A'
    
    # 가격 추출
    price_tag = item.select_one('p.deal-price-info small.product-price')
    price = price_tag.get_text(strip=True) if price_tag else 'N/A'
    
    # 카테고리 초기화 (나중에 분류할 예정)
    category = ''
    
    # 리스트에 추가
    product_list.append([product_name, price, category])
print(product_list)