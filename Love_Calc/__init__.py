from redbot.core import commands
from .love_calc import LoveCalc


def setup(bot):
	cog = LoveCalc(bot)
	bot.add_cog(cog)