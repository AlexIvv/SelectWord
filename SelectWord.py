import os.path

AllWords = []
SelectedWords = []
with open("russian_nouns.txt","r",encoding='utf-8') as file:
    line = file.readline()
    while len(line) > 0:
        # 6 - количество символов с учетом переноса каретки, сам файл заканчивается пустой строкой
        if(len(line) == 6):
            AllWords.append(line)
        line = file.readline()
    print(AllWords)
print("Введите первое слово из 5 букв (существительное в единственном числе):")
FirstWord = input()
if(len(FirstWord) == 5):
    SelectedWords.append(FirstWord)
i=0
while i < len(SelectedWords):
    print(SelectedWords)
    i+=1
print("Введите имеющиеся буквы в слове:")
HasLettersInWord = input()
print("Введите отсутсвующие буквы в слове:")
HasNotLettersInWord = input()