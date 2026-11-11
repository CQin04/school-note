# 4.3.1地区时间格式转换器
# 请根据PDF的内容，制作一个地区时间格式转换器，文件命名为4-3-1.py，提交该文件到学习通。
#
#
# 题目要求： 输入年、月、日、时、分、秒和国家，按所选国家输出时间：
#
# - 中国：YYYY年MM月DD日 HH:mm:ss
# - 美国：MM/DD/YYYY HH:mm:ss
# - 英国、澳大利亚、法国：DD/MM/YYYY HH:mm:ss
# - 德国、俄罗斯：DD.MM.YYYY HH:mm:ss
# - 加拿大：YYYY-MM-DD HH:mm:ss
#
# 例如俄罗斯格式可输出 15.11.2023 13:56:00。

# 用户输入的时间信息
year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
day = int(input("请输入日期: "))
hour = int(input("请输入小时: "))
minute = int(input("请输入分钟: "))
second = int(input("请输入秒数: "))
country = input("请输入要转换的国家(中国, 美国, 英国, 德国, 俄罗斯, 澳大利亚, 法国, 加拿大): ")

# 转换成指定国家的时间格式
if country == "中国":
    formatted_time = f"{year}年{month}月{day}日 {hour}时{minute}分{second}秒"
elif country == "美国":
    formatted_time = f"{month:02d}/{day:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"
elif country == "英国":
    formatted_time = f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"
elif country == "德国":
    formatted_time = f"{day:02d}.{month:02d}.{year} {hour:02d}:{minute:02d}:{second:02d}"
elif country == "俄罗斯":
    formatted_time = f"{day:02d}.{month:02d}.{year} {hour:02d}:{minute:02d}:{second:02d}"
elif country == "澳大利亚":
    formatted_time = f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"
elif country == "法国":
    formatted_time = f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"
elif country == "加拿大":
    formatted_time = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
else:
    formatted_time = None

# 输出转换结果
if formatted_time is not None:
    print(f"{country}的时间格式：{formatted_time}")
else:
    print("暂不支持这个国家，请输入提示中的国家名称。")

# f"{变量:格式规则}"
# Python 3.14.8
