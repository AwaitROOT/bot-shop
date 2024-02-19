import discord
from discord.ext import commands
from discord import app_commands

import json; data = json.load(open('config.json', 'r'))
import logging

import modules.vouch as vouchModule
import modules.log as log; logger = log.setup('search', level=logging.ERROR)


botGlobal = None


class Modals():
    async def embed(user:discord.User, stars:int, description:str):
        embed = discord.Embed(description=f'''\
## `{'⭐'*stars}`
### {description}''', colour=0x2d2d31)
        
        embed.set_footer(text=user.name, icon_url=user.avatar.url)
        
        await botGlobal.get_channel(data['vouch']['channel']).send(embed=embed)
        vouchModule.set(user.id, stars)

    
    class one(discord.ui.Modal, title="Avis: ⭐"):
        answer = discord.ui.TextInput(label="Description", placeholder="Le contenu fourni ne fonctionnait pas...", style=discord.TextStyle.short, max_length=1000)

        async def on_submit(self, interaction: discord.Interaction) -> None:
            await interaction.response.defer()
            await Modals.embed(interaction.user, 1, self.answer.value)
    
    class two(discord.ui.Modal, title="Avis: ⭐⭐"):
        answer = discord.ui.TextInput(label="Description", placeholder="Le contenu fourni ne fonctionnait pas...", style=discord.TextStyle.short, max_length=1000)

        async def on_submit(self, interaction: discord.Interaction) -> None:
            await interaction.response.defer()
            await Modals.embed(interaction.user, 2, self.answer.value)
    
    class three(discord.ui.Modal, title="Avis: ⭐⭐⭐"):
        answer = discord.ui.TextInput(label="Description", placeholder="Le contenu proposé est correct", style=discord.TextStyle.short, max_length=1000)

        async def on_submit(self, interaction: discord.Interaction) -> None:
            await interaction.response.defer()
            await Modals.embed(interaction.user, 3, self.answer.value)
    
    class four(discord.ui.Modal, title="Avis: ⭐⭐⭐⭐"):
        answer = discord.ui.TextInput(label="Description", placeholder="Je suis satisfait de mes achats !", style=discord.TextStyle.short, max_length=1000)

        async def on_submit(self, interaction: discord.Interaction) -> None:
            await interaction.response.defer()
            await Modals.embed(interaction.user, 4, self.answer.value)
    
    class five(discord.ui.Modal, title="Avis: ⭐⭐⭐⭐⭐"):
        answer = discord.ui.TextInput(label="Description", placeholder="Je suis satisfait de mes achats !", style=discord.TextStyle.short, max_length=1000)

        async def on_submit(self, interaction: discord.Interaction) -> None:
            await interaction.response.defer()
            await Modals.embed(interaction.user, 5, self.answer.value)


class vouchCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.choices(
        stars = [
            app_commands.Choice(name='⭐⭐⭐⭐⭐', value=5),
            app_commands.Choice(name='⭐⭐⭐⭐', value=4),
            app_commands.Choice(name='⭐⭐⭐', value=3),
            app_commands.Choice(name='⭐⭐', value=2),
            app_commands.Choice(name='⭐', value=1)
        ]
    )
    
    @app_commands.describe(stars='Etoiles')
    
    @app_commands.command(name="vouch")
    async def vouch(self, interaction: discord.Interaction, stars: int):
        if vouchModule.get(interaction.user.id):
            embed = discord.Embed(description=f'### Vous avez déjà donné votre avis.', colour=0x2d2d31)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        if interaction.channel.id != data['vouch']['channel']:
            embed = discord.Embed(description=f'### Veuillez faire cette commande dans <#{interaction.channel.id}>.', colour=0x2d2d31)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        if stars == 1: modal = Modals.one()
        elif stars == 2: modal = Modals.two()
        elif stars == 3: modal = Modals.three()
        elif stars == 4: modal = Modals.four()
        elif stars == 5: modal = Modals.five()

        await interaction.response.send_modal(modal)


    @vouch.error
    async def vouch_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.errors.AppCommandError
    ):
        embed = discord.Embed(description=f'### {str(error)}.', colour=0x2d2d31)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.error('\033[38;2;255;0;0m' + str(error))
    

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id != data['vouch']['channel']:
            return
        if message.author.id == self.bot.user.id:
            return
        
        await message.delete()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(vouchCog(bot))
    global botGlobal
    botGlobal = bot