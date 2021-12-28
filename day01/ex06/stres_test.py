import random, time
def main():
    for i in range(10):
        try:
            number = random.randint(1,10)
            if number >=4 and number <=6:
                raise ValueError
            else:
                print(number)
                time.sleep(1)
        except ValueError:
            print("Invalid value")
            time.sleep(1)
        
if __name__ == "__main__":
    main()