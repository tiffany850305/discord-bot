# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:28:44 2020

@author: MClab
"""

import discord
from discord.ext import commands
import json
import random
import os


with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
    print("I'm here.")

@bot.command()
async def load(ctx, extension):
    bot.load_extension("cmds.{extension}".format(extension=extension))
    await ctx.send("Loaded {extension} done!".format(extension=extension))

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension("cmds.{extension}".format(extension=extension))
    await ctx.send("Unloaded {extension} done!".format(extension=extension))

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension("cmds.{extension}".format(extension=extension))
    await ctx.send("Reloaded {extension} done!".format(extension=extension))



for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension("cmds.{filename}".format(filename=filename[:-3]))

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])