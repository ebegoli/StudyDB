import unittest

from studydb.query_parser import *


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
        print expression
        objects = parse_projection(expression)
        print objects
        self.assertIn("a.a",objects["columns"])
        self.assertIn("b.b",objects["columns"])
        self.assertIn("c",objects["columns"])
        self.assertIn("a",objects["tables"])
        self.assertIn("b",objects["tables"])
        self.assertNotIn(";",objects["clauses"])
        self.assertIn("a.a = b.a",objects["clauses"])

        expression = "select a.a,b.b,c from a,b;"
        print expression
        objects = parse_projection(expression)
        print objects
        self.assertIn("a.a",objects["columns"])
        self.assertIn("b.b",objects["columns"])
        self.assertIn("c",objects["columns"])
        self.assertIn("a",objects["tables"])
        self.assertIn("b",objects["tables"])
        self.assertNotIn(";",objects["clauses"])
        self.assertEquals(objects["clauses"],[])
        self.assertNotIn(";", objects["tables"])

    def test_delete_parsing(self):
        expression = "delete from a where a = 30;"
        print expression
        objects = parse_deletion(expression)
        print objects
        self.assertIn("a", objects["tables"])
        self.assertIn("a = 30", objects["clauses"])

        expression = "delete from a;"
        print expression
        objects = parse_deletion(expression)
        print objects
        self.assertIn("a", objects["tables"])
        self.assertNotIn(";", objects["tables"])
        self.assertEquals(objects["clauses"],[])

    def test_update_parsing(self):
        expression = "update a set a.a=30, a.b=\"A\" where a=10;"
        print expression
        objects = parse_update(expression)
        print objects
        self.assertIn("a", objects["tables"])
        self.assertIn("a=10", objects["clauses"])
        self.assertIn("a.a=30", objects["column_values"])
        self.assertIn("a.b=\"A\"", objects["column_values"])

        expression = "update a set a.a=30, a.b=\"A\";"
        print expression
        objects = parse_update(expression)
        print objects
        self.assertIn("a", objects["tables"])
        self.assertIn("a.b=\"A\"", objects["column_values"])
        self.assertIn("a.a=30", objects["column_values"])

    """
    print parse_deletion("delete from a where a = 30;")
    print parse_update("update a set a.a=30, a.b=\"A\" where a=10;")
    print parse_insert("insert into a(a,b) values(3,\"B\");")
    print parse_create_table("creatE table xyz (some type(12), some2 type(12));")
    print parse_drop_table("drop table abc;")
    print parse_alter_table("alter table abc add   xyz date;")
    print parse_alter_table("alter Table abc alter  column xyz string;")
    print parse_alter_table("alter table abc drop column    xyz;")
    """

if __name__ == '__main__':
    unittest.main()