import discord
from discord import app_commands
from discord.ext import commands

import modules.logger as log

async def setup(bot: commands.Bot) -> None:
    channelID = 1136482798635597856
    
    @bot.tree.context_menu(name="Reporter le message")
    async def receive(
        interaction: discord.Interaction,
        message: discord.Message
    ) -> None:
        content = message.content
        embeds = message.embeds
        embeds.append(discord.Embed(colour=0x2d2d31, description=f'## __Auteur:__ <@{message.author.id}>'))
        embeds.append(discord.Embed(colour=0x2d2d31, description=f'## __Reporté par:__ <@{interaction.user.id}>'))
        
        channel = await bot.fetch_channel(channelID)
        await channel.send(
            content=content,
            embeds=embeds
        )
        await interaction.response.send_message(
            embed=discord.Embed(colour=0x2d2d31, description=f"### Le message a été envoyé à l'équipe de modération"),
            ephemeral=True
        )