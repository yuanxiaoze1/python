class Screen():
    def __init__(self,width=0,height=0):
        self._width = width
        self._height =   height
        self._resolution = width * height
        wit=0
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return 
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height
    def __str__(self):
        return   'width:%d,height:%d,resolution:%d' % (self._width,self._height,self._width*self._height)
class Person():
    def __init__(self,name,weight):
        self._name = name
        self._weight = weight
    @property
    def name(self):
        return self._name
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        self._weight = value
    
    def run(self):
        self.weight-=0.5
    def eat(self):
        self.weight+=1
    def __str__(self):
        return "%s的体重为%.2fkg"%(self.name,self.weight)
class HouseIteminfo():
    def __init__(self,name,area):
        self._name = name
        self._area = area
    @property
    def name(self):
        return self._name
    @property
    def area(self):
        return self._area
    def __str__(self):
        return "%s 占地 %.2f"%(self.name,self.area)
class House():
    def __init__(self,house_type,area):
        self._house_type = house_type
        self._area = area
        self._items = []
        self._free_area = area
    def __str__(self):
        return "户型：%s,总面积：%.2f,剩余面积：%.2f,家具列表：%s"%(self._house_type,self._area,self._free_area,self._items)
    def add_item(self,item):
        print("要添加%s"%item)
        if item.area > self._free_area:
            print("剩余面积不足，无法添加")
            return
        self._items.append(item.name)
        self._free_area -= item.area
        print("添加%s成功"%item.name)
        print("剩余面积：%.2f"%(self._free_area))
        

bed=HouseIteminfo("席梦思",4)
chest=HouseIteminfo("餐桌",2)
衣柜=HouseIteminfo("衣柜",2.5)
myhome=House("两室一厅",120)
myhome.add_item(bed)
myhome.add_item(chest)
myhome.add_item(bed)
print(myhome)
class Gun():
    def __init__(self,type,num=0):
        self._type = type
        self._num = num
    @property
    def type(self):
        return self._type
    @property
    def num(self):
        return self._num
    @num.setter
    def num(self, value):
        self._num = value
    def __str__(self):
        return "枪的类型：%s,子弹数量：%d"%(self._type,self._num)
    def shoot(self):
        if self._num <= 0:
            print("没有子弹了")
            return
        self._num -= 1
        print("发射子弹，剩余%d"%(self._num))
    def add_bullet(self,num):
        self._num += num
        print("子弹数量为%d"%(self._num))
class Soldier():
    def __init__(self,name,gun):
        self._name = name
        self._gun = gun
    @property
    def name(self):
        return self._name
    @property
    def gun(self):
        return self._gun
    def __str__(self):
        return "%s的枪是%s"%(self._name,self._gun)
    def fire(self):
        print("士兵开枪")
        self._gun.shoot()
        


    