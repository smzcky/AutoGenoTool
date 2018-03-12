# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 08:24:41 2018

@author: shizhikai
工具名称：代码生成小工具

版本：1.0

功能：生成 App_Com.c、CanSys.if.h、CanSys_SigAccess.c、CanSys_SigAccess.h文件中需要手工配置的格式重复的
      接口及枚举类型

"""

from tkinter import *


#for GUI function
#information
def error_info1():
    import tkinter.messagebox as msg
    msg.showinfo(title = "错误提示", message = "请选择文件！")
def error_info2():
    import tkinter.messagebox as msg
    msg.showinfo(title = "失败", message = "请确认文件段首名称及位置是否正确！")
def author_info():
    import tkinter.messagebox as msg
    msg.showinfo(title = "作者",
                 message = "Zhikai.Shi\nNo copyright!")
def version_info():
    import tkinter.messagebox as msg
    msg.showinfo(title = "版本",
                 message = "Version 1.0\nWelcome to perfect it with me!")
def success_info():
    import tkinter.messagebox as msg
    msg.showinfo(title = "",
                 message = "success!")
#choose file function
def get_file(Event):
    import tkinter.filedialog
    global Filename
    global Filepath
    #get filename
    Filepath = tkinter.filedialog.askopenfilename()
    root.title('代码生成小工具'+'('+Filepath+')')
    #get filepath
    index = Filepath.rfind('/')
    Filename = Filepath[ : index+1]
    #display filepath
    Var.set(Filepath)
    
    
#data processing function
#get initial data
def Init_Data():
    try:
        global Filepath
        dataFile = open(Filepath, 'r')
        initData = []
        for line in dataFile.readlines():
            if line != '\n' :
                initData.append(line)
        dataFile.close()
        return initData
    except FileNotFoundError:
        raise
def List_Data():
    global DataSeg
    global Tx_MsgName
    global Tx_SigName
    global Rx_MsgName
    global Rx_SigName
    global DataList
    try:
        txMsgId = DataList.index(DataSeg[0])
        txSigId = DataList.index(DataSeg[1])
        rxMsgId = DataList.index(DataSeg[2])
        rxSigId = DataList.index(DataSeg[3])
        Tx_MsgName = DataList[txMsgId + 1 : txSigId]
        Tx_SigName = DataList[txSigId + 1 : rxMsgId]
        Rx_MsgName = DataList[rxMsgId + 1 : rxSigId]
        Rx_SigName = DataList[rxSigId + 1 :]
    except ValueError:
        raise
    return

#format the grouped data
def Format_Data():
    global Tx_MsgName
    global Tx_SigName
    global Rx_MsgName
    global Rx_SigName
    tx_MsgName_Buf = []
    tx_SigName_Buf = []
    rx_MsgName_Buf = []
    rx_SigName_Buf = []
    try:
        for list1 in Tx_MsgName:
            buf = list1.split(' ')
            id1 = buf[1].index('U')
            tx_MsgName_Buf.append(buf[1][id1 + 1 : ])
        for list2 in Tx_SigName:
            if list2[0] != '/':
                buf = list2.split(' ')
                id2 = buf[1].index('G')
                tx_SigName_Buf.append(buf[1][id2 +1 :])
            else:
                length = len(list2)
                list2 = list2[: length - 1]
                tx_SigName_Buf.append(list2)
        for list3 in Rx_MsgName:
            buf = list3.split(' ')
            id3 = buf[1].index('U')
            rx_MsgName_Buf.append(buf[1][id3 + 1 : ])
        for list4 in Rx_SigName:
            if list4[0] != '/':
                buf = list4.split(' ')
                id4 = buf[1].index('G')
                rx_SigName_Buf.append(buf[1][id4 +1 :])
            else:
                length = len(list4)
                list4 = list4[: length - 1]
                rx_SigName_Buf.append(list4)
    except ValueError:
        raise
        return
    Tx_MsgName = tx_MsgName_Buf
    Tx_SigName = tx_SigName_Buf
    Rx_MsgName = rx_MsgName_Buf
    Rx_SigName = rx_SigName_Buf
    return
         
#create CanSys_SigAccess file
def Geno_SigAccessFile():
    global Tx_SigName 
    global Rx_SigName
    global Filename
    file_H = open(Filename + 'CanSys_SigAccess.h', 'w+')
    file_C = open(Filename + 'CanSys_SigAccess.c', 'w+')
    
    #create CanSys_SigAccess.h
    buf = '/*****************************************************************************\n' + '\
* CAN signal send interfaces\n' + '\
*****************************************************************************/\n'
    file_H.write(buf)
    file_H.write('\n')
    file_H.write('\n')
    for code in Tx_SigName:
        if code[0] != '/':
            buf = 'void CanSig_vSend' + code + '(uint8 sigValue);\n'
            file_H.write(buf)
        else:
            file_H.write('\n')
            file_H.write(code + '\n')
    file_H.write('\n')
    file_H.write('\n')
    file_H.write('\n')
    buf = '/*****************************************************************************\n' + '\
* CAN signal read interfaces\n' + '\
*****************************************************************************/\n'
    file_H.write(buf)
    file_H.write('\n')
    file_H.write('\n')
    for code in Rx_SigName:
        if code[0] != '/':
            buf = 'uint8 CanSig_u8Rd' + code + '(void);\n'
            file_H.write(buf)
        else:
            file_H.write('\n')
            file_H.write(code + '\n')

    #create CanSys_SigAccess.c
    buf = '/*****************************************************************************\n' + '\
* CAN signal send interfaces\n' + '\
*****************************************************************************/\n'
    file_C.write(buf)
    file_C.write('\n')
    file_C.write('\n')
    for code in Tx_SigName:
        if code[0] != '/':
            buf = 'void CanSig_vSend' + code + '(uint8 sigValue)\n' + '{\n' + '\
    uint8 value = sigValue;\n' + '    (void) Com_SendSignal(COM_TXSIG' + code + ', &value);\n' + '}\n' 
            file_C.write(buf)
        else:
            file_C.write('\n')
            file_C.write(code + '\n')
    file_C.write('\n')
    file_C.write('\n')
    file_C.write('\n')
    buf = '/*****************************************************************************\n' + '\
* CAN signal read interfaces\n' + '\
*****************************************************************************/\n'
    file_C.write(buf)
    file_C.write('\n')
    file_C.write('\n')
    for code in Rx_SigName:
        if code[0] != '/':
            buf = 'uint8 CanSig_u8Rd' + code + '(void)\n' + '{\n' + '\
	uint8 sigValue = 0;\n' + '   	(void) Com_ReceiveSignal(COM_RXSIG' + code + ', &sigValue);\n' + '\
	return sigValue;\n' + '}\n'
            file_C.write(buf)
        else:
            file_C.write('\n')
            file_C.write(code + '\n')
            
    #close file
    file_H.close()
    file_C.close()
    return

#create CanSys.if.h file
def Geno_CanSysIfFile():
    global Rx_MsgName
    global Filename
    file_H = open(Filename + 'CanSys.if.h', 'w+')
    for code in Rx_MsgName:
        buf = 'CanSys_nen' + code + ',\n'
        file_H.write(buf)
    buf = 'CanSys_nenNumOfRevMsg,\n'
    file_H.write(buf)
    file_H.close()
    return

#create App_Com.c file
def Geno_AppComFile():
    global Tx_MsgName
    global Rx_MsgName
    global Filename
    file_C = open(Filename + 'App_Com.c', 'w+')
    buf = '/*****************************************************************************\n' + '\
* Tx confirmation callback\n' + '\
*****************************************************************************/\n'
    file_C.write(buf)
    file_C.write('\n')
    file_C.write('\n')
    for code in Tx_MsgName:
        buf = 'void AppIpdu' + code + '_Conf(void)\n' + '{\n\n}\n\n' 
        file_C.write(buf)
    buf = '/*****************************************************************************\n' + '\
* rx indication callback\n' + '\
*****************************************************************************/\n'
    file_C.write(buf)
    file_C.write('\n')
    file_C.write('\n')
    for code in Rx_MsgName:
        buf = 'void AppIpdu' + code + '_Ind(void)\n' + '{\n' + '\
    uint8 u8ByteIndex = 0;\n' + '    uint8 u8BitIndex = 0;\n' +'\
    u8ByteIndex = (uint8)(CanSys_nen' + code + '>> CanSys_nArrFactor);\n' + '\
    u8BitIndex = (uint8)(CanSys_nen' + code + '% CanSys_nArrBitSize);\n' + '\
    /* clear timeout Flag */\n' + '\
    CanSys__au16RxIpduTimeOutFlag[u8ByteIndex] &= (uint16)(~(1 << u8BitIndex));\n' + '\
    /* set first value flag */\n' + '    CanSys__au16RxIpduFvFlag[u8ByteIndex] |= (uint16)(1 << u8BitIndex);\n' + '}\n\n'
        file_C.write(buf)
    file_C.write('\n')
    file_C.write('\n')
    buf = '/*****************************************************************************\n' + '\
* Timeout callback\n' + '\
*****************************************************************************/\n' 
    file_C.write(buf)
    file_C.write('\n')
    file_C.write('\n')
    for code in Rx_MsgName:
        buf = 'void AppRxIpdu' + code + '_TimeOutInd(void)\n' + '{\n' + '\
    uint8 u8ByteIndex = 0;\n' + '    uint8 u8BitIndex = 0;\n' +'\
    u8ByteIndex = (uint8)(CanSys_nen' + code + '>> CanSys_nArrFactor);\n' + '\
    u8BitIndex = (uint8)(CanSys_nen' + code + '% CanSys_nArrBitSize);\n' + '\
    /* set timeout Flag */\n' + '    CanSys__au16RxIpduTimeOutFlag[u8ByteIndex] |= (uint16)(1 << u8BitIndex);\n' + '}\n\n'
        file_C.write(buf)
    return

#click button
def Click(Event):
    import os
    global Filename
    global DataList
    try:
        DataList = Init_Data()
        List_Data()
        Format_Data()
        Geno_SigAccessFile()
        Geno_CanSysIfFile()
        Geno_AppComFile()
        success_info()
        path = Filename.replace('/', '\\')
        os.system("explorer.exe %s" %path)
    except ValueError:
        error_info2()
        return
    except FileNotFoundError:
        error_info1()
        return

    
    
#declare Global Value
global Filename    
global DataSeg
global Tx_MsgName
global Tx_SigName
global Rx_MsgName
global Rx_SigName
global DataList
global Filepath
#initial Global Value  
DataSeg = ['DATASEG_Tx_Message\n', 'DATASEG_Tx_Signal\n', 'DATASEG_Rx_Message\n', 'DATASEG_Rx_Signal\n']
Tx_MsgName = []
Tx_SigName = []
Rx_MsgName = []
Rx_SigName = []
Filename = ''
Filepath = ''


#GUI
#creat the mainframe window
root = Tk()
#set title
root.wm_title("代码生成小工具")
#set window's size
root.geometry('300x80+150+200')
#set icon
root.iconbitmap('logo.ico')
menubar = Menu(root)
aboutmenu = Menu(menubar)
aboutmenu.add_command(label = '作者', command = author_info)
aboutmenu.add_command(label = '版本信息', command = version_info)
menubar.add_cascade(label = '关于', menu = aboutmenu)
root.config(menu = menubar)
Var = StringVar()
#add wdiget
l1 = Label(root, text = '文件')
e1 = Entry(root, textvariable = Var)
b1 = Button(root, text = '选择文件')
#add button click event
b1.bind("<Button-1>",get_file)
b2 = Button(root, text = 'start')
#add button click event
b2.bind("<Button-1>", Click)
#widget layout
l1.grid(row = 1, column = 0)
e1.grid(row = 1, column = 1)
b1.grid(row = 1, column = 2)
b2.grid(row = 1, column = 3)



root.mainloop()

