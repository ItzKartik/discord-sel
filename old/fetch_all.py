import discord
from discord.ext import commands
import csv

token = "NzY5MDY2OTM5Njc4MTk1NzEy.X5JnZg.L84-8u_GUvlhPw7j6seT1nWl5sE"
channel_id = 775252861272588310

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

data = []

# async def populate():
#     with open('users.csv', 'w+', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(["ID", "USERNAME", "STATUS"])
#         writer.writerows(data)
#         return True

@client.event
async def on_ready():
    print("Connected")
    user = client.get_user(325543894660153344)
    print(user)
    # channel = client.get_channel(channel_id)
    # members = channel.members
    # data.clear() 
    # for member in members:
        # data.append([str(member.id), str(member.name), "NONE"])
    # await populate()

# To Use Guilds:  
# for i in client.guilds:
#     for j in i.members:
#         print(j.id)

# @client.event
# async def on_message(message):
#     if message.content.startswith('!members'):  
#         data.clear() 
#         for guild in message.guild.members:
#             data.append([str(guild.id), str(guild.name), "NONE"])
#         await populate()

if __name__ == "__main__":
    client.run(token)