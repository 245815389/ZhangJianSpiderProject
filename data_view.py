from pyecharts.charts import Bar
from pyecharts import options as opts
import pymongo

# 链接数据库
conn = pymongo.MongoClient("localhost", 27017)
def zhaopin_dbc():
    db = conn.zhaopindb
    res_bj = db.zhaopintable.find({"city": {"$regex": "北京"}}).count()  # $regex  模糊查询 包含 北京 两字的数据都查询
    res_sh = db.zhaopintable.find({"city": {"$regex": "上海"}}).count()
    res_gz = db.zhaopintable.find({"city": {"$regex": "广州"}}).count()
    res_qd = db.zhaopintable.find({"city": {"$regex": "青岛"}}).count()
    res_hz = db.zhaopintable.find({"city": {"$regex": "杭州"}}).count()
    res_sz = db.zhaopintable.find({"city": {"$regex": "深圳"}}).count()
    res_yt = db.zhaopintable.find({"city": {"$regex": "烟台"}}).count()
    return res_bj, res_gz, res_hz, res_qd, res_sh, res_sz, res_yt

res_bj, res_gz, res_hz, res_qd, res_sh, res_sz, res_yt = zhaopin_dbc()

def fanyuan_dbc():
    db = conn.fangyuandb
    res = db.fangyuantable.find()  # 输出指定一列 第一个{}为条件，空代表查询所有
    num = db.fangyuantable.find().count()  # 有多少条数据
    res_list = list(res)
    info_list = []
    city_list = []
    num_list = []
    for i in range(num):
        for v in res_list[i].values():  # 这里 res_list 是个列表， res_list[i]是字典
            info_list.append(v)
        i += 1
    for i in range(1, len(info_list), 3):
        num_list.append(info_list[i])
    for i in range(2, len(info_list), 3):
        city_list.append(info_list[i])
    return city_list, num_list

city_list, num_list = fanyuan_dbc()

print(city_list)
bar = Bar()
bar.add_xaxis(city_list)
bar.add_yaxis("岗位",num_list)
bar.set_global_opts(title_opts=opts.TitleOpts(title="租房情况"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False))
bar.render("租房情况数据可视化.html")

bar = Bar()
bar.add_xaxis(["北京", "上海", "广州", "青岛", "杭州","深圳","烟台"])
bar.add_yaxis("岗位",[res_bj, res_sh, res_gz, res_qd, res_hz, res_sz, res_yt])

bar.set_global_opts(title_opts=opts.TitleOpts(title="IT岗位情况"),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=False))

bar.render("岗位情况数据可视化.html")



