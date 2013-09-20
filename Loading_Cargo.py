def checkio(data):
    data = sorted(data)
    x = []
    y = []
    
    for item in data:
        if sum(x) > sum(y):
            y.append(item)
        else:
            x.append(item)
     
    check = True
    while check:
        check = swap(x, y)
        if check:
            swapx, swapy = swap(x, y)
            x.append(swapy)
            y.append(swapx)
            x.remove(swapx)
            y.remove(swapy)

    for item in x:
        if abs(sum(x) - sum(y)) > abs((sum(x) - item) - (sum(y) + item)):
            y.append(item)
            x.remove(item)

    for item in y:
        if abs(sum(y) - sum(x)) > abs((sum(y) - item) - (sum(x) + item)):
            x.append(item)
            y.remove(item)

    x, y = swap2(x, y)
    y, x = swap2(y, x)
    #replace this for solution
            
    
    print(x)
    print(y)
    print(x + y)
    return abs(sum(x) - sum(y))
    
def swap(a, b):
    for itemA in a:
        for itemB in b:
            if(abs(sum(a) - sum(b)) > abs((sum(a) - itemA + itemB) - (sum(b) + itemA - itemB))):
               return itemA, itemB

    return False

def swap2(a, b):
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and i < len(a) and j < len(a):
                sumA = a[i] + a[j]
                c = []
                for item in a:
                    c.append(item)

                c.append(sumA)
                c.remove(a[i])
                c.remove(a[j])

                check =swap(c, b)
                if check:
                    a = []
                    for item in c:
                        a.append(item)


                    check = swap(a, b)
                    if check:
                        swapA, swapB = swap(a, b)
                        a.append(swapB)
                        b.append(swapA)
                        a.remove(swapA)
                        b.remove(swapB)

    return a, b

list1 = [10, 10] # == 0
list2 = [10] # == 10
list3 = [5, 8, 13, 27, 14] # == 3
list4 = [5, 5, 6, 5] # == 1
list5 = [12, 30, 30, 32, 42, 49] # == 9
list6 = [1, 1, 1, 3] # == 0
list7 = [10, 1, 6, 18, 47, 36, 38]
list8 = [17, 7, 41, 22, 20, 4, 12]
list9 = [1, 6, 8, 18, 36, 38, 47]

print("Final answer: ", checkio(list7))
