from discord.ext import commands

class closerspet:
	def __init__(self, bot):
		self.bot = bot
		self.base = 'data/closerspet/images/'

	@commands.command(pass_context=True)
	async def minibug(self, context):
	   await self.bot.send_file(context.message.channel, '{}bug.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def penguin(self, context):
	   await self.bot.send_file(context.message.channel, '{}penguin.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seha(self, context):
	   await self.bot.send_file(context.message.channel, '{}seha.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seulbi(self, context):
	   await self.bot.send_file(context.message.channel, '{}seulbi.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def levia(self, context):
		await self.bot.send_file(context.message.channel, '{}levia.png'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def selin(self, context):
		await self.bot.send_file(context.message.channel, '{}selin.png'.format(self.base))

	
def setup(bot):
	n = closerspet(bot)
	bot.add_cog(n)
