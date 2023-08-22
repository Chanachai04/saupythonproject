people = int(input('จำนวนคน : '))
money = float(input('จำนวนเงิน : '))

result = float(money / people)
a = format(float(result),".2f")
print(f'หารคนละ {result:.2f} บาท ')
print('หารคนละ', a ,"บาท")
print("หารคนละ"+" "+ str(a) + " "+ "บาท")
print("หารคนละ {:.2f} บาท".format(result))
