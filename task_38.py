# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".
text = 'абвшогпвгпрвяашпгнабвабвабв'
def editor(text1):
    text1 = ''
    string = 'абв'
    for i in text:
        text1 = text.replace('абв', '')
        return text1

   
print(editor(text))