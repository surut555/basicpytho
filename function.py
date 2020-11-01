# การสร้างฟังก์ชันแบบไม่มีการ return value
def hello(name):
    print(f"hell {name}")


# สร้างฟังก์ชันแบบมีการ return Vauue
def area(width, height):
    total = width*height
    return total


# เรียกใช้งานฟังก์ชัน hello()
hello("surut")

# เรียนใชังานฟังก์ชัน area()
print(area(2, 3))
print(area(5, 3))
print(area(58.2, 54.2))

# ฟังก์ชันแบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name:{name}")
    print(f"salary:{salary}")
    print(f"lang:{lang}")


# เรียนใชังานฟังก์ชัน show_info()
show_info()
print()
show_info('surut', 1200, 'PHP')
