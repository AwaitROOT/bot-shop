import discord
from discord.ext import commands
from discord import app_commands

import json; data = json.load(open('config.json', 'r'))
import logging

import modules.vouch as vouchModule
import modules.log as log; logger = log.setup('search', level=logging.ERROR)


class averageCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    group = app_commands.Group(name='average', description='...')
    
    
    @group.command(name="vouch")
    async def vouch(self, interaction: discord.Interaction):
        average = vouchModule.getAverage()

        embed = discord.Embed(description=f'La moyenne est de {round(average, 2)} ⭐', colour=0x2d2d31)
        
        await interaction.response.send_message(embed=embed, ephemeral=True)


    @vouch.error
    async def vouch_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.errors.AppCommandError
    ):
        embed = discord.Embed(description=f'### {str(error)}.', colour=0x2d2d31)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.error('\033[38;2;255;0;0m' + str(error))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(averageCog(bot))