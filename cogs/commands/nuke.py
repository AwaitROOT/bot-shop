import discord
from discord import app_commands
from discord.ext import commands

import modules.logger as log


class nuke(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.checks.has_permissions(administrator=True)
    
    @app_commands.command(name = "nuke", description = "Cloner un salon")
    async def nuke(
        self,
        interaction: discord.Interaction
    ) -> None:
        log.info(f'/nuke - {interaction.user} ({interaction.user.id})')
        
        await interaction.response.send_message(
            content='**Clonage en cours...**',
            ephemeral=True
        )
        
        new_channel = await interaction.channel.clone()
        await interaction.channel.delete()
        embed = discord.Embed(title='Le salon a été correctement cloné', color=discord.Color.blue)
        new_channel.send(embed=embed)
        
    @nuke.error
    async def nuke_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.errors.AppCommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                f"Vous n'avez pas la permission d'executer cette commande.",
                ephemeral = True
            )
        else:
            log.error(error)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        nuke(bot)
    )