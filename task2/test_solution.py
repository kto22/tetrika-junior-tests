import unittest
from unittest.mock import patch, MagicMock
from solution import get_page_content, parse_animals, save_counts_to_csv
import os
import csv

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_html = """
        <div class="mw-category mw-category-columns">
            <ul>
                <li><a href="/wiki/Акула">Акула</a></li>
                <li><a href="/wiki/Бабочка">Бабочка</a></li>
                <li><a href="/wiki/Волк">Волк</a></li>
                <li><a href="/wiki/Гепард">Гепард</a></li>
            </ul>
        </div>
        <a href="/wiki/Категория:Животные_по_алфавиту?pagefrom=Гепард">Следующая страница</a>
        """
        self.test_html_last_page = """
        <div class="mw-category mw-category-columns">
            <ul>
                <li><a href="/wiki/Ящерица">Ящерица</a></li>
            </ul>
        </div>
        """

    @patch('solution.get_page_content')
    def test_parse_animals(self, mock_get_content):
        mock_get_content.side_effect = [self.test_html, self.test_html_last_page]
        
        counts = parse_animals("http://test.com")
        
        self.assertEqual(counts['А'], 1)
        self.assertEqual(counts['Б'], 1)
        self.assertEqual(counts['В'], 1)
        self.assertEqual(counts['Г'], 1)
        self.assertEqual(counts['Я'], 1)
        self.assertEqual(len(counts), 5)

if __name__ == '__main__':
    unittest.main()
