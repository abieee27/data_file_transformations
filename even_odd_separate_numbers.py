#read numbers and separate even and odd numbers
with open ('numbers.txt') as f:
    numbers = f.read().split()

even = []
odd = []

for num in numbers:
    n = int(num)
    if n% 2 == 0:
        even.append(str(n))
    else:
        odd.append(str(n))

with open("even.txt", "w") as f:
    f.write(" ".join(even))
with open("odd.txt", "w") as f:
    f.write(" ".join(odd))

print("Even numbers:", " ".join(even))
print("Odd numbers:", " ".join(odd))
print("finish! check even.txt and odd.txt numbers")