import elf, munchkins, levers, lollipops, yeeters, pits
all_lollipops = lollipops.get()
lever = levers.get(0)
for lollipop in all_lollipops:
    elf.moveTo(lollipop.position)
elf.moveTo({"x":8,"y":1})
data = lever.data()
data.insert(0, "munchkins rule")
lever.pull(data)
elf.moveDown(3)
elf.moveTo({"x":2, "y":3})

