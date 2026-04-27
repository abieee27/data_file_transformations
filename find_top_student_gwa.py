with open("student.txt", "r") as f:
    lines = f.readlines()

top_name = ""
top_gwa = float("inf")

for line in lines:
    name, gwa = line.split()
    gwa = float(gwa)

    if gwa < top_gwa:
        top_gwa = gwa
        top_name = name

print(f"The top student is {top_name} with a GWA of {top_gwa:.2f}.")
print(f"congratulations {top_name}!")