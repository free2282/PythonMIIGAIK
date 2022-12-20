import pymorphy2
from translate import Translator
morph_features = pymorphy2.MorphAnalyzer()


text = "Здравствуйте. Я на больничном с температурой тридцать девять, завтра пар не будет, сообщите, пожалуйста, группе." \
       " Если поправлюсь до следующей субботы, то проведём два практических занятия с ноубуками, " \
       "а лекции оставшиеся я вам вышлю отдельно вместе с вопросами к экзамену. Но это чуть позже, " \
       "когда получше себя чувствовать буду "


text = text.replace(",", "").replace(".", "").replace("!", "").lower()
words_array = text.split(" ")
words_array.remove('')

parsing_array = list()
for x in words_array:
    p = morph_features.parse(x)[0].normal_form
    parsing_array.append(p)


d = dict()
for word in parsing_array:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

translator = Translator(to_lang="en", from_lang="ru")

with open("translated.txt", 'w') as words:
    words.write(f"Исходное слово|Перевод|Количество упоминаний\n")
    for v in sorted(d.values(), reverse=True):
        for k in d.keys():
            if d[k] == v:
                print(f"{k}|{translator.translate(k).lower()}|{d[k]}")
                words.write(f"{k}|{translator.translate(k).lower()}|{d[k]}\n")
                d.pop(k)
                break
