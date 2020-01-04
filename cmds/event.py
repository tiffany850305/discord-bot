# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:09:30 2020

@author: MClab
"""

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)
    
class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["general_channel"]))
        await channel.send("{member} join!".format(member=member))
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["general_channel"]))
        await channel.send("{member} leave!".format(member=member))
        
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if str(msg.channel) != "306同學會" and str(msg.channel) != "秘密":
            keywords = jdata["keywords"]
            #split author
            author = str(msg.author)
            author = author.split("#")[0]
            #string detection
            string = str(msg.content)
            keyword_flag = 0
            for i in keywords:
                if (string.find(i)+1):
                    keyword_flag = 1
                    break
            #print(msg.channel)
            #print(self.bot.get_channel(int(jdata["general_channel"])))
            if keyword_flag and msg.author != self.bot.user:
                await msg.channel.send("{author}，你這是性騷擾！:angry:".format(author=author))
        
        
def setup(bot):
    bot.add_cog(Event(bot))