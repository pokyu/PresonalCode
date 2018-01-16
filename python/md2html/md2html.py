#!/usr/bin/env python
# -*- coding: utf-8 

##########################################################################################
# - Copyright(C), 2017-2020, Pokyu Tung
# - File name: md2html.py
# - Author: Pokyu Tung    Version: 1.0    Date: 2018-01-16
# - Description: //将markdown文件转换成html文件
# - Execute: python md2html.py test.md test.html
# - Function List: //主要函数列表，每条记录应包括函数名及功能简要说明
#   - 1. mdtext2htmltext: 真正的文件内容处理函数
#   - 2. md2html: 参数校验，输入输出文件处理
# - History: 
#   - 1. Date: 2018-01-16
#        Author: Pokyu Tung
#        Modification: init
#   - 2. ...
##########################################################################################

import markdown
import os
import sys

# python的str默认是ascii编码，和unicode编码冲突，不加下面两行会报错:...'ascii' codec can't decode...
reload(sys)
sys.setdefaultencoding('utf8')

# 真正的文件内容处理函数
def mdtext2htmltext(mdstr):
	
	# html模板 %s就是填充的内容
    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="default.css" rel="stylesheet">
    <link href="github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''
	
	# 扩展块，格式不能转换，可在此增加扩展块
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
	
    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret


# 参数校验，输入输出文件处理
def md2html(pstr):

    if len(pstr) < 3:
        print('usage: md2html source_filename target_file')
        sys.exit()

    infile = open(pstr[1],'r')
    md = infile.read()
    infile.close()

    
    if os.path.exists(pstr[2]):
        os.remove(pstr[2])


    outfile = open(pstr[2],'a')
    outfile.write(mdtext2htmltext(md))
    outfile.close()

    print('convert %s to %s success!'%(pstr[1],pstr[2]))
	
	
if __name__ == '__main__':

    md2html(sys.argv)
	