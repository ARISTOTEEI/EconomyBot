import disnake as dis,disnake
from src.bot.core.client import EconomyBot
from disnake.ext.commands import Cog
from disnake.ext import commands
class EventReady(Cog):
    def __init__(self,bot:EconomyBot):
        self.bot = bot

    @commands.Cog.listener(name=dis.Event.ready)
    async def on_ready(self):
        pass

def setup(bot:EconomyBot):
    bot.add_cog(EventReady(bot))