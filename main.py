import discord #디스코드모듈로드
import os #걍로드함
import sys# sys모듈로드
import socket#소켓모듈로드
import discord, datetime, os, time



print("모듈로드 부팅중") # 모듈로드메시지

client = discord.Client()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#음 확인해보자!
resuit = sock.connect_ex(('rokserver.kro.kr',19132))#주소세팅!
chhanel = 544547327420137473

@client.event
async def on_ready():
    print('로그인된봇')
    print(client.user.name)
    print(client.user.id)
    print('---------')
    await client.change_presence(game=discord.Game(name="!가현봇 으로 사용할수 있습니다", type=1))



@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님 안내메시지를참고하여 서버를즐겁게 플레이해주시기 바랍니다.'
    channel = member.server.get_channel("544590286089617421")
    await client.send_message(channel, fmt.format(member, member.server))
 
@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("544590327420289029")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_message(message):#메시지로드시작부분
 if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.
 if message.content.startswith('!가현봇 시스템 로그아웃'):
        await client.logout()
 if message.content.startswith('!가현봇 서버'):
    if resuit == 0:
        print ("서버사롸있네")
        await client.send_message(message.channel, "현재 해당기능은비활성화돼었어요!")#전송
    else:
        print ("서버디짐")
        await client.send_message(message.channel, "현재 해당기능은비활성화돼었어요!")#전송

 if message.content.startswith('!가현봇 대한민국서버'):
        await client.send_message(message.channel, "대한민국서버는 BE고 매번최신버전을유지해요! 저를제작한 제작진분들도 하는 갓 서 버 라네요 저도해봤는데 개꿀잼이에요!")#전송


client.run("NTEzMTc3MjE0NzE2NDc3NDQ0.XosOBA.Dh5HzAU5mSGRaraLKpq6EU-8mRw")
