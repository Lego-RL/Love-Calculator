from redbot.core import commands
import LoveCalc


def setup(bot):
	cog = LoveCalc(bot)
	bot.add_cog(cog)
