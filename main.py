#완성된 게임 import
import random
from ascii_art import *
import zan
import train
import busker_game
import hangman

#인트로
draw_line(len(ag1))
paint_intro()
draw_line(len(ag1))


# player class
players=[]
class Player():
    def __init__(self,name,alcohol):
        self.name=name
        self.alcohol=alcohol

#사용자의 이름 받기
player_name = input("본인의 이름을 입력해주세욧:")

#사용자로부터 주량을 선택받는 함수
def drinking_amount():
    select_amount = {
        1: "소주 반 병 (3잔)",
        2: "소주 한 병 (5잔)",
        3: "소주 한 병 이상 두병 미만 (8잔)",
        4: "소주 두 병 (10잔)"
    }

    amount = [3, 5, 8, 10]
    while True:
        print("\n---------------주량을 선택하세요:---------------")
        for key, value in select_amount.items():
            print("%d. %s" % (key, value))
            
        choice = input("번호를 입력하세요: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in select_amount.keys():
                player_aof = amount[choice - 1]
                break
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")
        else:
            print("숫자를 올바르게 입력해주세요.")

    return player_aof

player_aof = drinking_amount()
print("선택한 주량: ", player_aof)

class Player:
    def __init__(self, name, aof):
        self.name = name
        self.aof = aof
        self.current = 0                      	
    
    def __str__(self) -> str:
        return f"{self.name}"

player1 = Player("세원", random.randint(3,13))
player2 = Player("경린", random.randint(3,13))
player3 = Player("서경", random.randint(3,13))
player4 = Player("선우", random.randint(3,13))

game_players = [player1, player2, player3, player4]

players = [Player(player_name, player_aof)]

class game:
    #같이 대결할 사람 초대하기(최대 3명, 예외처리 필수)
    def start_game():
        try:
            while True:
                n_players = int(input("오늘 같이 마실 친구들 n명 불러오기(숫자 3 입력)):"))
                if n_players > 3:
                    print("자리가 좁아서 최대 3명만 부르세요.")
                    continue
                elif n_players < 3:
                    print("술게임하려면 4명은 있어야지!!")
                    continue
                else:
                    break
        except:
            print("숫자를 제대로 입력하세요.")

        random_play_members = random.sample(game_players, 3)
        for player in random_play_members:
            players.append(player)
        
        return players #players = [사용자, 컴퓨터1, 컴퓨터2, 컴퓨터3]


#게임 리스트 출력하기
def print_game_list(game_lists):
    print("다음은 게임 리스트입니다:")
    for index, game in enumerate(game_lists, start=1):
        print(f"{index}. {game}")

def game_selection(game_lists):
    print_game_list(game_lists)

#컴퓨터(상대)의 참여목록, 주량 입력
def left_drink_until_die():
    for player in players:
        left_drink=player.drink-player.current
        print(f"{player.name}은(는) 지금까지 f{player.current}! 치사량까지 f{left_drink}")

def choose_game_random(player):
    end_or_continue=input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 'exit'을, 계속하고 싶으면 아무키나 입력해주세요! :")
    if(end_or_continue=='exit'):
        return
    print(f"{player.name} (이)가 좋아하는 랜덤~게임~ 무슨~게임~ 무슨~게임~? :")
    random_player=players[random.randint(0,len(players))]
    selected_game=random.randint(1,5)

# 게임 리스트
game_lists = ["행맨", "지하철게임", "버스커게임", "더게임오브데스"]

# 게임 선택
def game_result(select):
    if select == 1:
        if not hangman.play_game():
            for player in players:
                player.current += 1

    elif select == 2:
        loser = train.play_game(players, player_name)
        loser.current += 1 
        
    elif select == 3:
        loser = busker_game.play_game(players)
        loser.current += 1

    else:
        loser = zan.play_game(players)
        loser.current += 1


# #컴퓨터(상대)의 참여목록, 주량 입력
def left_drink_until_die():
    
    for player in players:
        left_drink = player.aof-player.current
        print(f"{player.name}은(는) 지금까지 {player.current}잔! 치사량까지 {left_drink}잔 남았습니다!!")

def choose_game_random(player):
    end_or_continue = input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 'exit'을, 계속하고 싶으면 아무키나 입력해주세요! :")
    if end_or_continue == 'exit':
        return False
    print(f"{player.name} (이)가 좋아하는 랜덤~게임~ 무슨~게임~ 무슨~게임~? :")
    selected_game = random.randint(1,5)

    return selected_game

while(True):
    for player in players[1:]:
        choose_game_random(player)
        #if 반복 
        left_drink_until_die()

#주량 출력
print()
print('--------------------------------')
for player in players:
    print(f'{player.name}의 주량은 {player.aof}잔 입니다!!')
print('--------------------------------')
print()

Flag = True
while Flag:
    select = game_selection(game_lists)
    game_result(select)
    print()
    print('--------------------------------------------')
    left_drink_until_die()
    print('--------------------------------------------')
    print()

    
    for player in players[1:]:  #2번째부턴 컴퓨터가 게임 선택
        select = choose_game_random(player)
        if select == False:
            draw_line(len(pt3))
            paint_team3()
            draw_line(len(pt3))
            Flag = False
            break
        
        else:
            game_result(select)
            
            print()
            print('-----------------------------------------------')
            left_drink_until_die()
            print('-----------------------------------------------')
            print()
            
            if not check_alive():
                draw_line(len(pt3))
                paint_team3()
                draw_line(len(pt3))
                Flag = False
                break








