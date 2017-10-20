import xlrd
import random
import easygui as g
data = xlrd.open_workbook('../alien_invasion/新名单.xlsx') #打开execl表
table = data.sheets()[0]  #获取第一张execl表的数据
b = []
cols = table.col_values(1)   #获取execl第一行的数据
#i = 0
#for cols[i] in cols:   #循环输出execl第一列的数据
#     print (cols[i])

def create():      #定义函数，方便调用
      while True:
                  randoms = random.choice(cols)
                  cols.remove(randoms)
                  g.msgbox("这位同学运气真好（偷笑）:" + randoms ) #输出结果
                  return
while True:
      command = g.buttonbox(msg="欢迎运行萌萌哒的抽奖小程序",title="",image="../alien_invasion/4n5t3oc4gvg66378.gif",choices=('点击抽奖','退出'))
      #定义描述和定义按钮
      if command == "点击抽奖":
            create()
      if command == "退出":
            break
