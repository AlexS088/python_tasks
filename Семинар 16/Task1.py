import os
def script(pth: str):
    file_counter = 0
    dir_counter = 0
    txt_files = []
    files = os.listdir(pth)
    lens = [len(file) for file in files]
    max_elem = files[lens.index(max(lens))]
    if not os.path.exists:
        return "Такой путь не найден"
    else:
        for obj in files:
            if os.path.isdir(obj):
                dir_counter += 1
            else:
                file_counter += 1
                if obj.endswith(".txt"):
                    txt_files.append(obj)
            print(f"Название файла: {obj}, размер: {os.path.getsize(obj)}")
    print(dir_counter)
    print(file_counter)
    print(max_elem)
print(script(os.getcwd()))     
    