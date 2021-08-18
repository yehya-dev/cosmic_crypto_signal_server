import uvicorn

uvicorn.run("app:app", debug=True, host="0.0.0.0", port=80)
