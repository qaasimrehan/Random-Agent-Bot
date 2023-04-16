import random
import discord
import asyncio
from discord.ext import commands

intents =discord.Intents.all()
intents.message_content = True #v2
prefix = "!"
bot = commands.Bot(command_prefix = prefix, intents=intents)
token = 'MTA5NzIxNDU2ODA5MjE0NzcxMg.Gpvrqz.gIHd0gK9Ghbfx6odquVX0uPcY3gFklc3gasJwU'

Agents = ["Jett","Killjoy", "Sova", "Omen", "Gekko", "KAY/O", "Skye", "Viper", "Fade", "Cypher", "Phoenix", "Yoru", "Neon", "Raze", "Reyna", "Astra", "Harbor" ]
agentImage =["Jett.png", "Killjoy.png", "Sova.png", "Omen.png", "Gekko.png", "KAYO.png", "Skye.png", "Viper.png", "Fade.png", "Cypher.png", " Phoenix.png", "Yoru.png", "Neon.png", "Raze.png", "Reyna.png", "Astra.png", "Harbor.png"]
@bot.event
async def on_ready():
    print("Agent select is ready")

@bot.command(pass_context = True)
async def RandomAgent(ctx):
        x = random.randint(0, 16)
        embed = discord.Embed(title = "Random Agent", description = (Agents[x]), color = (0xF85252))
        file = discord.File("Images/"+ (agentImage[x]), filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file,embed = embed)
     #   await ctx.send(file=discord.File('Valornt.jpg'))

        

bot.run(token)


