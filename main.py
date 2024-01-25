#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
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
    
    input1 = input()
    input2 = input()

    list1 = []
    list2 = []
    
    for i in input1:
        list1.append(i)
    for i in input2:
        list2.append(i)

    output = sum_of_products(list1, list2)

    print(output)
