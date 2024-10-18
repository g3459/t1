import hashlib

source=str(input('source: '))
sourcehash=hashlib.sha256(source.encode('utf-8')).hexdigest()
sourceint=int(sourcehash,16)
encoding=str(input('encoding: '))
base=len(encoding)

while sourceint>=base:
    rest=sourceint % base
    fstr=encoding[rest]+fstr
    sourceint=sourceint//base

fstr=encoding[sourceint]+fstr
print('fstr: '+fstr)
fstr256hash=hashlib.sha256(fstr.encode('utf-8')).hexdigest()
print('sha256hash: '+fstr256hash)