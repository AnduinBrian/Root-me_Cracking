s = list("ksuiealohgy")
index = 0
password = ""

# print s

# 1: eax + 4
index += 4
password += s[index]
index = 0
# 2: eax + 5
index += 5
password += s[index]
index = 0
# 3: eax + 1
index += 1
password += s[index]
index = 0
# 4: eax + 0xA
index += 0xA
password += s[index]
index = 0

print password
