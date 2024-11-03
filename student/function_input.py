from function_print import PagePrint
import system 
import fuction_list
from system import Pages

def PageInput_main():
    rx=input()
    if rx=="1":
        system.user_page=Pages.addCard_page
    elif rx=="2":
        system.user_page=Pages.showCard_page
    elif rx=="3":
        system.user_page=Pages.findCard_page
    elif rx=="0":
        system.user_page=Pages.exit_page

    else :
        print("输入错误，请重新输入")
  
def PageInput_find():
    name=input("请输入姓名：")
    for i in system.student_list:
        if i["name"]==name:
            print("查找成功，具体信息如下：")
            print("姓名：%s 电话：%s 邮箱：%s QQ：%s"%(i["name"],i["phone"],i["email"],i["QQ"]))
            break
    else:
        print("没有找到学生%s的信息"%name)
        return
    rx=input("输入1返回主菜单\n输入2删除学生\n输入3修改信息\n输入0退出系统\n")
    if rx=="0":
        system.user_page=Pages.exit_page
    elif rx=="1":
        system.user_page=Pages.main_page
    elif rx=="2":
        system.student_list.remove(i)
        print("成功删除%s的信息"%name)
        print(50*"*")
        system.user_page=Pages.main_page
    elif rx=="3":
        i["name"]=fuction_list.update(i["name"],"请输入姓名：(输入0或不输入不修改)")
        i["phone"]=fuction_list.update(i["phone"],"请输入电话：(输入0或不输入不修改)")
        i["email"]=fuction_list.update(i["email"],"请输入邮箱：(输入0或不输入不修改)")
        i["QQ"]=fuction_list.update(i["QQ"],"请输入QQ：(输入0或不输入不修改)")
        print("成功修改%s的信息"%name)
        print(50*"*")
        system.user_page=Pages.main_page
    else:
        print("输入错误，返回主菜单")
        system.user_page=Pages.main_page

def PageInput_Add():
    name=input("请输入姓名：")
    telephone=input("请输入电话：")
    email=input("请输入邮箱：")
    qq=input("请输入QQ：")
    system.student_list.append({"name":name,"phone":telephone,"email":email,"QQ":qq})
    print("成功添加%s的信息"%name)
    system.user_page=Pages.main_page
    print(50*"*")
def PageInput_show():
    rx=input("输入1返回主菜单  输入0退出系统")
    if rx=="0":
        system.user_page=Pages.exit_page
    elif rx=="1":
        system.user_page=Pages.main_page
def PageInput_exit():
    pass
def PageInput(user_page):
    from system import Pages 
    if user_page == Pages.main_page:PageInput_main()
    if user_page == Pages.addCard_page:PageInput_Add()
    if user_page == Pages.showCard_page:PageInput_show()
    if user_page == Pages.exit_page:PageInput_exit()
    if user_page == Pages.findCard_page:PageInput_find()
