from matchingframework.utils.readers import DBReader, FileReader
import pandas as pd
import MySQLdb

class CSVReader(FileReader):

    def read_func(self):
        return pd.read_csv(self.file_name)


class MySQLReader(DBReader):

    def connect(self):
        return MySQLdb.connect(self.db_host, self.db_user, self.db_passwd, self.db_name)

    def read_func(self):
        return pd.read_sql(con=self.connect(), sql=self.sql)
