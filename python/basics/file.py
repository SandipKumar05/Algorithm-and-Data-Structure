## file manupulation 
# Read json file
print('json file')
import json
with open('example.json','r') as json_file:
    json_data=json.load(json_file)
    print(json_data)
with open('write.json','w') as json_file:
    json.dump(json_data,json_file, indent=4)

print('yaml file')
import yaml
with open('example.yaml','r') as yaml_file:
    yaml_data=yaml.safe_load(yaml_file)
    print(yaml_data)
with open('write.yaml','w') as yaml_file:
    yaml.safe_dump(yaml_data,yaml_file,indent=2)

print('csv file')