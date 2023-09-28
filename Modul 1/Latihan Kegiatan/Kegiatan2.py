random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "world", 412, 5.5, "AI"]

int_dictionary = {}
float_tuple = ()
string_list = []

for angka in random_list:
    if isinstance(angka, int):
        # Memisahkan angka ratusan, puluhan,satuan
        ratusan = (angka // 100) % 10
        puluhan = (angka // 10) % 10
        satuan = angka % 10
        int_dictionary[angka] = (ratusan, puluhan, satuan)
    elif isinstance(angka, float):
        float_tuple += (angka,)
for item in random_list:
    if isinstance(item, str):
        string_list.append(item)

# Menampilkan hasil
print("Data Integer :")
for key, value in int_dictionary.items():
    print(F"{key}:\nratusan={value[0]}"),
    print(F"puluhan= {value[1]}") 
    print(F"satuan= {value[2]}")
print("\nData Float :")
print(float_tuple)
print("\nData String :")
print(string_list)