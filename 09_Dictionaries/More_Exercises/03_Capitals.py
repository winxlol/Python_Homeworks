from collections import defaultdict

countries = input().split(", ")
capitals = input().split(", ")

zip_method = list(zip(countries, capitals))

print(zip_method)