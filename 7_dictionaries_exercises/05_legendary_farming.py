key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr" ,
    "motes": "Dragonwrath"
}
junk = {}

limit = False
while not limit:
    line = input()
    materials = line.split()

    for i in range(0, len(materials) -1, 2):
        quantity = int(materials[i])
        some_mat = materials[i + 1].lower()
        if some_mat in key_materials:
            key_materials[some_mat] += quantity
            if key_materials[some_mat] >= 250:
                limit = True
                key_materials[some_mat] -= 250
                print(f"{legendary_items[some_mat]} obtained!")
                break
        else:
            if some_mat not in junk:
                junk[some_mat] = quantity
            else:
                junk[some_mat] += quantity
for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
for material, quantity in junk.items():
    print(f"{material}: {quantity}")