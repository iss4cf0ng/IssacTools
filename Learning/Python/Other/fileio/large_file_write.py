msg = ''
fn = 'out.txt'
size = len(msg)
offset = 0
chunk = 100
with open(fn, 'w') as file_obj:
    while True:
        if offset > size:
            break
        print(file_obj.write(msg[offset:offset+chunk]))
        offset += chunk