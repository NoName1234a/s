from discord.ext import commands
import discord
import random
from discord.ext.commands import BucketType
from discord.ext.commands import cooldown



prefix = '.'
gencooldown = 5
  
token = 'ODc2Nzk0NjE5ODM5NTE2Njcy.YRpQnw.y707_pmTPGerozsycGtbB8feRyw'
maincolor = 0x2ecc71

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help')

accountsfile = open("Spotify.txt").read().splitlines()
nordvpnfile = open("NordVPN.txt").read().splitlines()
disneyplus = open("DisneyPlus.txt").read().splitlines()

@bot.event
async def on_command_error(ctx, error: Exception):
  if isinstance(error, commands.CommandNotFound):
        return
  else:
	  embed = discord.Embed(color=maincolor, description=f'{error}')
	  await ctx.send(embed=embed)



@bot.command()
@cooldown(1, gencooldown, BucketType.user)
async def gen(ctx,type):
  if str(type).lower() == "spotify":
    chosenaccount = random.choice(accountsfile)
    embed=discord.Embed(title="Spotify Gen",description=f"Your spotify account is: `{chosenaccount}`", color=maincolor)
    embed.set_footer(text=f'Requested by {ctx.author.name}',  icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://c.tenor.com/Ez4n3mgLHxEAAAAC/spotify-cholo.gif")
    await ctx.author.send(embed=embed)
    embed=discord.Embed(title="Spotify Gen",description=f"I have sent you a spotify account to your dms.", color=maincolor)
    embed.set_footer(text=f'Requested by {ctx.author}',  icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://c.tenor.com/Ez4n3mgLHxEAAAAC/spotify-cholo.gif")
    await ctx.send(embed=embed)
  elif str(type).lower() == "nordvpn":
    chosenaccount = random.choice(nordvpnfile)
    embed=discord.Embed(title="nordvpn Gen",description=f"Your NordVPN account is: `{chosenaccount}`", color=maincolor)
    embed.set_footer(text=f'Requested by {ctx.author.name}',  icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cache.cracked.to/ce9c5f6270f2327fae6863508a5d74b10e236f19/68747470733a2f2f692e67697068792e636f6d2f6d656469612f3668566a676131765837366153536c5956662f67697068792e676966")
    await ctx.author.send(embed=embed)
    embed=discord.Embed(title="nordvpn Gen",description=f"I have sent you a nordvpn account to your dms.", color=maincolor)
    embed.set_footer(text=f'Requested by {ctx.author}',  icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cache.cracked.to/ce9c5f6270f2327fae6863508a5d74b10e236f19/68747470733a2f2f692e67697068792e636f6d2f6d656469612f3668566a676131765837366153536c5956662f67697068792e676966")
    await ctx.send(embed=embed)
  elif str(type).lower() == "disneyplus":
    chosenaccount = random.choice(disneyplus)
    embed=discord.Embed(title="disneyplus Gen",description=f"Your Disney+ account is: `{chosenaccount}`", color=maincolor)
    embed.set_footer(text=f'Requested by {ctx.author.name}',  icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://assets.bigcartel.com/product_images/251124173/F42F3593-636D-4E77-BF2B-3E12D5510FDA.gif?auto=format&fit=max&w=1500")
    await ctx.author.send(embed=embed)
    embed=discord.Embed(title="disneyplus Gen",description=f"I have sent you a disney+ account to your dms.", color=maincolor)
    embed.set_footer(text=f'Requested by {ctx.author}',  icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://assets.bigcartel.com/product_images/251124173/F42F3593-636D-4E77-BF2B-3E12D5510FDA.gif?auto=format&fit=max&w=1500")
    await ctx.send(embed=embed)
  else:
    await ctx.send("Please enter a supported type of account!")


bot.run(token)

