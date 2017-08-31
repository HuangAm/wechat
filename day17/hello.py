#coding:gbk
print("老男孩")

'''
不管在Python2还是在Python3中内存中的永远是Unicode字节，但在我们执行的时候Python2就见鬼了
在Python2里执行的时候我们现在看到的“老男孩”在我们看到后
她就被悄悄地改为字节形式存在了内存中，因为我们标明用GBK所以它是以GBK字节存在于内存中的，当我们要执行他后，他要把“老男孩”
转为明文展现给我们，只有先变为Unicode后才能变成明文，所以这时候我们的问题就放在他是通过什么方式变为Unicode的
既然是GBK字节当然要用gbk规则解码成Unicode对不对，如果我们这里没有decode这个步骤的话，这里会用pychm里面默认的utf-8
去解码，就会乱码
'''
print (repr("老男孩"))#'\xc0\xcf\xc4\xd0\xba\xa2' 6个字节

'''一定要注意的是：
        #coding:GBK 是在文件存储和打开的时候对Python2或者Python3说你们见到我后就把你们原来默认的编解码方式换成
                    GBK，同过GBK解码成Unicode然后在变成人类能看懂的明文，当我们看到文件内容后，这句话就完成了自
                    己的任务了

                    然后当我们在此刻执行print语句的时候问题就来了，如果是在Python2中，我们这个"老男孩"是以GBK字节
                    的形式待在内存中的，主要是因为贱贱2偷偷的把他从Unicode变回了字节，真贱！在执行的时候有需要把
                    "老男孩"这个字节存在变为我们能看到的明文，妈的，这个时候pycharm和cmd又来插一脚，这俩狗币说，
                    要怎么变成你们人类能看懂的明文，我们说了算，然后pycharm说老子就用utf-8给你解成Unicode，
                    cmd说老子就用GBK给你解成Unicode，知道真相后的人类心中有一万个草拟吗

                    GUI叔听到无数个草拟吗后，做了更改，在Python3中，所有都是Unicode，那次是这里的"老男孩"就是
                    Unicode字节，因为他现在就在内存中，好了，我们要执行他，一执行，又得从字节变为明文，但是这个
                    时候不需要考虑你是pycharm还是cmd因为老子是Unicode，老子自己就能变成明文
'''

# print(u"hello"+"yuanhao")
# print (u"袁浩"+u"最帅")
# print (u"袁浩"+"最帅")
