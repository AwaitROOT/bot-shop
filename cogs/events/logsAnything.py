import discord
from discord.ext import commands


class logsAnything(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.guild = 1191390137662312518
        
        self.channels = {
            'message':1193217375949049907
        }
        
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.guild.id != self.guild:
            return
        if not before.content:
            return
        if before.author == self.bot.user:
            return
        
        embed = discord.Embed(description=f"""
## Avant
```{before.content}```
## Après
```{after.content}```""", colour=0xE67E22)
        await before.guild.get_channel(self.channels['message']).send(content=f'<@{before.author.id}>', embed=embed)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id != self.guild:
            return
        if not message.content:
            return
        if message.author == self.bot.user:
            return
        
        embed = discord.Embed(description=f"""
## Message supprimé
```{message.content}```""", colour=0xE74C3C)
        await message.guild.get_channel(self.channels['message']).send(content=f'<@{message.author.id}>', embed=embed)
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        logsAnything(bot)
    )