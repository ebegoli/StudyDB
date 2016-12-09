import re


#TODO: Examine the regex approach. That might be the regex-based, concise alernative to this approach.
# http://stackoverflow.com/questions/16672539/regular-expression-to-extract-sql-query


def split_if_not_none(list,delim):
        if list:
                return list.split(delim)
        else:
                return []

def parse_projection(expression):
        """ parsing something like "select a.a,b.b,c from a,b where a.a = b.a;" """
        p = re.compile('select\s+(.*?)\s*from\s+(.*?)\s*(where\s(.*?)\s*)?;')
        m = p.match(expression)
        columns = split_if_not_none( m.group(1),",")
        tables = split_if_not_none(m.group(2),",")
        clauses = split_if_not_none(m.group(4),"and")
        return {"columns":columns,"tables":tables,"clauses":clauses}


def parse_deletion(expression):
        """ parsing something like "delete from a where a = 30;" """
        p = re.compile('delete\s+from\s+(.*?)\s*(where\s(.*?)\s*)?;')
        m = p.match(expression)
        tables = split_if_not_none(m.group(1),",")
        clauses = split_if_not_none(m.group(3),"and")
        return {"tables":tables,"clauses":clauses}


def parse_update(expression):
        """ parsing something like "update some_table set (x,y,z) where a = 30;" """
        p = re.compile('update\s+(.*?)set(.*?)\s*(where\s(.*?)\s*)?;')
        m = p.match(expression)
        tables = m.group(1)
        columns = split_if_not_none(m.group(2), ",")
        clauses = split_if_not_none(m.group(4), "and")
        return {"tables": tables, "columns":columns, "clauses": clauses}


def parse_insert(expression):
    """ parsing something like "insert into some_table(a,b,c) values ("A","B","C");" """
    p = re.compile('insert\s+into\s+(.*?)(\((.*?)\))?\s+values\((.*?)\)\s*;')
    m = p.match(expression)
    tables = m.group(2)
    print "tables: ", tables
    columns = split_if_not_none(m.group(3), ",")
    print "columns: ",columns
    values = split_if_not_none(m.group(4), ",")
    print "values: ", values
    return {"tables": tables, "columns": columns, "values":values}


if __name__ == '__main__':
    print parse_deletion("delete from a where a = 30;")
    print parse_update("update a set a.a=30, a.b=\"A\" where a=10;")
    print parse_insert("insert into a(a,b) values(3,\"B\");")



