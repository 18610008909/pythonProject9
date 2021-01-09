import yaml

with open("./data.yaml", 'r', encoding="utf-8")as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

data1= {'search_data': {'search_test_002': {'expect': {'value': '你好哈哈哈哈'}, 'value': 'hello'},
'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

with open("./hello.yaml", 'w', encoding='utf-8')as r:
    write = yaml.dump(data1, r, encoding='utf-8', allow_unicode=True)