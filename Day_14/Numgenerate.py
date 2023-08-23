# import random

# options = ['Nagpur', 'Gondia', 'Chandrapur', 'Bhandara']  # Your list of options
# selected_option = random.choice(options)
# correct_option="Amravati"
# print("Selected option:", selected_option , correct_option)


file_path = "file.txt"  # Replace with the actual path to your file

try:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())  # Strip to remove newline characters
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("An error occurred:", e)
