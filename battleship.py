SHIP_TYPES = ("Carriers", "Battleship", "Cruiser", "Submarine", "Destroyer")

class Ship():
    def __init__(self, length, ship_letter, ship_name):
        self.__length = length
        self.__hits = 0
        self.__ship_name = ship_name

        
    def hit(self):
        self.__hits += 1
        if self.__hits == self.__length:
            return True
        else:
            return False
        

    def get_hit(self):
        return self.__hits


    def get_length(self):
        return self.__length


    def get_ship_name(self):
        return self.__ship_name


    def set_hits(self, hits):
        self.__hits = hits


    def set_length(self, length):
        self.__length = length


    def set_ship_name(self, ship_name):
        self.__ship_name = ship_name            
        

class Carrier(Ship):
    def __init__(self, ship_letter):
        super().__init__(5, ship_letter)


class Battleship(Ship):
    def __init__(self, ship_letter):
        super().__init__(4, ship_letter)


class Cruiser(Ship):
    def __init__(self, ship_letter):
        super().__init__(3, ship_letter)


class Submarine(Ship):
    def __init__(self, ship_letter):
        super().__init__(3, ship_letter)


class Destroyer(Ship):
    def __init__(self, ship_letter):
        super().__init__(2, ship_letter) 
        self.size = 2



class Board():  
    def __init__(self):
        self.board = [['O' for i in range(10)] for j in range(10)]
        self.ships = []
        
    def get_ship_locations():
        for ship in SHIP_TYPES:
            print(f"Enter the location of {ship}")
            x = int(input("Enter the x coordinate: "))
            y = int(input("Enter the y coordinate: "))
            horizontal = input("Is the ship horizontal? (y/n) ")
            if horizontal == 'y':
                horizontal = True
            else:
                horizontal = False
            self.add_ship(ship, x, y, horizontal)

    def add_ship(self, ship, x, y, horizontal):
        if horizontal:
            for i in range(ship.length):
                self.board[y][x+i] = ship.ship_letter
        else:
            for i in range(ship.length):
                self.board[y+i][x] = ship.ship_letter
        self.ships.append(ship)
        
    def shoot(self, x, y):
        if self.board[y][x] == 'S':
            self.board[y][x] = 'X'
            for ship in self.ships:
                if ship.hit():
                    return True
            return False
        else:
            self.board[y][x] = 'M'
            return False

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.board])      


def main(): 
    board = Board()
    carrier = Carrier()
    battleship = Battleship()
    cruiser = Cruiser()
    submarine = Submarine()
    destroyer = Destroyer()

    board.get_ship_locations()

    # board.add_ship(carrier, 0, 0, True)
    # board.add_ship(battleship, 1, 0, True)
    # board.add_ship(cruiser, 2, 0, True)
    # board.add_ship(submarine, 3, 0, True)
    # board.add_ship(destroyer, 4, 0, True)

    print(board)
    print(board.shoot(0, 0))
    print(board.shoot(1, 0))
    print(board.shoot(2, 0))
    print(board.shoot(3, 0))
    print(board.shoot(4, 0))
    print(board.shoot(5, 0))
    print(board.shoot(6, 0))
    print(board.shoot(7, 0))
    print(board.shoot(8, 0))
    print(board.shoot(9, 0))
    print(board)


if __name__ == '__main__':
    main()      