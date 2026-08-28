# keyword argument = an argument preceded by an identifier
#                   help with readability 
#                   order of argument doesn't  matter
#                   1. POSITIONAL, 2. DEFAULT, 3. KEYWORD, 4. ARBITRARY

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")
# hello("Hello", "Mr.", "Aditya", "Raj")

# hello("Hello",last="Raj", title="Mr.", first="Aditya" )

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
# phone_num = get_phone(country= "+91", area=731, first = 965, last = 3851)
# print(phone_num)

# def add(*args):
#     total =  0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4,5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Aditya","Raj")