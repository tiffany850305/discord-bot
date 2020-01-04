# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:13:41 2020

@author: MClab
"""

import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot