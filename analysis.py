import os
import json
import numpy as np
import matplotlib.pyplot as plt
from constants import *


def show_plot_daynight(analysis_scope: str, username: str, date_filter: str, userdata: dict[int, int]):
    total_msgs = sum(userdata.values())
    hours = userdata.keys()
    msgs = userdata.values()

    # Generated by ChatGPT. Thanks a lot lol
    day_start = 7
    day_end = 19
    transition = 0
    fig, ax = plt.subplots()
    ax.bar(hours, msgs)
    x = np.linspace(0, 23, 1000)
    y_min, y_max = 0, max(msgs) * 1.1
    ax.set_xticks(range(24))
    ax.set_xticklabels(range(24))
    ax.fill_between(x, y_min, y_max,
                    where=(x >= day_start - transition) & (x <= day_end + transition),
                    facecolor='yellow', alpha=0.1, interpolate=True)
    ax.fill_between(x, y_min, y_max,
                    where=(x < day_start - transition) | (x > day_end + transition),
                    facecolor='black', alpha=0.1, interpolate=True)
    ax.set_title(f"Messages each hour by {username}\n"
                 f"in {analysis_scope} ({total_msgs} total)\n"
                 f"Date filter: {date_filter}")
    ax.set_xlabel(f"Hour ({TIMEZONE})")
    ax.set_ylabel("Messages")
    for i, v in enumerate(msgs):
        ax.text(i, v + y_max / 75, f"{str(v)}\n({round(v * 100/(total_msgs + 1), 1)}%)", ha='center', fontsize=7)
    plt.show()


def load_json_from_channel_id(channel_id: str) -> Channel:
    for jsonname in os.listdir(JSON_DIRECTORY):
        if channel_id in jsonname:
            with open(f"{JSON_DIRECTORY}/{jsonname}", encoding='utf-8') as f:
                try:
                    channel = Channel(json.load(f))
                except Exception as e:
                    channel = None
                    print(e, jsonname)
                break
    return channel


def load_all_jsons_in_directory() -> Server:
    list_of_channels: list[Channel] = []
    for jsonname in os.listdir(JSON_DIRECTORY):
        with open(f"{JSON_DIRECTORY}/{jsonname}", encoding='utf-8') as f:
            list_of_channels.append(Channel(json.load(f)))
    return Server(list_of_channels)


def hourly_of_channel(channel_id: str, username: str):
    channel = load_json_from_channel_id(channel_id)
    messages = channel.get_messages_by_author(username)
    userdata = hourly_data_of(messages)
    show_plot_daynight(f"#{channel.name} of server: {channel.server_name}", username, "all", userdata)


def hourly_of_channel_timeframe(channel_id: str, username: str, start: str, end: str):
    channel = load_json_from_channel_id(channel_id)
    messages = channel.get_messages_by_author_timeframe(username, start, end)
    userdata = hourly_data_of(messages)
    show_plot_daynight(f"#{channel.name} of server: {channel.server_name}",
                       username,
                       f"{start} to {end}",
                       userdata)


def hourly_of_channel_weekdays(channel_id: str, username: str):
    channel = load_json_from_channel_id(channel_id)
    messages = channel.get_messages_by_author_weekdays(username)
    userdata = hourly_data_of(messages)
    show_plot_daynight(f"#{channel.name} of server: {channel.server_name}",
                       username,
                       "Weekdays only", userdata)


def hourly_of_channel_weekends(channel_id: str, username: str):
    channel = load_json_from_channel_id(channel_id)
    messages = channel.get_messages_by_author_weekends(username)
    userdata = hourly_data_of(messages)
    show_plot_daynight(f"#{channel.name} of server: {channel.server_name}",
                       username,
                       "Weekends only", userdata)


def hourly_of_channel_timeframe_without_year(channel_id: str, username: str, start: str, end: str):
    start_split = start.split("-")
    end_split = end.split("-")
    channel = load_json_from_channel_id(channel_id)
    messages = channel.get_messages_by_author_timeframe_without_year(username, start, end)
    userdata = hourly_data_of(messages)
    show_plot_daynight(f"#{channel.name} of server: {channel.server_name}",
                       username,
                       f"{start_split[1]}-{start_split[2]} to {end_split[1]}-{end_split[2]}",
                       userdata)


def hourly_of_all_channels_in_server(username):
    server = load_all_jsons_in_directory()
    messages = server.get_messages_by_author_in_server(username)
    userdata = hourly_data_of(messages)
    show_plot_daynight(f"server: {server.name}",
                       username,
                       "all",
                       userdata)


if __name__ == "__main__":
    hourly_of_all_channels_in_server("goonmandu#4897")
    #hourly_of_channel("824350178924167185", "goonmandu#4897")
    #hourly_of_channel_timeframe_without_year("824350178924167185", "goonmandu#4897", "2022-08-15", "2023-05-15")
    #hourly_of_channel_timeframe_without_year("824350178924167185", "goonmandu#4897", "2022-05-15", "2022-08-15")
