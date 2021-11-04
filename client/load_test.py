
import pymysql

from random_sql_load_test import RandomSqlLoadTest

# Check db connectivity
print("Hello")


def check_db_connectivity():
    print("Connecting db")

    connection = pymysql.connect(host='127.0.0.1',
                                 user='clientuser',
                                 password='clientuser',
                                 database='performancetestdb',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("Db connection successful")


if __name__ == '__main__':
    check_db_connectivity()
    test = RandomSqlLoadTest(100000)
    test.start()
