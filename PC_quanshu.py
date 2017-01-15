# coding:utf-8
import urllib2
import re

def GET_book_url():
		html = urllib2.urlopen('http://www.quanshu.net/all/lastupdate_2_0_0_0_1_0_1.html').read()
		reg = '''<div class="yd-book-item yd-book-item-pull-left">.*?<a href="(.*?)" target="_blank">.*?<img alt="(.*?)" src="(.*?)" onerror="javascript:this.src='/kukuku/images/nophoto.jpg';" class="pull-left cover-container" width="127" height="160">.*?<h2>(.*?)</h2><br>.*?</a>.*?<div class="author-container">.*?<dl class="dl-horizontal-inline">.*?<dd><p>(.*?)</p></dd>.*?</dl>.*?</div>'''
		return re.findall(reg,html,re.S)
		#print html

def GET_lookurl(html):
		lookhtml = urllib2.urlopen(html).read()
		reg = '''<a href="(.*?)" class="reader" title=".*?">开始阅读</a>'''
		return re.findall(reg,lookhtml)

def GET_chapterurl(html):
		chapterhtml = urllib2.urlopen(html).read()
		reg = '''<li><a href="(.*?)" title=".*?">(.*?)</a></li>'''
		return re.findall(reg,chapterhtml)

def GET_contents(html):
		contentshtml = urllib2.urlopen(html).read()
		reg = '''style5.*?</script>(.*?)<script type="text/javascript">style6'''
		return re.findall(reg,contentshtml)

#GET_book_url()
for i in GET_book_url():
		#print i[0],i[3],i[4]
		for x in GET_lookurl(i[0]):
				#print x
				for y in GET_chapterurl(x):
						#print y
						joinurl = '/'.join([x,y[0]])
						#print joinurl
						for z in GET_contents(joinurl):
								#print i[3],i[4],y[1],z
								z = z.replace('&nbsp;',' ').replace('<br /><br />','\n')
								with open('%s_%s.txt'%(i[3],i[4]),'a') as f:
										f.write('%s\n\n%s\n\n\n\n\n'%(y[1],z))
										print '%s————下载完毕！'%i[3]
