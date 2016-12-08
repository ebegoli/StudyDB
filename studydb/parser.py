import re


#TODO: Examine the regex approach. That might be the regex-based, concise alernative to this approach.
# http://stackoverflow.com/questions/16672539/regular-expression-to-extract-sql-query


def parse_projection(expression):
        p = re.compile('select\s+(.*?)\s*from\s+(.*?)\s*(where\s(.*?)\s*)?;')
        m = p.match(expression)
        columns = m.group(1)
        tables = m.group(2)
        clauses = m.group(4)
        return {"columns":columns,"tables":tables,"clauses":clauses}


