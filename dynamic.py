# 导入所需要的库函数
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Map, Map3D
from pyecharts.faker import Faker
from openpyxl import load_workbook
import numpy as np
import openpyxl
import random
import xlrd
t1 = Timeline() # 创建Timeline对象
for i in range(2005, 2020):
    data = xlrd.open_workbook(r'C:\data\city.xlsx')
    table = data.sheet_by_name('Sheet1')
    province = table.col_values(0)[1:]
    num = table.col_values(i-2004)[1:]
    list1 = [[province[i], num[i]] for i in range(len(province))]  # 列表生成式
    map_1 = (
        Map()
        .add("城镇化", list1)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100, min_=20),
                          legend_opts =opts.LegendOpts(is_show=False),
                        title_opts=opts.TitleOpts(title="江苏省南京市浦口区绿化面积"))
    )
    t1.add(map_1,'{}年'.format(i))
t1.add_schema(
    symbol = 'arrow',# 设置标记时间；
    play_interval = 900,
    symbol_size=2,  # 标记大小;
)
t1.render(path="C://data//城镇化率变化.html")
