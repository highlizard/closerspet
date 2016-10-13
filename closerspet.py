from discord.ext import commands

class closerspet:
	"""Closers pet command."""
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

	@commands.command(pass_context=True, aliases=[])
	async def seha8(self, context):
		await self.bot.send_file(context.message.channel, '{}8seha.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def seulbi8(self, context):
		await self.bot.send_file(context.message.channel, '{}8seulbi.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def yuria8(self, context):
		await self.bot.send_file(context.message.channel, '{}8yuri.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def mistel8(self, context):
		await self.bot.send_file(context.message.channel, '{}8misteltein.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def nata8(self, context):
		await self.bot.send_file(context.message.channel, '{}8nata.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def levia8(self, context):
		await self.bot.send_file(context.message.channel, '{}8levia.PNG'.format(self.base))

	@commands.command(pass_context=True, aliases=[])
	async def harpy8(self, context):
		await self.bot.send_file(context.message.channel, '{}8harpy.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def j8(self, context):
		await self.bot.send_file(context.message.channel, '{}8J.PNG'.format(self.base))
			
	@commands.command(pass_context=True, aliases=[])
	async def vaccine(self, context):
		await self.bot.send_file(context.message.channel, '{}Vaccine.PNG'.format(self.base))
			
	@commands.command(pass_context=True, aliases=[])
	async def washing(self, context):
		await self.bot.send_file(context.message.channel, '{}washing.PNG'.format(self.base))
		
	@commands.command(pass_context=True, aliases=[])
	async def sehaok(self, context):
		await self.bot.send_file(context.message.channel, '{}sehaok.png'.format(self.base))
	
def setup(bot):
	n = closerspet(bot)
	bot.add_cog(n)
