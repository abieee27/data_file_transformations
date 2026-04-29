import os

def process_numbers_from_file():
    input_file_name = "integers.txt"
    even_output_file = "double.txt"
    odd_output_file = "triple.txt"

    even_numbers_squared = []
    odd_numbers_cubed = []

    with open(input_file_name, "r") as file_reader:
        numbers_list = file_reader.read().split()

        for number in numbers_list:
            converted_number = int(number)

            if converted_number % 2 == 0:
                squared_value = converted_number ** 2
                even_numbers_squared.append(str(squared_value))
            else:
                cubed_value = converted_number ** 3
                odd_numbers_cubed.append(str(cubed_value))

    with open(even_output_file, "w") as even_writer:
        even_writer.write(" ".join(even_numbers_squared))

    with open(odd_output_file, "w") as odd_writer:
        odd_writer.write(" ".join(odd_numbers_cubed))

    print("Processing complete. Check output files.")
    print("Contents of double.txt:", " ".join(even_numbers_squared))
    print("Contents of triple.txt:", " ".join(odd_numbers_cubed))


process_numbers_from_file()