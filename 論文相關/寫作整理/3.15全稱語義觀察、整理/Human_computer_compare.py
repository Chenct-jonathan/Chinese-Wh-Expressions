# 開啟 Universal_human.txt 檔案
with open('C:/Users/User/Desktop/Universal_human.txt', 'r', encoding='utf-8') as human_file:
    human_lines = human_file.readlines()

# 開啟 Universal_computer.txt 檔案
with open('C:/Users/User/Desktop/Universal_computer_0423.txt', 'r', encoding='utf-8') as computer_file:
    computer_lines = computer_file.readlines()

# 提取每個檔案的編號
human_numbers = [line.split()[0] for line in human_lines]
computer_numbers = [line.split('.')[0] for line in computer_lines]

# 找出只存在於其中一個檔案中的編號
unique_numbers = set(human_numbers).symmetric_difference(computer_numbers)

# 寫入不同的編號到 Human_computer_compare.txt 檔案
with open('C:/Users/User/Desktop/compare_0423.txt', 'w', encoding='utf-8') as compare_file:
    for number in unique_numbers:
        if number in human_numbers and number not in computer_numbers:
            compare_file.write(f"From Universal_human.txt: {number}\n")
        elif number in computer_numbers and number not in human_numbers:
            compare_file.write(f"From Universal_computer.txt: {number}\n")


