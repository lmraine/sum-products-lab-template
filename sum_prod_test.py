import main

l1 = [2, 4, 6]
l2 = [1, 3, 5]
l3 = [1]
l4 = []

def test_sum_prod():
    correct = (2 + 12 + 30)
    stud_result = main.sum_of_products(l1, l2)
    assert correct == stud_result

def test_sum_prod_length():
    correct = "Error"
    stud_result = main.sum_of_products(l1,l3)
    assert correct == stud_result