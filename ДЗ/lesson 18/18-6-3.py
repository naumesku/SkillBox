fail = input ('Название файла: ')
symb_beg='@', '№', '$', '%', '^ ', '&', '*','(',')'
symb_end='.txt', '.docx'
if fail.startswith(symb_beg):
  print ('Ошибка: название начинается на один из специальных символов')
elif not fail.endswith(symb_end):
 print ('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
  print ('Файл назван верно@example.txt.')