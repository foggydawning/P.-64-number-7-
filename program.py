def sort (list):
    if len(list)==0:
        return "В массиве нет чисел, встречающихся несколько раз"

    if list.count (max(list))>1:
        return max(list)

    list.remove (max(list))

    return sort(list)

list=[]

list_=sort(list)

if list_=="В массиве нет чисел, встречающихся несколько раз":
    print(list_)
else:
    print("Максимальное число, встречающееся в массиве несколько раз=",list_)
