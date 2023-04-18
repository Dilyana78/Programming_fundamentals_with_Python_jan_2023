count = int(input())
username_by_licenseplate = {}

for _ in range(count):
    info = input().split()
    status = info[0]
    if status == "register":
        username = info[1]
        license_plate = info[2]
        if username not in username_by_licenseplate:
            username_by_licenseplate[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif status == "unregister":
        username = info[1]
        if username in username_by_licenseplate:
            username_by_licenseplate.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for user, plate in username_by_licenseplate.items():
    print(f"{user} => {plate}")