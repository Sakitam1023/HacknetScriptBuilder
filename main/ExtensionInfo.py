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
doc = xml.dom.minidom.Document()

root = doc.createElement("HacknetExtension")
doc.appendChild(root)

clear()
'''设置语言'''
Language = doc.createElement("Language")
Language.appendChild(doc.createTextNode(input("""请设置你的语言
当前支持的列表:
 英语 : en-us
 德语 : de-de
 法语 : fr-be
 俄语 : ru-ru
 西班牙语 : es-ar
 朝鲜语 : ko-kr
 日本语 : ja-jp
 简体中文 : zh-cn\n""")))
root.appendChild(Language)

clear()
'''Mod名称'''
Name = doc.createElement("Name")
Name.appendChild(doc.createTextNode(input("请输入你的Mod名称\n")))
root.appendChild(Name)

clear()
'''允许存档'''
AllowSaves = doc.createElement("AllowSaves")
AllowSaves.appendChild(doc.createTextNode(input("请输入是否需要自动存档，输入true或false\n")))
root.appendChild(AllowSaves)

clear()
'''起始笔记'''
StartingVisibleNodes = doc.createElement("StartingVisibleNodes")
StartingVisibleNodes.appendChild(doc.createTextNode(input("请输入起始笔记，用逗号隔开，如果不需要笔记请输入空格\n")))
root.appendChild(StartingVisibleNodes)

clear()
'''起始任务'''
StartingMission = doc.createElement("StartingMission")
StartingMission.appendChild(doc.createTextNode(input("请输入一开始需要加载的任务（路径），需要.xml后缀\n")))
root.appendChild(StartingMission)

clear()
'''起始动作'''
StartingActions = doc.createElement("StartingActions")
StartingActions.appendChild(doc.createTextNode(input("请输入一开始需要加载的动作（路径），需要.xml后缀，如果不需要请输入NONE\n")))
root.appendChild(StartingActions)

clear()
'''起始描述'''
Description = doc.createElement("Description")
Description.appendChild(doc.createTextNode(input("请输入起始描述，建议输入空格后手动添加，因为无法换行，也可以自行标记后，手动换行\n")))
root.appendChild(Description)

clear()
'''起始派系'''
Faction = doc.createElement("Faction")
Faction.appendChild(doc.createTextNode(input("请输入起始派系（路径），可以为多个，第二个开始需要手动添加\n")))
root.appendChild(Faction)

clear()
'''伴随教程开启'''
StartsWithTutorial = doc.createElement("StartsWithTutorial")
StartsWithTutorial.appendChild(doc.createTextNode(input("是否需要伴随教程开启，输入true或false\n")))
root.appendChild(StartsWithTutorial)

clear()
'''是否需要扩展开启存档时伴随开机动画'''
HasIntroStartup = doc.createElement("HasIntroStartup")
HasIntroStartup.appendChild(doc.createTextNode(input("是否需要扩展开启存档时伴随开机动画，输入true或false\n")))
root.appendChild(HasIntroStartup)

clear()
'''起始主题'''
StartingTheme = doc.createElement("StartingTheme")
StartingTheme.appendChild(doc.createTextNode(input("""请输入起始主题路径，也可以输入以下名称
TerminalOnlyBlack——只有黑色的终端
HacknetBlue——蓝
HacknetTeal——深青
HacknetYellow——黄
HackerGreen——绿
HacknetWhite——白
HacknetPurple——紫
HacknetMint——薄荷\n""")))
root.appendChild(StartingTheme)

clear()
'''起始歌曲'''
IntroStartupSong = doc.createElement("IntroStartupSong")
IntroStartupSong.appendChild(doc.createTextNode(input("""请选择你的起始歌曲路径，也可以使用原版歌曲的名称，原创歌曲有以下路径
Content/Music
Content/DLC/Music\n""")))
root.appendChild(IntroStartupSong)

clear()
'''序列基准器'''
print("""序列基准器是一个像原版最后黑入离线服务器一样的软件，一个扩展只允许拥有一个
它会在你运行它之后，延迟一定的秒数，然后链接入目标计算机
并且在运行该软件之后，它会检测你的flag标记，并且开始执行action动作，再延迟一定的秒数
秒数结束之后，它会链接到目标计算机\n""")
SequencerTargetID = doc.createElement("SequencerTargetID")
SequencerSpinUpTime = doc.createElement("SequencerSpinUpTime")
SequencerFlagRequiredForStart = doc.createElement("SequencerFlagRequiredForStart")
ActionsToRunOnSequencerStart = doc.createElement("ActionsToRunOnSequencerStart")
SequencerTargetID.appendChild(doc.createTextNode(input("请选择目标的主机名称\n")))
SequencerSpinUpTime.appendChild(doc.createTextNode(input("请选择需要延迟的秒数，输入数字，可以带小数点，一位小数点\n")))
SequencerFlagRequiredForStart.appendChild(doc.createTextNode(input("开启所需的flag标记字符串\n")))
ActionsToRunOnSequencerStart.appendChild(doc.createTextNode(input("开启之后所执行的动作文件所在的路径，需要.xml后缀\n")))

clear()
'''创意工坊描述'''
WorkshopDescription = doc.createElement("WorkshopDescription")
WorkshopDescription.appendChild(doc.createTextNode(input("请键入此mod在steam创意工坊上的描述\n")))
root.appendChild(WorkshopDescription)

clear()
'''创意工坊语言'''
WorkshopLanguage = doc.createElement("WorkshopLanguage")
WorkshopLanguage.appendChild(doc.createTextNode("English"))
root.appendChild(WorkshopLanguage)

clear()
'''创意工坊模组可视性'''
WorkshopVisibility = doc.createElement("WorkshopVisibility")
WorkshopVisibility.appendChild(doc.createTextNode(input("""请输入该项目在Steam的可视性
 0 = 公众
 1 = 好友
 2 = 似有\n""")))
root.appendChild(WorkshopVisibility)

clear()
'''创意工坊标记'''
WorkshopTags = doc.createElement("WorkshopTags")
WorkshopTags.appendChild(doc.createTextNode("Extension"))
root.appendChild(WorkshopTags)

clear()
'''创意工坊模组Logo'''
WorkshopPreviewImagePath = doc.createElement("WorkshopPreviewImagePath")
WorkshopPreviewImagePath.appendChild(doc.createTextNode(input("""请输入Steam模组图标路径
该图标需要的后缀为.png/.jpg/.gif
并且像素比为1比1，大小小于1 MB
Steam最大支持的像素比为512*512，如果大于这个像素，它会自动帮你调节\m""")))
root.appendChild(WorkshopPreviewImagePath)

clear()
'''创意工坊ID号'''
WorkshopPublishID = doc.createElement("WorkshopPublishID")
WorkshopPublishID.appendChild(doc.createTextNode("NONE"))
root.appendChild(WorkshopPublishID)

filePrint = codecs.open(get_desktop()+"\\ExtensionInfo.xml","w","utf-8")
doc.writexml(filePrint, indent='\t', addindent='\t', newl='\n', encoding="utf-8")