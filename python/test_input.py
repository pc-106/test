import sys

# 读取所有输入，过滤 Ctrl+Z
input_data = sys.stdin.read().replace('\x1a', '')

# 按换行符分割
lines = input_data.split('\n')

data = []
for line in lines:
    # 跳过空行
    if line.strip():
        # 对每行按空格分割并尝试转换为整数
        for item in line.split():
            try:
                # 尝试转换为整数
                num = int(item)
                data.append(num)
            except ValueError:
                # 跳过非整数
                pass  # 静默跳过，不打印提示

print(data)