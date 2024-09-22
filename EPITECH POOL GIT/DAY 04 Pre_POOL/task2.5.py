# Task 2.5: 99 Bottles of Beer song lyrics
for i in range(99, 0, -1):
    if i == 1:
        print(f"1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottles of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer.")
