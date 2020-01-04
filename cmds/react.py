# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:30:20 2020

@author: MClab
"""

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)
    
class React(Cog_Extension):
    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
    @commands.command()
    async def freestyle(self, ctx):
        await ctx.send("你媽的頭，像皮球，一腳踢到百貨大樓。\n\
百貨大樓，賣皮球，賣的就是你媽的頭。\n\
你媽的屁，震天地，一屁蹦到了義大利。\n\
義大利的國王正在看戲，聞到這股屁，非常滿意。\n\
誰放的臭，當教授。\n\
誰放的響，那麼當校長。") 


def setup(bot):
    bot.add_cog(React(bot))