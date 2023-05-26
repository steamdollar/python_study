#
# 1 . Basic regular expressions syntax
# string의 패턴을 분석할 때 사용하는 표현.
# re module이 정규식을 지원한다.

# \d : [0-9] :어떤 decimal digit이든 match
# \D : [^0-9] : 어떤 non-digit이든 match
# \s : 모든 whitespace char match
# \S : \s와 반대ㅔ
# \w : [a-zA-Z0-9_] : 영어 숫자
# \W : [^a-zA-Z0-9_] : \w와 반대

#
# 2. Searching, Matching and Replacing w/ Regular Expressions
# `re` module을 가져와 사용하는 법을 알아보자.

import re
# search : 전체 string을 탐색

# re.search(pattern, string) : string에서 pattern을 만족하는 부분을 찾아 리턴
print(re.search(r'\d+', '123 hello 456')) # <re.Match object; span=(0, 3), match='123'>

# re.match(pattern, string) : string의 시작 부분만을 탐색.
print(re.match(r'\d+', 'hello 123 456')) # None

# re.findall(pattern, string) : string에서 겹치지 않는 모든 패턴을 리턴
print(re.findall(r'\d+', '123 hello 456')) # ['123', '456']

# sub : match되는 패턴을 지정된 패턴으로 대체
print(re.sub(r'\d+', 'replacement', '123 hello 456')) # replacement hello replacement

#
# 3. Regular Expressions Groups and Special Sequences
# 소괄호를 이용해 정규식에서 그룹을 정의할 수 있다.
# 추가적인 처리를 거치기 위해 조건에 만족하는 부분들을 뽑아올 수 있고,
# 특정 문자열에 quantifier를 적용할 수도 있음.

match = re.search(r'(\d+) (\w+)', '123 hello')
if match:
    print(match.group(0)) # 123 hello - 0번 그룹은 전체
    print(match.group(1)) # 123 
    print(match.group(2)) # hello