tem = float(input('อุณหภูมิ C: '))
far = 9/5* tem +32
a = format(float(far),".2f")
print(f'หารคนละ {far:.2f} บาท ')
print('หารคนละ', a ,"บาท")
print("หารคนละ"+" "+ str(a) + " "+ "บาท")
print("หารคนละ {:.2f} บาท".format(far))

