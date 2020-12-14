'''Scrivete il codice in python di un programma che calcoli la sequenza di Fibonacci'''

print("Questo programma calcola la sequenza di Fibonacci")
i=int(input("Inserire il numero di cicli desiderato: "))
num=int(input("Inserisci il numero con cui vuoi calcolare la sequenza di Fibonacci: "))
num2=0
num3=num+num2
inc=0
while True:
    print(num,"+",num2,"=",num3,"   ",inc)
    if num==0:
        break
    if i!=0:
        inc+=1
        num=num2
        num2=num3
        num3=num+num2
        i-=1
    else:
        break
