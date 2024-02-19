import discord
from discord import app_commands
from discord.ext import commands

import modules.logger as log


class embed_modal(discord.ui.Modal, title="Embed Generator"):
    content = discord.ui.TextInput(label= "Contenu", style= discord.TextStyle.short, placeholder= "Contenu", required=False)
    titre = discord.ui.TextInput(label= "Titre", style= discord.TextStyle.short, placeholder= "Titre", required=False)
    description = discord.ui.TextInput(label= "Description", style= discord.TextStyle.paragraph, placeholder= "Description", required=False)
    footer = discord.ui.TextInput(label= "Footer", style= discord.TextStyle.short, placeholder= "Footer", required=False)
    image = discord.ui.TextInput(label= "Image", style= discord.TextStyle.short, placeholder= "URL", required=False)
    
    async def on_submit(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(colour=0x5865f2)
            
            if self.titre.value != '':
                embed.title = self.titre.value
                
            if self.description.value != '':
                embed.description = self.description.value
                
            if self.footer.value != '':
                embed.set_footer(text=self.footer.value)
                
            if self.image.value != '':
                embed.set_image(url=self.image.value)
                
            
            await interaction.channel.send(content=self.content.value, embed=embed)
            
            embed = discord.Embed(description='## Votre embed a bien été envoyé', colour=0x5865f2)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        except Exception as e:
            embed = discord.Embed(description=f"**```{e}```**", colour=0xE74C3C)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            

class generate(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    group = app_commands.Group(name="generate", description="...")
    
    @app_commands.checks.has_permissions(administrator=True)
    
    @group.command(name = "embed", description = "Générer un embed")
    async def embed(
        self,
        interaction: discord.Interaction
    ) -> None:
        log.info(f'/generate embed - {interaction.user} ({interaction.user.id})')
        
        await interaction.response.send_modal(embed_modal())
        
    @embed.error
    async def embed_error(
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
        generate(bot)
    )