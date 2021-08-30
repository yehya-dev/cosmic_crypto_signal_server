from pony import orm

db = orm.Database()
orm.set_sql_debug(True)
db.bind(
    provider="postgres",
    user="qvxdducteeqqaq",
    password="431bad48ed80520606e6efd0b3e4350f8b6473cdf02e68f3b8d521c34e646018",
    host="ec2-54-155-87-214.eu-west-1.compute.amazonaws.com",
    database="dbitb00hnfh373",
)


def delete_entries():
    with orm.db_session:
        db.execute("""DELETE FROM future;DELETE FROM spot;""")
        print("deleted everything bijes!!")


def show_entries():
    with orm.db_session:
        cursor = db.execute("""SELECT * FROM spot ORDER BY created_at""")
        for item in cursor:
            print(item[:2] + item[3:-1])


# import this module and then run the required functions on the shell
