# LZW-Compression-Algo
LZW压缩算法
Lempel–Ziv–Welch (LZW) 是一种由 Abraham Lempel, Jacob Ziv 和 Terry Welch 发明的**无损压缩**算法。
广泛用于 unix 文件压缩，以及 GIF 图片格式压缩。

## 编码步骤
 1. 初始状态，字典里只有所有的默认项，例如0->a，1->b，2->c。此时P和C都是空的。
 2. 读入新的字符C，与P合并形成字符串P+C。
 3. 在字典里查找P+C，如果:
    - P+C在字典里，P=P+C。
    - P+C不在字典里，将P的记号输出；在字典中为P+C建立一个记号映射；更新P=C。
 4. 返回步骤2重复，直至读完原字符串中所有字符。

## 解码步骤
1. 初始状态，字典里只有所有的默认项，例如0->a，1->b，2->c。此时pW和cW都是空的。
2. 读入第一个的符号cW，解码输出。注意第一个cW肯定是能直接解码的，而且一定是单个字符。
3. 赋值pW=cW。
4. 读入下一个符号cW。
5. 在字典里查找cW，如果:
   a. cW在字典里：
     (1) 解码cW，即输出 Str(cW)。
     (2) 令P=Str(pW)，C=Str(cW)的**第一个字符**。
     (3) 在字典中为P+C添加新的记号映射。
   b. cW不在字典里:
     (1) 令P=Str(pW)，C=Str(pW)的**第一个字符**。
     (2) 在字典中为P+C添加新的记号映射，这个新的记号一定就是cW。
     (3) 输出P+C。
6. 返回步骤3重复，直至读完所有记号。

算法说明转载自CSDN博客
[LZW编解码详解](https://blog.csdn.net/hanzhen7541/article/details/91141112?tdsourcetag=s_pctim_aiomsg)
