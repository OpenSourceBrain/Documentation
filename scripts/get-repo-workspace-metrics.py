#!/usr/bin/env python3
"""
Enter one line description here.

File:

Copyright 2025 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""

import requests
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import matplotlib

# repositories_url = "https://v2.opensourcebrain.org/proxy/workspaces/api/osbrepository?page=1&per_page=4000"
repositories_url = "https://v2.opensourcebrain.org/proxy/workspaces/api/osbrepository?page=1&per_page=40"
workspaces_url = (
    "https://v2.opensourcebrain.org/proxy/workspaces/api/workspace?page=1&per_page=1500"
)


def get_repo_metrics():
    """Get metrics on number of repositories on OSBv2"""
    resp = requests.get(repositories_url)

    resp.raise_for_status()
    data = resp.json()
    repositories = data["osbrepositories"]
    total_number = data["pagination"]["total"]
    assert total_number == len(repositories)
    print(f">>> Number of repositories: {len(repositories)}")

    model_or_data = {"models": 0, "data": 0}
    repo_types = {"biomodels": 0, "dandi": 0, "github": 0, "figshare": 0}
    creation_time_stamps = []

    for repo in repositories:
        repo_types[repo["repository_type"]] += 1
        if repo["content_types_list"][0] == "modeling":
            model_or_data["models"] += 1
        else:
            model_or_data["data"] += 1

        creation_time_stamps.append(
            datetime.datetime.fromisoformat(repo["timestamp_created"])
        )

    print(">>> Type break down:")
    print(model_or_data)
    print(repo_types)
    print(creation_time_stamps[0:10])
    print(creation_time_stamps[0:-10])
    return creation_time_stamps


def get_workspace_metrics():
    """Get metrics on number of repositories on OSBv2"""
    resp = requests.get(workspaces_url)

    resp.raise_for_status()
    data = resp.json()
    workspaces = data["workspaces"]
    total_number = data["pagination"]["total"]
    assert total_number == len(workspaces)
    print(f">>> Number of workspaces: {len(workspaces)}")

    public_or_private = {"public": 0, "private": 0}

    creation_time_stamps = []

    for ws in workspaces:
        if ws["publicable"]:
            public_or_private["public"] += 1
        else:
            public_or_private["private"] += 1
        creation_time_stamps.append(
            datetime.datetime.fromisoformat(ws["timestamp_created"])
        )

    creation_time_stamps = sorted(creation_time_stamps)

    print(">>> Type break down:")
    print(public_or_private)
    print(creation_time_stamps[0:10])
    print(creation_time_stamps[0:-10])
    return creation_time_stamps


def plot_trend(title, creation_time_stamps, timewindow=2):
    time_now = datetime.datetime.now()
    trend_start = datetime.datetime(2021, 1, 1, 0, 0, 0)

    plot_data_x = []
    plot_data_y = []

    index = 0
    trend_point = trend_start
    for ts in creation_time_stamps:
        index += 1
        if ts.timestamp() > trend_point.timestamp():
            plot_data_x.append(trend_point)
            plot_data_y.append(index)
            trend_point += relativedelta(months=timewindow)

    assert index == len(creation_time_stamps)
    plot_data_x.append(time_now)
    plot_data_y.append(index)

    fig, ax = plt.subplots()
    ax.plot(
        plot_data_x,
        plot_data_y,
    )
    ax.set_xlabel("Date")
    ax.set_ylabel(f"Number of {title}")
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
    repo_timestamps = get_repo_metrics()
    plot_trend(title="Repositories", creation_time_stamps=repo_timestamps)
    workspace_timestamps = get_workspace_metrics()
    plot_trend(title="Workspaces", creation_time_stamps=workspace_timestamps)
