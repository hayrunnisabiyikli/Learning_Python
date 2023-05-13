"""Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
tuple1 = (4, 3, 2, 1, 0)
tuple2 = (5, 10, 2, 4)"""

# Hayrunnisa Bıyıklı - 21091010143

def calc_product(numbers_tuple):
    product = 1
    for num in numbers_tuple:
        product *= num
    return product

tuple1 = (4, 3, 2, 1, 0)
tuple2 = (5, 10, 2, 4)

product1 = calc_product(tuple1)
print("Product of tuple1:", product1)

product2 = calc_product(tuple2)
print("Product of tuple2:", product2)



