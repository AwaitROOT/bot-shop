import discord
from discord.ext import commands


class MemberCount(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def update_member_count(selft, guild):

        channel_id = 1193860024490008659
        channel = guild.get_channel(channel_id)

        if channel:
            await channel.edit(name=f"🌐Membres: {guild.member_count}")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.update_member_count(member.guild)

    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.update_member_count(member.guild)



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        MemberCount(bot)
    )