import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    with open('images/meme1.jpg', 'rb') as f:
        # Let's save the Discord file/library that is in this variable climb!
        picture = discord.File(f)
   # We can then send this file as a benchmark!
    await ctx.send(file=picture)

@bot.command()
async def sol(ctx):
    


bot.run("MTExNjY1MTAwMzEyNzgwODAxMQ.GVV4Gp.rfmisN0R_GLSWupFK2i2Il2JA8NnYAMOU-PFPI")

note: this code hasn't finished yet.
