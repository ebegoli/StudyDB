class SQLParser(object):
    def __init__(self,expression):
        pass

    @staticmethod
    def get(expression):
        # type: () -> object
        if expression.lower().strip().startswith("select"):
            return ProjectionParser(expression)

class ProjectionParser(SQLParser):
    pass


class InsertionParser(SQLParser):
    pass

class UpdateParser(SQLParser):
    pass

if __name__ == '__main__':
    instance = SQLParser.get("Select * from some_table;")
    print type(instance)


