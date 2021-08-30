from test_data import data
import requests
import json
from dbman import delete_entries

delete_entries()
host = "http://192.168.43.152:8080/"
delivery_endpoint = "__add_signal__?api_key=e158e1df-043a-4fa9-bcdd-b6548b9b47de"

requests.post(host + delivery_endpoint, data=json.dumps(data))
delete_entries()
