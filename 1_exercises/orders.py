orders = int(input())
total_order = 0
for i in range(1, orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or days < 1 or days > 31 or capsules_per_day < 1 or \
            capsules_per_day > 2000:
        continue
    price_for_one_day = capsules_per_day * price_per_capsule
    all_days_price = days * price_for_one_day
    print(f"The price for the coffee is: ${all_days_price:.2f}")
    total_order += all_days_price
print(f"Total: ${total_order:.2f}")