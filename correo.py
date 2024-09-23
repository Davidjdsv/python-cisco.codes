direc = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    direc += ch
print(direc)