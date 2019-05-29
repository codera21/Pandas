import json
from fns import *
filepath = 'vericred_valor.json'

speciality_count = 0
speciality = set([])
try:
    fp = open(filepath)
    for line in fp:
        arr = json.loads(line)
        specialities = get_specialities(arr['specialties'])
        for i in specialities:
            speciality.add(i)
finally:
    fp.close()
# print(speciality)
# print("\n\n")
# print("Optometry" in speciality)
