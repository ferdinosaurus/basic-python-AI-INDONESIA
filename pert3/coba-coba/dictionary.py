def check_value_kwargs(**kwargs):
    print("kwargs")
    print(kwargs)


#inialisasi dict
var_dict=dict(value1 = "isi value1",value2 = "isi value2")
print(var_dict['value1'])
print("==================================================")


#hapus key pada dict
var_dict.pop("value1")
print("setelah value1 dihapus : ")
print(var_dict)
print("==================================================")


#add key value pada dict
var_dict.update({"value3" : "isi value3"})
print("setelah diisi value3")
print(var_dict)
print("==================================================")


#print by items
print("print items")
print(var_dict.items())
print("==================================================")


#print menggunakan looping
print("print by loop")

for key,value in var_dict.items():
    print("key : {} and your value : {}".format(key,value))
print("==================================================")

#kwargs
print("**kwargs dan *args")
def check_value_kwargs(**kwargs):
    print("kwargs")
    print(type(kwargs))
    print(kwargs)

def check_value_args(*args):
    print("args")
    print(type(args))
    print(args)


check_value_kwargs(**var_dict)
check_value_kwargs(test = 123,test1 = 456, test3 =789)
check_value_args("test","test")
print("==================================================")

#clear dict
var_dict.clear()
print("setelah di clear")
print(var_dict)
print("==================================================")
