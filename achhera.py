from discord.ext import commands
import random
import os
import discord
import json

#Roulette Values
luck = random.randint(1,6)
bang = 6
luck = luck
#Gacha Values
prize = ['an ares', 'an eris', 'an eros', 'raw beef', 'raw pork',
          'raw fish', 'raw chicken', 'beans', 'chocolate', 'beer',
          'a weed', 'a headpat', 'a hug', 'lint', 'pocket sand',
          'a penny', 'a used napkin', 'a potato chip', 'a gun', 'a custom role',
         'new user-color']

def creator(ctx):
    return ctx.author.id == 220034017959870465

#'Useless' code letting me know the program made it this far.
print("Loading...")
#Prefix
client = commands.Bot(command_prefix = ".")
#'Useless' bit of code to let me know when Hera's logged in.
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("ACH Server"))
    print("Summoning.. She's here.")

#New Registry
@client.event
async def on_member_join(member):
#Opens .json
    with open('users.json', 'r') as f:
        users = json.load(f)
#Registry upon joining the server.
#Discord.py Rewrite doesn't work with ID's as integers.
    id = str(message.author.id)
    if not id in users:
        users[id] = {}
        users[id]['cash'] = 0
        users[id]['box'] = []        
#Updates .json
    with open('users.json', 'w') as f:
        json.dump(users, f)        
#Participation + Registry + Censor
@client.event
async def on_message(message):
    if message.author.bot:
        return
    no_no = [ 'fuck', 'fucking', 'fucked', 'fucks', 
                   'shit', 'shitting', 'shits', 'shitty', 
                   'bitch', 'bitching', 'bitches', 'bitched',
                  'pussy', 'asshole', 'damn', 'damned', 'motherfucker', 'motherfucka', ]
    messagez = message.content.split(" ")
    for word in messagez:
        if word.lower() in no_no:
            await message.channel.send("Language.")
    with open('users.json', 'r') as f:
        users = json.load(f)      
    id = str(message.author.id)  
    if not id in users:
        users[id] = {}
        users[id]['cash'] = 0
        users[id]['box'] = []
    with open('users.json', 'w') as f:
        json.dump(users, f)
    await client.process_commands(message)

#Allowance
@client.command(name="allowance",
                description="Grants or deducts money from the user.",
                brief="Here to ask me for currency again?",
                aliases=["mompls", "mommypls", "mapls", "mamapls", "gibmoni",])
async def allowance(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        mercy = random.randint(1,3)
        if mercy == 1:
            users[id]['cash'] += 100
            await ctx.send(ctx.author.mention + " Very well then. \
Here is $100.")
        if mercy == 2:
            users[id]['cash'] -= 25
            await ctx.send(ctx.author.mention + " You have asked for too much. \
I am taking $25 away from your balance.")
        if mercy == 3:
            await ctx.send(ctx.author.mention + " Perhaps another time.")

    with open('users.json', 'w') as f:
        json.dump(users, f)

#Bank
@client.command(name="bank",
                description="Displays the amount of cash the user has.",
                brief="Would you like to view your balance?",)
async def bank(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        await ctx.send(ctx.author.mention + " Your balance is ${}."
                       .format(users[id]['cash']))
#Choose
@client.command(name="choose",
                description="Chooses between several choices.",
                brief="Would you like your Mother to choose for you?",)
async def choose(ctx, *choices):
    if len(choices)<2:
        await ctx.send(ctx.author.mention +
                       " Then I really have no choice, do I?")
    else:
        await ctx.send(ctx.author.mention + " I choose {}."
                       .format(random.choice(choices)))

#Collection
@client.command(name="collection",
                description="Displays the items the user has earned.",
                brief="What have you won?",
                aliases=["box",])
async def collection(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        await ctx.send(ctx.author.mention + " The contents of your box are: {}"
                       .format(users[id]['box']))

#Gacha
@client.command(name="gacha",
                description="Spends $1000 to roll the gacha ONCE.",
                brief="What will you win?",)
async def gacha(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        if users[id]['cash'] < 1000:
            await ctx.send(ctx.author.mention +
                       " You do not have enough money.")
        if users[id]['cash'] >= 1000:
            got = random.choice(prize)
            users[id]['cash'] -= 1000
            users[id]['box'].append(got)
            await ctx.send(ctx.author.mention +
                           " Rolling. You won {}.".format(got))
    with open('users.json', 'w') as f:
        json.dump(users, f)

#Give
@client.command(name="give",
                description="Gives some money from the user to another user.",
                brief="How very generous of you.",)
async def give(ctx, member: discord.Member, money):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        money = int(money)
        if users[id]['cash'] < money:
                await ctx.send(ctx.author.mention + " You do not have that money.")
        if users[id]['cash'] >= money:
            id = str(ctx.author.id)
            users[id]['cash'] -= money
            id = str(member.id)
            users[id]['cash'] += money
            await ctx.send(ctx.author.mention + " How generous. \
You have given {} ${}.".format(member.mention, money))
    with open('users.json', 'w') as f:
        json.dump(users, f)

#Gift
@client.command(name="gift",
                description="Gives an item from the user to another user.",
                brief="How kind of you.",)
async def gift(ctx, member: discord.Member, *, thing):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        thing = str(thing)
        if thing not in users[id]['box']:
                await ctx.send(ctx.author.mention + " You do not have that \
item.")
        if thing in users[id]['box']:
            id = str(ctx.author.id)
            users[id]['box'].remove(thing)
            id = str(member.id)
            users[id]['box'].append(thing)
            await ctx.send(ctx.author.mention + " How kind. \
You have given {} {}.".format(member.mention, thing))
    with open('users.json', 'w') as f:
        json.dump(users, f)
        
#Gun
@client.command(name="gun",
                decsription="That is called robbing.",
                brief="What do you intend to do with that gun?",
                aliases=['rob', 'gimmetheloot', 'gimmetheloop', 'stickem',
                         'handsup', 'gimmeurFUCKINMONEY',])
async def gun(ctx, member: discord.Member, money):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        money = int(money)
        agun = 'a gun'
        if agun not in users[id]['box']:
            await ctx.send(ctx.author.mention + " You do not have a gun.")
        if agun in users[id]['box']:
            defense = 'pocket sand'
            id = str(member.id)
            if defense in users[id]['box']:
                users[id]['box'].remove(defense)
                id = str(ctx.author.id)
                users[id]['box'].remove(agun)
                await ctx.send(ctx.author.mention + " You attempt to rob \
{} but they throw their pocket sand into your eyes and get away!"
                               .format(member.mention))
                with open('users.json', 'w') as f:
                    json.dump(users, f)
        
            if defense not in users[id]['box']:
                id = str(member.id)
                if users[id]['cash'] < money:
                    await ctx.send(ctx.author.mention + " {} does not have \
the money you desire. Try someone else.".format(member.mention))
                if users[id]['cash'] >= money:
                    id = str(ctx.author.id)
                    users[id]['cash'] += money
                    users[id]['box'].remove(agun)
                    id = str(member.id)
                    users[id]['cash'] -= money
                    await ctx.send(ctx.author.mention + " Oh my. \
You have robbed {} for ${}.".format(member.mention, money))
    with open('users.json', 'w') as f:
        json.dump(users, f)

#How much?
@client.command(name="howmuch",
                decsription="Checks the balance of another user.",
                brief="Nosey, are we?",)
async def howmuch(ctx, member: discord.Member):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(member.id)
        await ctx.send(ctx.author.mention + " {}'s balance is ${}."
                       .format(member.mention, users[id]['cash']))
    with open('users.json', 'w') as f:
        json.dump(users, f)
        
#Mask
@client.command(name="mask",
                decsription="Gives a gun to the user.",
                brief="A gun?",)
@commands.check(creator)
async def mask(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        users[id]['box'].append('a gun')
        await ctx.send(ctx.author.mention + " You said you wanted a gun?")
    with open('users.json', 'w') as f:
        json.dump(users, f)

#Mom   
@client.command(name="mom",
                description="Determines the answer to yes-or-no style questions.",
                brief="Why do you not ask your Mother?",
                aliases=["mother", "mommy", "mama", "ma"])
async def mom(ctx, *, question):
    possible_responses = [" Yes.", " No.", " Maybe.",
                          " Why do you not ask me later?",]
    await ctx.send(ctx.author.mention +
                   f' ```{question}```\n{random.choice(possible_responses)}')
#Pocket Sand
@client.command(name="pocketsand",
                decsription="The best defense against a gun.",
                brief="A best defense.",
                aliases=['ps',])
@commands.check(creator)
async def pocketsand(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        users[id]['box'].append('pocket sand')
        await ctx.send(ctx.author.mention + " I am not sure what you want with this pocket sand.")
    with open('users.json', 'w') as f:
        json.dump(users, f)

#Prizes
@client.command(name="prizes",
                description="Display's the current prize pool.",
                brief="What can you win?",)
async def prizes(ctx):
    global prize
    await ctx.send(ctx.author.mention + " The prizes in the current prize pool \
are: {}.".format(prize))

#Roulette
@client.command(name="roulette",
                description="Adds $1000 to the server's account.",
                brief="Would you like some quick money?",
                aliases=["rr", "blyat",])
async def roulette(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        global luck
        global bang
        if luck == bang:
            luck = random.randint(1,6)
            users[id]['cash'] -= 100
            await ctx.send(ctx.author.mention + " ```Bang!```" +
                       "\n Unfortunate- I will be taking $100 to cover \
your medical expenses.")
        elif luck != bang:
            luck = luck + 1
            users[id]['cash'] += 100
            await ctx.send(ctx.author.mention + " ```Click.```" +
                       "\n Brave- Here is $100 as a reward.")     
    with open('users.json', 'w') as f:
        json.dump(users, f)
        
#Test
@client.command(name="test",
                decsription="A test command.",
                brief="A test command.",)
@commands.check(creator)
async def test(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
        id = str(ctx.author.id)
        users[id]['cash'] += 1000
        await ctx.send(ctx.author.mention + " Test command successfully executed.")
    with open('users.json', 'w') as f:
        json.dump(users, f)

#'Useless' code letting me know the program made it this far.   
print("Done...")

client.run(os.getenv("TOKEN"))
