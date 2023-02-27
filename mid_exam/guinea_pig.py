food = float(input()) * 1000
hey = float(input()) * 1000
cover = float(input()) * 1000
weight_pig = float(input()) * 1000

for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hey -= food * 0.05
    if day % 3 == 0:
        cover = cover - (weight_pig / 3)
    if food <= 0 or hey <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        exit()
print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hey / 1000:.2f}, Cover: {cover / 1000:.2f}.")