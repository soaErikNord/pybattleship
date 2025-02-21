SHIP_TYPES = ("Carriers", "Battleship", "Cruiser", "Submarine", "Destroyer")

class Ship():
    def __init__(self, length, ship_letter, ship_name):
        self.__length = length
        self.__hits = 0
        self.__ship_name = ship_name
        self.__ship_letter = ship_letter

        
    def hit(self):
        self.__hits += 1
        if self.__hits == self.__length:
            return True
        else:
            return False
        

    def get_hits(self):
        return self.__hits


    def get_length(self):
        return self.__length


    def get_ship_name(self):
        return self.__ship_name
    

    def get_ship_letter(self):
        return self.__ship_letter


    def set_hits(self, hits):
        self.__hits = hits


    def set_length(self, length):
        self.__length = length


    def set_ship_name(self, ship_name):
        self.__ship_name = ship_name   


    def set_ship_letter(self, ship_letter):
        self.__ship_letter = ship_letter             
        

class Carrier(Ship):
    def __init__(self):
        super().__init__(5, 'C', 'Carrier')


class Battleship(Ship):
    def __init__(self):
        super().__init__(4, 'B', 'Battleship')


class Cruiser(Ship):
    def __init__(self):
        super().__init__(3, 'R', 'Cruiser')


class Submarine(Ship):
    def __init__(self):
        super().__init__(3, 'S', 'Submarine')


class Destroyer(Ship):
    def __init__(self):
        super().__init__(2, 'D', 'Destroyer') 



class Board():  
    def __init__(self):
        self.board = [['O' for i in range(10)] for j in range(10)]
        self.ships = []
        
    def get_ship_locations(self, ships):
        for ship in ships:
            print(f"Enter the location of {ship.get_ship_name()}")
            x = -1
            y = -1
            while x < 0 or x > 10:
                x = int(input("Enter the x coordinate, between 0 - 10: "))
            while y < 0 or y > 10:
                y = int(input("Enter the y coordinate, between 0 - 10: "))
            horizontal = input("Is the ship horizontal? (y/n) ")
            if horizontal == 'y':
                horizontal = True
            else:
                horizontal = False
            self.add_ship(ship, x, y, horizontal)

    def add_ship(self, ship, x, y, horizontal):
        if horizontal:
            for i in range(ship.get_length()):
                self.board[y][x+i] = ship.get_ship_letter()
        else:
            for i in range(ship.get_length()):
                self.board[y+i][x] = ship.get_ship_letter()
        self.ships.append(ship)
        # print()
        
    def shoot(self, x, y):
        if self.board[y][x] != 'O':
            
            for ship in self.ships:  
                if ship.get_ship_letter() == self.board[y][x] and ship.hit():
                    if ship.get_hits() == ship.get_length():
                        print(f'{ship.get_ship_name()} has been sunk!')
                    
                    if not self.__check_board():
                        print('You have sunk all the ships!')
                        exit()
                    
                    self.board[y][x] = 'X'
                    return True
                    
            self.board[y][x] = 'X'
            return False
        else:
            self.board[y][x] = 'M'
            return False

    def __check_board(self):
        __ship_exists = False
        for row in self.board:
            for cell in row:
                for ship in self.ships:
                    if cell == ship.get_ship_letter():
                        __ship_exists = True
                        break
                
        return __ship_exists 
    
    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.board])      


def main(): 
    board = Board()
    
    ships = []
    carrier = Carrier()
    ships.append(carrier)
    battleship = Battleship()
    ships.append(battleship)
    cruiser = Cruiser()
    ships.append(cruiser)
    submarine = Submarine()
    ships.append(submarine)
    destroyer = Destroyer()
    ships.append(destroyer)

    board.get_ship_locations(ships)

    # board.add_ship(carrier, 0, 0, True)
    # board.add_ship(battleship, 1, 0, True)
    # board.add_ship(cruiser, 2, 0, True)
    # board.add_ship(submarine, 3, 0, True)
    # board.add_ship(destroyer, 4, 0, True)

    print(f'')
    print(board)
    print(board.shoot(0, 0))
    print(board.shoot(1, 1))
    print(board.shoot(2, 1))
    print(board.shoot(3, 3))
    print(board.shoot(4, 4))
    print(board.shoot(5, 5))
    print(board.shoot(6, 6))
    print(board.shoot(7, 7))
    print(board.shoot(8, 8))
    print(board.shoot(9, 9))
    print(board)

    print(board.shoot(2, 3))
    print(board.shoot(3, 3))
    print(board.shoot(4, 3))
    print(board.shoot(5, 3))
    print(board)


if __name__ == '__main__':
    main()      