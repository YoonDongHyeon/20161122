#객체 지향 프로그래밍
# 객체(Object)
# 오브젝트의 특성과 행동을 설정 특성은 attribute, 행동은 method라고 한다.
# 실제로는 클래스를 설계하는 것임.
# 클래스에 의해서 객체화 된 것을 이제는 개체(instance)라고 부른다.
# <1.캡슐화 : 객체의 특성은 외부에서 직접 바꿀 수 없다. program 적으로 허용되지않은 경로에 의해 바꿀 수 없다.
# public 파이썬에서는 public으로 선언하여, 외부에서 마음껏 접근이 가능하다.
# 객체 안에 있는 특성과 메소드를 가져올 수 있다.
# public의 반대가 private 다른 프로그래밍 언어가 이와 같은데, 이는 특성을 외부에서 임의로 가져갈 수 없다.
# 중간 개념인 protected 상속되어진 child class에서는 접근이 가능하지만 그외의 클래스로는 접근이 불가능하다.>
# <2. 상속 : 클래스 A가 있다고 가정. 클래스 A의 특성을 전부 가지고 있으면서 뭔가 추가된 클래스를 가지고 싶을 때
# Class A의 모든 것을 상속받은 Class B로 넘어 갈 수 있다.>
# <3. 추상화 : 특징적인 것만 가져와서 객체를 클래스로 모델링 하는 것>
# < 4. 다형성 : Class 중에 직선을 그리는 클래스가 있을 때 직사각형, 삼각형을 그리는 클래스에서 '그린다'라는 것을
# 재선언해서 다시 그리는 기능을 쓸 수 있다. 받는 인수 갯수가 달라도 같은 이름의 기능을 사용하여도 된다.>
# class pcclass():
    # __a = None
    # # private 은 언더스코어 두개 다른 클래스에서 선언도 못하고 쓰지도 못함.
    # _b = 3
    # protected는 언더스코어 한개
#     def __init__(self):
#         pass
# #     생성자에서 프라이빗으로 선언해 주는 법
#     def __init__(self):
#         self.a = 'my'
#         self.b = 3

# class myclass(pcclass):
    # 상속하는 법은 myclass()로 써주면 된다.
    # attribute 선언
    # def __init__(self,a ,b):
    #     self.a = a
    #     self.b = b
        # self 가 그 영역 안에서의 글로벌 변수라고 생각하면 된다.
        # f = 3
        # 단어의 양쪽에 밑줄이 두개 들어가게 하는 것은 특별한 경우 생성자로 불리는 함수
        # 이 클래스가 개체화 될때 처음 하는 행동을 지정해주는 행동 무조건 클래스 형성 후에 실행된다.

    # def __del__(self):
    #    print(self.a)
        # 소멸자로 불리는 함수 마지막에 지우기 전에 무조건 실행되는 기능.
    # def mymethod(self):
    #     print(self.a)
    #     print(self.b)

# myinstpc = pcclass()
# myinst = myclass(1,2)
# 인수를 넣어줘야 작동한다.
# myinst2 = myclass(3,4)
# print(myinst2.a)
# myinst2.mymethod()
# 만약에 myclass에서 a나 b를 private으로 설정하면 불러오면 에러 뜬다. protected도 마찬가지
# --------------------------------------------------------------------------------------------------------------
# class pcclass():
#
#     def __init__(self, a):
#         self.a = a
#     def mymethod(self):
#         print(self.a)
#
# class myclass(pcclass):
#
#     def __init__(self,a ,b):
#         pcclass.__init__(self, a)
#
#         self.b = b
#
#     def __del__(self):
#        print(self.a)
#     def mymethod(self):
#         print(self.a)
#         print(self.b)

# myinstpc = pcclass(4)
# myinstpc.mymethod()
#  부모에게 4를 넣어줌
#  부모와 자식 둘다 mymethod라는 함수가 있지만 각각 다른 기능을 수행한다.
# myinst = myclass(1,2)
#
# myinst2 = myclass(3,4)
# print(myinst2.a)
# myinst2.mymethod()
# -------------------------------------------------------------------------------------------------------------------
# class Car():
#     def __init__(self):
#         self.__color = None
#         self.size = None
#
#     def mymethodp(self):
#         pass
#     def sef_color(self, color):
#         self.color = color
#     def get_color(self):
#         return self.color
#
# class Truck(Car):
#     def __init__(self, color, size, Load_weight):
#         Car.__init__(self, color, size)
#         self.Load_weight = Load_weight
#     def __del__(self):
#         print(self.a)
#
#     def mymethod(self):
#         print(self.a)
#         print(self.b)
# -----------------------------------------------------------------------------------------------------------------
# <up down 게임 만들기>
# import random
# class game:
#     def __init__(self, title):
#         self.gmaetitle = title
#     def run(self):
#         pass
# class up_downgame():
#     def __init__(self):
#         pass
#     def run(self):
#         ans = random.randint(1,50)
#         while True:
#             attack = int(input('수를 입력하시오'))
#             if ans < attack:
#                 print('너무 크다')
#             elif ans > attack:
#                 print('너무 작다')
#             elif ans == attack:
#                 print('정답')
#                 break

# mygame = up_downgame()
# mygame.run()
# -----------------------------------------------------------------------------------------------------------------
# <업다운 게임 교수님꺼>
import random
class game:
    def __init__(self, title):
        self.gametitle = title
    def run(self):
        pass
class up_downgame(game):
    def __init__(self, title, ll, ul):
        game.__init__(self, title)
        self.ll = ll
        self.ul = ul
        self.pr_no = None

    def run(self):
        print('Start game range {} ~ {}'.format(self.ll,self.ul))
        if self.pr_no == None:
            self.makern()
        while True:
            attack = int(input('수를 입력하시오'))
            if attack == self.pr_no:
                print('당신이 이겼다')
                break
            elif attack < self.pr_no:
                print('너무 작다')
            else:
                print('너무 크다')
    def makern(self):
        self.pr_no = random.randint(self.ll,self.ul)

mygame = up_downgame('Mygame',10,100)
mygame.run()

