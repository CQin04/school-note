# 5.4.1成语接龙
# 1.
#
# 请根据PDF的内容，制作一个成语接龙，文件命名为5-4-1.py，提交该文件到学习通。
#
#
# 题目要求： 成语均为四字，后一个成语的首字等于前一个成语的末字，每轮不能重复。从“万事如意”开始，将“发愤图强、笑容满面、意气风发、强颜欢笑”自动接龙。
#
# 示例结果： 万事如意 → 意气风发 → 发愤图强 → 强颜欢笑 → 笑容满面。

# 成语接龙
first_idiom = '万事如意'
end_str = first_idiom[-1]
new_li = [first_idiom]
li = ['发愤图强', '笑容满面', '意气风发', '强颜欢笑']

for index in range(len(li)):
    for i in li:
        if end_str == i[0]:
            new_li.append(i)
            li.remove(i)
            end_str = i[-1]
            break

print(new_li)