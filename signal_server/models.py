from pony import orm

# Types
from decimal import Decimal
from datetime import datetime

db = orm.Database()


class Spot(db.Entity):
    spot_id = orm.PrimaryKey(str, auto=False)
    buy_price = orm.Required(Decimal, precision=20, scale=10)
    chart_url = orm.Optional(str)
    created_at = orm.Required(datetime)
    current_price = orm.Optional(Decimal, precision=20, scale=10)
    risk = orm.Required(str)
    pair = orm.Required(str)
    stop_price = orm.Required(Decimal, precision=20, scale=10)
    symbol = orm.Required(str)
    tp1 = orm.Required(Decimal, precision=20, scale=10)
    tp2 = orm.Required(Decimal, precision=20, scale=10)
    tp3 = orm.Required(Decimal, precision=20, scale=10)
    tp_done = orm.Required(int)
    total_tp = orm.Required(int)
    spot_type = orm.Required(str)
    coin_logo_url = orm.Required(str)


class Future(db.Entity):
    future_id = orm.PrimaryKey(str, auto=False)


def db_init(debug=False):
    orm.set_sql_debug(debug)
    # This is required because we don't want this database to be created when we are testing
    db.bind(
        provider="postgres",
        user="qvxdducteeqqaq",
        password="431bad48ed80520606e6efd0b3e4350f8b6473cdf02e68f3b8d521c34e646018",
        host="ec2-54-155-87-214.eu-west-1.compute.amazonaws.com",
        database="dbitb00hnfh373",
    )
    db.generate_mapping(create_tables=True)
