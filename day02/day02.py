import re

password_policies = []
with open("input") as f:
    password_policies = f.readlines()

pattern = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'

valid_pass_p1 = 0
valid_pass_p2 = 0

for i in password_policies:
    match = re.search(pattern, i)
    min_amount = int(match.group(1))
    max_amount = int(match.group(2))
    char = match.group(3)
    password = match.group(4)
    count = password.count(char)
    if count >= min_amount and count <= max_amount:
        valid_pass_p1 += 1
    # part 02
    if password[min_amount-1] == char and password[max_amount-1] != char:
        valid_pass_p2 = valid_pass_p2+1
    if password[min_amount-1] != char and password[max_amount-1] == char:
        valid_pass_p2 = valid_pass_p2+1

print(valid_pass_p1)
print(valid_pass_p2)