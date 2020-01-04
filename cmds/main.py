# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:09:00 2020

@author: MClab
"""

import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("{ms} (ms)".format(ms=round(self.bot.latency*1000)))
        
def setup(bot):
    bot.add_cog(Main(bot))