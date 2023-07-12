import requests
from bs4 import BeautifulSoup as bs
from itertools import cycle
import time
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
hdr={'User-Agent':user_agent}

# setting
song_list={}

# 노래 크롤링하는 함수
def song_crawling(song_list,songId):
    url=f"https://www.melon.com/song/detail.htm?songId={songId}"
    response=requests.get(url,headers=hdr)
    soup=bs(response.text,"html.parser")

    # 제목 크롤링
    raw_title=soup.select("#downloadfrm > div > div > div.entry > div.info > div.song_name")
    raw_title=raw_title[0].text
    raw_title=raw_title.replace('곡명','')
    title=raw_title.strip()
    # print(title)

    # 가사 크롤링
    raw_lyrics=soup.select("#d_video_summary")
    raw_lyrics=str(raw_lyrics)
    raw_lyrics=raw_lyrics.replace('<br/>','\n')
    raw_lyrics=raw_lyrics.replace('</div>]','')
    raw_lyrics=raw_lyrics.replace('[<div class="lyric" id="d_video_summary"><!-- height:auto; 로 변경시, 확장됨 -->','')
    raw_lyrics=raw_lyrics.strip()
    lyrics=raw_lyrics.split('\n')
    # l=len(lyrics)
    # print(lyrics[11:])

    return title,lyrics

# 여수밤바다
songId=3753303
title,lyrics=song_crawling(song_list,songId)
# 2절부터
lyrics=lyrics[11:]
song_list[title]=lyrics

#정말로 사랑한다면
songId=3832101
title,lyrics=song_crawling(song_list,songId)
lyrics=lyrics[26:]
song_list[title]=lyrics

# 그댈 마주하는 건 아직 힘들어
songId=3832098
title,lyrics=song_crawling(song_list,songId)
lyrics=lyrics[17:]
song_list[title]=lyrics


# 세 노래 중 하나 선택
def choose_song(song_list):
        
    print("\n******버스커 버스커의 노래들******")
    print("1. 여수밤바다")
    print("2. 정말로 사랑한다면")
    print("3. 그댈 마주하는 건 아직 힘들어")
    print("***********************************")
        
    while(True):
        try:
            song_num=input("1,2,3 중 하나를 고르세요! : ")
            if(song_num==''):
                raise Exception('값을 입력해주세요.')
            elif(song_num not in ['1','2','3']):
                raise Exception('1부터 3까지의 숫자를 입력하세요.')
            else:
                song_num=int(song_num)
                break
        except Exception as e:
            print(e)
        
    song_title=list(song_list.keys())[song_num-1]
    print(f"\n<{song_title}>를 선택했습니다.\n")
    print("**********노래를 불러주세요!**********\n")
    return song_list[song_title]

    # 선택한 노래 돌아가면서 부름
def play_game(players):

        song=choose_song(song_list)
        time.sleep(1)

        for player,line in zip(cycle(players), song):
            print(f"{player.name} : {line}")
            if("아아" in line or "워워" in line):
                loser = player
                time.sleep(2)
                print("\n잠깐!!")
                print(f"{loser}가 흐어어~~~를 불렀습니다!")
                break
            time.sleep(1)
        return loser


# main
# players=['player1','player2','player3','player4']
# 게임 실행
# game_result=play_game(players)