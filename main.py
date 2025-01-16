#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    result = 0
    if len(list1) != len(list2):
        return "Error"
    else:
        for i in range(len(list1)):
            result += list1[i] * list2[i]
        return result


if __name__ == '__main__':
    l1 = input().split()
    l2 = input().split()
    sum_of_products(l1,l2)
    