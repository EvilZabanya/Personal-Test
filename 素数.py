"""
判断是否是素数
"""
 
num = int(input('请输入一个正整数: '))
end = int(num // 2) + 1  # 只判断前半部分是否能整除即可，前半部分没有能整除的因此，后半部分肯定也没有
 
is_prime = True
for x in range(2, end):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('素数')
else:
    print('不是素数')
