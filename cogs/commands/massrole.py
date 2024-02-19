import discord
from discord import app_commands
from discord.ext import commands


class massrole(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    

    @app_commands.checks.has_permissions(administrator=True)
    
    @app_commands.command(name = "massrole", description = "Ajouter des roles en mass sur votre serveur")

    
    async def mass_role(self, interaction: discord.Interaction, role: discord.Role):
        
        embed1 = discord.Embed(description=f"### Ajout en cours...")
        await interaction.response.send_message(embed = embed1)
        
        i = 0
    
        for member in interaction.guild.members:
            if not member.bot:
                i += 1
            await member.add_roles(role)

        
        embed2 = discord.Embed(description=f"### Le rôle <@&{role.id}> a été ajouté à {i} membres.")


        await interaction.edit_original_response(embed= embed2)


    @mass_role.error
    async def mass_server_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.errors.AppCommandError
    ):
        print('\033[38;2;255;0;0m' + error)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        massrole(bot)
    )