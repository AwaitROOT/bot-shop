import discord
from discord.ext import commands

import json; data = json.load(open('config.json', 'r'))
import logging

from modules.welcome import generate
import modules.log as log; logger = log.setup('search', level=logging.ERROR)


class join(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        if member.guild.id != data['join']['guild']:
            return
        
        image = await generate(
            title = data['join']['image']['title'],
            subtitle = f'@{member.name}' if member.discriminator == '0' else f'{member.name}#{member.discriminator}',
            background = data['join']['image']['background'],
            picture = member.avatar.url if member.avatar else 'https://pbs.twimg.com/media/FpO0xbxaAAAtvPz.png'
        )
        
        await member.guild.get_channel(data['join']['channel']).send(content=f'<@{member.id}>', file=image)
        
        try:
            role = member.guild.get_role(data['join']['role'])
            await member.add_roles(role)
        except Exception as error:
            logger.error('\033[38;2;255;0;0m' + str(error))
    
    @commands.Cog.listener()
    async def on_member_remove(self, member:discord.Member):
        if member.guild.id != data['leave']['guild']:
            return
        
        image = await generate(
            title = data['leave']['image']['title'],
            subtitle = f'@{member.name}' if member.discriminator == 0 else f'{member.name}#{member.discriminator}',
            background = data['leave']['image']['background'],
            picture = member.avatar.url if member.avatar else 'https://pbs.twimg.com/media/FpO0xbxaAAAtvPz.png'
        )
        
        await member.guild.get_channel(data['leave']['channel']).send(content=f'<@{member.id}>', file=image)
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        join(bot)
    )