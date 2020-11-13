import discord
from discord.ext import commands
import os
import random

# ``` Hey ```

EghtBallAnsw = ['As I see it, yes',
 'Ask again later',
 'Better not tell you now',
 'Cannot predict now',
 'Concentrate and ask again',
 'Don’t count on it',
 'It is certain',
 'It is decidedly so',
 'Most likely',
 'My reply is no',
 'My sources say no',
 'Outlook not so good',
 'Outlook good',
 'Reply hazy, try again',
 'Signs point to yes',
 'Very doubtful',
 'Without a doubt',
 'Yes',
 'Yes – definitely',
 'You may rely on it']

RPS_Output = ['Rock', 'Paper', 'Scissors']
client = commands.Bot(command_prefix = 'm!')

#@client.event
#async def on_message(message):
#    if message.content.startswith('m!8ball'):
#        ...
        #question = message.content.split(' ', 1)

        #embedBall = discord.Embed(
        #title = '8 Ball',
        #color = discord.Color.blue()
        #)

        #embedBall.set_thumbnail(url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/248/pool-8-ball_1f3b1.png')
        #embedBall.add_field(name = 'Player:', value = '{}'.format(message.author), inline = False)
        #embedBall.add_field(name = 'Question:', value = '{}'.format(str(question[1])) + '\n', inline = False)
        #embedBall.add_field(name = 'Answer:', value = '{}'.format(random.choice(EghtBallAnsw)), inline = False)

        #await message.author.send(embed = embedBall)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='some jams🎵'))
    print('Bot Launched!')

@client.command()
async def commands(message):
    embedHelp = discord.Embed(
        title = '**-=COMMANDS=-**',
        color = discord.Color.blue()
    )

    embedHelp.set_thumbnail(url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/emojidex/112/black-question-mark-ornament_2753.png')
    embedHelp.add_field(name = 'm!commands:', value = 'sends you command list', inline = False)
    embedHelp.add_field(name = 'm!ping:', value = 'pings bot' + '\n', inline = False)
    embedHelp.add_field(name = 'm!8ball <question>:', value = 'tells your fortune', inline = False)
    embedHelp.add_field(name = 'm!rps <item> <bet>:', value = 'Rock, Paper, Scissors', inline = False)
    embedHelp.add_field(name = 'm!verify:', value = 'verify yourself and play games', inline = False)
    embedHelp.add_field(name = 'm!wallet:', value = 'check your server points', inline = False)
    embedHelp.add_field(name = 'm!clear:', value = 'clears the last 100 messages', inline = False)

    await message.author.send(embed = embedHelp)

@client.command()
async def clear(ctx):
    await ctx.channel.purge(limit = 100)

@client.command()
async def ping(message):
    await message.channel.send('Pong!')

@client.command()
async def wallet(message):
    with open('C:/Users/Johnathon/Desktop/Discord Bot - Mr Game Bot/Media/Players/{}.txt'.format(str(message.author.id)), 'r') as f:
        data = f.read()
        data = data.split('-b ', 1)


    embedWallet = discord.Embed(
        title = '**Player Wallet**',
        color = discord.Color.red()
    )

    embedWallet.set_thumbnail(url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/whatsapp/238/money-bag_1f4b0.png')
    embedWallet.add_field(name = 'Player:', value = '{}'.format(message.author), inline = False)
    embedWallet.add_field(name = 'Points:', value = '{}'.format(str(data[1])) + '\n', inline = False)


    await message.channel.send(embed = embedWallet)

@client.command()
async def verify(message):
    with open('C:/Users/Johnathon/Desktop/Discord Bot - Mr Game Bot/Media/Players/{}.txt'.format(str(message.author.id)), 'w') as f:
        f.write('-b 500')
        f.flush()

    await message.channel.send("{}, you've been **verified!**".format(message.author.mention))

@client.command()
async def rps(context):
    context.message.content = context.message.content.lower()
    item = context.message.content.split(' ', 2)

    embedRPS = discord.Embed(
        title = '**Player Wallet**',
        color = discord.Color.red()
    )

    embedRPS.set_thumbnail(url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/whatsapp/238/money-bag_1f4b0.png')
    embedRPS.add_field(name = "{}'s Choice:".format(context.message.author), value = '{}'.format(str(item[1])) + '\n', inline = False)
    embedRPS.add_field(name = "Mr Game Bot's Choice:", value = '{}'.format(random.choice(RPS_Output)) + '\n', inline = False)
    embedRPS.add_field(name = 'Output:', value = '{}'.format() + '\n', inline = False)

    await context.message.channel.send(embed = embedRPS)


client.run('')
