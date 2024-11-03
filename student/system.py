from enum import Enum
class Pages(Enum):
    main_page=1
    addCard_page=2
    findCard_page=3
    showCard_page=4
    exit_page=0
user_page=Pages.main_page
isruning=True
student_list=[]
def main():
    global isruning
    while isruning:
        global user_page
        from function_print import PagePrint
        PagePrint(user_page)
        from function_input import PageInput
        PageInput(user_page)


