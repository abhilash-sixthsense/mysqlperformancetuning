
import pymysql

from random_sql_load_test import RandomSqlLoadTest
from multiprocessing import Pool

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


def run_test(size):
    test = RandomSqlLoadTest(size)
    test.start()


if __name__ == '__main__':
    check_db_connectivity()
    p_count = 50
    pargs = [1000 for _ in range(p_count)]
    with Pool(p_count) as p:
        p.map(run_test, pargs)
