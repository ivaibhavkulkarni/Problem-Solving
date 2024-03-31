# write a program that reads num and prints no of 100,50,10 and 1

n = int(input())

hundreds = n // 100
r_h = n % 100
fifty = r_h // 50
r_f = r_h % 50
tens = r_f // 10
r_t = r_f % 10
ones = r_t // 1

print("100:"+str(hundreds))
print("50:"+str(fifty))
print("10:"+str(tens))
print("1:"+str(ones))