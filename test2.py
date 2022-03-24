"""
 * Project name(项目名称)：Python_break_and_continue
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 21:27
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    str1 = "1234567890123456789012345678901234567890"
    for i in str1:
        if i == "7":
            continue
        print(i, end=" ")

    input()
