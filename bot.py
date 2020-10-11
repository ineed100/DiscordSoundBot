import discord
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix=".")
client = discord.Client()
TOKEN = "Token here"


@bot.event
async def on_ready():
    print("BOT IS READY.....")

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.guild)
async def pig(ctx):
    ": ### will personally tell ### that he is a pig"
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients,guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(discord.FFmpegPCMAudio(
        executable="C:/Users/###\PycharmProjects\###/ffmpeg-20200413-59e3a9a-win64-static/bin/ffmpeg.exe",
        source="PigCommand.mp3"))

    while voice.is_playing():
        print("PLAYING...")
    print("DONE PLAYING")
    await voice.disconnect()

@pig.error
async def pig_error(ctx, error):
    if isinstance(error,commands.CommandOnCooldown):
        msg = 'This command pig is on cooldown try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error


@bot.command()
@commands.cooldown(1, 25, commands.BucketType.guild)
async def ping(ctx, target: discord.Member):
    ": Pings a user of your choice"
    n = 0
    while n < 5:
        await ctx.send(target.mention + ' GET ON')
        n += 1

@ping.error
async def ping_error(ctx, error):
    if isinstance(error,commands.CommandOnCooldown):
        msg = 'This command is on cooldown try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    elif isinstance(error,commands.BadArgument):
        await ctx.send("User doesn't exist.")
    else:
        raise error

@bot.event
async def on_typing(channel, user, when):
    """
    This event is called when someone in an accessible channel begins
    typing.
    Args:
        channel:
            The Channel object of where the typing originated from.
        user:
            The User object that started typing.
        when:
            A :class:`datetime.datetime` object of when the user started typing.
    """
    if user.id == 92758776385388544:
        print(user,"started to type in",channel,"on",when)
        await channel.send("MESSAGE!", tts= True)
    print("It is not ### typing")

@bot.event
async def on_voice_state_update(member, before, after):
    """
    This event is called when a member changed their voice state.
    This can be:
     * A member joins a voice channel.
     * A member leaves a voice channel.
     * A member becomes muted or deafened a voice channel.
    Args:
        member:
            A Member object whose voice states changed.
        before:
            The original VoiceState object before getting changed.
        after:
            The new VoiceState object after getting changed.
    """
    # this checks if ### muted himself
    if member.id == 92758776385388544 and (before.self_mute is False and after.self_mute is True):
        channel = bot.get_channel(92755352495349760) # Will send message in general
        await channel.send("### muted himself", tts= True)
    # this checks if ### muted himself
    if member.id == 102277299625275392 and (before.self_mute is False and after.self_mute is True):
        channel = bot.get_channel(92755352495349760) # Will send message in general
        await channel.send("### muted himself", tts= True)
    # this checks if ### muted himself
    if member.id == 92754531464527872 and (before.self_mute is False and after.self_mute is True):
        channel = bot.get_channel(92755352495349760) # Will send message in general
        await channel.send("### muted himself", tts= True)



bot.run(TOKEN)
