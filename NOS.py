#Neon Operating System v 1.0
import time
from colorama import init
from colorama import Fore, Back, Style

print(Fore.YELLOW + 'Загрузка ОС')
time.sleep(2)
print('Добро пожаловать в NOS!')
while True:
  com = input("Введите команду:")
  if com == ("инфоомация"):
    print("NOS была создана в 2023 в России.")
  if com == ("перезагрузка"):
    print("Загрузка ОС")
    time.sleep(2)
    print("Добро пожаловать в NOS!")
  if com == ("выключить"):
     break
  if com == ("запустить $Калькулятор"):
    what = input("Введите действие:")
    a = float(input("Введите первое число:"))
    b = float(input("Введите второе число:"))
    if what == "+":
      c = a + b
      print ("Результат:" + str(c))
      
    elif what == "-":
       c = a - b
       print ("Результат:" + str(c))
       
    elif what == "/":
       c = a / b
       print("Результат:" + str(c))
       
    elif what == "*":
       c = a * b
       print("Результат:" + str(c))
    
  if com == ("системная информация"):
   	print("Аккаунт: Администратор")
   	print("RAM: 100 мб")
   	print("NOS v 1.0")
   	
  if com == ("cd: Аккаунты-Новый"):
    us = input("Введите имя нового пользователя:")
    print("Вы создали новый аккаунт: " + us)
    
  if com == ("удалить $ОС"):
    vopros = input("При согласии вы потеряете доступ к системе. Продолжить? [y/n]")
    	
    if vopros == ("y"):
    		while True:
    			input(Fore.RED + 'НЕТ СИСТЕМЫ!')
    			
  if com == ("установить ROOT"):
    					print(Fore.GREEN + 'Установка. . .')
    					time.sleep(12)
    					print("Успешно!")
    					while True:
    						h = input("F:Root-CMD.exe:")
    						
    						if h == ("выйти ROOT"):
    							break
    					 
  if com == ("запустить $AIBot"):
  	print (Fore.YELLOW + 'Здравствуйте!')
  	while True:
  		uy = input('Введите вопрос:')
  		
  		if uy == ("Как тебя зовут"):
  			print("Меня зовут АИБот")
  			
  		if uy == ("Сколько тебе лет"):
  			print ("Мне -1 год)")
  			
  		if uy == ("Пока!"):
  			print("До свидания!")
  			break
  		