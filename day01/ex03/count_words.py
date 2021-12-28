
def count_words():
    try:
        text = input()
        word=text.split()
        count=len(word)
        if count > 0:
            print("Words number:", count)
        else:
            raise EOFError

    except EOFError:   
       print("No input provided") 

count_words()