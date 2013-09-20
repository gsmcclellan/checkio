def checkio(data):
    one_dim_list = []
    for item in data:
        if isinstance(item, list):
            for item2 in checkio(item):
            	one_dim_list.append(item2)
        else:
            one_dim_list.append(item)
            
    return one_dim_list

print(checkio([1,[2,2,2],4]))