import system 

def PagePrint_main():
    print(50*"*")
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print(50*"*")
def PagePrint_find():
    print(50*"*")
    print("查询名片")
    print("请输入相关信息")
    print(50*"*")
def PagePrint_Add():
    print(50*"*")
    print("新建名片")
    print("请输入相关信息")
def PagePrint_show():
    print(50*"*")
    if len(system.student_list)==0:
        print("没有学生信息")
    else:
        print("显示全部")
        print("%-20s\t%-20s\t%-20s\t%-20s"%("name","phone","QQ","email"))
        for i in system.student_list:
            print("%-20s\t%-20s\t%-20s\t%-20s"%(i["name"],i["phone"],i["QQ"],i["email"]))
    print(50*"*")
    
def Pageprint_exit():
    print("谢谢您的使用")
    print("----------END----------")
    system.isruning=False

def PagePrint(user_page):
    from system import Pages 
    if user_page == Pages.main_page:PagePrint_main()
    if user_page == Pages.addCard_page:PagePrint_Add()
    if user_page == Pages.showCard_page:PagePrint_show()
    if user_page == Pages.exit_page:Pageprint_exit()
    if user_page == Pages.findCard_page:PagePrint_find()

