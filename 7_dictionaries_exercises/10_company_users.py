employees_by_company = {}
line = input()

while line != "End":
    info = line.split(" -> ")
    company = info[0]
    employee_id = info[1]
    if company not in employees_by_company:
        employees_by_company[company] = []
    if employee_id not in employees_by_company[company]:
        employees_by_company[company].append(employee_id)
    line = input()
for company, employees in employees_by_company.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
