
weight = float(input("What is your weight?: "))
print()
metric = input("(K)g or L(bs): ")


if metric == "k""K":
    answer = (weight) / 0.45
    print("Weight in Lb's isL " + str(answer))
else:
    answer = (weight) * 0.45
    print("Weiht in Kgs is: " + str(answer))
    

numbers = [1, 2, 3, 4, 5]
numbers.remove(5)

print(numbers)