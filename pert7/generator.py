# def operasiBilangan():
#     a = 7
#     b = 8
#     yield a + b

#     x = 19
#     y = 90
#     yield x - y

#     z = 80
#     w = 90
#     yield z * w

#     c = 999
#     k = 10
#     yield c / k

# oprGen = operasiBilangan()

# for i in oprGen:
#     print(i)



def operasiBilangan():
    yield "Hello World"
    yield "Selamat Pagi"
    yield "Selamat Siang"
    yield "Selamat Sore"

oprGen = operasiBilangan()

for i in oprGen:
    print(i)