from fileinput import filename

def write_user_lines_to_file():
    file_name = "my_life.txt"

    with open(file_name, "w") as file_writer:
        while True:
              user_input_line = input("enter a line: ")
              file_writer.write(user_input_line + "\n")

              continue_input = input("do you want to add more lines? (y/n): ")
              if continue_input.lower() not in ["y", "yes"]:
                break

    print("all lines have been saved to ", file_name)

write_user_lines_to_file()
    