class Circle:
    def __init__(self,curcimsize, color):
        self.curcimsize = curcimsize
        self.color = color
        print('A new object has been created!\n', 'Its color is:', color,'Its curcim is:', curcimsize)


colored = input("What is the color? \n --> ")
cur = input('What is the curcimsize? \n --> ')

goodie = Circle(cur,colored)