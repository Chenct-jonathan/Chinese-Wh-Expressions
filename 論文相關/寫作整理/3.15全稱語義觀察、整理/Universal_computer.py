# 開啟 log_0315 檔案
with open('C:/Users/User/Desktop/Chinese-Wh-Expressions/log/log_0423.txt', 'r') as file:
    lines = file.readlines()

# 儲存開頭有 'c' 的句子
c_lines = []

# 尋找開頭有 'c' 的句子
for line in lines:
    if 'c' in line:
        c_lines.append(line)

# 將結果寫入 Universal_computer.txt 檔案
with open('C:/Users/User/Desktop/Universal_computer_0423.txt', 'w') as file:
    for line in c_lines:
        file.write(line)
