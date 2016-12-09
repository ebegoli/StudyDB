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


