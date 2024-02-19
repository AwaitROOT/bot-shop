import discord
from discord.ext import commands




class boost(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild = 1191390137662312518
        self.channel = 1193216932149739651
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.type != discord.MessageType.premium_guild_subscription:
            return
        
        guild = self.bot.get_guild(self.guild)
        
        
        embed = discord.Embed(description=f"## **`{message.author.name}` a boost le serveur.`💜`**", colour=0x9B59B6)
        await guild.get_channel(self.channel).send(content=f'<@{message.author.id}>',embed=embed)
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        boost(bot)
    )