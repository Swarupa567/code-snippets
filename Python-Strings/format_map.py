profession = { 'name':['swarupa','lavanya'],'profession':['software developer','Data Scientist'],'age':[22,21]}
print('{name[0]} is a {profession[1]} and she ' 'is of {age[0]} years old'.format_map(profession))
print('{name[1]} is a {profession[0]} and she ' 'is of {age[1]} years old'.format_map(profession))

