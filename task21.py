data_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

result = []
for d in data_list:
    for value in d.values():
        result.append(value)
print(set(result))
        