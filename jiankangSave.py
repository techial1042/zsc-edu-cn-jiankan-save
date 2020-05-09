import requests

payload = {
    'uaid': '',  # id
    'provinceJg': '',  # 籍贯 xx 省
    'cityJg': '',  # 籍贯 xx 市
    'province': '',  # 当前所在地
    'city': '',  # 当前所在地
    'address': '',  # 请详细填写当前住址，必填
    'mobile': '',  # 手机号
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
    'memberHealthDes': ''  # 请详细说明家庭成员目前健康状态
}

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
    'Cookie': ''  # 要修改
}

response = requests.post("http://srv.zsc.edu.cn/f/_jiankangSave", headers=headers, data=payload)
print(response.json())
