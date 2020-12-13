import discord
import asyncio
from discord.ext import commands


bot = commands.Bot(command_prefix='') # Dein Prefix
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Eingeloggt {}'.format(bot.user.name))
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening,
                                      name="")) # Status
        await asyncio.sleep(20)


bot.run('') # Bot Token
