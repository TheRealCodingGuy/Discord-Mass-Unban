import requests
import json


usertoken = 'usertoken-here'
guildid = 'guildid-here'

def main():
    x = 0
    headers = {f"authorization": usertoken}
    r = requests.get(f"https://discord.com/api/v9/guilds/{guildid}/bans", headers=headers).json()
    lol = ([userid['user']['id'] for userid in r])
    for wtf in lol:
        requests.delete(f'https://discord.com/api/v9/guilds/{guildid}/bans/{wtf}', headers=headers)
        x +=1
        print(f"Member Unbanned {x}")
        
main()