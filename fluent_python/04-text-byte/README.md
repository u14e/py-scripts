一个字符串是一个字符序列。

- 字符的标识(码位): Unicode (eg. A 的码位是 65(十进制), 41(十六进制))
- 字符的具体表述(字节序列): 取决于所用的编码 (eg. utf-8 的编码 A -> \x41)

把码位转换成字节序列的过程是 **编码**; 把字节序列转换成码位的过程是 **解码**

bytes 或 bytearray 对象的各个元素是介于 0~255（含）之间的整数
bytes 不可变, bytearray 可变

各个字节的值可能会使用下列三种不同的方式显示:
    - 可打印的 ASCII 范围内的字节（从空格到 ~），使用 ASCII 字符本身
    - 制表符、换行符、回车符和 \ 对应的字节，使用转义序列 \t、\n、\r 和 \\
    - 其他字节的值，使用十六进制转义序列（例如，\x00 是空字节）

常见编码错误:
    - UnicodeEncodeError: 编码时, 目标编码中没有定义某个字符(eg. ascii 里面就没有定义中文字符)
    - UnicodeDecodeError: 解码的编码和编码的编码不一致(不一致的编码可能不会报错, 但是解码出来的字符不符合预期)

`fp = open('z.txt')` 使用的编码是系统默认编码, 在 powershell 上面返回: `<_io.TextIOWrapper name='z.txt' mode='r' encoding='cp936'>`, 所以需要时刻记住一定要指定编码 `open('z.txt', encoding='utf-8')`

- 如果打开文件时没有指定 encoding 参数，默认值由 locale.getpreferredencoding() 提供
- 如果设定了 PYTHONIOENCODING 环境变量 (https://docs.python.org/3/using/cmdline.html#envvarPYTHONIOENCODING), `sys.stdout/stdin/stderr` 的编码使用设定的值；否则，继承自所在的控制台；如果输入/输出重定向到文件，则由locale.getpreferredencoding() 定义
- Python 在二进制数据和字符串之间转换时，内部使用 sys.getdefaultencoding() 获得的编码；Python3 很少如此，但仍有发生。 这个设置不能修改。 

综上，`locale.getpreferredencoding()` 返回的编码是最重要的：这 是打开文件的默认编码，也是重定向到文件的 sys.stdout/stdin/stderr 的默认编码

因此, 关于编码默认值的最佳建议是：别依赖默认值