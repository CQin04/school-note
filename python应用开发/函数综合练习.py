# 第6章课后编程题
# 五、编程题
#
# 1. 编写函数，输出 1～100 中偶数之和。
#
# 2. 编写函数，计算 20×19×18×…×3 的结果。
#
# 3. 编写函数，判断用户输入的整数是否为回文数。回文数是一个正向和逆向都相同的整数，如 123454321、9889。
#
# 4. 编写函数，判断用户输入的 3 个数字是否能作为边长构成三角形。
#
# 5. 编写函数，计算两个正整数的最小公倍数。
#
#
#
#
# 请完成第6章课后编程题，文件命名为chapter-6.py，提交该文件到学习通。

print('题目1:')
# 计算1~100偶数之和
def fun1():
    s = 0
    for i in range(2, 101, 2):
        s += i
    print(s)

fun1()
print(' ')


print('题目2:')
# 计算20×19×18×...×3
def fun2():
    s = 1
    for i in range(3, 21):
        s *= i
    print(s)

fun2()
print(' ')


print('题目3:')
# 判断回文数
def fun3():
    n = input('请输入整数：')
    if n == n[::-1]:
        print('是回文数')
    else:
        print('不是回文数')

fun3()
print(' ')


print('题目4:')
# 判断能否构成三角形
def fun4():
    a = int(input('第一条边：'))
    b = int(input('第二条边：'))
    c = int(input('第三条边：'))
    if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
        print('能构成三角形')
    else:
        print('不能构成三角形')

fun4()
print(' ')


print('题目5:')
# 计算最小公倍数
def fun5():
    a = int(input('第一个正整数：'))
    b = int(input('第二个正整数：'))
    n = max(a, b)
    while n % a != 0 or n % b != 0:
        n += 1
    print(n)

fun5()