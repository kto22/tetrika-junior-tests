import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict
import re

def get_page_content(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

def save_counts_to_csv(counts, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        for letter in russian_alphabet:
            if letter in counts:
                writer.writerow([letter, counts[letter]])

def parse_animals(url):
    counts = defaultdict(int)
    while url:
        content = get_page_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        
        category_div = soup.find('div', {'class': 'mw-category mw-category-columns'})
        if category_div:
            items = category_div.find_all('li')
            for item in items:
                animal_name = item.text.strip()
                print(f"{animal_name}")
                first_letter = animal_name[0].upper()
                if re.match('[А-Я]', first_letter):
                    counts[first_letter] += 1
                    save_counts_to_csv(counts, 'result.csv')
        
        next_page = soup.find('a', string='Следующая страница')
        url = f"https://ru.wikipedia.org{next_page['href']}" if next_page else None
    
    return counts

def main():
    start_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    parse_animals(start_url)

if __name__ == '__main__':
    main()
