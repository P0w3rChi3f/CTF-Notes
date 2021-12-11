import elf, munchkins, levers, lollipops, yeeters, pits
lever0 = levers.get(0)
lollipop0 = lollipops.get(0)
sum = lever0.data() + 2
elf.moveTo({"x":6, "y":12})
lever0.pull(sum)
elf.moveLeft(4)
elf.moveTo({"x":2, "y":2})