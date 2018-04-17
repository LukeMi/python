class tClass():
    def __init__(self, orig=0):
        self.storedValue = orig

    def read(self):
        return self.storedValue

    def write(self, x):
        self.storedValue = x


def Test():
    a = tClass()
    print
    "a: " + str(a.read())
    a.write(10)
    print
    "a: " + str(a.read())

    b = tClass(100)
    print
    "b: " + str(b.read())


if __name__ == '__main__':
    Test()


    def myolution():
        numbers = [int(input('Enter a value: ')) for i in range(10)]
        odds = [y for y in numbers if y % 2 != 0]
        if odds:
            return max(odds)
        else:
            return 'All even'


    print(" ------------------ hello world ------------------")
    # print(myolution())

    print( 9//2)
    print( 9**2 )
    a =1
    print(a)
