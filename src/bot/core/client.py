import disnake as dis,disnake
import os
from disnake.ext.commands import InteractionBot

class EconomyBot(InteractionBot):
    def __init__(self):
        super().__init__(intents=dis.Intents.all())

    def load_cogs(self):
        for file in os.listdir(os.path.join("src","cogs")):
            self.load_extensions(os.path.join("src","cogs",file))
        
    