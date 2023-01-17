last_sector = input()
first_sector_rows = int(input())
odd_seats = int(input())

first_sector = 65
first_seat = 97
counter = 0

for sector in range(first_sector, ord(last_sector) + 1):
    for row in range(1, first_sector_rows + 1):
        if row % 2 != 0:
            for seat in range(first_seat, (first_seat + odd_seats)):
                counter += 1
                print(f"{chr(sector)}{row}{chr(seat)}")
        elif row % 2 == 0:
            for seat in range(first_seat, (first_seat + odd_seats) + 2):
                counter += 1
                print(f"{chr(sector)}{row}{chr(seat)}")
    if first_sector_rows + 1 > first_sector_rows:
        first_sector_rows += 1

print(counter)

