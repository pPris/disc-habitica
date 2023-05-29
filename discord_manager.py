import requests
from secrets_1 import token_secret
import os

work_ti = '875294338622570587' # same channel id between ti and work_ti dm
disc_habitica_chat = '1111197485516455977'
forward_to = disc_habitica_chat if os.getenv("ENV") == "PRD" else work_ti

def get_channel_api_string(channel_id: int):
    channel_string_start = "https://discord.com/api/v9/channels/"
    channel_string_end = "/messages"
    return (channel_string_start + str(channel_id) + channel_string_end)

def getChannelName(channelID: str):
    authToken = token_secret
    header = {"authorization": authToken}
    res = requests.get(url=f'https://discord.com/api/v9/channels/{channelID}', headers=header)
    try:
        return res.json()["name"] 
    except KeyError:
        return res.json()["recipients"][0]["username"]
    except:
        return "can't find channel name"

# class SendMessage:
def sendMessage(channelID: str, payload: str, authToken: str=token_secret):
    payload = {"content": payload}
    header = {"authorization": authToken}
    res = requests.post(get_channel_api_string(channelID), data=payload, headers=header)
    print(f'message was sent to channelID: {getChannelName(channelID)} with code {res.status_code}')

# simpleFormat = f'>>> {content} \n *sent by {sender}*'

def fwdToDiscordParty(formatted: str, unformattedVersion:str, sender: str):
    message = f'```\n{unformattedVersion}```*-{sender}*'
    sendMessage(forward_to, message)

sendMessage(forward_to, "ti's hrpg-discord bot going online 💻")