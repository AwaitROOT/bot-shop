import discord
from discord import app_commands
from discord.ext import commands
import http.client
import time

import modules.logger as log


class ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.discord_url = "discord.com"
    
    @app_commands.command(name = "ping", description = "Avoir le ping du bot")
    async def ping(
        self,
        interaction: discord.Interaction
    ) -> None:
        
        conn = http.client.HTTPConnection(self.discord_url)
        try:
            start_time = time.time()
            conn.request("HEAD", "/")
            response = conn.getresponse()
            end_time = time.time()
            
            latence = round((end_time - start_time)*1000)
            
            color = 0x2ECC71 if latence < 200 else 0xE67E22
            embed = discord.Embed(title=f'**Le ping du bot est de `{latence}`ms.**', colour=color)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message('**Une erreur est survenue**')
            raise e
        finally:
            conn.close()
        
    @ping.error
    async def ping_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.errors.AppCommandError
    ):
        log.error(error)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ping(bot)
    )