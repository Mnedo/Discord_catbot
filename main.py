import asyncio
import discord
from requests import get

TOKEN = str(get('https://tokens-secure.herokuapp.com/api/token/telegram').json())


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            if "stop" in message.content.lower():
                await 'logout'
            elif '!' in message.content.lower():
                file = get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
                await message.channel.send(file)


client = YLBotClient()
client.run(TOKEN)

