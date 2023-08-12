fn = 'aaa.txt'
chunk = 100
msg = ''
with open(fn) as file_obj:
    while True:
        txt = file_obj.read(chunk)
        if not txt:
            break
        msg += txt
print(msg)