Задание
=======

Вход: описание стран на карте множеством отрезков (страна - многоугольник). Выход: минимальное число цветов, необходимое для раскраски данной карты (т.е. 2 соседних страны не могут быть одного цвета), и соответствующая раскраска. Примечание: данная программа предполагает визуализацию.

Реализация
==========

Структура программы
-------------------

- Creator.py
- Reader.py
- Geometry.py
- Graphs.py
- GeoTests.py
- Visual.py
+ task_map.py
- file1.txt
- file2.txt
 
Описание
---------
 
### Creator.py
 Модуль, хранящий класс для создания карты по умолчанию.Легко дописываются нужные страны в виде: страна = (отрезок, отрезок, отрехок....), отрезок=(точка, точка), точка=(х,у), итого: страна=(((х0,у0),(х1,у1)),((х1,у1),(х2,у2)), ... , ((.,.),(х0,у0)));
 
 Имеет два метода записи в файл: текстовый (для текстового чтения) и сериализация pickle
Также в этом модуле хранится функция записи карты из памяти в текстовый файл.

### Reader.py
 Модуль, хранящий класс для чтения карты из файла.(два типа файлов)
  
  Текстовый файл с картой представляет из себя:
 В первой строке натуральное число - количество стран.
 Каждая последующая строка - отдельная страна. Страна - набор вершин многоугольника записанных через пробел, где вершина это записанные через пробел координаты х и у.
 Пример в файле file1
  
### Geometry.py
В этом модуле хранятся функции работы с геометрией(вычисление длины отрезка, проверка отрезков на смежность, проверка многоугольников на смежность).

### Graphs.py
Модуль хранит класс граф с методами создания графа смежности по списку стран(с помощью списка смежности), сортировки графа по степени смежности, раскраски графа.

### GeoTests.py
Модуль тестирования геометрических функций.

### Visual.py
Модуль с функцией создания окна, отображения стран, и прочей визуализации программы.

### file1.txt, file2_pickle.txt
Две карты с различным числом цветов и смежностей.

### task_map.py
Основной скрипт программы.
Состоит из нескольких частей:
1. Импорт всего необходимого
2. Обработка аргументов.
task_map.py [-h] [-o FILENAME] [-f METHOD] [-v] [-t]
- Содержит вывод краткой справки по аргументам (ключ -h)
- Обработка ключа '-o', позволяющая открыть файл с картой
- Ключ '-f' позволяет задать формат входного файла(pickle или текст). По умолчанию, в программе используются текстовые файлы.
- Ключ '-v' показывающий версию программы
- Ключ '-t' запускающий тесты.
3. Если аргументы отсутствовали, то последовательно выполняются шаги по раскраске карты - чтение, создание графа, сортировка, раскраска, визуализация.

Versions
========

UPD v1.7:

1. Обработка ошибок
2. тесты

UPD v1.8:

1.  о программе, хэлп
2.  использование ООП

UPD v1.9:

Добавлена возможность работы с текстовыми файлами.

UPD v2.0:

Рефакторинг, исправление ошибок, добавлен аргумент выбора формата входного файла.
