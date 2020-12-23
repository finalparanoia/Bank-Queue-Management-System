import os
import time
def get_op():
    global port_normal,port_vip,normal_num,vip_num,port_vip_status,port_normal_status,pos_dict
    #定义全局变量，用来切换客户和工作人员窗口时数据能同步更新。
    #port_normal,port_vip表示对应业务的排队名单
    #pos_dict  是整个数据存储的字典
    while True:
        print("""
             \033[5;32;40m银行排队叫号系统\033[0m
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃    1. 普通服务\t\t    ┃
    ┃    2. VIP服务\t\t    ┃
    ┃    3. 用户评价\t\t    ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        id = eval(input("     \033[1;34;40m请选择业务类型: [  ]\b\b\b\033[0m"))
        os.system("cls")
        if id == 1:
            normal_num = normal_num + 1
            A_num = "N" + str(normal_num)
            port_normal.append(A_num)
            pos_dict['银行卡服务窗口'] = port_normal
            print('    \033[1;35;40m你的排队号码是N{},当前你选择的是普通服务。\033[0m\n'.format(normal_num))
            time.sleep(1)
            os.system("cls")
            #print(pos_dict['银行卡服务窗口'])
            #上面是一行禁用的代码，不禁用时用来测试运行时结果是否正确。
            nor_list(pos_dict)
        elif id == 2:
            vip_num = vip_num + 1
            D_num = "V" + str(vip_num)
            port_vip.append(D_num)
            pos_dict['VIP服务窗口'] = port_vip
            print('    \033[1;35;40m你的排队号码是V{},当前你选择的是VIP服务。\033[0m\n'.format(vip_num))
            time.sleep(1)
            os.system("cls")
            vip_list(pos_dict)
        elif id == 3:
            yell_num()
        else:
            print("输入有误，请重新输入！")
            time.sleep(0.2)
        return pos_dict

def yell_num():
    while True:
        print("""
            \033[5;32;40m评价窗口\033[0m
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃    1. 普通服务\t\t    ┃
    ┃    2. VIP服务\t\t    ┃
    ┃    3. 切换到叫号窗口\t    ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        window_num = input("     \033[1;34;40m请选择服务类型: [  ]\b\b\b\033[0m")
        if window_num =="1":
            evaluation()
            global port_normal_status
            port_normal_status = 0
            os.system("cls")
            nor_list(pos_dict)
            get_op()
        elif window_num =="2":
            evaluation()
            global port_vip_status
            port_vip_status = 0
            vip_list(pos_dict)
            os.system("cls")
            vip_list(pos_dict)
            get_op()
        elif window_num =="3":
            #设置输入3切换到用户界面
            os.system("cls")
            get_op()
        else:
            print("输入错误，请重新输入！\n")

def vip_list(pos_dict):
    while True:
        time.sleep(0.2)
        global port_vip_status
        if port_vip_status == 0:
            port_vip_status = 1
            port_vip = pos_dict['VIP服务窗口']
            popped_num = port_vip.pop(0)
            print("\033[1;35;40m请{}号客户前往VIP窗口办理业务，当前排队人数为{}人\033[0m\n"\
            .format(popped_num,len(port_vip)))
            time.sleep(1)
            #os.system("pause")
            get_op()
        else:
            get_op()


def nor_list(pos_dict):
    while True:
        time.sleep(0.2)
        global port_normal_status
        if port_normal_status == 0:
            port_normal_status = 1
            port_normal = pos_dict['普通服务窗口']
            popped_num = port_normal.pop(0)
            print("\033[1;35;40m请{}号客户前往普通窗口办理业务，当前排队人数为{}人\033[0m\n"\
            .format(popped_num,len(port_normal)))
            #os.system("pause")
            time.sleep(1)
            get_op()
        else:
            get_op()
        

def evaluation():
    os.system("cls")
    print("        您对本次服务是否满意？(5-1)\n")
    eva = input("     \033[1;34;40m请对我们的服务进行评价: [  ]\b\b\b\033[0m")
    os.system("cls")
    print("        您的评价是"+eva+",谢谢,期待您的下次光临!")
    time.sleep(1)
    os.system("cls")

def main():
    global port_normal,port_vip,normal_num,vip_num,port_vip_status,port_normal_status,pos_dict   
    normal_num=0
    vip_num=0
    port_normal = []
    port_vip = []
    port_vip_status = 0
    port_normal_status = 0
    pos_dict = {
    "普通服务窗口":port_normal,
    "VIP服务窗口":port_vip,
    }
    while True:
        pos_dict = get_op()

main()
