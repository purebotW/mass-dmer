import discord, json, contextlib
from discord.ext import commands

with open('config.json', 'r') as file:
    data = json.loads(file.read())
    token = data.get('token')
    prefix = data.get('prefix') 
    owner_id = data.get('owner_id')

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), owner_id=int(owner_id))

@client.event
async def on_ready():
    print('Ready')
    
@client.command()
@commands.is_owner()
async def massdm(ctx, *, message):
    for member in ctx.guild.members:
        try:
            await member.send(message)
            print(f'Dm sent to {str(member)}')
        except:
            print(f'Could not dm {str(member)}')
            
client.run(token)