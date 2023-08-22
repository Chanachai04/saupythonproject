celsius = float(input("อุณหภูมิ C: "))
fahrenheit = 9 / 5 * celsius + 32

c = format(float(celsius), ".2f")
f = format(float(fahrenheit), ".2f")

print(f"อุณหภูมิ {celsius:.2f} C อุณหถูมิที่แปลง {fahrenheit:.2f} F ")
print("อุณหถูมิ", c, "C", "อุณหถูมิที่แปลง", f, "F")
print("อุณหถูมิ" + " " + c + " C " + "อุณหถูมิที่แปลง" + " " + str(f) + " " + "F")
print("อุณหถูมิ {:.2f} C อุณหถูมิที่แปลง {:.2f} F".format(celsius, fahrenheit))
