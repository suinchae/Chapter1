n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k  #이때 int가 없고 m/k+1이 딱 떨어지지 않을 때에는 소수점이 나오지만, int가 있음으로 그 몫의 값이 나옴(//)
count += m%(k+1) #이거는 m/k+1이 딱 떨어질 때는 어짜피 남는게 없으니 0, 딱 떨어지지 않을 때는 나머지 값이 나와서 더해짐
'''So, 위의 count코드는 무조건 정수형의 값이 나오게 됨!!'''

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second #두번째로 큰 수 더하기

print(result)
