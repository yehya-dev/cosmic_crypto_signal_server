import uvicorn
import os

port = os.environ.get("PORT")

uvicorn.run("app:app", port=int(port))
