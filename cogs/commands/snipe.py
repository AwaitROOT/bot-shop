import discord
from discord import app_commands
from discord.ext import commands

import modules.logger as log


class snipe(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.content = None
        self.author = None
    
    access = [1114613392980836352]
    
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.content = message.content
        self.author = message.author
    
    
    @app_commands.checks.has_permissions(administrator=True)
    
    @app_commands.command(name = "snipe", description = "Sniper le dernier message supprimé")
    async def snipe(
        self,
        interaction: discord.Interaction
    ) -> None:
        log.info(f'/snipe - {interaction.user} ({interaction.user.id})')
        
        if self.content == None:
            embed = discord.Embed(description='### Aucun message à snipe', colour=0x3498DB)
            
            await interaction.response.send_message(
                embed=embed
            )
            return
        
        embed = discord.Embed(description=f'```{self.content}```', colour=0x3498DB)
        embed.set_footer(text=f'{self.author} ({self.author.id})')
            
        await interaction.response.send_message(
            embed=embed
        )
        
    @snipe.error
    async def snipe_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.errors.AppCommandError
    ):
        if isinstance(error, app_commands.MissingAnyRole):
            await interaction.response.send_message(
                f"Vous n'avez pas la permission d'executer cette commande.",
                ephemeral = True
            )
        else:
            log.error(error)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        snipe(bot)
    )