# การสร้างข้อมูลแบบ List
number = [3, 6, 4, 2, 16]
name = ['johh', 'jane', 'Wasan']
mixed = [14, 25.5, True, 'Samit']

# การเข้าถึงสมาชิกใน List
print(number[1])
print(name[2])
print(mixed[1], mixed[3])

# การนับจำนวนสมาชิกใน List
print("สมาชิกทั้งหมดของ number=", len(number))
print(number)

# การสร้าง list แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกในไปใน List ว่าง
data.append(10)
data.append(15)
data.append(20)

print(data)

# การอัพสมาชิกใน List

data[1] = 12

print(data)

# ฟังก์ชันวนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print(n)

# Loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num

print(sum)
