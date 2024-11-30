# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume_in_byte = 1.44*1024*1024
pages = 100
strings_on_pages = 50
chars_in_string = 25
one_char = 4
volume_of_ine_book = one_char*chars_in_string*strings_on_pages*pages
print("Количество книг, помещающихся на дискету:", int(disk_volume_in_byte//volume_of_ine_book))
