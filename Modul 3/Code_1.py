def konversi(minggu=0):
    def step1(hari=0):
        def step2(jam=0):
            def step3(menit=0):
                total_menit = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
                return total_menit
            return step3
        return step2
    return step1

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

outputData = []

for item in data:
    parts = item.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])
    konvert = konversi(minggu)(hari)(jam)(menit)
    outputData.append(konvert)

print("Output Data =", outputData)