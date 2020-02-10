# 使用turtle库绘制图形
# 画出NUESOFT
# 导入turtle库 使用import + 模块名  as 起别名
import turtle as t
# 设置画笔大小 10px
t.pensize(6)
t.color('blue','pink')

# 抬笔
t.penup()

# set position
t.goto(-250,0)

# 落笔 pendown
t.pd()

t.lt(90)
t.fd(80)
t.rt(145)
t.fd(100)
t.lt(145)
t.fd(80)

# 抬笔
t.penup()
# set position
t.goto(-80,80)
# 落笔 pendown
t.pd()

t.rt(90)
t.fd(80)
t.back(80)
t.rt(90)
t.fd(100)
t.lt(90)
t.fd(80)

t.pu()
t.goto(-80,30)
t.pd()
t.fd(70)

# # 画 S
# t.pu()
# t.goto(150,60)
# t.pd()
# t.lt(90)
# t.circle(30,270)
# t.circle(-30,270)
t.pu()
t.goto(150,60)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()

t.done()

# 使用pyinstaller进行程序打包
# 安装pyinstaller
# 使用pip 安装第三方模块


