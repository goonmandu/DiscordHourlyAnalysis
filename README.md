# DiscordHourlyAnalysis
This project analyzes the hourly message count by a person within a channel, or across multiple channels.  
Intended to be used with **[DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)**.

# Prerequisites
Python 3.9 or newer

# External Dependencies
pytz - `pip3 install pytz`  
numpy - `pip3 install numpy`  
matplotlib - `pip3 install matplotlib`

# How to use
1. Create a directory called `data` in the root directory of this project.
2. Choose the channels that you want to analyze in **DiscordChatExporter**.
3. Choose the `data` directory that you made in Step 1 for the export directory.
4. Choose JSON format.
5. Wait for DiscordChatExporter to finish.
6. Choose the timezone to be analyzed with by editing the `TIMEZONE` constant in `constants.py`.
7. `python3 main.py`

# Screenshots
<img src="https://i.imgur.com/1fgTLEu.png" width="720">
<br>
<img src="https://i.imgur.com/jNChrLU.png" width="720">