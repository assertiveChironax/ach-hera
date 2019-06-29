import discord
from discord.ext import commands
import random
import os

#Cash
dollars = 0
dollars = dollars

#Roulette Values
luck = random.randint(1,6)
bang = 6
luck = luck

#Gacha Values
won = []
prize = ["an ares", "an eris", "an eros", "raw beef", "raw pork",
          "raw fish", "raw chicken", "beans", "chocolate", "beer",
          "a weed", "a headpat", "a hug", "lint", "pocket sand",
          "a penny", "a used napkin", "a potato chip"]

#'Useless' code letting me know the program made it this far.
print("Loading...")

client = commands.Bot(command_prefix = ".")

#'Useless' bit of code to let me know when Hera's logged in.
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("ACH Server"))
    print("Summoning.. She's here.")
    
## Censor code? WIP.
##async def on_message(message):
##    if message.content.find("fuck") != -1:
##        await message.channel.send("Watch it.")
##        print(message.content)

#Actual command code translated from old Juno bot to work with
#new discord.py doc

#Allowance
@client.command(name="allowance",
                description="Grants or deducts money from the server.",
                brief="Here to ask me for currency again?",
                aliases=["mompls", "mommypls", "mapls", "mamapls", "gibmoni",])
async def allowance(ctx):
    global dollars
    mercy = random.randint(1,3)
    if mercy == 1:
        dollars = dollars + 100
        await ctx.send(ctx.author.mention + " Very well then. Here is $100.")
        return (dollars)
    if mercy == 2:
        await ctx.send(ctx.author.mention + " Perhaps another time.")
    if mercy == 3:
        dollars = dollars - 25
        await ctx.send(ctx.author.mention + " You have asked for too much." +
                       "I am taking $25 away from the server.")
        return (dollars)
    
#Bank
@client.command(name="bank",
                description="Displays the server's saved money.",
                brief="Would you like to check the balance?",)
async def bank(ctx):
    global dollars
    await ctx.send(ctx.author.mention + " The server currently has $" + str(dollars) + ".")
    
#Choose
@client.command(name="choose",
                description="Chooses between several choices.",
                brief="Would you like your Mother to choose for you?",)
async def choose(ctx, *choices):
    if len(choices)<2:
        await ctx.send(ctx.author.mention +
                       " Then I really have no choice, do I?")
    else:
        await ctx.send(ctx.author.mention + " I choose " +
                       random.choice(choices) + ".")
#Collection
@client.command(name="collection",
                description="Displays the server's collection of gacha prizes.",
                brief="What have you won?",)
async def collection(ctx):
    global won
    await ctx.send(ctx.author.mention + " The server has won: " + str(won) + ".")

#Gacha
@client.command(name="gacha",
                description="Spends $1000 to roll the server's gacha ONCE.",
                brief="What will you win?",)
async def gacha(ctx):
    global dollars
    global prize
    global won
    if dollars < 1000:
        await ctx.send(ctx.author.mention +
                       " The server does not have enough money.")
    elif dollars >= 1000:
        dollars = dollars - 1000
        got = random.choice(prize)
        won.append(got)
        await ctx.send(ctx.author.mention + " You won " + str(got) + ".")

#Mom   
@client.command(name="mom",
                description="Determines the answer to yes-or-no style questions.",
                brief="Why do you not ask your Mother?",
                alias
                es=["mother", "mommy", "mama", "ma"])
async def mom(ctx, *, question):
    possible_responses = [" Yes.", " No.", " Maybe.",
                          " Why do you not ask me later?",]
    await ctx.send(ctx.author.mention +
                   f' ```{question}```\n{random.choice(possible_responses)}')

#Prizes
@client.command(name="prizes",
                description="Display's the current prize pool.",
                brief="What can you win?",)
async def prizes(ctx):
    global prize
    await ctx.send(ctx.author.mention + " The prizes in the current prize pool are: "
                   + str(prize) + ".")
#Roulette
@client.command(name="roulette",
                description="Adds $1000 to the server's account.",
                brief="Would you like some quick money?",
                aliases=["rr", "blyat",])
async def roulette(ctx):
    global dollars
    global luck
    global bang
    if luck == bang:
        luck = random.randint(1,6)
        dollars = dollars - 100
        await ctx.send(ctx.author.mention + " Bang. Unfortunate- I will be taking $100 to cover your medical expenses.")
        return (luck, dollars)
    elif luck != bang:
        luck = luck + 1
        dollars = dollars + 100
        await ctx.send(ctx.author.mention + " Click. Brave- Here is $100 as a reward.")
        return (luck, dollars)

    
#'Useless' code letting me know the program made it this far.   
print("Done.")

client.run(os.getenv("TOKEN"))
