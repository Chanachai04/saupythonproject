# คำสั่ง break กับ continue ที่มักใข้ร่วมกับ Control Flow
for x in range(5):
    if x == 3:
        break;#break ทำงานเมื่อไหร่จบ loop ทันที
    print(f'SAU....{x}')

print('++++++++++++++++++++')
for y in range(5):
    if y == 3:
        continue;#continue ทำงานเทื่อไหร่จนรอบนั้น ไปรอบต่อไปทันที
    print(f'DTI....{y}')