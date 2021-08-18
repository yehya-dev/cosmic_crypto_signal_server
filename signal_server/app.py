from fastapi import FastAPI
from _schema import SignalSchema
from helper import handle_signals

from logger import logger

app = FastAPI()


@app.post(
    "/__add_signal__", include_in_schema=True
)  # TODO Set include_in_schema to false on production
def add_signal(Signal: SignalSchema):
    logger.info("Add signal request")
    handle_signals(Signal)
    return {"status": True}
