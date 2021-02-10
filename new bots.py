import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비")
    game = discord.Game("모찌")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async  def on_message(message):
    if message.content.startswith("하이"):
        await message.channel.send("반갑다모찌")
    if message.content.startswith("바이"):
        await message.channel.send("잘가라모찌")
    if message.content.startswith("뭐해"):
        await message.channel.send("답한다모찌")
    if message.content.startswith("모찌야"):
        await message.channel.send("모찌?")
    if message.content.startswith("잘자"):
        await message.channel.send("너두모찌")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("/mute"):
        author = message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("/Unmute"):
        author = message.guild.get_member(int(message.content[8:26]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)





