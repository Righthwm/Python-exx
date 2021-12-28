def mix_lists(list1, list2, list3, list4):
    myDict = {str(a):{x:y for (x,y) in zip(["key2","key3","key4"],[list2[list1.index(a)],list3[list1.index(a)],list4[list1.index(a)]]) } for a in list1}
    return(myDict)

