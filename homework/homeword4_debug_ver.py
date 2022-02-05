import random
import string

def get_word():
    # สามารถเพิ่มคำใน words ได้
    words = ["HAPPY", "IMAGE", "TOURS", "FLOOD", "BLOCK", 
             "STORE", "AMONG", "TWEET", "OFTEN", "STILL",
             "STYLE", "LIGHT", "MIGHT", "WOULD", "SEVEN"]
    return random.choice(words).upper()

def get_five_letter_word():
    # คืนค่าเป็นคำที่มีความยาว = 5
    print('  Guess a five-letter word >> ', end='')
    guess = input()
    while len(guess) != 5:
        print('  Please enter a five-letter word >> ', end='')
        guess = input()
    return guess.upper()
            
def show_game_status(correct, wrong, not_used):
    correct = color_text(correct, 'green')
    wrong = color_text(wrong, 'yellow')
    print('  Correct letters - [{}]'.format(correct))
    print('  Wrong position - [{}]'.format(wrong))
    print('  Letters not used - [{}]'.format(not_used))

def replace_letter(original, old_letter, new_letter):
    # คืนค่าเป็นสตริงที่เปลี่ยน อักขระใน original จาก old_letter ไปเป็น new_letter
    # original เป็นสตริงที่ไม่มีตัวอักขระซ้ำกันแน่ ๆ
    if old_letter in original:
        k = original.find(old_letter)
        original = original[:k] + new_letter + original[k+1:]
    return original    

def replace_letters(letters, letters_to_remove):
    # เปลี่ยนทุกอักขระใน letters ที่อยู่ใน letters_to_remove ให้เป็น '-'
    for ch in letters_to_remove:
        # เปลี่ยนอักขระ ch ใน letters ให้เป็น '-'
        letters = replace_letter(letters, ch, '-')
    return letters
#-----------------------------------------------------------------------------------------------
def position_in_word(ch, word):
    position = -1
    if word[0] == ch:
        position = 0
    elif word[1] == ch:
        position = 1
    elif word[2] == ch:
        position = 2
    elif word[3] == ch:
        position = 3
    elif word[4] == ch:
        position = 4
    return position

def check_correct_position(puzzle_word, guess_word):
    correct = ''
    new_guess_word = ''
    new_puzzle_word = puzzle_word
    if puzzle_word[0] == guess_word[0]:
        correct += puzzle_word[0]
        new_puzzle_word = replace_kth_letter_in_str(new_puzzle_word,0,'-')
        new_guess_word += '*' #add
    else:        
        correct += '?'
        new_guess_word += guess_word[0] #add
    if puzzle_word[1] == guess_word[1]:
        correct += puzzle_word[1]
        new_puzzle_word = replace_kth_letter_in_str(new_puzzle_word,1,'-')
        new_guess_word += '*' #add
    else:
        correct += '?'
        new_guess_word += guess_word[1] #add
    if puzzle_word[2] == guess_word[2]:
        correct += puzzle_word[2]
        new_puzzle_word = replace_kth_letter_in_str(new_puzzle_word,2,'-')
        new_guess_word += '*' #add
    else:
        correct += '?'
        new_guess_word += guess_word[2] #add
    if puzzle_word[3] == guess_word[3]:
        correct += puzzle_word[3]
        new_puzzle_word = replace_kth_letter_in_str(new_puzzle_word,3,'-')
        new_guess_word += '*' #add
    else:
        correct += '?'
        new_guess_word += guess_word[3] #add
    if puzzle_word[4] == guess_word[4]:
        correct += puzzle_word[4]
        new_puzzle_word = replace_kth_letter_in_str(new_puzzle_word,4,'-')
        new_guess_word += '*' #add
    else:
        correct += '?'
        new_guess_word += guess_word[4] #add
    return correct, new_puzzle_word , new_guess_word

def replace_kth_letter_in_str(original_str, k, ch):
    replace_original = original_str[:k:] + ch + original_str[k+1::]
    return replace_original

def check_wrong_position(puzzle_word, guess_word):
    wrong_position = ''
    if guess_word[0] == puzzle_word[1]:
        wrong_position += guess_word[0]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,1,'-')
    elif guess_word[0] == puzzle_word[2]:
        wrong_position += guess_word[0]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,2,'-')
    elif guess_word[0] == puzzle_word[3]:
        wrong_position += guess_word[0]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,3,'-')
    elif guess_word[0] == puzzle_word[4]:
        wrong_position += guess_word[0]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,4,'-')
    else:
        wrong_position += '*'
    if guess_word[1] == puzzle_word[0]:
        wrong_position += guess_word[1]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,0,'-')
    elif guess_word[1] == puzzle_word[2]:
        wrong_position += guess_word[1]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,2,'-')
    elif guess_word[1] == puzzle_word[3]:
        wrong_position += guess_word[1]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,3,'-')
    elif guess_word[1] == puzzle_word[4]:
        wrong_position += guess_word[1]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,4,'-')
    else:
        wrong_position += '*'
    if guess_word[2] == puzzle_word[0]:
        wrong_position += guess_word[2]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,0,'-')
    elif guess_word[2] == puzzle_word[1]:
        wrong_position += guess_word[2]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,1,'-')
    elif guess_word[2] == puzzle_word[3]:
        wrong_position += guess_word[2]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,3,'-')
    elif guess_word[2] == puzzle_word[4]:
        wrong_position += guess_word[2]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,4,'-')
    else:
        wrong_position += '*'
    if guess_word[3] == puzzle_word[0]:
        wrong_position += guess_word[3]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,0,'-')
    elif guess_word[3] == puzzle_word[1]:
        wrong_position += guess_word[3]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,1,'-')
    elif guess_word[3] == puzzle_word[2]:
        wrong_position += guess_word[3]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,2,'-')
    elif guess_word[3] == puzzle_word[4]:
        wrong_position += guess_word[3]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,4,'-')
    else:
        wrong_position += '*'
    if guess_word[4] == puzzle_word[0]:
        wrong_position += guess_word[4]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,0,'-')
    elif guess_word[4] == puzzle_word[1]:
        wrong_position += guess_word[4]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,1,'-')
    elif guess_word[4] == puzzle_word[2]:
        wrong_position += guess_word[4]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,2,'-')
    elif guess_word[4] == puzzle_word[3]:
        wrong_position += guess_word[4]
        puzzle_word = replace_kth_letter_in_str(puzzle_word,3,'-')
    else:
        wrong_position += '*'
    return wrong_position

def color_text(text, color):
    # สีที่ใช้แสดง ห้ามเปลี่ยน
    white_on_green = '\033[37;42m'
    white_on_yellow = '\033[34;43m'
    normal = '\033[0;0m'
    colored_text = ''
    if text[0] != '?' and text[0] != '*':
        if color == 'green':
            colored_text += white_on_green + text[0] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[0] + normal
    else:
        colored_text += text[0]
    if text[1] != '?' and text[1] != '*':
        if color == 'green':
            colored_text += white_on_green + text[1] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[1] + normal
    else:
        colored_text += text[1]
    if text[2] != '?' and text[2] != '*':
        if color == 'green':
            colored_text += white_on_green + text[2] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[2] + normal
    else:
        colored_text += text[2]
    
    if text[3] != '?' and text[3] != '*':
        if color == 'green':
            colored_text += white_on_green + text[3] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[3] + normal
    else:
        colored_text += text[3]
    if text[4] != '?' and text[4] != '*':
        if color == 'green':
            colored_text += white_on_green + text[4] + normal
        elif color == 'yellow':
            colored_text += white_on_yellow + text[4] + normal
    else:
        colored_text += text[4]
        
    return colored_text

def main():
    # ห้ามแก้ไขหรือเพิ่มเติม code ใน main()
    win = False
    puzzle_word = 'TWEET'#get_word()

    print("Do you want to show the puzzle word? [enter y or n]")
    show_puzzle = (input().upper() == 'Y')
    if show_puzzle:
        print('Puzzle word:', puzzle_word)

    correct_letters = '?????' 
    letters_wrong_position = '*****'
    letters_never_used = string.ascii_uppercase
    show_game_status(correct_letters, letters_wrong_position, letters_never_used)

    MAX_TRIES = 6
    for i in range(MAX_TRIES):
        print('-'*30)
        print('Try #', i+1)
        guess_word = get_five_letter_word()
        
        correct_letters, new_puzzle_word, new_guess_word= check_correct_position(puzzle_word, guess_word) # add
        letters_wrong_position = check_wrong_position(new_puzzle_word, new_guess_word) #change
        letters_never_used = replace_letters(letters_never_used, guess_word)
        
        show_game_status(correct_letters, letters_wrong_position, letters_never_used)
        if guess_word == puzzle_word:
            win = True
            break
        
    if win:
        print('You got it in {}/{}'.format(i+1, MAX_TRIES))
    else:
        print('You cannot solve this puzzle after', MAX_TRIES, 'times.')

main()