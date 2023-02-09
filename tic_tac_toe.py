print('''
    +=====================================+   
    |             Привет!!!               |
    |      это игра крестики-нолики       |
    +=====================================+ 
    |           Правила игры:             |
    |  для хода введите координаты -      |
    |  две цифры через пробел, где        |
    |  первая цифра - строка,             |
    |  вторая цифра - столбец.            |
    +=====================================+ 
       ''')


def rules_of_the_game():
    print("Координаты (две цифры) нужно водить через пробел \n "
          "где первая цифра (от 0 до 2) - строка, \n "
          "вторая цифра (от 0 до 2) - столбец")


game_field = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']
              ]


def draw_game_field():
    print('    | 0 | 1 | 2 |')
    print('-----------------')
    print(f'  0 | {game_field[0][0]} | {game_field[0][1]} | {game_field[0][2]} |')
    print('-----------------')
    print(f'  1 | {game_field[1][0]} | {game_field[1][1]} | {game_field[1][2]} |')
    print('-----------------')
    print(f'  2 | {game_field[2][0]} | {game_field[2][1]} | {game_field[2][2]} |')
    print('-----------------')


def entry_and_verification_data():
    while True:
        coordinates = input('введите координаты поля: ').replace(' ', '')
        if len(coordinates) != 2:
            rules_of_the_game()
            continue

        if not coordinates.isdigit():
            rules_of_the_game()
            continue

        x, y = int(coordinates[0]), int(coordinates[1])

        if 0 > x or x > 2 or 0 > y or y > 2:
            rules_of_the_game()
            continue

        if game_field[x][y] != ' ':
            print('Это поле уже занято.')
            continue

        return x, y


def check_winner():
    if any([game_field[0][0] == game_field[0][1] == game_field[0][2] == 'X',
            game_field[1][0] == game_field[1][1] == game_field[1][2] == 'X',
            game_field[2][0] == game_field[2][1] == game_field[2][2] == 'X',
            game_field[0][0] == game_field[1][0] == game_field[2][0] == 'X',
            game_field[0][1] == game_field[1][1] == game_field[2][1] == 'X',
            game_field[0][2] == game_field[1][2] == game_field[2][2] == 'X',
            game_field[0][0] == game_field[1][1] == game_field[2][2] == 'X',
            game_field[0][2] == game_field[1][1] == game_field[2][0] == 'X']):
        print('ВЫИГРАЛИ КРЕСТИКИ!')
        return True
    elif any([game_field[0][0] == game_field[0][1] == game_field[0][2] == '0',
              game_field[1][0] == game_field[1][1] == game_field[1][2] == '0',
              game_field[2][0] == game_field[2][1] == game_field[2][2] == '0',
              game_field[0][0] == game_field[1][0] == game_field[2][0] == '0',
              game_field[0][1] == game_field[1][1] == game_field[2][1] == '0',
              game_field[0][2] == game_field[1][2] == game_field[2][2] == '0',
              game_field[0][0] == game_field[1][1] == game_field[2][2] == '0',
              game_field[0][2] == game_field[1][1] == game_field[2][0] == '0']):
        print('ВЫИГРАЛИ НОЛИКИ!')
        return True


draw_game_field()
move_counter = 0
while move_counter < 9:
    move_counter += 1

    if move_counter % 2 == 1:
        print('ХОДИТ КРЕСТИК')
        x, y = entry_and_verification_data()
        game_field[x][y] = 'X'
    else:
        print('ХОДИТ НОЛИК')
        x, y = entry_and_verification_data()
        game_field[x][y] = '0'
    draw_game_field()

    if check_winner():
        break

    if move_counter == 9:
        print('НИЧЬЯ!')
