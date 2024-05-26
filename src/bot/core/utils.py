import disnake as dis,disnake
import asyncpg

class Economy:
    def __init__(self,connection_params) -> None:
        self.__connection__:asyncpg.Connection = None

    async def launch(self):
        pass

    async def add_balance(self,user:dis.Member):
        pass

    async def remove_balance(self,user:dis.Member):
        pass

    async def create_user(self,user:dis.Member):
        pass

    