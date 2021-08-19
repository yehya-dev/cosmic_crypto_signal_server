import uvicorn
import os
from pprint import pprint

pprint(os.environ)

port = os.environ.get("PORT") or 8080
uvicorn.run("app:app", host="0.0.0.0", port=int(port))

# TODO - Remove UI ( redocs )
# TODO - add unique key for accessing api
