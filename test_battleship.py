from battleship import Board, Carrier, Battleship, Cruiser, Submarine, Destroyer

class test_battleship():
    def __init__(self):
        self.board = Board()


    def test_game(self):
        board = Board()
    
        ships = []
        carrier = Carrier()
        ships.append(carrier)
        board.add_ship(carrier, 1, 2, 'y')

        battleship = Battleship()
        ships.append(battleship)
        board.add_ship(battleship, 2, 3, 'y')

        cruiser = Cruiser()
        ships.append(cruiser)
        board.add_ship(cruiser, 3, 4, 'y')

        submarine = Submarine()
        ships.append(submarine)
        board.add_ship(submarine, 5, 6, 'y')

        destroyer = Destroyer()
        ships.append(destroyer)
        board.add_ship(destroyer, 7, 8, 'y')
        

        print(f'')
        print(board)

        # Sink the carrier
        print(board.shoot(1, 2))
        print(board.shoot(2, 2))
        print(board.shoot(3, 2))
        print(board.shoot(4, 2))
        print(board.shoot(5, 2))
        print(board.shoot(6, 2))

        # Sink the battleship
        print(board.shoot(2, 3))
        print(board.shoot(3, 3))
        print(board.shoot(4, 3))
        print(board.shoot(5, 3))
        print(board.shoot(6, 3))

        # Sink the cruiser
        print(board.shoot(3, 4))
        print(board.shoot(4, 4))
        print(board.shoot(5, 4))
        print(board.shoot(6, 4))

        # Sink the submarine
        print(board.shoot(5, 6))
        print(board.shoot(6, 6))
        print(board.shoot(7, 6))
        print(board.shoot(8, 6))

        # Sink the destroyer
        print(board.shoot(7, 8))
        print(board.shoot(8, 8))
        print(board.shoot(9, 8))
        print(board)


if __name__ == '__main__':
    test = test_battleship()
    test.test_game()