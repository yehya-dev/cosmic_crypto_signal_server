from typing import List
from pony import orm
from models import Spot, Future, db_init

from typing import Type, Iterator, Union
from _schema import SpotSchema, FutureSchema, SignalSchema

from logger import logger

db_init()  # Initialize the database, call this only once


def handle_signals(data: SignalSchema):
    logger.info(f"Handle data func")
    spots = data.spots
    spot_insight = _get_signals_diff_data(spots, Spot)

    # db_map = spot_insight["db_map"]
    request_map = spot_insight["request_map"]

    new_set = spot_insight["new_set"]
    with orm.db_session:
        for spot_id in new_set:
            Spot(**request_map[spot_id].dict())
            logger.info(f"New signal: {spot_id}")
        # TODO Call function that sends a request to bot server (new)

    update_set = spot_insight["update_set"]
    with orm.db_session:
        for spot_id in update_set:
            Spot[spot_id].set(**request_map[spot_id].dict())
        # TODO Call function that sends a request to bot server (update)

    removed_set = spot_insight["removed_set"]
    with orm.db_session:
        for spot_id in removed_set:
            Spot[spot_id].delete()
            logger.info(f"Signal Removed: {spot_id}")

        # TODO Call function that sends a request to bot server (remove)


@orm.db_session
def _get_signals_diff_data(
    data: Union[List[SpotSchema], List[FutureSchema]],
    model: Union[Type[Spot], Type[Future]],
):
    db_data = orm.select(item for item in model).order_by(model.created_at)[:]

    request_map = _create_id_maps(data)
    db_map = _create_id_maps(db_data)

    request_set = set(request_map)
    db_set = set(db_map)

    new_set = request_set.difference(db_set)
    removed_set = db_set.difference(request_set)
    update_set = request_set.difference(new_set)
    return {
        "db_map": db_map,
        "request_map": request_map,
        "new_set": new_set,
        "removed_set": removed_set,
        "update_set": update_set,
    }


def _create_id_maps(data: Union[List[SpotSchema], Iterator[Type[Spot]]]):
    _map = dict()
    for item in data:
        _map[item.spot_id] = item
    return _map
