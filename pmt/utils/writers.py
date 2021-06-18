from matchingframework.utils.writers import FileWriter, DBWriter
import sqlalchemy
import MySQLdb

class CSVWriter(FileWriter):

    def write(self):
        self.dataset.df.to_csv(self.file_name, encoding='utf-8', index=False)

class MySQLWriter(DBWriter):


    def connect(self):
        return MySQLdb.connect(self.db_host, self.db_user, self.db_passwd, self.db_name)

    def write(self, table_name):
        self.dataset.df[self.dataset.df.columns.difference(['id_left', 'id_right'])].to_sql(table_name, con=self.connect(), if_exists='append', index=False)

    def update(self, table_name, pk):
        con = self.connect()
        cursor = con.cursor()
        cursor.execute("SHOW columns FROM {}".format(table_name))
        if 'match_cluster_id' not in [column[0] for column in cursor.fetchall()]:
            cursor.execute("ALTER TABLE {} ADD match_cluster_id INT(20)".format(table_name))
        for i in range(0, len(self.dataset.df)):
            id = self.dataset.df._get_value(i, pk)
            cluster_id = self.dataset.df._get_value(i, 'match_cluster_id')
            sql = "UPDATE {} SET match_cluster_id = {} WHERE {} = {}".format(table_name, cluster_id, pk, id)
            cursor.execute(sql)
        con.commit()
        cursor.close()
