import elf, munchkins, levers, lollipops, yeeters, pits
# Gets all lollipops as a list
all_lollipops = lollipops.get()
# Can set lollipop1 using:
lollipop1 = all_lollipops[1]
# Can also set lollipop0 using:
lollipop0 = lollipops.get(0)
elf.moveTo(lollipop1.position)
elf.moveTo(lollipop0.position)
elf.moveTo({"x":2,"y":2})