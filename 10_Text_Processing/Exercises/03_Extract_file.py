data = input().split('\\')

need_files = data[-1].split(".")

print(f"File name: {need_files[0]}")
print(f"File extension: {need_files[1]}")