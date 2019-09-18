'''
    Tests for CSV processing lib
'''
import os
import unittest
import pytest
from csv_utils import CSVParser

RESOURCE_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class TestCSVProcessing(unittest.TestCase):
    '''
        CSV processing tests using Pytest and unittest libs
    '''
    valid_parser = CSVParser(RESOURCE_BASE_DIR + '/resources/AppleStore.csv')
    invalid_parser = CSVParser(None)

    def test_top_size_invalid_parser(self):
        with pytest.raises(Exception) as error:
            assert self.invalid_parser.top_n(1, 1, 'News')
        assert str(error.value) == "Invalid file"

    def test_top_n_invalid_inputs(self):
        with pytest.raises(Exception) as error:
            assert self.valid_parser.top_n(0, 1, 'News')
        assert str(error.value) == "Invalid size"

        with pytest.raises(Exception) as error:
            assert self.valid_parser.top_n(1, -1, 'News')
        assert str(error.value) == "Invalid lambda index"

        with pytest.raises(Exception) as error:
            assert self.valid_parser.top_n(1, 1)
        assert str(error.value) == "Invalid categories"

    def test_top_size(self):
        top_five = self.valid_parser.top_n(5, 6, 'News')
        len(top_five) == 5
        for app in top_five:
            assert app['type'] == 'News'

    def test_top_one_news(self):
        top_one = self.valid_parser.top_n(1, 6, 'News')
        assert top_one[0]['name'] == 'Twitter'
        assert int(top_one[0]['count']) == 354058
        assert top_one[0]['type'] == 'News'

    def test_top_ten_books_and_music(self):
        top_ten = self.valid_parser.top_n(10, 6, 'Music', 'Book')

        # Should have 10 items
        assert len(top_ten) == 10

        # Should be ordered by count
        for i in range(len(top_ten) - 1):
            assert int(top_ten[i]['count']) >= int(top_ten[i + 1]['count'])

        # Should have 'Pandora - Music & Radio' as top #1
        assert top_ten[0]['name'] == 'Pandora - Music & Radio'

        # Should have only Music and Book as type
        types = list(set(map(lambda row: row['type'], top_ten)))
        types.sort()
        assert types == ['Book', 'Music']
