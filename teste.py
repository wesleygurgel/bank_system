import re

string = "#7 - oi"


string2 = "# 8 - qwewqqweqweqweqweqweqwqw"
string2 = "# 8 - eaiqweqqweqww"


print(re.match("#\s?\d{1,3}\s?-\s?(\w|\s){,49}", string))