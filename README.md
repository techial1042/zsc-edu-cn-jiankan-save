个人健康信息上报


* 在微信公众号，绑定成功后，会返回一个 oid

* 通过 oid 可以拿到 cookie

* 表单提交的时候需要带上 cookie



每隔 4 个小时自动打卡（可以接入使用方糖 / 钉钉机器人）

```bash
echo "0 */4 * * * /usr/bin/python /root/jiankangSave.py > /dev/null" >> /var/spool/cron/root
```
