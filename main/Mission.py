# -*- coding:utf-8 -*-
import xml.dom.minidom
import codecs
import winreg
import os

def clear():
    os.system("cls")

def get_desktop():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

clear()
'''文件创建相关'''
fileName = input("请输入文件名，不需要添加.xml后缀\n")

doc = xml.dom.minidom.Document()

clear()
'''任务设置'''
print("任务设置")
id = input("任务id\n")
activeCheck = input("是否需要检查任务完成进度，输入true或false\n")
shouldIgnoreSenderVerification = input("是否要检查回复邮件时的收件人，输入true或false，意义不明，建议false\n")
mission = doc.createElement("mission")
mission.setAttribute("id",id)
mission.setAttribute("activeCheck",activeCheck)
mission.setAttribute("shouldIgnoreSenderVerification",shouldIgnoreSenderVerification)
doc.appendChild(mission)

clear()
'''创建任务目标模块'''
goals = doc.createElement("goals")
var1 = 1
while var1 == 1:
    judge = int(input("""是否需要任务目标，并且选择任务目标类型
    0——不需要任务目标
    1——删除文件
    2——清理文件夹
    3——文件下载
    4——文本添加字符
    5——文本删除字符
    6——获取管理员权限
    7——回复字符串
    8——延迟任务，在延迟时间内完成任务，需要开启自动检查
    9——拥有标记任务
    10——上传不需解密的文件
    11——上传需要解密的文件
    12——添加学位名称
    13——从指定所有者写学术服务器中删除学位任务
    14——邮件发送任务（推荐医疗记录发送）
    15——使用链接服务器的当前管理员密码进行回答\n"""))
    if(judge == 0):
        goals.appendChild(doc.createTextNode(""))
        mission.appendChild(goals)
    elif(judge == 1):
        target = input("请输入任务目标主机的id名称\n")
        file = input("文件名称，需要后缀\n")
        path = input("文件目录，不需要添加/目录标识符\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type","filedeletion")
        goal.setAttribute("target",target)
        goal.setAttribute("file",file)
        goal.setAttribute("path",path)
        goals.appendChild(goal)
    elif(judge == 2):
        target = input("请输入任务目标主机的id名称\n")
        path = input("文件目录，不需要添加/目录标识符\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "clearfolder")
        goal.setAttribute("target", target)
        goal.setAttribute("path", path)
        goals.appendChild(goal)
    elif(judge == 3):
        target = input("请输入任务目标主机的id名称\n")
        file = input("文件名称，需要后缀\n")
        path = input("文件目录，不需要添加/目录标识符\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "filedownload")
        goal.setAttribute("target", target)
        goal.setAttribute("file", file)
        goal.setAttribute("path", path)
        goals.appendChild(goal)
    elif(judge == 4):
        target = input("请输入任务目标主机的id名称\n")
        file = input("文件名称，需要后缀\n")
        path = input("文件目录，不需要添加/目录标识符\n")
        keyword = input("关键字")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "filechange")
        goal.setAttribute("target", target)
        goal.setAttribute("file", file)
        goal.setAttribute("path", path)
        goal.setAttribute("keyword",keyword)
        goals.appendChild(goal)
    elif(judge == 5):
        print("生成器有问题，暂时无法生成此方法\n")
    elif(judge == 6):
        target = input("请输入任务目标主机的id名称\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "getadmin")
        goal.setAttribute("target", target)
        goals.appendChild(goal)
    elif(judge == 7):
        target = input("请输入任务目标的字符串\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "getstring")
        goal.setAttribute("target", target)
        goals.appendChild(goal)
    elif(judge == 8):
        time = input("请输入延迟任务的秒数\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "delay")
        goal.setAttribute("time", time)
        goals.appendChild(goal)
    elif(judge == 9):
        target = input("请输入任务目标的标记名称（FlagName）\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "hasflag")
        goal.setAttribute("target", target)
        goals.appendChild(goal)
    elif(judge == 10):
        target = input("请输入任务被上传主机的id名称\n")
        file = input("文件名称，需要后缀\n")
        path = input("文件目录，不需要添加/目录标识符\n")
        destTarget = input("请输入任务目标主机的id名称\n")
        destPath = input("目标文件目录\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "fileupload")
        goal.setAttribute("target",target)
        goal.setAttribute("file",file)
        goal.setAttribute("path",path)
        goal.setAttribute("destTarget",destTarget)
        goal.setAttribute("destPath",destPath)
        goals.appendChild(goal)
    elif(judge == 11):
        target = input("请输入任务被上传主机的id名称\n")
        file = input("文件名称，需要后缀\n")
        path = input("文件目录，不需要添加/目录标识符\n")
        destTarget = input("请输入任务目标主机的id名称\n")
        destPath = input("目标文件目录\n")
        decrypt = input("是否需要文件解密，输入true或false\n")
        decryptPass = input("文件解密所需的密码\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "fileupload")
        goal.setAttribute("target", target)
        goal.setAttribute("file", file)
        goal.setAttribute("path", path)
        goal.setAttribute("destTarget", destTarget)
        goal.setAttribute("destPath", destPath)
        goal.setAttribute("decrypt",decrypt)
        goal.setAttribute("decryptPass",decryptPass)
        goals.appendChild(goal)
    elif(judge == 12):
        owner = input("请输入主人姓名\n")
        degree = input("学位名称\n")
        uni = input("大学名称\n")
        gpa = input("gpa值\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "AddDegree")
        goal.setAttribute("owner",owner)
        goal.setAttribute("degree",degree)
        goal.setAttribute("uni",uni)
        goal.setAttribute("gpa",gpa)
        goals.appendChild(goal)
    elif(judge == 13):
        owner = input("请输入主人姓名\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "wipedegrees")
        goal.setAttribute("owner", owner)
        goals.appendChild(goal)
    elif(judge == 14):
        mailServer = input("请输入邮件服务器名称，例如输入jmail，就会产生@jmail后缀\n")
        recipient = input("请输入接受者邮箱，不需要@后缀\n")
        subject = input("主题\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "sendemail")
        goal.setAttribute("mailServer",mailServer)
        goal.setAttribute("recipient",recipient)
        goal.setAttribute("subject",subject)
        goals.appendChild(goal)
    elif(judge == 15):
        target = input("请输入任务目标主机的id名称\n")
        goal = doc.createElement("goal")
        goal.setAttribute("type", "getadminpasswordstring")
        goal.setAttribute("target",target)
        goals.appendChild(goal)
    '''判断'''
    whileJudge = int(input("是否继续添加，如果继续添加请输入1，否则请输入任意字母\n"))
    if (whileJudge != 1):
        break
mission.appendChild(goals)

clear()
'''下一个任务'''
print("下一个任务")
target = input("请输入下一个任务的路径，相对于extension，需要.xml后缀，不存在请输入NONE\n")
silent = input("是否需要静默加载，请输入true或false\n")
nextMission = doc.createElement("nextMission")
nextMission.setAttribute("IsSilent",silent)
nextMission.appendChild(doc.createTextNode(target))
mission.appendChild(nextMission)

clear()
'''分支任务'''

clear()
'''任务供求'''
print("任务供求")
judge = int(input("是否需要开启任务供求？不需要请输入0\n"))
if(judge != 0):
    title = input("任务供求的名称\n")
    reqs = input("任务所需的flag\n")
    requiredRank = input("任务所需的rank值，输入int数字\n")
    text = input("输入任务介绍\n")
    posting = doc.createElement("posting")
    posting.setAttribute("title", title)
    posting.setAttribute("reqs", reqs)
    posting.setAttribute("requiredRank", requiredRank)
    posting.appendChild(doc.createTextNode(text))
    mission.appendChild(posting)


clear()
'''邮件系统'''
print("邮件系统")
email = doc.createElement("email")
sender = doc.createElement("sender")
sender.appendChild(doc.createTextNode(input("请输入邮件系统发送者姓名\n")))
subject = doc.createElement("subject")
subject.appendChild(doc.createTextNode(input("邮件主题\n")))
body = doc.createElement("body")
body.appendChild(doc.createTextNode(input("主文本，使用<br>换行\n")))
email.appendChild(sender)
email.appendChild(subject)
email.appendChild(body)
print("附件部分\n")
if(int(input("是否需要启动附件，不启用请输入0\n")) != 0):
    attachments = doc.createElement("attachments")
    var1 = 1
    while var1 == 1:
        judgeNum = int(input("""请选择需要添加的附件类型
        1——note便签
        2——link节点
        3——account账号\n"""))
        if(judgeNum == 1):
            note = doc.createElement("note")
            note.setAttribute("title", input("请输入创建的便签主题\n"))
            note.appendChild(doc.createTextNode(input("请输入创建的便签文本\n")))
            attachments.appendChild(note)
        elif(judgeNum == 2):
            link = doc.createElement("link")
            link.setAttribute("comp",input("请输入链接主机的id\n"))
            attachments.appendChild(link)
        elif(judgeNum == 3):
            account = doc.createElement("account")
            comp = input("请输入链接主机的id\n")
            user = input("请输入用户名\n")
            password = input("请输入密码\n")
            account.setAttribute("comp",comp)
            account.setAttribute("user",user)
            account.setAttribute("pass",password)
            attachments.appendChild(account)
        '''判断'''
        whileJudge = int(input("是否继续添加附件，如果继续添加请输入1，否则请输入任意字母\n"))
        if (whileJudge != 1):
            break
    email.appendChild(attachments)
else:
    attachments = doc.createElement("attachments")
    attachments.appendChild(doc.createTextNode(""))
    email.appendChild(attachments)
mission.appendChild(email)

filePrint = codecs.open(get_desktop()+"\\"+fileName+".xml","w","utf-8")
doc.writexml(filePrint, indent='\t', addindent='\t', newl='\n', encoding="utf-8")