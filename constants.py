from pytz import all_timezones

'''
Yes I know this is hella scuffed. But I really don't feel like refactoring my code because... because.
I am abusing the fact that dependency files *will* execute as it is being imported into other files.

If I wanted to have this as a debug for some reason,
I'd have put it in an "if __name__ == "__main__"(): " conditional.
'''

JSON_DIRECTORY: str = input("Specify the JSON directory:\n")

TIMEZONE: str = input("Specify a timezone:\n")
while TIMEZONE not in all_timezones:
    TIMEZONE: str = input("Unrecognized timezone. Try again: ")
