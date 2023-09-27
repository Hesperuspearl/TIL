import json

json_data = '''
{
    "name": "김싸피",
    "age": 28,
    "hobbies": [
        "공부하기",
        "복습하기"
    ]
}'''

data = json.loads(json_data)
print(data)
print(type(data))

#json 데이터에서 원하는 데이터만 가져오기
name = data.get('name')

print(name)