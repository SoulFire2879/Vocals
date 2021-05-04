import discord
from collections import defaultdict
import re
import urllib.request

from keep_alive import keep_alive
keep_alive()
from discord.ext import commands
import youtube_dl
import os
import asyncio
import nacl
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)
bot.remove_command('help')





@bot.event
async def on_ready():
	activity = discord.Game(name="lel", type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)
	print('We have logged in as {0.user}'.format(bot))


new = defaultdict(list)

@bot.command()
async def add(ctx, *, name = ' '):
  bruh = new[ctx.guild.id].append(name)
  print (dict(new))

  ydl_opts = {
        
  'format': 'bestaudio/best',
  'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostderr': False,
  'quiet': True,
  'no_warnings': True,
  'default_search': 'auto',
   }
    
    

    
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    result = ydl.extract_info(name, download=False)
        
    audio = result['entries'][0]['url']
    title = result['entries'][0]['title'] 
    new_title = title.replace(' ', '')

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_title)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = ("https://www.youtube.com/watch?v=" + video_ids[0])
    embed = discord.Embed(title = 'Song added to queue', description = f'Added [{title}]({link})  to queue ', color = discord.Color.green())



def play_next(ctx):
  
  data = dict(new).get(next(iter(dict(new))))
  lel = new[ctx.guild.id]
  
  if len(lel) == 0:
    
    print('helo')
    return

  else:
    
   
    lel = new[ctx.guild.id]
    song = lel[0]
   
    print(song)
    
    
    voice = ctx.guild.voice_client
    
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    ydl_opts = {
        
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    }
    
    

    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(song, download=False)
        
        audio = result['entries'][0]['url']
        title = result['entries'][0]['title'] 
        new_title = title.replace(' ', '')

        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_title)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = ("https://www.youtube.com/watch?v=" + video_ids[0])
        embed = discord.Embed(title = 'Song added to queue', description = f'Now Playing [{title}]({link})  ', color = discord.Color.green())
        voice.play(discord.FFmpegPCMAudio( result['entries'][0]['url']))
        del lel[0]
        
        
        
    
    


def skip(ctx):
  
  lel = new[ctx.guild.id]
  
  if len(lel) == 0:
    
    print('helo')
    return

  else:
    
  
    lel = new[ctx.guild.id]
    song = lel[0]
   
    
   
    
    
    voice = ctx.guild.voice_client
    voice.stop()
    
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    ydl_opts = {
        
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    }
    
    

    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(song, download=False)
        del lel[0]
       
        
        audio = result['entries'][0]['url']
        title = result['entries'][0]['title'] 
        new_title = title.replace(' ', '')

        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_title)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        link = ("https://www.youtube.com/watch?v=" + video_ids[0])
        embed = discord.Embed(title = 'Song added to queue', description = f'Now Playing [{title}]({link})  ', color = discord.Color.green())
        voice.play(discord.FFmpegPCMAudio(audio,options = FFMPEG_OPTS), after=lambda e: play_next(ctx))
        
        



@bot.command()
async def next(ctx):
   skip(ctx)
 


@bot.command() 
async def play(ctx, *, url = '' ):
    
  
    voice = ctx.guild.voice_client

    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    ydl_opts = {
        
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    }
    
    
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        
        audio = result['entries'][0]['url']
        title = result['entries'][0]['title']
        if ' ' in title:

          new_title = title.replace(' ', '')

        else:

           new_title = title.replace(' ', '')

           html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_title)
           video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
           link = ("https://www.youtube.com/watch?v=" + video_ids[0])

           voice.play(discord.FFmpegPCMAudio(audio,options = FFMPEG_OPTS), after=lambda e: play_next(ctx))
        
           embed = discord.Embed(title = 'Song playing',      description = f'Now playing [{title}]({link})')
           await ctx.send(embed = embed)

        
@bot.command()
async def join(ctx):
  
  
  voice_state = ctx.author.voice
  if voice_state is  None:
    await ctx.send('You have to be in a voice channel to use that command')
  
  else:
    channel = ctx.author.voice.channel
    await channel.connect()
  






@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        message = ctx.message
        await message.add_reaction('⏸️')
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        message = ctx.message
        await message.add_reaction('✅')
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

@bot.command()
async def leave(ctx):
    voice = ctx.guild.voice_client
    if  voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")



bot.run(os.getenv('token'))