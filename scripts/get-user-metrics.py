#!/usr/bin/env python3
"""
Script to get user metrics and plot them. This can only be used by admins,
since it requires access to the complete user list in KeyCloak.

File: get-user-metrics.py

Copyright 2025 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import sys
import datetime
import requests
import logging
import matplotlib
matplotlib.use('qtagg')
import matplotlib.pyplot as plt
import json
from dateutil.relativedelta import relativedelta

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def run(keycloak_user, keycloak_password, save_json=False):
    """Main runner method.

    :param keycloak_user: keycloak username
    :type keycloak_user: string
    :param keycloak_password: keycloak password
    :type keycloak_password: string
    :param save_json: whether the downloaded user data should be saved to file
    :type save_json: bool

    """
    keycloak_url = "https://accounts.v2.opensourcebrain.org/auth"
    keycloak_realm = "osb2"
    logger.debug(f"Username: {keycloak_user}   Password: {keycloak_password}")

    resp = requests.post(
        f"{keycloak_url}/realms/master/protocol/openid-connect/token",
        data={
            "client_id": "admin-cli",
            "username": keycloak_user,
            "password": keycloak_password,
            "grant_type": "password",
        },
    )
    resp.raise_for_status()
    data = resp.json()
    access_token = data["access_token"]
    logger.debug(access_token)

    auth_headers = {"Authorization": f"Bearer {access_token}"}

    resp = requests.get(
        f"{keycloak_url}/admin/realms/{keycloak_realm}/users/count",
        headers=auth_headers,
    )

    resp.raise_for_status()
    data = resp.json()
    total_users = data
    print(f">>> Number of users: {total_users}")

    resp = requests.get(
        f"{keycloak_url}/admin/realms/{keycloak_realm}/users",
        headers=auth_headers,
        params={"max": total_users},
    )

    resp.raise_for_status()
    data = resp.json()

    if save_json:
        with open("osbv2-user-data.json", 'w') as f:
            json.dump(data, f)

    get_user_trends(data)


def get_user_trends(data, timewindow=2):
    """Get trends for user registration, and plot figure

    :param data: user data from keycloak
    :type data: list[dict]
    :param timewindow: size of window/bin for plotting, in months
    :type timewindow: int
    """
    time_now = datetime.datetime.now()
    trend_start = datetime.datetime(2021, 1, 1, 0, 0, 0)

    # note, milliseconds
    creation_time_stamps = sorted([au["createdTimestamp"] / 1000 for au in data])

    plot_data_x = []
    plot_data_y = []

    index = 0
    trend_point = trend_start
    for ts in creation_time_stamps:
        index += 1
        if ts > trend_point.timestamp():
            plot_data_x.append(trend_point)
            plot_data_y.append(index)
            trend_point += relativedelta(months=timewindow)

    assert index == len(creation_time_stamps)
    plot_data_x.append(time_now)
    plot_data_y.append(index)

    fig, ax = plt.subplots()
    plt.title("OSBv2 users over time")
    ax.plot(
        plot_data_x,
        plot_data_y,
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of users")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.xaxis.set(
        major_locator=matplotlib.dates.MonthLocator(interval=timewindow),
        major_formatter=matplotlib.dates.DateFormatter("%Y-%m"),
    )

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: two arguments required: username and password")
        sys.exit(-1)
    run(sys.argv[1], sys.argv[2])
