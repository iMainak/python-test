a =  [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]

return_list = []
def return_data(_list= None):
    for i in _list:
        if isinstance(i,list):
            return_data(i)
        else:
            return_list.append(i)
    return return_list

print(return_data(a))