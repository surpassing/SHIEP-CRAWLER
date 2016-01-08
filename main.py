# -*- coding: utf-8 -*-
# SHIEP STUDENT CENTER CRAWLER - June 2014 by Sam
# 上海电力学院学生信息查询简易版本
# python 2
# 使用方法：手动输入学号范围和cookie，登陆管理系统(非学生)获取cookies后开爬

# import chardet
import requests
import re
# import io


def start():
    global stu_db

    start = 20096005 #起始学号手动输入
    end = 20096005 #结束学号手动输入
    t_id = range(start, end)


    for each_id in t_id:

        headers ={
                #'GET /schoolmanager/teacher/query/studentResult.jsp?sno=20111368 HTTP/1.1'
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'JSESSIONID=nUU5FTQ6gKYciyZDidFtY6Z5.undefined', #手动输入cookie
                'Host': '210.35.95.64:7777',
                'RA-Sid': '7C4DEE2C-20140708-044937-c9f6d7-553185',
                #'Pragma': 'no-cache',
                #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'RA-Ver': '3.0.7',
                'Referer': 'http://210.35.95.64:7777/schoolmanager/teacher/query/student.jsp',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
                 }

        payload = {
            'sno': str(each_id)
        }

        r = requests.get(
            'http://210.35.95.64:7777/schoolmanager/teacher/query/studentResult.jsp?sno=' + str(each_id),
            params=payload, headers=headers)

        html1 = r.content #Requests 自动的把返回信息由Unicode解码

        #文件是gb2312的str
        #{'confidence': 0.99, 'encoding': 'GB2312'}
        #print isinstance(html1, unicode)
        try:
            file = html1.decode('gb2312').encode('utf-8') #{'confidence': 0.99, 'encoding': 'utf-8'}
            #将gb2312解码为unicode之后编码为utf8

        except:
            print 'wrong_code'

        try:
            stu_id_lst = re.findall('学号:&nbsp;([^<]+)</font></td>', file) #0
            stu_mail_lst = re.findall('邮件:&nbsp;([^<]+)</font></td>', file)  #1
            stu_tel_lst = re.findall('电话:&nbsp;([^<]+)</font></td>', file)  #2
            stu_name_lst = re.findall('姓名:&nbsp;([^<]+)</font></td>', file) #3
            stu_sex_lst = re.findall('性别:&nbsp;([^<]+)</font></td>', file)  #4
            stu_home_lst = re.findall('生源所在地:&nbsp;([^<]+)</font></td>', file)  #5
            stu_birth_lst = re.findall('出生日期:&nbsp;([^<]+)</font></td>', file) #6

            stu_id =  stu_id_lst[0]
            stu_mail = stu_mail_lst[0]
            stu_tel = stu_tel_lst[0]
            stu_name = stu_name_lst[0] #{'confidence': 0.87625, 'encoding': 'utf-8'}
            stu_sex = stu_sex_lst[0]
            stu_home = stu_home_lst[0]
            stu_birth = stu_birth_lst[0]

            print stu_id+','+stu_mail+','+stu_tel+','+stu_name+','+stu_sex+','+stu_home+','+stu_birth

        except:
            print 'find_nothing'
        #a = unicode(stu_name)
            #list_2013.extend(stu_id_list)
            #list_2013.extend(stu_mail)
            #list_2013.extend(stu_tel)
            #list_2013.append(stu_name)
            #list_2013.extend(stu_sex)
            #list_2013.extend(stu_home)
            #list_2013.extend('\n')





    #with io.open('stu_mail_2013', 'wb') as dict:
    #    print >> dict, result







start()











