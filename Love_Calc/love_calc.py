import discord
from discord.ext import commands
from redbot.core import commands
import random

class Love_Calc(commands.Cog):
	'''Love Calculator cog! '''

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def lovecalc(self, ctx, name1: str, name2: str):
	    '''This function will take two people's names and return a randomized percentage of compatibility.'''
	    percentage = random.choice(range(1, 100))

	    name1, name2 = name1.lower(), name2.lower()

	    if(name1 == 'joey' and name2 == 'gianna') or (name1 == 'gianna' and name2 == 'joey'):
	    	await ctx.send(f'{name1} and {name2} are {100 + percentage}% compatible.')
	    else:
	    	await ctx.send(f'{name1} and {name2} are {percentage}% compatible.')
	


def setup(bot):
	bot.add_cog(Love_Calc(bot))