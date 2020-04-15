import discord #디스코드모듈로드
import os #걍로드함
import sys# sys모듈로드
import socket#소켓모듈로드
import discord, datetime, os, time
import asyncio


print("모듈로드 부팅중") # 모듈로드메시지

client = discord.Client()

port = 19132
addr = ("localhost",port)


chhanel = 544547327420137473

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
 if message.content.startswith('!가현봇 시스템'):
     time.sleep(2.5)
     await client.send_message(message.channel, "Discord API : :white_check_mark: \nDiscord Bot :white_check_mark:") 
 if message.content.startswith('!가현봇 시스템 LOOOOGOUT'):
        await client.logout()

     

 if message.content.startswith('!가현봇 대한민국서버'):
        await client.send_message(message.channel, "대한민국 서버는 BE고 매번 최신 버전을 유지해요! 저를 제작한 제작진분들도 하는 갓 서버라네요 저도 해봤는데 재미있어요")#전송


client.run("소듕한토큰!")
