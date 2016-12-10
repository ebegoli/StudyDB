import re

""" Parser for the database queries.  """


def match(expression, pattern):
    p = re.compile(pattern,re.IGNORECASE)
    return p.match(expression)


def split_if_not_none(list, delim):
    if list:
        return list.split(delim)
    else:
        return []


def parse_projection(expression):
    """ parsing something like "select a.a,b.b,c from a,b where a.a = b.a;" """
    m = match(expression, 'select\s+(.*?)\s*from\s+(.*?)\s*(where\s(.*?)\s*)?;')
    columns = split_if_not_none(m.group(1), ",")
    tables = split_if_not_none(m.group(2), ",")
    clauses = split_if_not_none(m.group(4), "and")
    return {"columns": columns, "tables": tables, "clauses": clauses}


def parse_deletion(expression):
    """ parsing something like "delete from a where a = 30;" """
    pattern = 'delete\s+from\s+(.*?)\s*(where\s(.*?)\s*)?;'
    m = match(expression,pattern)
    tables = split_if_not_none(m.group(1), ",")
    clauses = split_if_not_none(m.group(3), "and")
    return {"tables": tables, "clauses": clauses}


def parse_update(expression):
    """ parsing something like "update some_table set (x,y,z) where a = 30;" """
    pattern = 'update\s+(.*?)set(.*?)\s*(where\s(.*?)\s*)?;'
    m = match(expression,pattern)
    tables = m.group(1)
    columns = map(str.strip,split_if_not_none(m.group(2), ","))
    clauses = split_if_not_none(m.group(4), "and")
    return {"tables": tables, "column_values": columns, "clauses": clauses}


def parse_insert(expression):
    """ parsing something like "insert into some_table(a,b,c) values ("A","B","C");" """
    pattern = 'insert\s+into\s+(.*?)(\((.*?)\))?\s+values\((.*?)\)\s*;'
    m = match(expression,pattern)
    tables = m.group(2)
    columns = split_if_not_none(m.group(3), ",")
    values = map(str.strip, split_if_not_none(m.group(4), ","))
    return {"tables": tables, "columns": columns, "values": values}


def parse_create_table(expression):
    pattern = "create\s+table\s+(.*?)\s+\(\s*(.*?)\s*\)\s*;"
    m = match(expression,pattern)
    table = m.group(1)
    columns = split_if_not_none(m.group(2),",")
    return {"table":table,"columns":columns}


def parse_alter_table(expression):
    """ parsing something like "alter table xyz add column a date;" """
    pattern = 'alter\s+table\s+(.*?)\s+(add|drop|alter)(?:\s+column)?\s+(.*?)\s*;'
    m = match(expression,pattern)
    table = m.group(1)
    alter = m.group(2)
    column = m.group(3)
    return {"table":table,"alter":alter,"column":column}


def parse_drop_table(expression):
    """ parsing something like "drop table xyz;" """
    pattern = 'drop\s+table\s+(.*?)\s*;'
    m = match(expression,pattern)
    table = m.group(1)
    return {"table": table}


if __name__ == '__main__':
    print parse_deletion("delete from a where a = 30;")
    print parse_update("update a set a.a=30, a.b=\"A\" where a=10;")
    print parse_insert("insert into a(a,b) values(3,\"B\");")
    print parse_create_table("creatE table xyz (some type(12), some2 type(12));")
    print parse_drop_table("drop table abc;")
    print parse_alter_table("alter table abc add   xyz date;")
    print parse_alter_table("alter Table abc alter  column xyz string;")
    print parse_alter_table("alter table abc drop column    xyz;")
