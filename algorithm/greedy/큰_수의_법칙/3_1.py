n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
'''
data.sort(reverse = True)
first = data[0]
second = data[1]
'''

result = 0


while True:  #무한 반복분(따라서 m이 0이 될때까지 break를 설정해주지 않으면 계속 더해짐)
  for i in range(k):  #가장 큰 수를 k번 만큼 반복
    if m==0: 
      break
    result += first
    m -= 1 #m은 first가 더해질 때마다 감소(first는 k번만큼만 더해짐)
  if m==0:
    break
  result += second #first가 k번만큼 더해지면 second를 한 번 더하기
  m -= 1

'''어찌됐건 if m==0: break는 first를 더하는 중이던 second를 더하는 중이던 어느때나 멈출 수 있도록 하기 위해
  first를 더할때와 second를 더할때의 코드에서 설정된 것임'''

print(result)
    

