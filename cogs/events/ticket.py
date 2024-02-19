import discord
from discord.ext import commands

import asyncio
import os
import pytz

logChannel = 1193217375949049907
categoryChannel = 1193592013891850281

class create(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Créer', style=discord.ButtonStyle.blurple)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(thinking=True, ephemeral=True)
        channel: discord.TextChannel = await interaction.guild.create_text_channel(name=f'ticket-{interaction.user.name}', category=interaction.guild.get_channel(categoryChannel), topic=f'Ticket de {interaction.user.name}'
                                                                                 , overwrites={interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False), interaction.user: discord.PermissionOverwrite(view_channel=True)})
        
        embed = discord.Embed(description=f'## Salut <@{interaction.user.id}> !\n\u200b\n### Décrivez la raison de votre ticket', color=0x5865f2)
        await channel.send(embed=embed, view=delete())
        
        embed = discord.Embed(description=f'## Ticket créé ! <#{channel.id}>', color=0x5865f2)
        await interaction.followup.send(embed=embed)
        
        embed = discord.Embed(description=f'### <@{interaction.user.id}> a créé son ticket', color=0x2ECC71)
        await interaction.client.get_channel(logChannel).send(embed=embed)


class delete(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Supprimer', style=discord.ButtonStyle.danger)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(description=f'### Êtes-vous sûr de supprimer ?', color=0xE67E22)
        await interaction.channel.send(embed=embed, view=sure())
        await interaction.response.defer()
        button.disabled = True


class sure(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Oui', style=discord.ButtonStyle.green)
    async def yesButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(description=f'### Le ticket va être supprimé.', color=0x5865f2)
        await interaction.channel.send(embed=embed)
        button.disabled = True
        
        await interaction.response.defer()
        
        if not os.path.exists('temp'):
            os.makedirs('temp')

        tz = pytz.timezone("Europe/Paris")
        fileName = f"temp/{interaction.channel.name}.txt"
        with open(fileName, "w") as file:
            async for msg in interaction.channel.history(limit=None):
                file.write(f"{msg.created_at.astimezone(tz)} - {msg.author.name}: {msg.clean_content}\n")
        
        embed = discord.Embed(description=f'### <@{interaction.user.id}> a supprimé son ticket', color=0xE74C3C)
        await interaction.client.get_channel(logChannel).send(embed=embed, file=discord.File(fileName))
        os.remove(fileName)
        
        await interaction.channel.delete()
    
    @discord.ui.button(label='Non', style=discord.ButtonStyle.red)
    async def noButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()
        button.disabled = True



class ticket(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.channel = 1191390209099710494
        self.message = 1193583165181267969
        
    @commands.Cog.listener()
    async def on_ready(self):
        message:discord.Message = await self.bot.get_channel(self.channel).fetch_message(self.message)
        await message.edit(embeds=message.embeds, view=create())
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ticket(bot)
    )