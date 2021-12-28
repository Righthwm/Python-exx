def main():
    list = []
    interval=input()
    nr_list = interval.split()
    try:
        if len(nr_list) == 0:
            raise EOFError("No input provided")
        elif len(nr_list) != 2:
            raise TypeError("Inccorect type")
        else: 
            a = nr_list[0]
            b = nr_list[1]
            if a.isnumeric() == False or b.isnumeric() == False :
                raise TypeError("Inccorect type")
            elif a > b:
                raise ValueError ("Invalid interval")
            else:
                for i in range (int(a), int(b)+1):
                    list.append(i)
                print(*list, sep=' ')
    except(TypeError, EOFError, ValueError) as err:
        print(err)

main()