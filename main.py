import char_to_path
from turtle import *

color('black', 'yellow')
begin_fill()
left_chars = ["S", "emp", "O", "emp", "R", "emp", "R", "emp", "Y"]
char = left_chars[0]
left_chars_ = left_chars
for char in left_chars_:
    path_char = char_to_path.chars[char]
    for i in path_char:
        print(i)
        try:
            right(path_char[i]["right"])
        except:
            try:
                forward(path_char[i]["forward"])
            except:
                left(path_char[i]["left"])

done()
