import re

class SQLParser(object):


#TODO: Examine the regex approach. That might be the regex-based, concise alernative to this approach.
# http://stackoverflow.com/questions/16672539/regular-expression-to-extract-sql-query

    def __init__(self,source_expression):
        self.expression = source_expression
        self.parsed_query = {"source_tables":[],"target_tables":[],"conditons":[],
                             "values":[],"ordering":[],"grouping":[]}

    @staticmethod
    def get(expression):
        # type: () -> object
        if expression.lower().strip().startswith("select"):
            return ProjectionParser(expression)
        if expression.lower().strip().startswith("insert"):
            return InsertionParser(expression)
        if expression.lower().strip().startswith("update"):
            return UpdateParser(expression)

    def get_query_plan(self):
        pass

class ProjectionParser(SQLParser):

    def get_query_plan(self):
        p = re.compile('select (.*) from (.*) (where (.*))?;')
        m = p.match(self.expression)
        columns = m.group(1)
        table = m.group(2)
        clause = m.group(4)
        return (columns,table,clause)

class DeletionParser(SQLParser):
    pass

class InsertionParser(SQLParser):
    pass

class UpdateParser(SQLParser):
    pass



