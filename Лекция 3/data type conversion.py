st = "True"
b = bool(st) #Преобразование булевого

num_st = "123"
num_int = int(num_st)
num_float = float(num_st)
print(f"Тип данных для num_st: {type(num_st)}") # <class 'str'>
print(f"Тип данных для num_int: {type(num_int)}") # <class 'int'>
print(f"Тип данных для num_float: {type(num_float)}\n") # <class 'float'>

float_st = "1.2345"
fl_st = float(float_st)
print(f"Тип данных для fl_st: {type(fl_st)}") # <class 'float'>