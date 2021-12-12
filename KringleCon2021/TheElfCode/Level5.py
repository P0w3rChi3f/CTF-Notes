import elf, munchkins, levers, lollipops, yeeters, pits
# Complete the code below:
lever0, lever1, lever2, lever3, lever4 = levers.get()
# Move onto lever4
elf.moveLeft(2)
# This lever wants a str object:
lever4.pull(lever4.data() + " concatenate")
# Need more code below:
elf.moveUp(2)
if lever3.data() == True:
    l3answer = False
else:
    l3answer = True
lever3.pull(l3answer)
elf.moveUp(2)
lever2.pull(int(lever2.data() + 1))
elf.moveUp(2)
l1answer = lever1.data() + [1]
lever1.pull(l1answer)
elf.moveUp(2)
l0data = lever0.data()
l0data["strkey"]="strvalue"
lever0.pull(l0data)
elf.moveUp(2)