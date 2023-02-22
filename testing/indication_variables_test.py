from collections import defaultdict

indication = (('0', 'DEFAULT'), ('chronic_depression', '192080009'), ('chronic_depression', '161891005'))

indication_dict = defaultdict(list)
for key, value in indication:
    indication_dict[key].append(value)


print(indication)
print(indication_dict)