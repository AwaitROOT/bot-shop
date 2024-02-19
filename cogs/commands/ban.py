import discord
from discord import app_commands
from discord.ext import commands




class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="ban", description="Bannir un utilisateur")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, utilisateur: discord.Member, raison: str = None):
        for member in interaction.guild.members:
            if not member.bot:
                await utilisateur.ban(reason=raison)
                await interaction.response.send_message(f"{utilisateur.mention} a été banni avec comme raison {raison}.")


    @ban.error
    async def ban_error(self, interaction: discord.Interaction, error: app_commands.errors.AppCommandError):
        print('\033[38;2;255;0;0m' + error)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Ban(bot)
    )