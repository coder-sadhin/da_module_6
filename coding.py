# def char_at_pos(r, s):
#     return r[::2] if s == "odd" else r[1::2]

# print(char_at_pos([2, 4, 6, 8, 10], "even"))
# print(char_at_pos("EDABIT", "odd"))
# print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))

# char_at_pos = lambda r, s: r[1::2] if s == "even" else r[0::2]


# print(char_at_pos([2, 4, 6, 8, 10], "even"))
# print(char_at_pos("EDABIT", "odd")) 
# print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))

x=int(input())
y=int(input())
# result = product_or_sum(x, y)
result = lambda x, y: x*y if x*y <= 1000 else x+y
print("The result is {}".format(result(x,y)))