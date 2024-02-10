#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(input1, input2):
    
    list1 = input1.split()
    list2 = input2.split()
    
    
    '''for i in range(-1,0):
        if list1[i] == " ":
            list1.pop(i)
    for i in range(-1,0):
        if list2[i] == " ":
            list2.pop(i)'''
    

    if len(list1) == len(list2):

        total = 0
        for i in range(len(list1)):
            product = int(list1[i]) * int(list2[i])
            total += product
        return total
    else:
        return "error"


if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    i1 = input()
    i2 = input()

    print(sum_of_products(i1, i2))

    