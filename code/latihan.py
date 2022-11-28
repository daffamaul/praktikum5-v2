# Membuat dictionary daftar kontak 
data = {
	"Daffa": "0812",
	"Aji": "0821"
}
print(data)
# output : {'Daffa': '0812', 'Aji': '0821'}

# Menmapilkan kontak milik aji
print(data['Aji'])
# output: 0821

# Menmabhkan kontak baru
data.update({'Riko': '0876'})
print(data)
# output : {'Daffa': '0812', 'Aji': '0821', 'Riko': '0876'}

# Ubah kontak aji dengan nomer baru
data['Aji'] = '0889'
print(data)
# output : {'Daffa': '0812', 'Aji': '0889', 'Riko': '0876'}

# Menghaous kontak riko
del data['Riko']
print(data)
# output : {'Daffa': '0812', 'Aji': '0889'}

# Menampilkan seluruh nama
for data in data.items():
	print(data[0])
	print(data[1])
# output: Daffa Aji Riko
# ourpur: 0812 0889 0876