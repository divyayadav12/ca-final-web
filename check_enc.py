data = open('src/App.jsx', 'rb').read()
idx = data.find(b'60')
# find the dash character used
while idx != -1:
    chunk = data[idx-3:idx+10]
    if b'60' in chunk and b'90' in chunk:
        print(repr(chunk))
        break
    idx = data.find(b'60', idx+1)
