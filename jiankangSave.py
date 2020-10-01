# -*- coding: utf-8 -*-
import requests
import json

# 方糖 / 钉钉机器人
webHookUrl = "https://google.com"

payload = {
    'uaid': '',  # id
    'provinceJg': '',  # 籍贯 xx 省
    'cityJg': '',  # 籍贯 xx 市
    'province': '',  # 当前所在地
    'city': '',  # 当前所在地
    'address': '',  # 请详细填写当前住址，必填
    'mobile': '',  # 手机号
    'touchZhongGaoFlag': '没有',  # 近 14 天内有没有去过中高风险地区   
    'leaveGDFlag58': '否',  # 5月8日后是否离开广东
    'backGDDate58': '',  # 如果已经返回请填写返回广东时间,必填
    'huBeiManFlag2': '否',  # 是否近两周接触过疑似病例或确诊病例
    'touchDate2': '',  # 接触时间
    'touchDays2': '--请选择--',  # 接触时长
    'touchProvince': '',  # 接触地点
    'touchCity': '',  #
    'touchMember2': '',  # 与接触人关系
    'sheQuTouchFlag': '否',  # 是否近两周接触过有病例报告的社区街道的发热、咳嗽等呼吸道症状的患者
    'sheQuTouchDate': '',  # 接触时间
    'sheQuTouchDays': '--请选择--',  # 接触时长
    'sheQuTouchProvince': '',  # 接触地点
    'sheQuTouchCity': '',
    'sheQuTouchMember': '',  # 与接触人关系
    'jinWaiTouchFlag': '否',  # 是否近两周接触过境外或高风险国家人员
    'jinWaiTouchDate': '',  # 接触时间
    'jinWaiTouchDays': '--请选择--',  # 接触时长
    'jinWaiTouchProvince': '',  # 接触地点
    'jinWaiTouchCity': '',
    'jinWaiTouchMember': '',  # 与接触人关系
    'huCheckFlag': '否',  # 返校前7天是否已做学校安排的核酸检测
    'health': '正常',  # 本人目前健康状态
    'exceptionDate': '',  # 异常出现时间
    'dealMethod': '',  # 处理办法
    'dealResule': '',  # 诊断结果
    'memberHealth': '正常',  # 家庭成员目前健康状态
    'memberHealthDes': '',  # 请详细说明家庭成员目前健康状态
    'suikangCode': '绿码'  # 个人粤康码持码情况
}


def web_hook(body):
    """
    方糖 / 钉钉机器人提醒
    """
    requests.post(webHookUrl, data=body)
    # requests.get(webHookUrl)


# fix ServerChan
def server_chan(title, content):
    sckey = " "  # your key
    url = 'https://sc.ftqq.com/{}.send'.format(sckey)
    data = {
        'text': title,
        'desp': content
    }
    result = requests.post(url, data)
    print(result)


headers = {
    'Host': 'srv.zsc.edu.cn',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Proxy-Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://srv.zsc.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Connection': 'keep-alive',
}


def get_cookie():
    response = requests.get('http://srv.zsc.edu.cn/f/wxJKOauthCode?code={}'.format(payload['uaid']),
                            headers=headers)
    response.encoding = 'utf-8'
    cookie = response.headers['Set-Cookie']
    headers['Cookie'] = cookie
    check_change(response.text)


def check_change(text):
    count = text.count('field ui-field-contain')
    if count != 30:
        # web_hook("from change")
        server_chan("Checkin Error", "From Changed")


def jian_kan_save():
    response = requests.post("http://srv.zsc.edu.cn/f/_jiankangSave", headers=headers, data=payload)
    print(response.text)
    # web_hook(response.text)
    text1 = json.loads(response.text)
    if text1["message"] == "提交成功。":
        server_chan("Checkin Success", "打卡成功")
    else:
        server_chan("Checkin Error", "打卡失败，请检查")


# if __name__ == '__main__':
#    get_cookie()
#    jian_kan_save()

# compatible with Serverless
def main_handler(event, context):
    try:
        get_cookie()
    except Exception as e:
        print(e)
        server_chan("Checkin Error", "GET Cookie Error")
    try:
        jian_kan_save()
    except Exception as e:
        print(e)
        server_chan("Checkin Error", "打卡失败，请检查")
