# -*- coding:utf-8 -*-

from flask import Flask, render_template
import json
from models import Chart

app = Flask(__name__)

@app.route("/")
def index():
    chart1 = Chart().pie("饼图", data={
            u"衬衫": 100,
            u"羊毛衫": 360,
            u"雪纺衫": 120,
            u"裤子": 500,
            u"高跟鞋": 300
        })
    chart2 = Chart() \
             .legend(data=[u"最高气温", u"最低气温"]) \
             .x_axis(data=[u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]) \
             .y_axis(formatter="{value} C") \
             .line(u"最高气温", [10, 20, 30, 40, 30, 20, 10], mark_max_point=True, show_item_label=True) \
             .bar(u"最低气温", [5, 10, 5, 10, 5, 6, 7]) \
             .pie(name="测试", data={"Java": 50, "PHP": 50, "Python": 100}, center=["20%", "30%"], radius="15%")


    print json.dumps(chart2, indent=2)

    render = {
        "title": u"测试的标题",
        "templates": [
            {"type": "radio"},
            {"type": "table"},
            {"type": "chart", "option": json.dumps(chart1, indent=2)},
            {"type": "chart", "option": json.dumps(chart2, indent=2)}
        ]
    }
    return render_template("main.html", **render)

if __name__ == "__main__":
    app.run(debug=True)
