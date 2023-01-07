import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    # if the message is from the bot itself, ignore it
    if message.author == client.user:
        return

    # replace the "!hello" to whatever you want the bot to react
    if message.content.startswith('!hello'):
        await message.channel.send("You are a worthless bitch-ass nigga. Your life literally is as valuable as a summer ant." 
           "I'm just gonna stomp you, you're gonna keep coming back, I'm gonna seal up all my cracks,"
           "you're gonna keep coming back why? Because you keep smelling the syrup, you worthless bitch-ass nigga." 
           "You're gonna stay on my dick until you die. You serve no purpose in life." 
           "Your purpose in life is to be in my stream sucking on my dick daily." 
           "Your purpose in life is to be in that chat blowing a dick daily." 
           "Your life is nothing. You serve zero purpose. You should kill yourself now." 
           "and give somebody else a piece of that oxygen," 
           "and ozone layer that's covered up so that we can breathe inside this blue trap bubble." 
           "because what are you here for, to worship me? Kill yourself. I mean that with a hundred percent," 
           "with a thousand percent.")
        await message.channel.send("https://media.tenor.com/67LIumILNRsAAAAd/ltg-low-tier-god.gif")

client.run('YOUR TOKEN')
