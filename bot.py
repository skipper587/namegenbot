# -*- coding: utf-8 -*-
import discord

from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

import random

import asyncio
import os

# Initialize Client
nameGen = discord.Client()

# Initialize Bot
nameGenBot = commands.Bot(command_prefix="+")

versionNumber = "1.1.7"
modRoleNames = ["Olo'eyktan","Eyktan"]

# Na'vi Alphabet
vowels = ["a","ä","e","i","ì","o","u","aw","ay","ew","ey"]
vowelProbabilities = [10,10,10,10,10,10,10,2,2,2,2]
consonants = ["'","f","h","k","kx","l","m","n","ng","p","px","r","s","t","tx","ts","v","w","y","z"]
consonantProbabilities = [1,6,6,6,3,6,6,6,4,6,3,4,6,6,3,6,5,5,5,5]
pseudovowels = ["ll","rr"]
diphthongs = ["aw","ay","ew","ey"]

preconsonants = ["f","s","ts"]
onsets_withpre = ["k","kx","l","m","n","ng","p","px","r","t","tx","w","y"]
onsetProbabilities = [5,2,5,5,5,4,5,2,4,5,2,3,3]
codas = ["'","k","kx","l","m","n","ng","p","px","r","t","tx"]
codaProbabilities = [50,8,3,8,8,8,3,8,3,8,8,3]

# Language Rules #
# A syllable may start with a vowel
# A syllable may end with a vowel
# A consonant may start a syllable
# A consonant cluster comprised of f, s, or ts + p, t, k, px, tx, kx, m, n, ng, r, l, w, or y may start a syllable
# Px, tx, kx, p, t, k, ', m, n, l, r, or ng may occur in syllable-final position
# Ts, f, s, h, v, z, w, or y may not occur in syllable-final position
# No consonant clusters in syllable-final position
# A syllable with a pseudovowel must start with a consonant or consonant cluster and must not have a final consonant

# Valid Syllables #
# Just one vowel
# Consonant and vowel
# Consonant cluster and vowel
# Vowel and coda
# Consonant, vowel and coda
# Consonant cluster, vowel and coda
# Consonant and pseudovowel
# Consonant cluster, pseudovowel

def ruleOne():
    vowel = random.choices(vowels, weights=vowelProbabilities)
    return vowel[0]

def ruleTwo():
    vowel = random.choices(vowels, weights=vowelProbabilities)
    consonant = random.choices(consonants, weights=consonantProbabilities)
    s = consonant[0] + vowel[0]
    return s

def ruleThree():
    vowel = random.choices(vowels, weights=vowelProbabilities)
    onset = random.choices(onsets_withpre, weights=onsetProbabilities)
    s = preconsonants[random.randint(0,2)] + onset[0] + vowel[0]
    return s

def ruleFour():
    vowel = random.choices(vowels, weights=vowelProbabilities)
    s = vowel[0] + codas[random.randint(0,11)]
    return s

def ruleFive():
    consonant = random.choices(consonants, weights=consonantProbabilities)
    vowel = random.choices(vowels, weights=vowelProbabilities)
    coda = random.choices(codas, weights=codaProbabilities)
    s = consonant[0] + vowel[0] + coda[0]
    return s

def ruleSix():
    vowel = random.choices(vowels, weights=vowelProbabilities)
    onset = random.choices(onsets_withpre, weights=onsetProbabilities)
    coda = random.choices(codas, weights=codaProbabilities)
    s = preconsonants[random.randint(0,2)] + onset[0] + vowel[0] + coda[0]
    return s

def ruleSeven():
    consonant = random.choices(consonants, weights=consonantProbabilities)
    s = consonant[0] + pseudovowels[random.randint(0,1)]
    return s

def ruleEight():
    onset = random.choices(onsets_withpre, weights=onsetProbabilities)
    s = preconsonants[random.randint(0,2)] + onset[0] + pseudovowels[random.randint(0,1)]
    return s

def outputCheck(user):
    fileName = 'users/' + str(user.id) + '.tsk'

    if not os.path.exists(fileName):
        return "English"
    else:
        # Determines Language Output
        fh = open(fileName, 'r')
        lang = fh.readline().strip()
        fh.close()
        return lang

def nameGen(numOut, numSyllables):
    names = []
    name = ""
    output = " "

    n = int(numOut)
    i = int(numSyllables)

    # Conditional Loop for Number of Names
    while n>0:
        i = int(numSyllables)

        # Conditional Loop for Number of Syllables
        while i>0:
            syllables = [1, 2, 3, 4, 5, 6, 7, 8]
            p = [20, 7.5, 7.5, 30, 30, 4, .5, .5]
            rule = random.choices(syllables, weights = p)
            rule = int(rule[0])
            # rule = random.randint(0,7)
            if rule == 1 and not i == 1:
                name = name + ruleOne()
                i-=1
            elif rule == 2:
                name = name + ruleTwo()
                i-=1
            elif rule == 3:
                name = name + ruleThree()
                i-=1
            elif rule == 4:
                name = name + ruleFour()
                i-=1
            elif rule == 5:
                name = name + ruleFive()
                i-=1
            elif rule == 6:
                name = name + ruleSix()
                i-=1
            elif rule == 7:
                name = name + ruleSeven()
                i-=1
            else:
                name = name + ruleEight()
                i-=1

        # Building the Output
        name = name.replace("''", "'")
        name = name.replace("kk","k")
        name = name.replace("kxkx", "kx")
        name = name.replace("mm", "m")
        name = name.replace("nn", "n")
        name = name.replace("ngng", "ng")
        name = name.replace("pp", "p")
        name = name.replace("pxpx", "px")
        name = name.replace("tt", "t")
        name = name.replace("txtx", "tx")
        name = name.replace("yy","y")
        name = name.replace("aa", "a")
        name = name.replace("ää", "ä")
        name = name.replace("ee", "e")
        name = name.replace("ii", "i")
        name = name.replace("ìì", "ì")
        name = name.replace("oo", "o")
        name = name.replace("uu", "u")
        name = name.replace("lll","ll")
        name = name.replace("rrr","rr")
        name = name.capitalize()
        names.append(name)

        # Resetting for next loop
        name = ""
        n-=1

    # Finalizing the Output    
    n = int(numOut)
    for num in names:
        output = output + names[n-1]
        if n > 1:
            output = output + ", "
        n -= 1
    return output

@nameGenBot.event
async def on_ready():
        # This will be called when the bot connects to the server.
        print("NameGenBot is ready.")

# Help Module
@nameGenBot.command(name="howto")
async def howto(ctx):

    langCheck = outputCheck(ctx.message.author)
    
    if langCheck.lower() == "english":
        await ctx.send("Syntax for the command is `+generate <number of names> <number of syllables>`. Maximum number of names is capped at 20 and syllables is capped at 4.")
    elif langCheck.lower() == "na'vi":
        await ctx.send("Fte sivar `+generate`ti, fìkem si: `+generate <stxoä holpxay> <aylì'kongä holpxay>`. Stxoä txantewä holpxay lu mevotsìng ulte lì'kongä txantewä holpxay lu tsìng.")
    else:
        await ctx.send("Somehow, and god knows how, you fucked up.")

# Generate # of random names
@nameGenBot.command(name="generate",aliases=['ngop'])
async def generate(ctx, numOut, numSyllables):
    # Initializing Variables
    n = int(numOut)
    i = int(numSyllables)

    langCheck = outputCheck(ctx.message.author)

    if not n <= 0 and not i <= 0:
        if langCheck.lower() == "english":
            if not i <= 3:
                await ctx.send("Maximum syllable count allowed by the bot is 4. It is highly recommended that you select a name that is between 1 and 3 syllables.")
            elif not n <= 20:
                await ctx.send("Maximum name count allowed is 20.")
            else:
                output = nameGen(n, numSyllables)
                await ctx.send("Here are your names:" + output)
        elif langCheck.lower() == "na'vi":
            if not i <= 3:
                await ctx.send("Lì'kongä txantewä holpxay lu tsìng. Sweylu txo ngal ftxivey tstxoti a lu tsa'ur lì'kong apxey, lì'kong amune, fu lìkong a'aw.")
            elif not n <= 20:
                await ctx.send("Stxoä txantxewä holpxay lu mevotsìng.")
            else:
                output = nameGen(n, numSyllables)
                await ctx.send("Faystxo lu ngaru:" + output)
        else:
            await ctx.send("Somehow, and god knows how, you fucked up.")
    else:
        if langCheck.lower() == "english":
            await ctx.send("Please enter a value greater than zero. If you need help with the `+generate` command, type `+howto`")
        elif langCheck.lower() == "na'vi":
            await ctx.send("Rutxe sar holpxayti a to kew lu apxa. Txo kivin srungti ngal, `+howto`ri pamrel si nga.")
        

# Error Handling for !generate
@generate.error
async def generate_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send("Invalid syntax. If you need help with the `+generate` command, type `+howto`")

# Version
@nameGenBot.command(name='version',aliases=['srey'])
async def version(ctx):
    displayversion = ["Srey: ", versionNumber]
    await ctx.send(''.join(displayversion))

# User Preferences
@nameGenBot.command(name='language',aliases=['lì\'fya'])
async def profile(ctx, *setting):
    user = ctx.message.author
    fileName = 'users/' + str(user.id) + '.tsk'
    setting = ''.join(setting)
    preference = str(setting).lower()
    
    # Updates the user profile.
    if not os.path.exists(fileName):
        fh = open(fileName, 'w')
        fh.write('English')
        fh.close()
        
        await ctx.send("Setting up a new user profile. To change your default output settings, use `+profile <english/na'vi>`.")
    elif preference == "":
        fh = open(fileName, 'r')
        profile = fh.readline().strip()
        fh.close()
        if profile == "Na'vi":
            embed=discord.Embed(color=0x3154cc, title=user.name, description="Nulnawnewa Lì'fya: **" + profile + "**")
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(color=0x3154cc, title=user.name, description="Language Preference: **" + profile + "**")
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
    elif preference == "na'vi":
        fh = open(fileName, 'w')
        fh.write(preference.capitalize() + "\n")
        fh.close()

        await ctx.send("Nulnawnewa lì'fya set lu " + preference.capitalize() + ".")
        
    elif preference == "english":
        fh = open(fileName, 'w')
        fh.write(preference.capitalize() + "\n")
        fh.write(user.name)
        fh.close()

        await ctx.send("Language preference updated to " + preference.capitalize() + ".")
        
    elif preference == "show":
        fh = open(fileName, 'r')
        profile = fh.readline().strip()
        fh.close()

        embed=discord.Embed(color=0x3154cc, title=user.name, description="Language Preference: **" + profile + "**")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid criteria entered. Please select `English` or `Na'vi`, or use `show` to view your current settings.")

# Error Handling for !profile
@profile.error
async def profile_error(ctx, error):
    if isinstance(error, commands.CommandError):
        await ctx.send("Invalid syntax. If you need help with the `+profile` command, type `+howto`")

# Quit command
@nameGenBot.command(name='stop',aliases=['ftang'])
async def botquit(ctx):
    user = ctx.message.author
    if user.top_role.name == "Olo'eyktan":
        await ctx.send("Herum. Hayalovay!")
        await nameGenBot.close()
        await nameGen.close()
        quit()

# Run Bot    
nameGenBot.run("PRIVATE KEY")
