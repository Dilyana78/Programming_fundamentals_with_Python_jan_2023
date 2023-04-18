countries = input().split(", ")
capitals = input().split(", ")
final_result = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in final_result.items():
    print(f"{country} -> {capital}")

# version with zip
# countries = input().split(", ")
# capitals = input().split(", ")
# my_dict = dict(zip(countries, capitals))
# for country, capital in my_dict.items():
#     print(f"{country} -> {capital}")