# -*- coding: utf-8 -*-
"""
Китайский гороскоп делит время на 12-летние циклы, и  каждому году 
соответствует конкретное животное. Один из таких циклов приведен ниже
Год Животное 
2000 Дракон
2001 Змея 
2002 Лошадь 
2003 Коза 
2004 Обезьяна 
2005 Петух 
2006 Собака
2007 Свинья
2008 Крыса
2009 Бык
2010 Тигр
2011 Кролик
Напишите программу, которая будет запрашивать у пользователя год 
рождения и  выводить ассоциированное с  ним название животного по 
китайскому гороскопу. При этом программа не должна ограничиваться 
только годами из приведенной таблицы, а должна корректно обрабатывать все годы нашей эры.
"""

year = int(input())
final_pet = ""
years_array = [0,1,2,3,4,5,6,7,8,9,10,11]
pet_array = ['Обезьяна','Петух','Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Кролик', 'Дракон', 'Змея', 'Лошадь', 'Коза']
print(pet_array[year % 12]) #Животное

#for i in range (0 , 11):
#    if (divmod(year, 12)[1] == years_array[i]):
#       final_pet = pet_array[i]
#print(final_pet) #Животное
