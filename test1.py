"""
 * Project name(项目名称)：Python_break_and_continue
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 21:22
 * Version(版本): 1.0
 * Description(描述)： break 语句可以立即终止当前循环的执行，跳出当前所在的循环结构。
 无论是 while 循环还是 for 循环，只要执行 break 语句，就会直接结束当前正在执行的循环体。
 """

if __name__ == '__main__':
    str1 = "1234567890123456789012345678901234567890"
    for i in str1:
        if i == "7":
            break
        print(i, end=" ")

    print()

    str2 = "1234567890123456789012345678901234567890"
    # 提前定义一个 bool 变量，并为其赋初值
    flag = False
    for i in range(3):
        for j in str2:
            if j == '7':
                # 在 break 前，修改 flag 的值
                flag = True
                break
            print(j, end="")
        print("\n跳出内循环")
        # 在外层循环体中再次使用 break
        if flag:
            print("跳出外层循环")
            break

        input()
