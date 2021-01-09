import os
import yaml

def analyze_file(key):
                with open(r"D:\softwaretest\PyCharme\pythonProject9\data\contact1.yml", "r") as f:
                    case_data = yaml.load(f)[key]
                    data_list = list()
                    for i in case_data.values():
                        print(i)
                        data_list.append(i)
                        print(data_list)
                    return data_list

if __name__ == "__main__":
    analyze_file("test_contact")