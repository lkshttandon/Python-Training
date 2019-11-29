import os
os.chdir(str(os.getcwd()) + '\\test')
print(list(
    map(lambda el: open(el, "r").read(), filter(lambda el: os.path.splitext(el)[1] == '.log', os.listdir()))))
