from fastapi import FastAPI
from _schema import SignalSchema
from helper import handle_signals
from logger import logger


app = FastAPI()


@app.post(
    "/__add_signal__", include_in_schema=True
)  # TODO Set include_in_schema to false on production
def add_signal(Signal: SignalSchema, api_key):
    if api_key != "e158e1df-043a-4fa9-bcdd-b6548b9b47de":
        return {"status": "Api key is not valid mwonuse"}
    logger.info("Add signal request")
    handle_signals(Signal)
    return {"status": True}
