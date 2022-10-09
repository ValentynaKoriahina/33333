import os
import random


desk = ['_', 1, 2, 3, 4, 5, 6, 7, 8, 9]
rest_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_seq = []

def determ_winning_sequences(desk):
    """Обрабатывает выигрышные последовательности"""

    global win_seq

    win_seq = [desk[1:4],
               desk[4:7],
               desk[7:],
               desk[1:8:3],
               desk[2:9:3],
               desk[3::3],
               desk[1::4],
               desk[3:8:2],
               ]


def create_desk(val):
    """Формирует игровое визуальное поле"""

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[1], val[2], val[3]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[4], val[5], val[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[7], val[8], val[9]))
    print("\t     |     |")
    print("\n")


def pc_mined():
    """Моделирует ходы ПК"""

    # Глубина анализа: пока ПК может только предотвратить проигрыш, завершить существующую
    # выигрышную последовательность и выполнить рандомный ход'''

    global win_seq
    global desk
    global rest_moves
    move_pc = 0
    move_selected = False

    determ_winning_sequences(desk)

    while rest_moves:

        '''Может выиграть'''
        for i in win_seq:
            if i.count('O') == 2 and 'X' not in i:
                for field in i:
                    if str(field).isnumeric():
                        move_pc = field
                        desk[move_pc] = 'O'
                        move_selected = True
                        break
            if move_selected:
                break

        if move_selected:
            break

        '''Предотвратить проигрыш'''
        for i in win_seq:
            if i.count('X') == 2 and 'O' not in i:
                for field in i:
                    if str(field).isnumeric():
                        move_pc = field
                        desk[move_pc] = 'O'
                        move_selected = True
                        break

            if move_selected:
                break

        if move_selected:
            break

        '''Просто ход'''
        move_pc = random.choice(rest_moves)  # Симулятор ходов ПК
        desk[move_pc] = 'O'
        move_selected = True

        if move_selected:
            break

    return move_pc


def start_game(whose_move):
    """Запускает игру"""
    global rest_moves
    global desk
    global win_seq
    desk = ['_', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rest_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_seq = []

    if whose_move == 'player':
        while rest_moves:
            create_desk(desk)

            try:
                move_pl = int(input('Твой ход. Введи поле: '))

                if move_pl in rest_moves:
                    desk[move_pl] = 'X'
                    rest_moves.remove(move_pl)

                    determ_winning_sequences(desk)
                    if ['X', 'X', 'X'] in win_seq or ['O', 'O', 'O'] in win_seq:
                        os.system("clear")  # Очищает консоль от предыдущих ходов
                        break

                    move_pc = pc_mined()  # Симулятор ходов ПК
                    if move_pc != 0:
                        desk[move_pc] = 'O'
                        rest_moves.remove(move_pc)

                    os.system("clear")  # Очищает консоль от предыдущих ходов

                    ''' Провермяем не порa ли заканчивать игру '''
                    determ_winning_sequences(desk)
                    if ['X', 'X', 'X'] in win_seq or ['O', 'O', 'O'] in win_seq:
                        break

                else:
                    if move_pl == 0:
                        os.system("clear")  # Очищает консоль от предыдущих ходов
                        print('0 - это ход твоего соперника, выбери номер свободного поля')
                    else:
                        os.system("clear")  # Очищает консоль от предыдущих ходов
                        print('Это поле уже сыграло, выбери другое...')

            except ValueError:
                os.system("clear")  # Очищает консоль от предыдущих ходов
                print('Ты ввел что-то не то, нужно ввести цифру')

        create_desk(desk)


    else:

        print('Теперь первым ходит компьютер')

        while rest_moves:

            move_pc = pc_mined()  # Симулятор ходов ПК
            if move_pc != 0:
                desk[move_pc] = 'O'
                rest_moves.remove(move_pc)
                create_desk(desk)

            ''' Провермяем не порa ли заканчивать игру '''
            determ_winning_sequences(desk)
            if ['X', 'X', 'X'] in win_seq or ['O', 'O', 'O'] in win_seq:
                os.system("clear")  # Очищает консоль от предыдущих ходов
                break

            if rest_moves:
                move_pl = int(input('Введи поле: '))
                os.system("clear")  # Очищает консоль от предыдущих ходов

                if move_pl in rest_moves:
                    desk[move_pl] = 'X'
                    rest_moves.remove(move_pl)
                    create_desk(desk)
                    os.system("clear")  # Очищает консоль от предыдущих ходов

            ''' Провермяем не порa ли заканчивать игру '''

            determ_winning_sequences(desk)
            if ['X', 'X', 'X'] in win_seq or ['O', 'O', 'O'] in win_seq:
                os.system("clear")  # Очищает консоль от предыдущих ходов
                break

        create_desk(desk)


def have_winner():
    """Определяет есть ли победитель"""
    determ_winning_sequences(desk)

    if ['X', 'X', 'X'] in win_seq and ['O', 'O', 'O'] not in win_seq:
        print('Поздравляем, ты выиграл!')
    elif ['O', 'O', 'O'] in win_seq and ['X', 'X', 'X'] not in win_seq:
        print('Жаль, но ты прогирал.')
    elif ['O', 'O', 'O'] in win_seq and ['X', 'X', 'X'] in win_seq:
        print('Победила дружба:)')
    else:
        print('Ни кто не выиграл;-)')  # доработать другие варианты исхода игры


if __name__ == "__main__":
    first_choice_made = False
    whose_move = ''
    round = 1

    print('Привет. Выбери 1 для начала игры или 2 для выхода.')

    while not first_choice_made:
        start_or_exit = input()
        os.system("clear")  # Очищает консоль от предыдущих ходов

        if start_or_exit == '1':
            first_choice_made = True
            while start_or_exit != '2':
                if round % 2 != 0:
                    start_game("player")
                    have_winner()
                    round += 1
                else:
                    start_game("computer")
                    have_winner()
                    round += 1

                print('Хочешь сыграть еще? ДА - 1, НЕТ - 2')
                start_or_exit = input()
                os.system("clear")  # Очищает консоль от предыдущих ходов

            print('Спасибо за игру, до новых встреч!')

        elif start_or_exit == '2':
            print('До новых встреч!')
            first_choice_made = True

        else:
            print('Ты ввел что-то не то, выбери цифру')
