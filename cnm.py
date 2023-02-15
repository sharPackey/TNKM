import requests
import sys

from requests.packages import urllib3
urllib3.disable_warnings()

MAP=dict()
MAP[0]='EC6185E7B9514622E053CB0412AC81E0'#C++ 30
MAP[3]='ED02DC6D3BFD2AF9E053CB0412AC66C4'#想象力 10
MAP[5]='EE19A4B60F5E33C0E053CA0412AC26C2'#文化创意 10

number=int(sys.argv[1])
courseid=MAP[number]
COO = "_ga=GA1.1.1147501122.1662707658; _ga_0KD226TRZ5=GS1.1.1665300145.2.0.1665300147.0.0.0; route=a4e23ebc43fc46391667782b865e973a; JSESSIONID=E27E6A3EF3A51FB0252FA309DA670DBC"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': COO,
    'Origin': 'https://tis.sustech.edu.cn',
    'Referer': 'https://tis.sustech.edu.cn/Xsxk/query/1',
    'RoleCode': '01',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
   'p_pylx': '1',
    'mxpylx': '1',
    'p_sfgldjr': '0',
    'p_sfredis': '0',
    'p_sfsyxkgwc': '0',
    'p_xktjz': 'rwtjzyx',
    'p_chaxunxh': '',
    'p_gjz': '',
    'p_skjs': '',
    'p_xn': '2022-2023',
    'p_xq': '2',
    'p_xnxq': '2022-20232',
    'p_dqxn': '2022-2023',
    'p_dqxq': '2',
    'p_dqxnxq': '2022-20232',
    'p_xkfsdm': 'kzyxk',
    'p_xiaoqu': '',
    'p_kkyx': '',
    'p_kclb': '',
    'p_id':courseid,
    'p_xkxs': '',
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
    'pageNum': '1',
    'pageSize': '16',
}

s = requests.session()

while True:
    response = s.post('https://tis.sustech.edu.cn/Xsxk/addGouwuche', headers=headers, data=data,verify=False)
    print(response.text)