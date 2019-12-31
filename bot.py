# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:15:45 2019

@author: MClab
"""

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
    print("I'm here.")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(661444571854536715)
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(661444571854536715)
    await channel.send(f"{member} leave!")

bot.run("NjYxNDMxNjQ4MDE2OTI0Njky.XgrUfg.SM1_sfEM7p0WnYjnycgvZ6URF1c")