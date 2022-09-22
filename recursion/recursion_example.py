# def recursionMethod(Parameters):
#         if exit from condition satisfied:
#             return some value
#         else:
#             recursionMethod(modified Parameters)



def recursionMethod(n):
    assert n>=0 and int(n)==n, "the number must be integer only"
    if n<1:
        print("n is less than 1")
    else:
        recursionMethod(n-1)
        print(n)


recursionMethod(-4)

# output
# n is less than 1
# 1
# 2
# 3
# 4
