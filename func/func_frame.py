class func_frame(object):
  classval1 = 1   #类变量
  def __init__(self):
    self.val2 = 200   #成员变量
  def help(num=1):
    localval3 = 300    #函数内部的局部变量
    print("Show all functions list and infos")
    # ex) mean(x) : x is the data which will be averaged, and it's data type is 'list'; the output is x's mean value, data type is 'float'.



if __name__ == '__main__':
    inst = func_frame()
    inst.help()

'''
from func_frame import func_frame as dd

x = dd()
dd.help()

x.help()
dd.help()
'''
