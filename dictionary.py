scores = {'john': 12000, 'bobby': 2000, 'janny': 42000}
print(scores)
print(scores['john'])

# เพิ่มสมาชิกใหม่เข้า dictionary
scores['roger'] = 32000

print(scores)

# การสร้าง dictionary ว่าง
points = {}

# เพิ่มค่าเข้า dictionary ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 12.3
points['mr_c'] = 14.5

print(points)

# การ loop อ่านสมาชิกของ dictionary ออกมา
for k, v in scores.items():
    print(k, v)
