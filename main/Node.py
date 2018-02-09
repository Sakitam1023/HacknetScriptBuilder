# -*- coding:utf-8 -*-
import xml.dom.minidom
import codecs
import os
import winreg

def clear():
    os.system("cls")

def get_desktop():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

clear()
'''文件创建相关'''
fileName = input("请输入文件名，不需要添加.xml后缀\n")

doc = xml.dom.minidom.Document()

clear()
'''电脑属性'''
id = input("电脑id——唯一标识，需要小本本记下来\n")
clear()
name = input("电脑名称——实际名称\n")
clear()
ip = input("电脑ip——如果需要随机生成ip，请输入none\n")
clear()
security = input("""电脑安全等级——他是一个从0到5的一个数字，表示攻击有多难
 建议为3，为5需要自定义下面的一些设置（如代理、端口、防火墙）——输入数字0~5\n""")
clear()
allowsDefaultBootModule = input("自动启动程序——当你连接到这个节点（电脑）时，会自动启动这个电脑的守护进程——输入1开启或0不开启\n")
clear()
icon = input("""节点图标——
 laptop 笔记本电脑
 chip 芯片
 kellis 硬币
 tablet 平板电脑
 ePhone 手机1
 ePhone2 手机2
 PacificAir 太平洋飞机
 Alchemist 生命之树
 DLCLaptop 笔记本电脑
 DLCPC1 主机1
 DLCPC2 主机2
 DLCServer DLC服务器\n""")
clear()
type = input("类型——输入1为企业类型，2为家庭类型，3为服务器，你也可以输入4让这个节点为空\n")
root = doc.createElement("Computer")
root.setAttribute('id', id)
root.setAttribute('name', name)
if(ip != "none"):
    root.setAttribute("ip", ip)
root.setAttribute('security', security)
if(int(allowsDefaultBootModule) == 0):
    root.setAttribute('allowsDefaultBootModule', "true")
else:
    root.setAttribute('allowsDefaultBootModule', "false")
root.setAttribute('icon', icon)
root.setAttribute('type', type)
doc.appendChild(root)

clear()
'''电脑密码'''
adminPassword = input("请输入管理员密码\n")
adminPasswordDom = doc.createElement("adminPass")
adminPasswordDom.setAttribute('pass',adminPassword)
root.appendChild(adminPasswordDom)

clear()
'''添加账号密码'''
accountJudge = int(input("是否要添加额外的账号密码，是输入1，否输入0\n"))
if(accountJudge == 1):
    accountNum = 1
    while accountNum == 1:
        '''本体'''
        userName = input("请输入用户名\n")
        passWord = input("请输入密码\n")
        type = input("""请输入权限类型
        0为admin权限
        1为可以删除文件的账户
        2为邮件账户
        3为任务列表服务器账户\n""")
        accountDom = doc.createElement("account")
        accountDom.setAttribute("username",userName)
        accountDom.setAttribute("password",passWord)
        accountDom.setAttribute("type",type)
        root.appendChild(accountDom)
        '''判断'''
        whileJudge = int(input("是否继续添加，如果继续添加请输入1，否则请输入任意字母\n"))
        if(whileJudge != 1):
            break

clear()
portsForPortRemap = 0
'''添加端口'''
portsJudge = int(input("是否添加额外端口，如果不需要更改端口，请输入0，会使用默认安全类型所提供的端口，添加输入非0任意\n"))
if(portsJudge != 0):
    ports = input("""输入形式：22, 23, 24, 25
    这样输入。用逗号隔开
    可选的端口21 = FTP
    22 = SSH
    25 = SMTP
    80 = Web / Http
    1433 = SQL
    104 = Medical
    6881 = Torrent
    443 = SSL
    192 = Pacific\n""")
    portsForPortRemap = ports
    portsDom = doc.createElement("ports")
    portsDom.appendChild(doc.createTextNode(ports))
    root.appendChild(portsDom)

clear()
'''添加代理服务器'''
proxyJudge = int(input("是否需要添加代理，不需要添加请输入0\n"))
if(proxyJudge == 0):
    proxyDom = doc.createElement("proxy")
    proxyDom.setAttribute("time","-1")
    root.appendChild(proxyDom)
else:
    proxy = input("代理服务器时间，里面的数字是30的倍数。1为1倍，也是正常值。2为2倍，是比较长的。\n")
    proxyDom = doc.createElement("proxy")
    proxyDom.setAttribute("time",proxy)
    root.appendChild(proxyDom)

clear()
'''使用PortHack所需的端口数'''
portsForCrack = input("请输入PortHack所需的端口数，可以为0\n")
portsForCrackDom = doc.createElement("portsForCrack")
portsForCrackDom.setAttribute("val",portsForCrack)
root.appendChild(portsForCrackDom)

clear()
'''防火墙'''
fireWallJudge = int(input("是否需要添加防火墙，不需要请输入0\n"))
if(fireWallJudge == 0):
    fireWallDom = doc.createElement("firewall")
    fireWallDom.setAttribute("level","-1")
    fireWallDom.setAttribute("solution","")
    fireWallDom.setAttribute("additionalTime","")
    root.appendChild(fireWallDom)
else:
    level = input("请输入复杂度，默认值为6\n")
    solution = input("请输入防火墙密码\n")
    additionalTime = input("请输入延迟扫描时间，一般没有特殊情况为1\n")
    fireWallDom = doc.createElement("firewall")
    fireWallDom.setAttribute("level", level)
    fireWallDom.setAttribute("solution", solution)
    fireWallDom.setAttribute("additionalTime", additionalTime)
    root.appendChild(fireWallDom)

clear()
'''添加倒数计时器'''
trace = input("请输入倒数计时器的秒数，输入-1取消该功能\n")
traceDom = doc.createElement("trace")
traceDom.setAttribute("time",trace)
root.appendChild(traceDom)

clear()
'''是否启用端口替换'''
portRemapJudge = int(input("是否启用端口替换，不需要请输入0，需要输入非0任意\n"))
if(portRemapJudge != 0):
    print("已经开放的端口为",portsForPortRemap)
    portRemap = input("请输入需要替换的端口，形式为：22=1234,21=8765\n")
    portRemapDom = doc.createElement("portRemap")
    portRemapDom.appendChild(doc.createTextNode(portRemap))
    root.appendChild(portRemapDom)

clear()
'''单向链接此计算机到其他计算机'''
dlinkJudge = int(input("是否需要单向链接此电脑到其他计算机，注意！单向！不需要请输入0\n"))
if(dlinkJudge != 0):
    dlinkNum = 1
    while dlinkNum == 1:
        target = input("请输入目标计算机的id\n")
        dlinkDom = doc.createElement("dlink")
        dlinkDom.setAttribute("target",target)
        root.appendChild(dlinkDom)
        '''判断'''
        whileJudge = int(input("是否继续添加，如果继续添加请输入1，否则请输入任意字母\n"))
        if (whileJudge != 1):
            break

clear()
'''计算机辐射性放置节点'''
positionNearJudge = int(input("是否需要开启计算机辐射性放置节点，不需要请输入0\n"))
if(positionNearJudge != 0):
    positionNearNum = 1
    while positionNearNum == 1:
        target = input("请输入目标计算机的id\n")
        position = input("position为这台计算机在总数里的编号\n")
        total = input("total为总数\n")
        extraDistance = input("extraDistance为额外距离，0.1是一个正常距离。在-0.6~0.3之间\n")
        positionNearDom = doc.createElement("positionNear")
        positionNearDom.setAttribute("target",target)
        positionNearDom.setAttribute("position",position)
        positionNearDom.setAttribute("total",total)
        positionNearDom.setAttribute("extraDistance",extraDistance)
        positionNearDom.setAttribute("force","false")
        root.appendChild(positionNearDom)
        '''判断'''
        whileJudge = int(input("是否继续添加，如果继续添加请输入1，否则请输入任意字母\n"))
        if (whileJudge != 1):
            break

clear()
'''文件系统'''
fileJudge = int(input("是否需要创建文件，不需要请输入0\n"))
if(fileJudge != 0):
    var1 = 1
    while var1 == 1:
        fileChoiceNum = int(input("""请输入你要生成的file类型
            0——普通文本
            1——特殊文本（例如二进制文本、随机IP地址、随机任命、主机电脑ip）
            2——软件类型
            3——特殊软件
            4——主题文件
            5——特殊文件
            6——自定义主题
            7——DLC软件\n"""))
        if(fileChoiceNum == 0):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = input("请输入名称\n")
                text = input("请输入文本\n")
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path",path)
                fileDom.setAttribute("name",name)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加普通文本，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 1):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = input("请输入名称\n")
                text = input("""请输入你需要的特殊文本
                1为随机2000个字符的二进制文件
                2为随机1000个字符的二进制文件
                3为电脑IP——#PLAYER_IP#
                4为玩家名称——#PLAYERNAME#
                5为随机IP——#RANDOM_IP#
                6为混合文本特殊文件
                注：3,4,5可以混在文本6中使用，但需要输入代替字\n""")
                if(int(text) == 1):
                    text = "#BINARY#"
                elif(int(text) == 2):
                    text = "#BINARYSMALL#"
                elif(int(text) == 3):
                    text = "#PLAYER_IP#"
                elif(int(text) == 4):
                    text = "#PLAYERNAME#"
                elif(int(text) == 5):
                    text = "#RANDOM_IP#"
                elif(int(text) == 6):
                    text = input("请输入混合文本\n")
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加特殊文本，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 2):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = 0
                text = input("""请输入需要的软件名称
                1——SSHCrack.exe
                2——FTPBounce.exe
                3——WebServerWorm.exe
                4——SMTPOverflow.exe
                5——SQLBufferOverflow.exe
                6——HexClock.exe
                7——Clock.exe
                8——Decypher.exe
                9——DECHead.exe
                10——KBTPortTest.exe
                11——ThemeChanger.exe
                12——eosDeviceScan.exe
                13——SecurityTracer.exe
                14——Tracekill.exe\n""")
                if(int(text) == 1):
                    name = "SSHCrack.exe"
                    text = "#SSH_CRACK#"
                elif (int(text) == 2):
                    name = "FTPBounce.exe"
                    text = "#FTP_CRACK#"
                elif (int(text) == 3):
                    name = "WebServerWorm.exe"
                    text = "#WEB_CRACK#"
                elif (int(text) == 4):
                    name = "SMTPOverflow.exe"
                    text = "#SMTP_CRACK#"
                elif (int(text) == 5):
                    name = "SQLBufferOverflow.exe"
                    text = "#SQL_CRACK#"
                elif (int(text) == 6):
                    name = "HexClock.exe"
                    text = "#HEXCLOCK_EXE#"
                elif (int(text) == 7):
                    name = "Clock.exe"
                    text = "#CLOCK_PROGRAM#"
                elif (int(text) == 8):
                    name = "Decypher.exe"
                    text = "#DECYPHER_PROGRAM#"
                elif (int(text) == 9):
                    name = "DECHead.exe"
                    text = "#DECHEAD_PROGRAM#"
                elif (int(text) == 10):
                    name = "KBTPortTest.exe"
                    text = "#MEDICAL_PROGRAM#"
                elif (int(text) == 11):
                    name = "ThemeChanger.exe"
                    text = "#THEMECHANGER_EXE#"
                elif (int(text) == 12):
                    name = "eosDeviceScan.exe"
                    text = "#EOS_SCANNER_EXE#"
                elif (int(text) == 13):
                    name = "SecurityTracer.exe"
                    text = "#SECURITYTRACER_PROGRAM#"
                elif (int(text) == 14):
                    name = "Tracekill.exe"
                    text = "#TRACEKILL_EXE#"
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加普通软件，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 3):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = 0
                text = input("""请输入需要的软件名称
                                1——RTSPCrack.exe
                                2——ESequencer.exe
                                3——OpShell.exe\n""")
                if (int(text) == 1):
                    name = "RTSPCrack.exe"
                    text = "#RTSP_EXE#"
                elif (int(text) == 2):
                    name = "ESequencer.exe"
                    text = "#EXT_SEQUENCER_EXE#"
                elif (int(text) == 3):
                    name = "OpShell.exe"
                    text = "#SHELL_OPENER_EXE#"
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加特殊软件，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 4):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = 0
                text = input("""请输入需要的主题名称
                                                1——White-Theme.sys
                                                2——Green-Theme.sys
                                                3——Yellow-Theme.sys
                                                4——Teal-Theme.sys
                                                5——Base-Theme.sys
                                                6——LE-Theme.sys
                                                7——Mint-Theme.sys\n""")
                if (int(text) == 1):
                    name = "White-Theme.sys"
                    text = "#WHITE_THEME#"
                elif (int(text) == 2):
                    name = "Green-Theme.sys"
                    text = "#GREEN_THEME#"
                elif (int(text) == 3):
                    name = "Yellow-Theme.sys"
                    text = "#YELLOW_THEME#"
                elif (int(text) == 4):
                    name = "Teal-Theme.sys"
                    text = "#TEAL_THEME#"
                elif (int(text) == 5):
                    name = "Base-Theme.sys"
                    text = "#BASE_THEME#"
                elif (int(text) == 6):
                    name = "LE-Theme.sys"
                    text = "#PURPLE_THEME#"
                elif (int(text) == 7):
                    name = "Mint-Theme.sys"
                    text = "#MINT_THEME#"
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加主题文件，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 5):
            var2 = 1
            while var2 == 1:
                fileChoiceChildNum = int(input("""请输入需要制作的特殊文件
                1——完整的dec文件
                2——dec头文件
                3——内存文件\n"""))
                if(fileChoiceChildNum == 1):
                    path = input("请输入路径，可以使用/进入下级目录\n")
                    name = input("文件名称，需要输入.dec后缀\n")
                    extension = input("解码后的后缀，例：.txt\n")
                    ip = input("输入解码后的ip\n")
                    header = input("头文件显示的文本\n")
                    password = input("解码密码\n")
                    text = input("解码后的文本，用\\n分行\n")
                    fileDom = doc.createElement("encryptedFile")
                    fileDom.appendChild(doc.createTextNode(text))
                    fileDom.setAttribute("path",path)
                    fileDom.setAttribute("name",name)
                    fileDom.setAttribute("extension",extension)
                    fileDom.setAttribute("ip",ip)
                    fileDom.setAttribute("header",header)
                    fileDom.setAttribute("pass",password)
                    root.appendChild(fileDom)
                elif(fileChoiceChildNum == 2):
                    path = input("请输入路径，可以使用/进入下级目录\n")
                    name = input("文件名称，需要输入.dec后缀\n")
                    ip = input("输入解码后的ip\n")
                    header = input("头文件显示的文本\n")
                    text = input("解码后的文本，用\\n分行\n")
                    fileDom = doc.createElement("encryptedFile")
                    fileDom.appendChild(doc.createTextNode(text))
                    fileDom.setAttribute("path", path)
                    fileDom.setAttribute("name", name)
                    fileDom.setAttribute("ip", ip)
                    fileDom.setAttribute("header", header)
                    root.appendChild(fileDom)
                elif(fileChoiceChildNum == 3):
                    path = input("请输入路径，可以使用/进入下级目录\n")
                    name = input("文件名称，需要输入.md后缀\n")
                    fileDom = doc.createElement("memoryDumpFile")
                    fileDom.setAttribute("name",name)
                    fileDom.setAttribute("path",path)
                    memory = doc.createElement("Memory")
                    data = doc.createElement("Data")
                    data.appendChild(doc.createTextNode(""))
                    commands = doc.createElement("Commands")
                    commands.appendChild(doc.createTextNode(""))
                    images = doc.createElement("Images")
                    images.appendChild(doc.createTextNode(""))
                    judge = int(input("""请键入需要创建的内存类型
                    1——文本
                    2——命令
                    3——图片（需要xnb文件，不需要添加后缀）\n"""))
                    if(judge == 1):
                        var3 = 1
                        while var3 == 1:
                            text = input("请输入文本\n")
                            block = doc.createElement("Block")
                            block.appendChild(doc.createTextNode(text))
                            data.appendChild(block)
                            '''判断'''
                            whileJudge = int(input("是否继续添加内存内的文本，如果继续添加请输入1，否则请输入任意字母\n"))
                            if (whileJudge != 1):
                                break
                    elif(judge == 2):
                        var3 = 1
                        while var3 == 1:
                            text = input("请输入命令\n")
                            command = doc.createElement("Command")
                            command.appendChild(doc.createTextNode(text))
                            commands.appendChild(command)
                            '''判断'''
                            whileJudge = int(input("是否继续添加内存内的命令，如果继续添加请输入1，否则请输入任意字母\n"))
                            if (whileJudge != 1):
                                break
                    elif(judge == 3):
                        var3 = 1
                        while var3 == 1:
                            text = input("请输入图片路径，相对于extension，例：Misc/Demo，注：需要xnb文件\n")
                            image = doc.createElement("Images")
                            image.appendChild(doc.createTextNode(text))
                            '''判断'''
                            whileJudge = int(input("是否继续添加内存内的图片，如果继续添加请输入1，否则请输入任意字母\n"))
                            if (whileJudge != 1):
                                break
                    memory.appendChild(data)
                    memory.appendChild(commands)
                    memory.appendChild(images)
                    fileDom.appendChild(memory)
                    root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加特殊文件，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 6):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = input("请输入自定义主题名称\n")
                themePath = input("请输入相对于Extension根目录下的目录。例：Themes/YuriTheme.xml\n")
                fileDom = doc.createElement("customthemefile")
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                fileDom.setAttribute("themePath", themePath)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加自定义主题，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif(fileChoiceNum == 7):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = 0
                text = input("""请输入需要的DLC软件名称
                            1——TorrentStreamInjector.exe
                            2——SSLTrojan.exe
                            3——FTPSprint.exe
                            4——SignalScramble.exe
                            5——MemForensics.exe
                            6——MemDumpGenerator.exe
                            7——PacificPortcrusher.exe
                            8——NetmapOrganizer.exe
                            9——ComShell.exe
                            10——DNotes.exe
                            11——Tuneswap.exe
                            12——Clockv2.exe\n""")
                if (int(text) == 1):
                    name = "TorrentStreamInjector.exe"
                    text = "#TORRENT_EXE#"
                elif (int(text) == 2):
                    name = "SSLTrojan.exe"
                    text = "#SSL_EXE#"
                elif (int(text) == 3):
                    name = "FTPSprint.exe"
                    text = "#FTP_FAST_EXE#"
                elif (int(text) == 4):
                    name = "SignalScramble.exe"
                    text = "#SIGNAL_SCRAMBLER_EXE#"
                elif (int(text) == 5):
                    name = "MemForensics.exe"
                    text = "#MEM_FORENSICS_EXE#"
                elif (int(text) == 6):
                    name = "MemDumpGenerator.exe"
                    text = "#MEM_DUMP_GENERATOR#"
                elif (int(text) == 7):
                    name = "PacificPortcrusher.exe"
                    text = "#PACIFIC_EXE#"
                elif (int(text) == 8):
                    name = "NetmapOrganizer.exe"
                    text = "#NETMAP_ORGANIZER_EXE#"
                elif (int(text) == 9):
                    name = "ComShell.exe"
                    text = "#SHELL_CONTROLLER_EXE#"
                elif (int(text) == 10):
                    name = "DNotes.exe"
                    text = "#NOTES_DUMPER_EXE#"
                elif (int(text) == 11):
                    name = "Tuneswap.exe"
                    text = "#DLC_MUSIC_EXE#"
                elif (int(text) == 12):
                    name = "Clockv2.exe"
                    text = "#CLOCK_V2_EXE#"
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                root.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加DLC软件，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        '''判断'''
        whileJudge = int(input("是否继续添加文件，如果继续添加请输入1，否则请输入任意字母\n"))
        if (whileJudge != 1):
            break

clear()
'''eOS手机驱动器'''
eOSJudge = int(input("是否要添加手机驱动器，不需要请输入0\n"))
if(eOSJudge != 0):
    id = input("请输入手机id，唯一识别\n")
    name = input("请输入名称\n")
    icon = input("""请输入图标
    ePhone 手机1
    ePhone2 手机2\n""")
    empty = input("是否要让手机内为空——输入true或false，建议false，增加游戏难度\n")
    passOverride = input("手机密码，使用默认密码请输入0\n")
    if(int(passOverride) == 0):
        passOverride = "alpine"
    eOSDom = doc.createElement("eosDevice")
    eOSDom.setAttribute("id",id)
    eOSDom.setAttribute("name",name)
    eOSDom.setAttribute("icon",icon)
    eOSDom.setAttribute("empty",empty)
    eOSDom.setAttribute("passOverride",passOverride)
    var1 = 1
    while var1 == 1:
        judge = int(input("""是否需要创建文件，并且选择文件类型
            0——不创建
            1——note类型
            2——mail类型
            3——文件类型\n"""))
        if (judge == 0):
            eOSDom.appendChild(doc.createTextNode(""))
        elif (judge == 1):
            var2 = 1
            while var2 == 1:
                text = input("请输入note文本\n")
                note = doc.createElement("note")
                note.appendChild(doc.createTextNode(text))
                eOSDom.appendChild(note)
                '''判断'''
                whileJudge = int(input("是否继续添加手机记事本类型，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif (judge == 2):
            var2 = 1
            while var2 == 1:
                username = input("请输入来源邮件地址（对方邮箱）\n")
                password = input("对方邮箱密码\n")
                mail = doc.createElement("mail")
                mail.setAttribute("username", username)
                mail.setAttribute("pass", password)
                eOSDom.appendChild(mail)
                '''判断'''
                whileJudge = int(input("是否继续添加mail类型，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        elif (judge == 3):
            var2 = 1
            while var2 == 1:
                path = input("请输入路径，可以使用/进入下级目录\n")
                name = input("请输入名称\n")
                text = input("请输入文本\n")
                fileDom = doc.createElement("file")
                fileDom.appendChild(doc.createTextNode(text))
                fileDom.setAttribute("path", path)
                fileDom.setAttribute("name", name)
                eOSDom.appendChild(fileDom)
                '''判断'''
                whileJudge = int(input("是否继续添加文件类型，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
        '''判断'''
        whileJudge = int(input("是否继续添加手机文件（输入完会继续进入3选1环节），如果继续添加请输入1，否则请输入任意字母\n"))
        if (whileJudge != 1):
            break
    root.appendChild(eOSDom)

clear()
'''守护进程'''
judgeA = int(input("是否要开启守护进程，不开启请输入0，否则请输入任意字母\n"))
if(judge != 0):
    var1 = 1
    while var1 == 1:
        judgeB = int(input("""请选择需要开启的守护进程
1——邮件服务器
2——上传服务器
3——Web服务器
4——在线Web服务器
5——死亡人员数据库
6——学术系统数据库
7——ISP系统
8——留言板服务器
9——医疗系统数据库
10——心脏起搏器
11——鼠标点击游戏
12——歌曲变换服务器
13——像新闻或Entropy任务系统一样的服务器
14——任务中心
15——DLC守护进程\n"""))
        if(judgeB == 1):
            mailServer = doc.createElement("mailServer")
            mailServer.setAttribute("name",input("请输入邮件服务器的名称\n"))
            mailServer.setAttribute("color",input("请输入邮件服务器颜色配置，使用RGB，例：16,25,38，例2：215,234,123\n"))
            mailServer.setAttribute("generateJunk",input("是否需要生成垃圾邮件，输入true或false\n"))
            judgeC = int(input("是否需要在该邮件服务器内手动添加邮件，不需要请输入0\n"))
            if(judgeC != 0):
                var2 = 1
                while var2 == 1:
                    email = doc.createElement("email")
                    email.setAttribute("recipient",input("请输入接收人的account账号名称\n"))
                    email.setAttribute("sender",input("请输入发送人的名称\n"))
                    email.setAttribute("subject",input("请输入邮件主题\n"))
                    email.appendChild(doc.createTextNode(input("请输入邮件文本\n")))
                    mailServer.appendChild(email)
                    '''判断'''
                    whileJudge = int(input("是否继续添加邮件，如果继续添加请输入1，否则请输入任意字母\n"))
                    if (whileJudge != 1):
                        break
            elif(judgeC == 0):
                mailServer.appendChild(doc.createTextNode(""))
            root.appendChild(mailServer)
        elif(judgeB == 2):
            uploadServerDaemon = doc.createElement("uploadServerDaemon")
            uploadServerDaemon.setAttribute("name",input("请输入上传服务器的名称\n"))
            uploadServerDaemon.setAttribute("folder",input("请输入默认的上传文件所在的文件夹，例：Drop\n"))
            uploadServerDaemon.setAttribute("needsAuth",input("是否需要登录就能上传文件，输入true或false\n"))
            uploadServerDaemon.setAttribute("color",input("请输入上传服务器颜色配置，使用RGB，例：16,25,38，例2：215,234,123\n"))
            root.appendChild(uploadServerDaemon)
        elif(judgeB == 3):
            addWebServer = doc.createElement("addWebServer")
            addWebServer.setAttribute("name",input("请输入Web服务器的名称\n"))
            addWebServer.setAttribute("url",input("请输入Web服务器所用的html文件地址，例：Web/Example/Demo.html\n"))
            root.appendChild(addWebServer)
        elif(judgeB == 4):
            addOnlineWebServer = doc.createElement("addOnlineWebServer")
            addOnlineWebServer.setAttribute("name",input("请输入Web服务器的名称\n"))
            addOnlineWebServer.setAttribute("url",input("请输入在线网址的地址，例：http://www.baidu.com\n"))
            root.appendChild(addOnlineWebServer)
        elif(judgeB == 5):
            deathRowDatabase = doc.createElement("deathRowDatabase")
            root.appendChild(deathRowDatabase)
        elif(judgeB == 6):
            academicDatabase = doc.createElement("academicDatabase")
            root.appendChild(academicDatabase)
        elif(judgeB == 7):
            ispSystem = doc.createElement("ispSystem")
            root.appendChild(ispSystem)
        elif(judgeB == 8):
            messageBoard = doc.createElement("messageBoard")
            messageBoard.setAttribute("name",input("请输入留言板名称\n"))
            var2 = 1
            while var2 == 1:
                thread = doc.createElement("thread")
                thread.appendChild(doc.createTextNode(input("请输入留言板内内容的地址，例：Docs/MessageBoard/Demo.txt\n")))
                messageBoard.appendChild(thread)
                '''判断'''
                whileJudge = int(input("是否继续添加其他留言板内容，如果继续添加请输入1，否则请输入任意字母\n"))
                if (whileJudge != 1):
                    break
            root.appendChild(messageBoard)
        elif(judgeB == 9):
            MedicalDatabase = doc.createElement("MedicalDatabase")
            root.appendChild(MedicalDatabase)
        elif(judgeB == 10):
            HeartMonitor = doc.createElement("HeartMonitor")
            HeartMonitor.setAttribute("patient",input("请输入心脏起搏器主人名称\n"))
            root.appendChild(HeartMonitor)
        elif(judgeB == 11):
            PointClicker = doc.createElement("PointClicker")
            root.appendChild(PointClicker)
        elif(judgeB == 12):
            SongChangerDaemon = doc.createElement("SongChangerDaemon")
            root.appendChild(SongChangerDaemon)
        elif(judgeB == 13):
            variableMissionListingServer = doc.createElement("variableMissionListingServer")
            variableMissionListingServer.setAttribute("name",input("请输入服务器名称\n"))
            variableMissionListingServer.setAttribute("iconPath",input("请输入图标路径，相对extension\n"))
            variableMissionListingServer.setAttribute("articleFolderPath",input("请输入任务文件夹路径，如Docs/ListingServerFolder\n"))
            variableMissionListingServer.setAttribute("color",input("请输入上传服务器颜色配置，使用RGB，例：16,25,38，例2：215,234,123\n"))
            variableMissionListingServer.setAttribute("assigner","false")
            variableMissionListingServer.setAttribute("public","false")
            variableMissionListingServer.setAttribute("title",input("主题文本\n"))
            root.appendChild(variableMissionListingServer)
        elif(judgeB == 14):
            missionHubServer = doc.createElement("missionHubServer")
            missionHubServer.setAttribute("groupName",input("请输入组名称\n"))
            missionHubServer.setAttribute("serviceName",input("请输入服务器名称\n"))
            missionHubServer.setAttribute("missionFolderPath",input("请输入任务文件夹，例：Missions/Misc\n"))
            missionHubServer.setAttribute("themeColor",input("请输入上传服务器主题颜色配置，使用RGB，例：16,25,38，例2：215,234,123\n"))
            missionHubServer.setAttribute("lineColor", input("请输入上传服务器线条颜色配置，使用RGB，例：16,25,38，例2：215,234,123\n"))
            missionHubServer.setAttribute("backgroundColor", input("请输入上传服务器背景颜色配置，使用RGB，例：16,25,38，例2：215,234,123\n"))
            missionHubServer.setAttribute("allowAbandon", input("是否允许放弃任务，输入true或false\n"))
            root.appendChild(missionHubServer)
        elif(judgeB == 15):
            clear()
            judgeC = int(input("""请选择需要开启的DLC守护进程
            0——主机首页排列方式为DLC的排列方式（具体自行测试）
            1——在服务器前面显示一个大标志，下面显示可选的信息。如果您不提供图像路径，它将显示一个随机的加载（不提供生成方法）
            2——自定义链接显示屏上带有名牌和标题的图形，如PacificAir图标（不提供生成方法）
            3——这是您的基本白名单服务器“主机”类型，它不会根据其列表检查到本身的传入链接，只是对它连接到的其他计算机提供保护
            4——这是您的基本白名单服务器，它只针对您在标记里提供的计算机设置去保护远程主机，通常不需要它与被保护主机连接，并且通常只保护一个服务器
            5——这是您的基本白名单服务器，它会根据其列表检查到本身的传入链接，并且对它连接到的其他计算机提供保护
            6——IRC（聊天服务器）
            7——DLC（带任务板的聊天服务器，需要使用action注入消息）
            8——浏览记录数据库（不提供生成方法）\n"""))
            if(judgeC == 0):
                root.appendChild(doc.createElement("CustomConnectDisplayDaemon"))
            elif(judgeC == 3):
                Whitelist = doc.createElement("WhitelistAuthenticatorDaemon")
                Whitelist.setAttribute("SelfAuthenticating","false")
                root.appendChild(Whitelist)
            elif(judgeC == 4):
                Whitelist = doc.createElement("WhitelistAuthenticatorDaemon")
                Whitelist.setAttribute("Remote",input("请输入需要保护的计算机的id\n"))
                root.appendChild(Whitelist)
            elif(judgeC == 5):
                Whitelist = doc.createElement("WhitelistAuthenticatorDaemon")
                Whitelist.setAttribute("SelfAuthenticating", "true")
                root.appendChild(Whitelist)
            elif(judgeC == 6):
                IRC = doc.createElement("IRCDaemon")
                IRC.setAttribute("themeColor",input("请输入主题颜色，RGB颜色，例：123,123,123\n"))
                IRC.setAttribute("name",input("请输入名称\n"))
                IRC.setAttribute("needsLogin",input("是否需要登录，输入true或false\n"))
                var2 = 1
                while var2 == 1:
                    user = doc.createElement("user")
                    user.setAttribute("name",input("请输入需要添加的用户的名称\n"))
                    user.setAttribute("color",input("请输入用户的RGB颜色，例：123,123,123"))
                    IRC.appendChild(user)
                    '''判断'''
                    whileJudge = int(input("是否继续添加其他用户，如果继续添加请输入1，否则请输入任意字母\n"))
                    if (whileJudge != 1):
                        break
                judgeD = int(input("是否需要添加对话，不需要请输入0\n"))
                if(judgeD != 0):
                    while var2 == 1:
                        post = doc.createElement("post")
                        post.setAttribute("user", input("请输入说话的人名，使用上面添加的人名\n"))
                        post.appendChild(doc.createTextNode(input("请输入说话的文本\n")))
                        IRC.appendChild(post)
                        '''判断'''
                        whileJudge = int(input("是否继续添加其他对话，如果继续添加请输入1，否则请输入任意字母\n"))
                        if (whileJudge != 1):
                            break
                root.appendChild(IRC)
            elif(judgeC == 7):
                DHS = doc.createElement("DHSDaemon")
                DHS.setAttribute("groupName",input("请输入DHS服务器组名称\n"))
                DHS.setAttribute("addsFactionPointOnMissionComplete","true")
                DHS.setAttribute("autoClearMissionsOnPlayerComplete","true")
                DHS.setAttribute("themoColor",input("请输入RGB主题配色，例：111,111,111\n"))
                DHS.setAttribute("allowContractAbbandon","false")
                var2 = 1
                while var2 == 1:
                    agent = doc.createElement("agent")
                    agent.setAttribute("name",input("请输入用户名称\n"))
                    agent.setAttribute("pass",input("请输入用户密码\n"))
                    agent.setAttribute("color",input("请输入用户颜色RGB配色\n"))
                    DHS.appendChild(agent)
                    '''判断'''
                    whileJudge = int(input("是否继续添加其他用户，如果继续添加请输入1，否则请输入任意字母\n"))
                    if (whileJudge != 1):
                        break
                root.appendChild(DHS)
        '''判断'''
        whileJudge = int(input("是否继续添加其他进程，如果继续添加请输入1，否则请输入任意字母\n"))
        if (whileJudge != 1):
            break
        clear()

filePrint = codecs.open(get_desktop()+"\\"+fileName+".xml","w","utf-8")
doc.writexml(filePrint, indent='\t', addindent='\t', newl='\n', encoding="utf-8")