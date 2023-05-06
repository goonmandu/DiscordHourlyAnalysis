from datetime import datetime
import pytz
import re

JSON_DIRECTORY: str = "data"
TIMEZONE: str = "America/New_York"


def iso8601ize(time_string: str):
    if '.' in time_string:
        sanit = re.split("\.|\+", time_string)
        return f"{sanit[0]}+{sanit[2]}"
    else:
        return time_string


class Message:
    def __init__(self, message_data):
        self.content: str = message_data["content"]
        self.author: str = f'{message_data["author"]["name"]}#{message_data["author"]["discriminator"]}'
        self.time: datetime = datetime.fromisoformat(iso8601ize(message_data["timestamp"])) \
                                      .astimezone(pytz.timezone(TIMEZONE))

    def __str__(self) -> str:
        return f"Text: {self.content}, " \
               f"By: {self.author}, " \
               f"At: {str(self.time)}"


class Channel:
    def __init__(self, channel_data):
        self.server_name: str = channel_data["guild"]["name"]
        self.name: str = channel_data["channel"]["name"]
        self.messages: list[Message] = [Message(m) for m in channel_data["messages"]]
        self.message_count: int = len(self.messages)

    def __str__(self) -> str:
        return f"Name: {self.name}, " \
               f"Message Count: {self.message_count}, " \
               f"Messages:\n {[str(m) for m in self.messages]}"

    def get_messages_by_author(self, name_and_discrim: str) -> list[Message]:
        return [msg for msg in self.messages if msg.author == name_and_discrim]

    def get_hourly_data_of_author(self, name_and_discrim: str) -> dict[int, int]:
        hourly = {key: 0 for key in range(24)}
        for msg in self.get_messages_by_author(name_and_discrim):
            hourly[msg.time.hour] += 1
        return hourly


class Server:
    def __init__(self, data_of_all_channels: list[Channel]):
        self.channel_names: list[str] = [channel.name for channel in data_of_all_channels]
        self.channels: list[Channel] = data_of_all_channels
        self.name: str = self.channels[0].server_name if len(set([ch.server_name for ch in self.channels])) == 1\
            else "undefined"

    def get_messages_by_author_in_server(self, name_and_discrim: str) -> list[Message]:
        all_messages: list[Message] = []
        for ch in self.channels:
            for msg in ch.get_messages_by_author(name_and_discrim):
                all_messages.append(msg)
        return all_messages

    def get_hourly_data_of_author_in_server(self, name_and_discrim: str) -> dict[int, int]:
        hourly = {key: 0 for key in range(24)}
        for ch in self.channels:
            for key in hourly.keys():
                hourly[key] += ch.get_hourly_data_of_author(name_and_discrim)[key]
        return hourly


if __name__ == "__main__":
    print(iso8601ize("2023-01-11T15:54:10.96+00:00"))
