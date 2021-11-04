import random

import pymysql


from utils import rand_sql_bool, rand_upper_lower_string, timeitutil


class RandomSqlLoadTest:
    test_start_time = None
    test_end_time = None
    sqls = []

    db_host = None
    db_user = None
    db_password = None
    db_name = None
    db_port = None
    table_name = 'RANDOMSQLLOADTEST'

    def populate_sqls(self, no_of_iterations
                      ):
        for _ in range(no_of_iterations):
            rand_str = rand_upper_lower_string(random.randrange(1, 50))
            rand_float = random.uniform(1, 1000)
            rand_bool = rand_sql_bool()
            self.sqls.append(
                f"insert into {self.table_name}(msg,status,value) values('{rand_str}',{rand_bool},{rand_float})"
            )
            # print(self.sqls)

    def __init__(self, no_of_iterations):
        print("No of Iterations", no_of_iterations)
        print("Generating sqls started")
        self.populate_sqls(no_of_iterations=no_of_iterations)
        print("Generating sqls completed")

    @timeitutil
    def execute_sqls(self):
        # create db connection
        print("Db connection creation started")
        connection = pymysql.connect(host='127.0.0.1',
                                     user='clientuser',
                                     password='clientuser',
                                     database='performancetestdb',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True)
        print("Db connection creation completed")

        create_table_script = f"CREATE TABLE  IF NOT EXISTS {self.table_name}(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, msg varchar(100) COLLATE utf32_unicode_ci NOT NULL,status tinyint(1) NOT NULL,value float NOT NULL) ENGINE = InnoDB DEFAULT CHARSET = utf32 COLLATE = utf32_unicode_ci "
        cursor = connection.cursor()
        print("Table creation starting ")
        cursor.execute(create_table_script)
        print("Table creation completed")
        print("Sql execution starting")
        for idex, sql in enumerate(self.sqls):
            if(idex % 1000) == 0:
                print(f"Inserted {idex+1} rows.")
            cursor.execute(sql)
        print("Sql execution completed")
        cursor.execute(
            f'select count(*) from {self.table_name}')
        print('Total Rows', cursor.fetchone())

    def start(self):
        self.execute_sqls()
