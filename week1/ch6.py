# Day 5 -Part3. Working with different file formats (.txt, .csv, .json)

# 1. Working w/ .csv files
# CSV(comma separated value)
# csv 내장 모듈이 있다.

import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        # 각 row는 string의 list가 됨
  
  
    
# csv file을 쓰는 법
data = [['Name', 'Age'], ['Alice', 24], ['Bob', 22]]

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
# json
# json은 데이터 포맷 변환의 허브로 쓰임.

import json

with open('jsonfile.json', 'r') as file:
    // # load가 파일을 읽어 json을 파이썬 dictionary로 바꿔줌
    data = json.load(file)self
    print(data)
    
data = {
    'name' : "Alice",
    'age' : 24,
    'is_student' : True
}

with open('jsonfile.json', 'w') as file:
    # .dump()는 dictionary를 json format file로 바꿔줌
    json.dump(data, file) # write dictionary to file