import discord
from discord.ext import commands

import modules.logger as log
import os
import json; data = json.load(open('config.json', 'r'))
import threading
import asyncio


async def console():
    while False:
        response = await asyncio.to_thread(input)
        
        if response.startswith('load '):
            ext = response[5:]
            try:
                await bot.load_extension(ext)
                print(f'{ext} chargé')
            except Exception as e:
                print(e)
        elif response.startswith('unload '):
            ext = response[7:]
            try:
                await bot.unload_extension(ext)
                print(f'{ext} déchargé')
            except Exception as e:
                print(e)
        elif response.startswith('reload '):
            ext = response[7:]
            try:
                await bot.reload_extension(ext)
                print(f'{ext} rechargé')
            except Exception as e:
                print(e)


class client(commands.Bot):
    
    def __init__(self):
        super().__init__(
            command_prefix='$',
            intents = discord.Intents.all(),
            application_id = data["app_id"]
        )

        self.initial_extensions = []
        
        for file in os.listdir("cogs/commands"):
            if file != '__pycache__':
                self.initial_extensions.append(f"cogs.commands.{file[:-3]}")
        for file in os.listdir("cogs/events"):
            if file != '__pycache__':
                self.initial_extensions.append(f"cogs.events.{file[:-3]}")
        for file in os.listdir("cogs/tasks"):
            if file != '__pycache__':
                self.initial_extensions.append(f"cogs.tasks.{file[:-3]}")
        for file in os.listdir("cogs/menus"):
            if file != '__pycache__':
                self.initial_extensions.append(f"cogs.menus.{file[:-3]}")

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        
        global synced
        synced = await bot.tree.sync()
        
    async def on_ready(self):
        print(f'{self.user} est connecté avec {len(synced)} commande(s) synchronisée(s)')
        await asyncio.create_task(console())
    

bot = client(); bot.run(data["token"])