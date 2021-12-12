import elf, munchkins, levers, lollipops, yeeters, pits
# Fix/Complete the below code
lever = levers.get(0)
data = lever.data()
if type(data) == bool:
    answer = not data
elif type(data) == int:
    answer = data * 2 
elif type(data) == list:
    answer = []
    for x in data:
        answer.append(x + 1)
elif type(data) == str:
    answer = data + data
elif type(data) == dict:
    answer = data["a"] + 1
elf.moveUp(2)
lever.pull(answer)
elf.moveUp(2)

