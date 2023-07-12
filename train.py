import random
import requests
from bs4 import BeautifulSoup

cookies = {
    'NNB': '3R42ACHBPOPWI',
    'csrf_token': '720f187576211c20f3b9d28a5bcdbfb52c95aab2efa277946ff43a0f2ff2ae8fbb7cffbe9ba811c7328e58d23f7b816bac152e72f157095f701c56695d896a3b',
    'page_uid': 'da03243a-455b-4ec2-a14a-5a6e010a3a31',
    'nid_inf': '-1179569099',
    'NID_AUT': 'BKWpFt+nvQBEaL0nthFYFK8LzOvtUxblTCI9mzz+HC+6FAvgBln1qHao7mOQLKF1',
    'NID_JKL': '85kebQacOKNKgiqsKumKATpu9291gSPEyfgz4aTWvb8=',
    'NID_SES': 'AAABvKsZ34A65oe9F0KeQeUIFo2tjtM0cbQ3yv9ICHUECRY0FckGhAo75yytYwL0GjTwtLiPm+5UgK8CW5LRrkuPH3XlhRoFeAPcTBM1OObHgjRsm+UU36Ds7kSGWYifBEgCp8NpFb7QW6TQANCbMvcZZlG8hiAoLaFz7/OQOZtOB9DJOnLAd7rQPzj5j7iZas2DCsYNJLvyXIY5Mq41LyzTGdoERWur2QzZewLNeI30B7dW3LQcswCB7mDdY2GKtMxwjSubmzrOQ9I2alMgWwz/6sel/jgf2CeEgoblseHjGufQqM1ENCQcCI5fnNShcqk0ZvIztoCXIWg/efvhkwvDZNM3P1uTiVNv8CjoMuCcphizMz/IldmfLGOBMLiFUL0eSHiFCtnzZtpUime5Pr+Twj4DWPAPc5ANuie9YN53XOHWEefr/X+ppzl9oXSbiVfzEheZBxIpLhNmReDjUwcYk6gxHlkMyea0LqNa6ITkiU3akEm8JfJVO5muww2lt4NQ6p3Bh6AGhN09YVJiCxsMdfEi0cs+kmpEW/tUgJmPBpN2Dc4GtWyvnHiiaZ5BmE1/tlz7XwJQJ32LCarXq4H4UPQ=',
}

headers = {
    'authority': 'map.naver.com',
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'NNB=3R42ACHBPOPWI; csrf_token=720f187576211c20f3b9d28a5bcdbfb52c95aab2efa277946ff43a0f2ff2ae8fbb7cffbe9ba811c7328e58d23f7b816bac152e72f157095f701c56695d896a3b; page_uid=da03243a-455b-4ec2-a14a-5a6e010a3a31; nid_inf=-1179569099; NID_AUT=BKWpFt+nvQBEaL0nthFYFK8LzOvtUxblTCI9mzz+HC+6FAvgBln1qHao7mOQLKF1; NID_JKL=85kebQacOKNKgiqsKumKATpu9291gSPEyfgz4aTWvb8=; NID_SES=AAABvKsZ34A65oe9F0KeQeUIFo2tjtM0cbQ3yv9ICHUECRY0FckGhAo75yytYwL0GjTwtLiPm+5UgK8CW5LRrkuPH3XlhRoFeAPcTBM1OObHgjRsm+UU36Ds7kSGWYifBEgCp8NpFb7QW6TQANCbMvcZZlG8hiAoLaFz7/OQOZtOB9DJOnLAd7rQPzj5j7iZas2DCsYNJLvyXIY5Mq41LyzTGdoERWur2QzZewLNeI30B7dW3LQcswCB7mDdY2GKtMxwjSubmzrOQ9I2alMgWwz/6sel/jgf2CeEgoblseHjGufQqM1ENCQcCI5fnNShcqk0ZvIztoCXIWg/efvhkwvDZNM3P1uTiVNv8CjoMuCcphizMz/IldmfLGOBMLiFUL0eSHiFCtnzZtpUime5Pr+Twj4DWPAPc5ANuie9YN53XOHWEefr/X+ppzl9oXSbiVfzEheZBxIpLhNmReDjUwcYk6gxHlkMyea0LqNa6ITkiU3akEm8JfJVO5muww2lt4NQ6p3Bh6AGhN09YVJiCxsMdfEi0cs+kmpEW/tUgJmPBpN2Dc4GtWyvnHiiaZ5BmE1/tlz7XwJQJ32LCarXq4H4UPQ=',
    'referer': 'https://map.naver.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'readPath': '1000',
    'version': '6.36',
    'language': 'ko',
    'style': 'normal',
    'requestFile': 'optimize_web.svg',
    'caller': 'NaverMapPcBetaWeb',
}

response = requests.get('https://map.naver.com/v5/api/subway/provide', params=params, cookies=cookies, headers=headers)

#입력된 호선에 따라 네이버지도에서 역 정보 가져오는 함수
def craw(line):
    soup = BeautifulSoup(response.content, 'xml')
    #station_list = [element.get('id')[2:] for element in soup.select(f'#역_{line} > circle')]
    station_list = [element.text for element in soup.select(f'#라벨_{line} > g > text')]
    for idx, station in enumerate(station_list):
        if '\n' in station:
            station_list[idx] = station.replace('\n', '')
    return station_list

#예외 만들기
class EmptyListError(Exception):
    def __init__(self):
        super().__init__('존재하지 않는 지하철 노선이에요!!')


#역이 노선에 있는지 확인하는 함수
def station_check(name, station, station_list, history=list):
    if station in station_list and station not in history:
        #한번 나온건 기록해주기
        history.append(station)
        return 'ok', True
    else:
        return name, False 

#station_list에 함정 넣어주는 함수
def delude(line_choice, station_list):
    #정답 리스트 개수의 30퍼센트 정도를 함정 리스트에서 슬라이싱
    if line_choice == '1호선':
        trap_list = craw('2호선')
    else:
        trap_list = craw('1호선')
    
    count = int(len(station_list)*0.3)  
    deluded_list = station_list + trap_list[:count]
    return deluded_list   
    
#게임 실행하는 함수
def play_game(players=list, user_name=str):
    #사용자가 몇 호선 할지 입력 및 세팅
    while True:
        try:
            line_choice = input('몇 호선~! 몇 호선~!: ')
            station_list = craw(line_choice)    #정답 리스트
            if not station_list:
                raise EmptyListError
            break
        except Exception as e:
            print(e, '다시 골라주세요~')
        
    deluded_list = delude(line_choice, station_list)    #함정 리스트
    history = []
    turn = 0

    #게임 진행    
    Flag = True
    while Flag:
        turn += 1
        print(f'-------------------turn {turn}---------------------')
        for player in players:
            if player.name == user_name:    #사용자의 경우 직접 역 이름 입력
                station = input(f'{user_name}: ')
            else: #컴퓨터의 경우 역 노선에서 랜덤으로 선택
                station = random.choice(deluded_list)
                print(f'{player.name}: {station}')

            loser, Flag = station_check(player, station, station_list, history) #station_check는 정답리스트를 가지고 체크
            if not Flag:
                break

    return loser
