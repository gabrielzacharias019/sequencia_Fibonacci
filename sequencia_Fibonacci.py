num = int(input("Digite um número inteiro: "))

# define os dois primeiros números da sequência
fib1 = 0
fib2 = 1

# verifica se o número está na sequência de Fibonacci
while fib2 < num:
    temp = fib2
    fib2 = fib1 + fib2
    fib1 = temp

if fib2 == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
