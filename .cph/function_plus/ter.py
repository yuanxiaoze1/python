class student(object):
    def __init__(self, name,id,qq):
        self.__name=name
        self.__id=id
        self.__qq=qq
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_qq(self):
        return self.__qq
    def set_name(self,name):
        self.__name=name
    def set_id(self,id):
        self.__id=id
    def set_qq(self,qq):
        self.__qq=qq
a=student("xinggy","65230514","3171901686")