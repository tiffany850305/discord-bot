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
    async def on_voice_state_update(self, member, before, after):
        channel = self.bot.get_channel(int(jdata["bot_channel"]))
        before_ = str(before.channel)
        after_ = str(after.channel)
        member_ = str(member).split("#")[0]
        if before_ == "306同學會" or before_ == "兩人世界":
            before_ = "None"
        if after_ == "306同學會" or after_ == "兩人世界":
            after_ = "None"
        # join
        if before_ == "None":
            if after_ == "髒話色情性別歧視酒毒品" or after_ == "清新健康" or after_ == "讀書會" or after_ == "掛機":
                await channel.send("{member_}加入「{after_}」。".format(member_=member_, after_=after_))
        # leave
        if after_ == "None":
            if before_ == "髒話色情性別歧視酒毒品" or before_ == "清新健康" or before_ == "讀書會" or before_ == "掛機":
                await channel.send("{member_}離開「{before_}」。".format(member_=member_, before_=before_))
        # change
        if before_ != after_:
            if before_ == "髒話色情性別歧視酒毒品" or before_ == "清新健康" or before_ == "讀書會" or before_ == "掛機":
                if after_ == "髒話色情性別歧視酒毒品" or after_ == "清新健康" or after_ == "讀書會" or after_ == "掛機":
                    await channel.send("{member_}加入「{after_}」！".format(member_=member_, after_=after_))
        if before_ == after_ and (before_ == "髒話色情性別歧視酒毒品" or before_ == "清新健康" or before_ == "讀書會" or before_ == "掛機"):
            if before.self_mute == False and after.self_mute == True:
                await channel.send("{member_}靜音。".format(member_=member_))
            if before.self_mute == True and after.self_mute == False:
                await channel.send("{member_}解除靜音。".format(member_=member_))
        
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author != self.bot.user:
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
                        print("{author}: {string}".format(author=author, string=string))
                        await msg.delete()
                        break
                if keyword_flag:
                    await msg.channel.send("{author}，你這是性騷擾！:angry:".format(author=author))
        
        
def setup(bot):
    bot.add_cog(Event(bot))