
import unittest
import pytest
from lib.csv_processing import *

class TestCSVProcessing(unittest.TestCase):
    parser = CSVParser()
    def test_not_implemented_exception(self):
        with pytest.raises(Exception):
            self.parser.top_n(1, 1, None)
