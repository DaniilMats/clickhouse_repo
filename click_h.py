from clickhouse_driver import Client


def get_connection(host='localhost', password='root'):
    client = Client(host=host, password=password)
    return client


if __name__ == "__main__":
    show_db_query = "SHOW DATABASES"""
    create_test_query = "CREATE TABLE IF NOT EXISTS test (x Int32, y String) ENGINE = Memory"
    drop_table_query = "DROP TABLE IF EXISTS test"
    insert_to_test_query = f"INSERT INTO test VALUES"
    select_all_query = "SELECT * FROM test"

    client = get_connection()
    client.execute(drop_table_query)
    client.execute(create_test_query)
    client.execute(insert_to_test_query, [{'x': 1, 'y':"test1"}, {'x': 2, 'y':"test2"}, {'x': 3, 'y':"test3"}, {'x': 100, 'y':"test4"}])

    print(client.execute(select_all_query))

    # print(client.execute(show_db_query))
