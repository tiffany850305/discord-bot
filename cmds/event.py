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
import time

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
        voice_channel_1 = str(self.bot.get_channel(jdata["voice_channel"][0]))
        voice_channel_2 = str(self.bot.get_channel(jdata["voice_channel"][1]))
        voice_channel_3 = str(self.bot.get_channel(jdata["voice_channel"][2]))
        voice_channel_4 = str(self.bot.get_channel(jdata["voice_channel"][3]))
        voice_channel_hidden_1 = str(self.bot.get_channel(jdata["voice_channel_hidden"][0]))
        voice_channel_hidden_2 = str(self.bot.get_channel(jdata["voice_channel_hidden"][1]))
        if before_ == voice_channel_hidden_1 or before_ == voice_channel_hidden_2:
            before_ = "None"
        if after_ == voice_channel_hidden_1 or after_ == voice_channel_hidden_2:
            after_ = "None"
        # time
        #localtime = time.localtime(time.time())
        time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # join
        if before_ == "None":
            if after_ == voice_channel_1 or after_ == voice_channel_2 or after_ == voice_channel_3 or after_ == voice_channel_4:
                await channel.send("{member_}加入「{after_}」。{time_}".format(member_=member_, after_=after_, time_=time_))
        # leave
        if after_ == "None":
            if before_ == voice_channel_1 or before_ == voice_channel_2 or before_ == voice_channel_3 or before_ == voice_channel_4:
                await channel.send("{member_}離開「{before_}」。{time_}".format(member_=member_, before_=before_, time_=time_))
        # change
        if before_ != after_:
            if before_ == voice_channel_1 or before_ == voice_channel_2 or before_ == voice_channel_3 or before_ == voice_channel_4:
                if after_ == voice_channel_1 or after_ == voice_channel_2 or after_ == voice_channel_3 or after_ == voice_channel_4:
                    await channel.send("{member_}加入「{after_}」。{time_}".format(member_=member_, after_=after_, time_=time_))
        if before_ == after_ and (before_ == voice_channel_1 or before_ == voice_channel_2 or before_ == voice_channel_3 or before_ == voice_channel_4):
            if before.self_mute == False and after.self_mute == True:
                await channel.send("{member_}靜音。{time_}".format(member_=member_, time_=time_))
            if before.self_mute == True and after.self_mute == False:
                await channel.send("{member_}解除靜音。{time_}".format(member_=member_, time_=time_))
        
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        text_channel_3 = str(self.bot.get_channel(jdata["text_channel"][2]))
        text_channel_4 = str(self.bot.get_channel(jdata["text_channel"][3]))
        if msg.author != self.bot.user:
            if str(msg.channel) != text_channel_3 and str(msg.channel) != text_channel_4:
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
    # online or offline
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # time
        #localtime = time.localtime(time.time())
        time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        channel = self.bot.get_channel(int(jdata["bot_channel"]))
        channel_lonely = self.bot.get_channel(int(jdata["text_channel"][6]))
        before_ = str(before.status)
        after_ = str(after.status)
        id_ = str(before).split("#")[1]
        member_ = str(before).split("#")[0]
        if before_ == "offline" and before_ != after_:
            await channel.send("{member_}上線啦！{time_}".format(member_=member_, time_=time_))
            if id_ == "0800":
                await channel_lonely.send("{member_}上線啦！{time_}".format(member_=member_, time_=time_))
        if before_ != after_ and after_ == "offline":
            await channel.send("{member_}下線啦！{time_}".format(member_=member_, time_=time_))
            if id_ == "0800":
                await channel_lonely.send("{member_}下線啦！{time_}".format(member_=member_, time_=time_))
        
def setup(bot):
    bot.add_cog(Event(bot))