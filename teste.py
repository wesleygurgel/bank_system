import re

string = "#7 - oi"

<<<<<<< Updated upstream
string2 = "# 8 - qwewqqweq"
=======
string2 = "# 8 - eaiqweqqweqww"
>>>>>>> Stashed changes

print(re.match("#\s?\d{1,3}\s?-\s?(\w|\s){,49}", string))