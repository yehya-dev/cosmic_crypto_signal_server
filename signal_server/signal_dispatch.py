import requests
from _schema import SpotSchemaRequestData, SpotSchema
from typing import List


class Signal_Dispatch:
    remote_url = "http://127.0.0.1:8081"

    def __init__(self) -> None:
        self.token = requests.post(
            f"{self.remote_url}/token",
            data={
                "grant_type": "password",
                "username": "kronos",
                "password": "iammessiah",
            },
        ).json()["access_token"]

    def send_data(self, data: List[SpotSchema], end_point):
        data = SpotSchemaRequestData.parse_obj(data).json()
        requests.post(
            f"{self.remote_url}/{end_point}",
            data=data,
            headers={"Authorization": f"Bearer {self.token}"},
        ).json()


signal_dispatch = Signal_Dispatch()
