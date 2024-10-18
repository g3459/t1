import hashlib
import string

base=62
nstr=string.ascii_lowercase+string.ascii_uppercase+'0123456789'

source=str(input('source: '))
sourcehash=hashlib.sha256(source.encode('utf-8')).hexdigest()
sourceint=int(sourcehash,16)
encoding=str(input('encoding: '))
estr=''
ap=0
for e in encoding.split():
    for ch in nstr:
        if ch==e[0]:
            ap=1
        if ap==1:
            estr+=ch
        if ch==e[1]:
            ap=0
fstr=''
while sourceint>=base:
    rest=sourceint % base
    fstr=estr[rest]+fstr
    sourceint=sourceint//base

fstr=estr[sourceint]+fstr
fstr256hash=hashlib.sha256(fstr.encode('utf-8')).hexdigest()
print('fstr: '+fstr)
print('sha256hash: '+fstr256hash)