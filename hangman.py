import requests
from bs4 import BeautifulSoup
import random

def crawl_words(url):
    # 주어진 URL에서 단어 크롤링
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    words = []

    # <tr>에서
    trs = soup.find_all('tr')
    for tr in trs:
        # width='120'인 <td> 요소를 찾기
        td_tags = tr.find_all('td', width='120')
        for td in td_tags:
            # <a> 태그를 찾고 텍스트 추출
            a_tags = td.find_all('a')
            for a in a_tags:
                word = a.text.strip()
                words.append(word)

    return words

def play_game():
    answer_word = random.choice(words)
    selected_letters = set()
    attempt = 1

    while attempt <= 10:    #기회 10번
        print()
        for letter in answer_word:
            if letter in selected_letters:
                print(letter, end=" ")  # 이미 선택된 글자인 경우 해당 글자 출력
            else:
                print("_", end=" ")  # 선택되지 않은 글자인 경우 밑줄 출력

        if set(answer_word) == selected_letters:
            print("\n성공")  # 모든 글자를 맞춘 경우 게임 성공
            break

        guess = input("\n알파벳 한글자나 정답단어를 입력하세요 > ")
        if len(guess) == 1:
            selected_letters.add(guess)  # 한 글자를 선택한 경우 글자를 추가
            if guess not in answer_word:
                print("실패")  # 선택한 글자가 정답 단어에 없으면 실패 메시지 출력
        else:
            if guess == answer_word:
                print("모두 술을 안마셔도 됩니다!!")  # 전체 단어를 맞춘 경우 게임 성공
                return True
            else:
                print("실패")  # 전체 단어를 맞추지 못한 경우 실패 메시지 출력
        attempt += 1

    if attempt > 10:
        print("\n행맨 게임에서 패배하셨습니다.")
        print("정답은", answer_word, "입니다.")
        return False
        
    
    
url = 'https://ko.talkenglish.com/vocabulary/top-1500-nouns.aspx'
words = crawl_words(url)

#hangman_game(words, max_attempts=10)
