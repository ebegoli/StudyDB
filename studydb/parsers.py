class SQLParser(object):

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
    pass

class DeletetionParser(SQLParser):
    pass

class InsertionParser(SQLParser):
    pass

class UpdateParser(SQLParser):
    pass



