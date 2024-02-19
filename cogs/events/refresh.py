import discord
from discord.ext import commands


class refresh(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} membres"))
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} membres"))
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} membres"))
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        refresh(bot)
    )