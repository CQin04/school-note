# 第5章课后编程题
# 请根据图片的内容，完成第5章课后编程题，文件命名为chapter-5.py，提交该文件到学习通。
#
# 五、编程题
# 1. 已知列表 li_num1 = [4, 5, 2, 7] 和 li_num2 = [3, 6]，
#    请将两个列表合并为一个列表，并将合并后的元素按降序排列。
# 2. 已知元组 tu_num1 = ('p', 'y', 't', ['o', 'n'])，
#    请向元组的最后一个列表中添加新元素 'h'。
# 3. 已知字符串 str_demo = 'skdaskerkjsalkj'，请统计该字符串中各字母出现的次数。
# 4. 已知列表 li_one = [1, 2, 1, 2, 3, 5, 4, 3, 5, 7, 4, 7, 8]，
#    编写程序实现删除列表 li_one 中重复数据的功能。

print('题目 1:')
# 列表合并
li_num1 = [4,5,2,7]
li_num2 = [3,6]
li_num3 = li_num1 + li_num2
print(f'列表合并，{li_num3}')

# 降序排列
li_num3.sort(reverse=True)
print(f'降序排列，{li_num3}')
print(' ')


print('题目 2:')
# 元组中的列表添加元素
tu_num1 = ('p','y','t',['o','n'])
tu_num1[3].append('h')
print(f'添加新元素后，{tu_num1}')
print(' ')


print('题目 3:')
# 统计字符出现次数
str_demo = 'skdaskerkjsalkj'
for i in set(str_demo):
    print(f'{i}出现的次数：{str_demo.count(i)}')
print(' ')


print('题目 4:')
# 删除重复数据
li_one = [1,2,1,2,3,5,4,3,5,7,4,7,8]
li_two = []
for i in li_one:
    if i not in li_two:
        li_two.append(i)
print(f'去重后的列表，{li_two}')