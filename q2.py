
originalweight = float(input())

weight = originalweight
count = 0

weight = round(weight, 0)
while weight % 50 != 0:
    weight += 1


print (round(weight - originalweight,1))