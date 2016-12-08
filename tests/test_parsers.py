import unittest

from studydb.parser import *


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

class TestParser(unittest.TestCase):

    def test_projection_parsing(self):
        expression = "select a.a,b.b,c from a,b where a.a = b.a;"
        objects = parse_projection(expression)
        print objects
        expression = "select a.a,b.b,c from a,b;"
        objects = parse_projection(expression)
        print objects


if __name__ == '__main__':
    unittest.main()