# 開啟文字檔
with open('C:/Users/User/Desktop/論文相關/全句數備份/全句數.txt', 'r' , encoding='utf-8') as file:
    lines = file.readlines()

# 初始化編號
count = 1

# 儲存開頭有 'c' 的句子
c_lines = []

# 對每一行進行處理
for line in lines:
    # 刪除換行符號
    line = line.strip()
    
    # 如果開頭有 'c'，則加入 c_lines
    if line.startswith('c'):
        c_lines.append((count, line))
    
    # 輸出編號和句子
    print(f"{count} {line}")
    
    # 編號加一
    count += 1

# 輸出開頭有 'c' 的句子
print("\n開頭有 'c' 的句子:")
for line_num, line_content in c_lines:
    print(f"{line_num} {line_content}")
