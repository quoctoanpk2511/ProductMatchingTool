from base.utils.writers import FileWriter, DBWriter
import sqlalchemy

class CSVWriter(FileWriter):

    def write(self):
        self.dataset.df.to_csv(self.file_name, encoding='utf-8', index=False)

class MySQLWriter(DBWriter):

    def connect(self):
        return sqlalchemy.create_engine("mysql://{user}:{pw}@{host}/{db}".format(host=self.db_host, db=self.db_name, user=self.db_user, pw=self.db_passwd))

    def write(self, table_name):
        self.dataset.df[self.dataset.df.columns.difference(['id_left', 'id_right'])].to_sql(table_name, con=self.connect(), if_exists='append', index=False)
