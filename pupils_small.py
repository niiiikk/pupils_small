# Дан файл pupils.txt, содержащий сведения об успеваемости в классе (оценки за четверть по информатике). 

# В файле pupils_small.py напиши программу для подсчёта средней оценки класса и отображения списка лучших учеников. Для этого:
# 1) Создай класс Pupil, в котором будут храниться: фамилия, имя и оценка ученика. Также создай список pupils [ ], в котором будут храниться объекты типа Pupil.
# 2) Открой файл pupils.txt на чтение. Каждую строку данных преобразуй в объект типа Pupil и добавь в список pupils. Используй метод str.split( ) для разделения строки на части.
# 3) Посчитай среднюю оценку и найди отличников. Выведи на консоль список класса и подсчитанные данные (см. скриншот)

class Pupil():
    def __init__(self, surname, name, mark) -> None:
        self.surname = surname
        self.name = name
        self.mark = mark
    # def __st (self) -> str:
    #     return f'Pupil is {self.surname}'
    def __str__(self) -> str:
        return f'Pupil is {self.surname}'

pupils = []
file = open('pupils.txt', 'r', encoding = 'utf-8')
raw_info = file.readlines()
file.close()


def parse_info(part:str):
    data = part.split()
    return Pupil(data[0], data[1],int(data[2]))
for part in raw_info:
    pupils.append(parse_info(part))
print(pupils[0])

