import requests
import sys

MAP=dict()
MAP[1]='D08FF9B8C3B5714DE053CA0412ACC812'

number=int(sys.argv[1])
courseid=MAP[number]
COO = "UM_distinctid=17bbe09cf29e0-0c8dba5386608-5734174f-125f51-17bbe09cf2a39a; JSESSIONID=C8FF0B332A48E375860BDB0FE1E95317; route=27c91390986ed8d24aaf1bc72068f4f5"
headers = {
    'authority': 'tis.sustech.edu.cn',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'rolecode': '01',
    'origin': 'https://tis.sustech.edu.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://tis.sustech.edu.cn/Xsxk/query/1',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': COO
}

data = {
  'p_pylx': '1',
  'mxpylx': '1',
  'p_sfgldjr': '0',
  'p_sfredis': '0',
  'p_sfsyxkgwc': '0',
  'p_xktjz': 'rwtjzyx',
  'p_chaxunxh': '',
  'p_skjs': '',
  'p_xn': '2021-2022',
  'p_xq': '2',
  'p_xnxq': '2021-20222',
  'p_dqxn': '2021-2022',
  'p_dqxq': '2',
  'p_dqxnxq': '2021-20222',
  'p_xkfsdm': 'bxxk',
  'p_xiaoqu': '',
  'p_kkyx': '',
  'p_kclb': '',
  'p_xkxs': '',
  'p_id':courseid,
  'p_sfhlctkc': '0',
  'p_sfhllrlkc': '0',
  'p_kxsj_xqj': '',
  'p_kxsj_ksjc': '',
  'p_kxsj_jsjc': '',
  'p_kcdm_js': '',
  'p_kcdm_cxrw': '',
  'p_kc_gjz': '',
  'p_xzcxtjz_nj': '',
  'p_xzcxtjz_yx': '',
  'p_xzcxtjz_zy': '',
  'p_xzcxtjz_zyfx': '',
  'p_xzcxtjz_bj': '',
  'p_sfxsgwckb': '1',
  'p_skyy': '',
  'p_chaxunxkfsdm': '',
  'pageNum': '2',
  'pageSize': '13'
}
s = requests.session()

while True:
    response = s.post('https://tis.sustech.edu.cn/Xsxk/addGouwuche', headers=headers, data=data)
    print(response.text)