# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число. Вам необхідно "перевернути" цє число задом наперед, тобто щоб у результаті вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.
# Вам не потрібно перевіряти, що користувач ввів правильне число - зробіть вигляд, що користувач завжди вводить 5 значне число. Тобто введене користувачем число завжди складатиметься з 5 цифр.
# Якщо користувач ввів інше число, це проблема користувача, а не вашої програми.
# Використовуються лише цілі числа.
# Для розв'язання задачі потрібно використовувати лише той зріз даних, який було пройдено. Тобто використовувати строки не можна.
# Приклади:
# Користувач ввів: 12345 - на екрані відображається: 54321
# Користувач ввів: 37568 - на екран відображається: 86573
number = int(input("Enter your number: "))
print(number)

n1 = number // 10000
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number % 100 // 10
n5 = number % 10

result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)