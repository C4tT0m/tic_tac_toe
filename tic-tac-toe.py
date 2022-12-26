import time
def slow_text(s):
    for i in range(len(s)):
        print(s[i], end="", flush=True)
        time.sleep(0.01)
slow_text("""╭━━━╮
┃▉┊▉┃
┃┊┊┊╰━╮
┃╰━━┳━╯
┃╭━━╯           -Приветствую вас, дорогие игроки!
┃┃╭━━╮          -Меня зовут - питон Чарли.
┃┃┃╭╮┃          -Вы запустили увлекательную игру крестики-нолики.
┃╰┫┣┻┻━╮        -Игра рассчитана на двоих игроков.
╰━┫┣┳┳╮┃            Игрок вводит координаты ячейки: 'X Y',
╭━┻┻┫┣╯┃                где 'X' - номер строки,
┃╭┳┳┫┣━╯                а 'Y' - номер столбца.
┃╰┫┣┻┻━╮     
╰━┫┣┳┳╮┃        -Первый ход делают крестики 'x'.
╭━┻┻┫┣╯┃        -Далее продолжают нолики 'o'.
┃╭┳┳┫┣━╯        
┃╰╯┃┃╰┓
╰━━╯╰━╯""")

gamer_name1 = input('\n Введите имя первого игрока: ')
gamer_name2 = input('\n Введите имя второго игрока: ')
slow_text('Делай первый ход '+gamer_name1+'\n')

field = [['-'] * 3 for i in range(3)]
def draw_field(board):
    print('  0 1 2')
    n = 0
    for row in board:
        print(f'{n} {row[0]} {row[1]} {row[2]}')
        n += 1

def input_coord(arg):
    value = False
    while not value:
        try:
            x, y = list(map(int, input(f"Ход игрока - '{arg}'. Введите координаты хода через пробел: ").split()))
        except:
            print('Некорректный ввод. Введите две координаты через пробел!')
            continue
        if not (x < 0 or y < 0 or x > 2 or y > 2):
            if not(field[x][y] != '-'):
                value = True
            else:
                print('Клетка занята!')
        else:
            print('Координаты должны иметь значения от 0 до 2')
    return x, y

def main(board):
    count = 0
    while True:
        draw_field(board)
        if count% 2 == 0:
            x, y = input_coord('x')
            board[x][y] = 'x'
        else:
            x, y = input_coord('o')
            board[x][y] = 'o'
        count += 1
        if count > 4:
            maybe_win = check_win()
            if maybe_win:
                draw_field(board)
                if maybe_win == 'x':
                    print("Крестики победили!"
                                     "\n Поздравляем "+gamer_name1+'!!!')
                else:
                    print("Нолики победили!"
                                     "\n Поздравляем " + gamer_name2 + '!!!')
                break
            if count == 9:
                draw_field(board)
                print("Увы. Ничья!")
                break

def check_win():
    win_coord = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for coord in win_coord:
        a, b, c = coord[0], coord[1], coord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != '-':
            return field[c[0]][c[1]]
    return False


main(field)