import unittest

from studydb.parsers import *

class TestParsers(unittest.TestCase):

    def test_projection(self):
        expression = "select * from all;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,ProjectionParser))

    def test_insertion(self):
        expression = "insert into table values;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,InsertionParser))

    def test_update(self):
        expression = "update table set;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,UpdateParser))

    def test_deletion(self):
        expression = "delete from;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,DeletionParser))

if __name__ == '__main__':
    unittest.main()