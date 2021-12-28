
def create_types():
    try:
        with open("demo.txt","r") as file:
            line = file.readline().strip()
            my_list = []
            my_dict = {}
            numbers=line.split(",")
            for i in range(0,len(numbers)):
                if int(numbers[i].isnumeric()):
                    my_list.append(int(numbers[i]))
                    my_dict[i]=int(numbers[i])
                else:
                    raise ValueError
            if len(my_list)==0:
                raise EOFError
            my_tuple=tuple(my_list)
            print (str(my_list))
            print (str(my_dict))
            print (str(my_tuple))
            file.close()
    except (ValueError,EOFError):
        print("Invalid input")

create_types()
