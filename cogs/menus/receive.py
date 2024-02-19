import discord
from discord import app_commands
from discord.ext import commands

import modules.logger as log

async def setup(bot: commands.Bot) -> None:
    @bot.tree.context_menu(name="Recevoir en DMs")
    async def receive(
        interaction: discord.Interaction,
        message: discord.Message
    ) -> None:
        if message.author.id != bot.user.id:
            await interaction.response.send_message(
                embed=discord.Embed(colour=0x2d2d31, description=f'### Seul les messages de <@{bot.user.id}> peuvent être envoyé en MP'),
                ephemeral=True
            )
            return
        
        content = message.content
        embeds = message.embeds
        embeds.append(discord.Embed(colour=0x2d2d31, description=f'## __Auteur:__ <@{message.author.id}>'))
        await interaction.user.send(
            content=content,
            embeds=embeds
        )
        await interaction.response.send_message(
            embed=discord.Embed(colour=0x2d2d31, description=f'## Message envoyé'),
            ephemeral=True
        )