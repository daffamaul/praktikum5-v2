# Adalah pasangan key-value nya, yang indeksnya bisa dirubah dari numerik menjadi tipe data lainnya
# contoh 
dict = {'Name' : ['Daffa', 'Aji'],
		'Age' : 17,
		'Class' : ['TIA4']
		}
print("dict[\"Name\"] : ", dict['Name'])
# ouput: dict["Name"] : Daffa

# Mengakses nilai pada dictionary
# name = dict['Name']
# print(name)
# output : Daffa
# clas = dict.get("Class")
# print(clas)
# output : TIA4

# Menghapus element dictionary
# del dict['Name']
# print(dict)
# output : {'Age': 17, 'Class': 'TIA4'}
# dict.clear()
# print(dict)
# output : {}

# Menambahkan 
dict.update({"Country": "Indonesian"}) # menambahkan key-value terbaru
print(dict)
