import random
import discord
import asyncio
from discord.ext import commands

intents =discord.Intents.all()
intents.message_content = True #v2
prefix = "!"
bot = commands.Bot(command_prefix = prefix, intents=intents)

token = ''

with open('token.txt', 'r') as file:
    token = file.read().rstrip()

Agents = ["Jett","Killjoy", "Sova", "Omen", "Gekko", "KAY/O", "Skye", "Viper", "Fade", "Cypher", "Phoenix", "Yoru", "Neon", "Raze", "Reyna", "Astra", "Harbor" ]
agentImage = ["Jett.png", "Killjoy.png", "Sova.png", "Omen.png", "Gekko.png", "KAYO.png", "Skye.png", "Viper.png", "Fade.png", "Cypher.png", "Phoenix.png", "Yoru.png", "Neon.png", "Raze.png", "Reyna.png", "Astra.png", "Harbor.png"]
sideAffect = ["Play With only Marshal for 4 rounds", "Only use Sidearms for the next round", "Increase your sens by 0.5", "Decrease your Sense by 0.5" ]
Crosshair = ["0;P;c;1;h;0;0t;8;0l;10;0o;7;0a;0.584;1b;0", "0;P;o;0.562;0t;6;0l;12;0o;20;0a;0.93;1b;0", "0;P;c;1;h;0;0t;3;0l;19;0o;7;0a;0.61;1b;0", "0;P;c;5;t;5;o;0.393;0t;4;0l;15;0o;15;0a;0.659;1b;0", "0;P;c;3;h;0;d;1;z;6;a;0.773;0l;19;0o;19;0a;0.224;1b;0", "0;P;c;7;h;0;d;1;z;1;a;0.528;0t;3;0l;10;0o;19;0a;0.473;1b;0", "0;P;c;4;t;2;o;0.655;0t;5;0l;10;0o;7;0a;0.136;1b;0", "0;P;c;4;t;5;o;0.154;d;1;z;1;a;0.716;0t;10;0l;4;0o;13;0a;0.211;1b;0", "0;P;c;4;h;0;d;1;z;6;a;0.831;0t;7;0l;12;0o;8;0a;0.957;1b;0", "0;P;c;6;t;4;o;0.732;d;1;z;5;a;0.836;0t;4;0l;0;0o;13;0a;0.285;1b;0"]
Crosshairpic = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png"]
@bot.event
async def on_ready():
    print("Agent select is ready")

@bot.command(pass_context = True)
async def RandomCrosshair(ctx):
        b = random.randint(0, 9)
        embed = discord.Embed(title = "Random Crosshair", description = (Crosshair[b]), color = (0x4465a2))
        file = discord.File("CrossHairs/"+ (Crosshairpic[b]), filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file,embed = embed)

@bot.command(pass_context = True)
async def SideAffect(ctx):
        a = random.randint(0, 3)
        embed = discord.Embed(title = "Random Side Affect", description = (sideAffect[a]), color = (0x4465a2))
        file = discord.File("Agents/"+ (agentImage[a]), filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file,embed = embed)

@bot.command(pass_context = True)
async def RandomAgent(ctx):
        x = random.randint(0, 16)
        embed = discord.Embed(title = "Random Agent", description = (Agents[x]), color = (0x4465a2))
        file = discord.File("Agents/"+ (agentImage[x]), filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file,embed = embed)

@bot.command(pass_context = True)
async def RandomAgents(ctx, num):
        tempAgents=Agents.copy()
        tempagentImages=agentImage.copy()
        for y in range(int(num)):
            x = random.randint(0, len(tempAgents)-1)
            embed = discord.Embed(title = "Random Agent " + str(y+1), description = (tempAgents[x]), color = (0x4465a2))
            file = discord.File("Agents/"+ (tempagentImages[x]), filename="image.png")
            embed.set_image(url="attachment://image.png")
            tempAgents.pop(x)
            tempagentImages.pop(x)
            await ctx.send(file=file,embed = embed)
        

bot.run(token)