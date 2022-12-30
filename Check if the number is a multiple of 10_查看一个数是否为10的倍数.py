user_answer = input("输入一个数，程序会判断这个数是否能被10整除，否则我会告诉你离它最近的十的倍数是几")
number = float(user_answer)
result = number / 10
# result为这个数直接除以10得到结果
after_number = number % 10
# after_number为这个数除以10的余数
if after_number == 0:
    print(str(int(result)))
    print("这个数可以被10整除，结果是" + str(int(result)))
else:
    print(str(result))
    print("这个数不可被10整除，最后答案是" + str(result))
second_answer = input("请问是否继续求出离这个数最近的10的倍数？回车表示继续，q表示结束")
if second_answer != "q":
    nearest_number = 10 - after_number
    # nearest_number为10减去这个数除以10的余数，也为后面程序判断四舍五入得到一个前提
    if nearest_number <= 5:
        last_number = number + nearest_number
        # last_number为当这个数除以10余下的数小于等于5时，程序应该输出的离这个数最近的10的倍数，也就是“四舍五入”中的“五入”
        print(str(int(last_number)))
        print("离您输入的数最近的可以被10整除的数为" + str(int(last_number)))
    else:
        last_second_number = number - after_number
        # last_second_number为当这个数除以10余下的数大于5时，程序应该输出的离这个数最近的10的倍数，也就是“四舍五入”中的“四舍”
        print(str(int(last_second_number)))
        print("离您输入的数最近的可以被10整除的数为" + str(int(last_second_number)))
else:
    print("结束")
last_answer = input("是否还有其他需求？否则你可以查看结果并复制了")
if last_answer != "":
    # 也就是说，无论输入啥都会显示“感谢使用”
    print("感谢使用")
else:
    print("感谢使用")
