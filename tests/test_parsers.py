import unittest

from studydb.parsers import *


''''

Postgres parsing:
https://www.postgresql.org/docs/current/static/parser-stage.html

Oracle parsing:
See https://docs.oracle.com/database/121/TGSQL/tgsql_sqlproc.htm#TGSQL186

Parsing Exercise:
Implement full Postgres gram.y and scan.l parser and scanner
https://github.com/postgres/postgres/tree/master/src/backend/parser
in Python using PLY:
http://www.dabeaz.com/ply/

'''

class TestParsers(unittest.TestCase):

    def test_projection(self):
        expression = "select a.a,b.b,c from a,b where a.a = b.a;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,ProjectionParser),"Did not get the projection parser.")
        objects = parser.get_query_plan()
        print objects

    def test_insertion(self):
        expression = "insert into table values;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,InsertionParser),"Did not get the insert parser.")

    def test_update(self):
        expression = "update table set;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,UpdateParser),"Did not get the update parser.")

    def test_deletion(self):
        expression = "delete from;"
        parser = SQLParser.get(expression)
        self.assertTrue(isinstance(parser,DeletionParser),"Did not get the delete parser.")

if __name__ == '__main__':
    unittest.main()