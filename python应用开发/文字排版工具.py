# 4.5.2文字排版工具
# 请根据PDF的内容，制作一个文字排版工具，文件命名为4-5-2.py，提交该文件到学习通。
#
#
# 题目要求： 显示欢迎信息并接收待排版文字，用菜单反复选择功能，直至退出：
#
# - 1：删除文字中的空格。
# - 2：将英文逗号、句号、问号、感叹号、冒号替换为对应中文标点。
# - 3：以输入中的 \r\n 作为段落标记，将文字分段显示。
# - 4：将英文字母转换为大写。
# - 0：显示感谢信息并退出；无效编号应提示错误。

print("欢迎使用文字排版工具！")

string = input(r"请输入要排版的文字（多段文字之间用\r\n标记）：")

print(f"排版前的文本：\n{string}")



while True:

    print('=========================')

    print('1.段落分割')

    print('2.英文标点替换')

    print('3.删除空格')

    print('4.字母大写')

    print('5.字符串第一个字母大写，其余小写')

    print('0.退出')

    print('=========================')

    option = input("请输入功能选项：")



    if option == '3':  # 删除空格

        string = string.replace(' ', '')

        print(f"删除空格后的文本：\n{string}")

    elif option == '2':  # 英文标点替换

        string = string.replace(',', '，')

        string = string.replace('.', '。')

        string = string.replace('?', '？')

        string = string.replace('!', '！')

        string = string.replace(':', '：')

        print(f"替换标点后的文本：\n{string}")

    elif option == '1':  # 段落分割

        paragraphs = string.split(r'\r\n')

        string = '\n'.join(paragraphs)

        print(f"段落分割后的文本：\n{string}")

    elif option == '5':

         string = string.title()

         print(f"字符串第一个字母大写，其余小写：\n{string}")

    elif option == '4':  # 字母大写

        string = string.upper()

        print(f"字母大写：\n{string}")

    elif option == '0':  # 退出

        print("感谢使用文字排版工具，再见！")

        break

    else:

        print("无效选项，请重新输入！")