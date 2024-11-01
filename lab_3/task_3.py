# TODO  Напишите функцию count_letters
def count_letter(strr: str):
    dict_letters_amount = dict()
    for el in strr:
        el = el.lower()
        if el.isalpha():
            dict_letters_amount[el] = dict_letters_amount.get(el, 0)+1
    return dict_letters_amount


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letter_amount: dict):
    letters_number = sum(dict_letter_amount.values())
    frequency_letters = {}
    for let, num in dict_letter_amount.items():
        frequency_letters[let] = num/letters_number
    return frequency_letters

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result = calculate_frequency(count_letter(main_str))
for k, v in result.items():
    print(f'{k}: {v:.2f}')