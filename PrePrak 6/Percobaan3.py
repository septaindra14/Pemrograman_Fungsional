from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
image = Image.open(
    "D:\Pelajaran Kuliah\Praktikum\Smt 5\Pem. Fungsional\Modul 6\Cuplikan_layar.png")

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightness_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightness_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("brightness_contrast_image.png")

# TODO 4: Tampilkan hasil
final_image.show()
