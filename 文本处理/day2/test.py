import re


s = "<div>\
<p>岗位职责：</p>\
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>\
<p><br></p>\
<p>必备要求：</p>\
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>\
<p>&nbsp;<br></p>\
<p>技术要求：</p>\
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>\
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>\
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>\
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>\
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>\
<p>&nbsp;<br></p>\
<p>加分项：</p>\
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>\
</div> "

# print(re.sub(r"</?\w+>|&nbsp", "", s))  # &nbsp 在html代码中表示空格


# 提取出域名
s2 = """http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415"""

# p = r"(http://.+?/).*"
#
# print(re.sub(p, lambda x: x.group(1), s2))
#
# regex = re.compile(r"(http://.*?/)", re.M)
# result = regex.findall(s2)  # 结果是列表
# print(result)


string = '''
http://mirrors.kernel.org/gnu/coreutils/coreutils-6.11.tar.gz  
http://mirrors.kernel.org/gnu/bash/bash-5.0.tar.gz  
https://www.baidu.com/  
https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.1.2/hadoop-3.1.2-src.tar.gz  
https://apache.org/dist/hbase/2.1.4/api_compare_2.1.3_to_2.1.4RC1.html
https://www.apache.org/dyn/closer.lua/hbase/2.1.4/hbase-2.1.4-src.tar.gz
https://tomcat.apache.org/download-90.cgi  
http://mirrors.kernel.org/gnu/grub/grub-2.02.tar.xz 
http://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.19/bin/apache-tomcat-9.0.19-fulldocs.tar.gz  
https://archive.apache.org/dist/zookeeper/current/zookeeper-3.4.14.tar.gz  
https://hub.docker.com/editions/community/docker-ce-desktop-mac  
https://home.firefoxchina.cn/  
http://docs.ceph.com/docs/master/
'''
# regex = re.compile(r"(http[s]?://.*?/)", re.M)
#
# res = regex.findall(string)
# print(res, len(res))

# reg = re.compile(r"(http[s]?://.*?/).*")
# res = reg.sub(lambda x: x.group(1), string)
# print(res)


regex = re.compile(r"</?\w+>|&nbsp")
result = regex.sub("", s)
print(result)
