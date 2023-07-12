import random
import time

print("신이 난다~")
time.sleep(1)
print("앗싸 재미난다~")
print("더 게임 오브 뎃!쓰!!!")

def play_game(players):
    M = int(input("임의의 양의 정수 M을 입력하세요: "))  # M 입력 받기
    N = len(players)  # 전체 인원 수
    current = random.randint(0, N - 1)  # 시작할 사람 랜덤 선택
    selected = players[current]  # 시작 시 선택한 사람
    print("시작하는 사람:", selected)
    
    for i in range(1, M + 1):
        print(f"{players[current].name}이(가) {i}번째로 {players[(current + 1) % N].name}을(를) 지목합니다.")
        time.sleep(2)
        current = (current + 1) % N  # 다음 사람으로 이동
    
    return players[current] #loser

