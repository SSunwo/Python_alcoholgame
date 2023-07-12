def print_game_list(game_lists):
    print("다음은 게임 리스트입니다:")
    for index, game in enumerate(game_lists, start=1):
        print(f"{index}. {game}")



def game_selection(game_lists):
    print_game_list(game_lists)

    while True:
        selection = input("게임 번호를 선택하세요: ")
        
        try:
            selection = int(selection)
            if 1 <= selection <= len(game_lists):
                selected_game = game_lists[selection - 1]
                print(f"{selected_game}을 선택하셨습니다. 게임을 실행합니다.")
                # 선택한 게임 실행하는 코드 여기에 쓰기
                break 
            else:
                print("유효한 게임 번호를 입력하세요.")
        except ValueError:
            print("유효한 게임 번호를 입력하세요.")

# 게임 리스트
game_lists = ["행맨", "지하철게임", "버스커게임", "더게임오브데스"]

# 게임 선택
game_selection(game_lists)
