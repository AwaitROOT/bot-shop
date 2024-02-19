import discord
from discord.ext import commands


class autorole(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild = 1191390137662312518
        self.role = 1191390161414664304

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        if member.guild.id != self.guild:
            return
        role = member.guild.get_role(self.role)
        await member.add_roles(role)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        autorole(bot)
    )