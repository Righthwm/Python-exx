import sys
import datetime
def get_details():
    print ("Python", sys.version)
    timp=datetime.datetime.now()
    print ("Current date and time:", timp.strftime("%d-%m-%Y %H:%M:%S"))
get_details()