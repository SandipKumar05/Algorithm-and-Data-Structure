# Question: Write a Python script to parse a YAML configuration file named "config.yaml" and print the values of the "database," "username," and "password" keys.
import yaml
print("hello world")
with open("creds.yaml") as file:
    print("sandip")
    data=yaml.safe_load(file)
print(data['user'])