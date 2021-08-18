import uvicorn
import os

port = os.environ.get("PORT")

uvicorn.run("app:app", host="0.0.0.0", port=int(port))
