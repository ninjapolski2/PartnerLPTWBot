import discord
from discord import channel
from discord.ext import commands, tasks

intents1 = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents1)
client.remove_command('help')

@client.event
async def on_ready():
    print("Dołączyłem.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='10.06.2021r. Twórca bota: @NinjaaaSK#7850'))

@tasks.loop(hours=24.0)
async def promotor():
    guild1 = client.get_guild(851566107834974268)
    channel1 = discord.utils.find(lambda r: r.name == 'współpraca', guild1.text_channels)
    await channel1.send("Szukasz wsparcia technicznego, opieki nad serwerem discord? \n Szukasz odpowiedzi na nurtujące Cie pytania ze świata IT? \n Zapraszamy na naszego discorda oraz grupę na facebooku. \n Za działanie serwera oraz opiekę techniczną świadczy LP&TW. \n https://discord.gg/eUcb5xvyXs \n https://www.facebook.com/groups/linuxpolska \n https://i.ibb.co/Qvn4m65/Wideo-Full-HD-1920x1080-px.gif")
    return

@promotor.before_loop
async def before_printer():
        print('Czekanie...')
        await client.wait_until_ready()

promotor.start()

client.run('your_token_here')
