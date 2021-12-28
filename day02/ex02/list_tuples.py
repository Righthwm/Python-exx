def gen_tuples(start, end):
    tuples_list = list((x,y) for x in range(y,0,-1) for y in range (start,end+1))
    return(tuples_list)