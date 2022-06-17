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
    # try:
    data = json.loads(string)
    print(data)
    class_name = data['class_name']
    del data['class_name']  # now the data variable contains only fields

    final_dart_code = ""

    generator = Generator(class_name, data)
    final_dart_code += generator.create_class() + "\n\n"

    for key, value in data.items():
        if type(value) == dict:
            temp_generator = Generator(key.capitalize(), value)
            final_dart_code += temp_generator.create_class()
        elif type(value) == list:
            dtype = type(value[0])
            if dtype == dict:
                temp_generator = Generator(key.capitalize(), value[0])
                final_dart_code += temp_generator.create_class() + "\n\n"

    file_name = class_name.lower() + ".dart"
    with open(file_name, "w") as f:
        f.write(final_dart_code)
    await message.channel.send(file=discord.File(file_name))
    os.remove(file_name)
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    client.run(constants.TOKEN)
