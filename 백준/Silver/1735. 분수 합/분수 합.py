def gcd(a, b):
    while (b > 0):
        t = a % b
        a = b
        b = t
    return a


n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())
s = 0
if m1 >= m2:
    s = gcd(m1, m2)
else:
    s = gcd(m2, m1)

s = s * (m2 // s) * (m1 // s)
s1 = s // m1
s2 = s // m2

answer = (n1 * s1) + (n2 * s2)

a = gcd(answer, s)
answer = answer // a
s = s // a
print(answer, s)
# answer / s

# 최대 공약수를 찾은뒤 그걸로 값들을 나누고 다 곱하자
# 그거에 대해서 각각 계산 뒤 곱해서 더하기
