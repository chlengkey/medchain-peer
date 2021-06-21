from dirsync import sync

s = "./Realme 2"
t = "./Realme C2"

sync(s,t, 'sync', verbose=True)
sync(t,s, 'sync', verbose=True)
