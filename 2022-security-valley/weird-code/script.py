from dis import disassemble

f = open("code.txt", "r")
content = f.read()

print(content)
res = disassemble(content)
print(res)
