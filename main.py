import json
import discord
from discord.ext import commands
import constants
from class_generator import Generator
import os

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix='/', help_command=None, intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')


@client.command(name="test")
async def test(ctx):
    print('-------', ctx.channel, '---', type(ctx.channel))
    await ctx.send(f'Tested!')


@client.event
async def on_message(message):
    string = message.content
    try:
        data = json.loads(string)
        print(data)
        class_name = data['class_name']

        del data['class_name']
        generator = Generator(class_name, data)

        file_name = class_name.lower() + ".dart"
        with open(file_name, "w") as f:
            f.write(generator.create_class())
        await message.channel.send(file=discord.File(file_name))
        os.remove(file_name)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    client.run(constants.TOKEN)
