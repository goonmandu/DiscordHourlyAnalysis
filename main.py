from analysis import hourly_of_channel, hourly_of_all_channels_in_server

if __name__ == "__main__":
    option: int = int(input("Enter 1 for one-channel analysis, or 2 to analyze all JSON files.\n"))
    while option not in [1, 2]:
        option = int(input("Enter either 1 or 2: "))

    # TODO: Implement commented out section in analysis.py and constants.py
    '''
    id_or_name: str = input("Enter 'id' to analyze by the person's numerical ID, or 'name' to analyze by name.").lower()
    while id_or_name not in ['name', 'id']:
        id_or_name: str = input("Enter either 'id' or 'name'.").lower()
    if id_or_name == "id":
        user: str = input("Enter the numerical ID.\n")
    else:
        user: str = input("Enter the name and discriminator of the person to analyze. (e.g. discordname#2758):\n")
    '''

    user: str = input("Enter the name and discriminator of the person to analyze. (e.g. discordname#2758):\n")

    if option == 1:
        channel_id: str = input("Enter the ID of the channel:\n")
        print("Analyzing...")
        hourly_of_channel(channel_id, user)
    elif option == 2:
        print("Analyzing...")
        hourly_of_all_channels_in_server(user)
