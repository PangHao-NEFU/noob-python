# 对于二进制文件：
# with open('demo.txt','rb') as file_obj:
#     # print(file_obj.read(100))
#     # print(file_obj.read(30))

#     # seek(size,可选值) 可以修改当前读取的位置，size为字节数
#     file_obj.seek(55)
#     file_obj.seek(80,0)
#     file_obj.seek(70,1)
#     file_obj.seek(-10,2)
#     # seek()需要两个参数
#     #   第一个 是要切换到的位置
#     #   第二个 计算位置方式
#     #       可选值：
#     #           0 从头计算，默认值
#     #           1 从当前位置计算
#     #           2 从最后位置开始计算

#     print(file_obj.read())

#     # tell() 方法用来查看当前读取的位置(文件内指针所在位置)
#     print('当前读取到了 -->',file_obj.tell())

# 对于文本文件：
with open('demo2.txt','rt' , encoding='utf-8') as file_obj:
    # print(file_obj.read(100))
    # print(file_obj.read(30))

    # seek(size,可选值) 可以修改当前读取的位置，size表示字节，注意处理文本文件时，一个中文字符占几个字节
    #   utf-8一个中文字符占3个字节，ASC2一个英文字符占1个字节
    file_obj.seek(9)
    # seek()需要两个参数
    #   第一个 是要切换到的位置
    #   第二个 计算位置方式
    #       可选值：
    #           0 从头计算，默认值
    #           1 从当前位置计算
    #           2 从最后位置开始计算

    print(file_obj.read())

    # tell() 方法用来查看当前读取的位置
    print('当前读取到了 -->',file_obj.tell())