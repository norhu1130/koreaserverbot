import discord
import socket




client = discord.Client()

port = 19132#포트지정
addr = ("rokserver.kro.kr",port)#주소지정

embed = discord.Embed(colour = discord.Colour.blue())

@client.event
async def on_ready():
    print('로그인된봇')

    print(client.user.name)
    print(client.user.id)
    print('---------')


@client.event
async def on_message(message):#메시지로드시작부분
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다. 
    if message.content.startswith('!가현봇 서버'):
     socket.setdefaulttimeout(2)  
     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
      try:
        s.sendto("data".encode(),addr)
        s.recvfrom(1024)
        print("open!")
        embed = discord.Embed(
            title = "서버상태",
            description = "서버가 열려있습니다.\n서버 IP: `rokserver.kro.kr`\n서버 버전: `항상 최신`",
            colour = discord.Colour.green()
        )
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/sZrLwD372CD16C07gLiWYP52-xLDwGvtQ8ww0h5DbmI/https/cdn.discordapp.com/avatars/513177214716477444/2718d5413cb1720d27f727d70dc11043.webp")
        await client.send_message(message.channel, embed=embed)
      except Exception as e:#에러가나고 타임아웃에러라면?
        print(e)
        if str(e) == "timed out":
            print("OPEN")
            embed = discord.Embed(
                title = "서버상태",
                description = "서버가 열려있습니다.\n서버 IP: `rokserver.kro.kr`\n서버 버전: `항상 최신`",
                colour = discord.Colour.green()
            )
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/sZrLwD372CD16C07gLiWYP52-xLDwGvtQ8ww0h5DbmI/https/cdn.discordapp.com/avatars/513177214716477444/2718d5413cb1720d27f727d70dc11043.webp")
            await client.send_message(message.channel, embed=embed)
        else:
            print("닫힘")        
            embed = discord.Embed(
                title = "서버상태",
                description = "서버가 닫혀있습니다.",
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/sZrLwD372CD16C07gLiWYP52-xLDwGvtQ8ww0h5DbmI/https/cdn.discordapp.com/avatars/513177214716477444/2718d5413cb1720d27f727d70dc11043.webp")
            await client.send_message(message.channel, embed=embed)



client.run("NTEzMTc3MjE0NzE2NDc3NDQ0.XpANxw.mEtmUmnAn2Y4g4ug-A_vN0jK_CU")
     