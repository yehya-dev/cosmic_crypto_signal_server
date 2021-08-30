import sqlite3
import subprocess
import os
from pathlib import Path
import json
import requests
from pprint import pprint as print
from time import sleep


package_name_for_notifications = "com.zyncas.signals"
last_notification_time = None

delivery_endpoint = "https://cryptosignalserver.herokuapp.com/__add_signal__?api_key=e158e1df-043a-4fa9-bcdd-b6548b9b47de"
# delivery_endpoint = "http://192.168.43.152:8080/__add_signal__?api_key=e158e1df-043a-4fa9-bcdd-b6548b9b47de"


def main():
    global last_notification_time

    proc = subprocess.Popen("termux-notification-list", stdout=subprocess.PIPE)
    output = proc.stdout.read()
    notifications = json.loads(output)

    flag = False
    if last_notification_time:
        for notification in filter(
            lambda item: item["packageName"] == package_name_for_notifications,
            notifications,
        ):
            when = float(notification["when"])
            if when > last_notification_time:
                last_notification_time = when
                flag = True
                # Flag is required here because if me break when the first new notification is found, there could be other newer notification
                # and this leads to trigger db_fetch and requests again for the same notification set. the flag allows for the last_notification_time
                # to be set to the newest notificatin from signals app
        if not flag:
            return

    if last_notification_time is None:
        last_notification_time = 1.0
        print("Initial update : Even if there are no notifications")
    else:
        print("New notification detected")

    subprocess.call(
        [
            "sudo",
            "cp",
            "/data/data/com.zyncaa.signals/databases/MVVMDatabase",
            Path(os.getcwd()) / "signals.sqlite",
        ]
    )

    db_connection = sqlite3.connect("./signals.sqlite")
    db_connection.row_factory = sqlite3.Row

    cursor = db_connection.cursor()

    signals_data = cursor.execute(
        """
    SELECT 
    id AS spot_id, buy AS buy_price, chart_url, created_at, current AS current_price, risk, pair, stop AS stop_price, symbol, tp1, tp2, tp3, tp_done, tpNum AS total_tp, type AS spot_type, coin 
    FROM `Signal`
    ORDER BY created_at
    DESC
    """
    )

    spots = []
    # for _, row in enumerate(signals_data):
    for row in signals_data:
        this_signal = dict(row)
        coin_data = json.loads(this_signal["coin"])
        coin_logo_url = coin_data["logo"]
        del this_signal["coin"]
        this_signal["coin_logo_url"] = coin_logo_url
        spots.append(this_signal)
    # futures_data = cursor.execute('''
    # SELECT id, chart_url, created_at, current, entry, future_type, initial_price, is_filled, risk, leverage, pair, stop, tp1, tp2, tp3, tpDone, tpNum, type  FROM `Future` ORDER BY created_at
    # ''')

    print({"spots": spots})

    try:
        requests.post(
            delivery_endpoint,
            data=json.dumps({"spots": spots}),
        ).raise_for_status()
    except requests.exceptions.HTTPError:
        print("Could not send request to server")


while True:
    main()
    sleep(2)  # TODO Adjust if notification is arriving slow
