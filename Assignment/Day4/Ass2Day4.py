import re
import os

if re.search("^[0-9]{10}$", input("Enter number: ")):
    print("Valid")
else:
    print("Invalid")
os.chdir(str(os.getcwd()) + '\\test')
print(list(map(lambda rel: (re.findall("[a-z]*@[a-z]*.[a-z]*", rel, re.IGNORECASE)),
               map(lambda el: open(el, "r").read(),
                   filter(lambda el: os.path.splitext(el)[1] == '.log', os.listdir())))))
