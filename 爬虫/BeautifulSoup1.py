import urllib.request
import urllib.parse
import html_to_json

url='https://y.qq.com/n/ryqq/albumDetail/000bviBl4FjTpO'

# 携带cookie进行访问
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'Cookie': 'psrf_musickey_createtime=1658712634; uin=1761166825; wxopenid=; login_type=1; wxunionid=; psrf_qqaccess_token=96C9CC48BE753EC611573CFF9BB5D49C; fqm_sessionid=48e7fb34-4103-4f03-963d-8415de2e468e; pgv_pvid=7176230645; qm_keyst=Q_H_L_5uTS6_yjWejXwFMmFZHbWYaMKGSM7sPI0mCdOSvXN7Fl78YW0UjMqWg; ts_uid=9325555724; psrf_qqrefresh_token=B191D680C3492CAB3197FEDA727E589D; psrf_access_token_expiresAt=1666488634; RK=Q7XIPxsxYy; ptcz=529ac1bb9d40ebefd8d522bb8b1adbb4c5a20f6a3ec91d3964ef5e715e96c457; fqm_pvqid=4579e758-559c-4dc2-9995-4c350ef1a131; pgv_info=ssid=s246057525; qm_keyst=Q_H_L_5uTS6_yjWejXwFMmFZHbWYaMKGSM7sPI0mCdOSvXN7Fl78YW0UjMqWg; psrf_qqopenid=E1ED718A3536084B1A9820D972004806; _qpsvr_localtk=0.04488077315126526; tmeLoginType=2; psrf_qqunionid=98FC1FE7B66D64BF326425409FD903C8; qqmusic_key=Q_H_L_5uTS6_yjWejXwFMmFZHbWYaMKGSM7sPI0mCdOSvXN7Fl78YW0UjMqWg; euin=oKSsoK6s7wcA7v**; wxrefresh_token=; ts_last=y.qq.com/n/ryqq/albumDetail/000bviBl4FjTpO'
}
request=urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(request)
# 输出所有



# 将内容写入文件中
with open('111.html', 'wb') as fp:
    ppp=response.read()
    html_string=ppp
    output_json=html_to_json.convert(html_string)
    tables=html_to_json.convert_tables(html_string)
    print(ppp)
    print(output_json)
    print(tables)
    fp.write(ppp)

