# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите число: "))
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(sum)    


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#          Сколько журавликов сделал каждый ребенок, если известно,
#          что Петя и Сережа сделали одинаковое количество журавликов,
#          а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# shadoofs = int(input("Введите сколько всего сделали журавликов: "))
# if shadoofs%6:
#     print("неверное число")
# else:
#     shadoofsPetya = shadoofs//6
#     shadoofsKatya = shadoofs//3*2
#     shadoofsSeryoga = shadoofs//6
#     print(shadoofsPetya, shadoofsKatya, shadoofsSeryoga)


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#         Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#         Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#         Вам требуется написать программу, которая проверяет счастливость билета.

# number = int(input("Введите шестизначный номер билета: "))
# number_str = str(number)
# if int(number_str[0]) + int(number_str[1]) + int(number_str[2]) == int(number_str[3]) + int(number_str[4]) + int(number_str[5]):
#     print("yes")
# else: 
#     print("no") 


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите размер шоколадки n: "))
# m = int(input("Введите размер шоколадки m: "))
# k = int(input("Введите сколько долек вы хотите отломить: "))
# if (k % n and k % m) or k > n * m:
#     print("no")
# else:
#     print("yes")