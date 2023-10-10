var1 = [10, 20, 'Hello', True, [111, 'Wow'], 'มานะ']

var2 = var1
var3 = var1.copy()

print(var1)
print(var2)
print(var3)
print('-----------------------------------')
var2[0] = 111
print(var1)
print(var2)
print(var3)
print('-----------------------------------')
var3[0] = 999
print(var1)
print(var2)
print(var3)
print('-----------------------------------')
