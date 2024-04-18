from json import loads

import requests
import re

cookies = {
    'tt_chain_token': 'RsODu7vcrXyCun9viGKJyw==',
    'tiktok_webapp_theme': 'light',
    'passport_csrf_token': '5902da3cb4ed40b87d520405ffed2261',
    'passport_csrf_token_default': '5902da3cb4ed40b87d520405ffed2261',
    '_ttp': '2bkzLzELiwAXubktic8G817GGyR',
    'd_ticket': 'dbeb65d8b0128d6aee8d9fb43240e81c1e540',
    'multi_sids': '6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736',
    'cmpl_token': 'AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw',
    'passport_auth_status': '554847a7c512b04417f4ee904e3a385b%2C',
    'passport_auth_status_ss': '554847a7c512b04417f4ee904e3a385b%2C',
    'sid_guard': '6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT',
    'uid_tt': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
    'uid_tt_ss': 'e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073',
    'sid_tt': '6574fbb17a1fcd9c7dfa2df381f83736',
    'sessionid': '6574fbb17a1fcd9c7dfa2df381f83736',
    'sessionid_ss': '6574fbb17a1fcd9c7dfa2df381f83736',
    'sid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
    'ssid_ucp_v1': '1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY',
    'store-idc': 'maliva',
    'store-country-code': 'id',
    'store-country-code-src': 'uid',
    'tt-target-idc': 'alisg',
    'tt-target-idc-sign': 'NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb',
    'last_login_method': 'sms_verification',
    'perf_feed_cache': '{%22expireTimestamp%22:1709830800000%2C%22itemIds%22:[%227313519542037171462%22%2C%227334214300615167265%22%2C%227333544490633825541%22]}',
    'tt_csrf_token': 'hm7hpCWb-RloDc24XsRfRmr_zHkuISHJ-cLw',
    'ak_bmsc': 'D9553C11EED7802091BA115772375955~000000000000000000000000000000~YAAQQ+nOFwYhJf+NAQAAAOJoFxf/L8tbHRllAbHU/2uWrBfyloZnXnuJmf+0Qq0Q7klb+be9+amgrmQMn8YgSACOvRoJekrgahvstgrjLXN4cDqsThD0vfwL0l4vlnI3CtejJ/WCyE7qjpcDOfWG8zKrUos5a/AYT8XHweYSsii2NUPh3XGdGpdqUPWYSUNLX5WQYJ6h7MyYYoXLIS5qSgtts5wBjJln9igkQVdxPz8h4O6EXvq2tG2VmAKOLNqtJJNSkPkLkP1ORA6ykUxLtere8Vai/XMxt91lMVJF9LSYdYggIBW+fmQDT0jMCYLwtc+IETGqFf1i9hlFZckB0Y+i/aGK2o7xe6ZStxUdNcO/N2zsQQE2QCsAF5HFDCjJ+ja4qoJmbogIiR9y',
    'passport_fe_beating_status': 'true',
    'ttwid': '1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709789848%7C1cc9757557b3caef334807200b288bf87e0eb8a139fd640f7574c704a494d3ef',
    'bm_sv': 'AEBF757BEF7A4843CC4AAB240A2BD496~YAAQZ+nOF99KbvmNAQAA4u9qFxeo+BPyNXRXncfu6DE7tgUXZgf89Vtisen+MNxp3yv5fFZaJiZMgguwVnhhGjAUJPkUmNW4acvz1sZEhz9J7QHHqP3tSlJ0PmjW6icDdAJxu/f64XgdDlBRZFAoziI879mVTvUCZ9f8o8lehJB91E4qT5w0ObKqML7jtMmDaZW9qtBXNoI1faBTBwJH1f9oFpmNLF01LYp/sX1zQn6oCw5XPysJQC/kUU7NjTyp~1',
    'odin_tt': '216864a36a1f6f530f30b827bf1835b2c43d9835f871a40fd6a31cc886abff7d1b540016e19668d15c505488bb28eefe5f9cbd6491198bbaa2774f72bfd890bd',
    'msToken': 'dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
    'msToken': 'dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
}

headers = {
    'authority': 'www.tiktok.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'tt_chain_token=RsODu7vcrXyCun9viGKJyw==; tiktok_webapp_theme=light; passport_csrf_token=5902da3cb4ed40b87d520405ffed2261; passport_csrf_token_default=5902da3cb4ed40b87d520405ffed2261; _ttp=2bkzLzELiwAXubktic8G817GGyR; d_ticket=dbeb65d8b0128d6aee8d9fb43240e81c1e540; multi_sids=6749780217957532673%3A6574fbb17a1fcd9c7dfa2df381f83736; cmpl_token=AgQQAPPdF-RO0o2S5_8jY504_9q4vEdZv4ArYNFfVw; passport_auth_status=554847a7c512b04417f4ee904e3a385b%2C; passport_auth_status_ss=554847a7c512b04417f4ee904e3a385b%2C; sid_guard=6574fbb17a1fcd9c7dfa2df381f83736%7C1709623899%7C15552000%7CSun%2C+01-Sep-2024+07%3A31%3A39+GMT; uid_tt=e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073; uid_tt_ss=e22de1c80eb4388c48031ad7f387c3177a0b497e257faddcf41580cba8791073; sid_tt=6574fbb17a1fcd9c7dfa2df381f83736; sessionid=6574fbb17a1fcd9c7dfa2df381f83736; sessionid_ss=6574fbb17a1fcd9c7dfa2df381f83736; sid_ucp_v1=1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY; ssid_ucp_v1=1.0.0-KDYwOGM2NTZmYTI2ZDY3NjUyZWQ5NWQwZTBlMTFhZDY2ODU2N2RmYTUKIAiBiMXaiquC1l0Q25SbrwYYswsgDDCEk7DtBTgCQPEHEAMaBm1hbGl2YSIgNjU3NGZiYjE3YTFmY2Q5YzdkZmEyZGYzODFmODM3MzY; store-idc=maliva; store-country-code=id; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=NxBeUNWDj20Xon206PhslbBOhRNyp9D3NLN6HS9leq2nBJatkqIW-eWyknQCuWdkfh38iaKwunxSjBvWEoIN5hn_wiMVpjEcMENxFa4U-UysRbbDSiXdpQccbqEpxDUeO4i6bQm9I5Uj1T0GYMoM36FrV7NMKB-c6sHotPSjszstb0qKXiftL25xJdo06roMaGBe-mZwyh5M2fvr_5eCLu9xXx0b6CxWIauOtKZTaDWVHzIGmOUNteIy643X45x8_bo9v2M0I4_GMfisP7AA2hgT9dT-03tw7oO30v14IVoDQTYpnQ1gms9gOUCgnEpxsZGsoxuQ_utTf_3cosHqrwFxauQW15MBovW690nkjI7cJ2BrgJUeta6ixBdLBAfHkFhDDS1NKIH2x5iBN2xOfY11NFXtCLb3F7Eeznvq_iTrHiE0Z1DTNX5PGVLWc_XFh1kMsbfMo_-te9bQbRvohj9KAimpbNpgT2Fii19enaX_ZvnZQUp5hq78pPnDT8Wb; last_login_method=sms_verification; perf_feed_cache={%22expireTimestamp%22:1709830800000%2C%22itemIds%22:[%227313519542037171462%22%2C%227334214300615167265%22%2C%227333544490633825541%22]}; tt_csrf_token=hm7hpCWb-RloDc24XsRfRmr_zHkuISHJ-cLw; ak_bmsc=D9553C11EED7802091BA115772375955~000000000000000000000000000000~YAAQQ+nOFwYhJf+NAQAAAOJoFxf/L8tbHRllAbHU/2uWrBfyloZnXnuJmf+0Qq0Q7klb+be9+amgrmQMn8YgSACOvRoJekrgahvstgrjLXN4cDqsThD0vfwL0l4vlnI3CtejJ/WCyE7qjpcDOfWG8zKrUos5a/AYT8XHweYSsii2NUPh3XGdGpdqUPWYSUNLX5WQYJ6h7MyYYoXLIS5qSgtts5wBjJln9igkQVdxPz8h4O6EXvq2tG2VmAKOLNqtJJNSkPkLkP1ORA6ykUxLtere8Vai/XMxt91lMVJF9LSYdYggIBW+fmQDT0jMCYLwtc+IETGqFf1i9hlFZckB0Y+i/aGK2o7xe6ZStxUdNcO/N2zsQQE2QCsAF5HFDCjJ+ja4qoJmbogIiR9y; passport_fe_beating_status=true; ttwid=1%7CSs-WSXwK_P549vAAUSfYFc_KGNjCrwrNZgUwp62lKwI%7C1709789848%7C1cc9757557b3caef334807200b288bf87e0eb8a139fd640f7574c704a494d3ef; bm_sv=AEBF757BEF7A4843CC4AAB240A2BD496~YAAQZ+nOF99KbvmNAQAA4u9qFxeo+BPyNXRXncfu6DE7tgUXZgf89Vtisen+MNxp3yv5fFZaJiZMgguwVnhhGjAUJPkUmNW4acvz1sZEhz9J7QHHqP3tSlJ0PmjW6icDdAJxu/f64XgdDlBRZFAoziI879mVTvUCZ9f8o8lehJB91E4qT5w0ObKqML7jtMmDaZW9qtBXNoI1faBTBwJH1f9oFpmNLF01LYp/sX1zQn6oCw5XPysJQC/kUU7NjTyp~1; odin_tt=216864a36a1f6f530f30b827bf1835b2c43d9835f871a40fd6a31cc886abff7d1b540016e19668d15c505488bb28eefe5f9cbd6491198bbaa2774f72bfd890bd; msToken=dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5; msToken=dpUxs1zNqibwOftsKnG9i2PfJX8LwhiIuDsokQoZIVa12KamQ-6XKITJV6neMhNpsrcXoz29A31KBUMrZ0GiZbUCcP8JvSybNvGTLf4pTmpMXgIS3vhcib-TtE1QzRBkeTF8qb2_r5iNkVT5',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

response = requests.get('https://www.tiktok.com/@evosesports', cookies=cookies, headers=headers)

response_text: str = response.text

from bs4 import BeautifulSoup
import json


soup = BeautifulSoup(response_text, 'html.parser')

script_tag = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__', type='application/json')

if script_tag:
    json_content = script_tag.string
    parsed_json = json.loads(json_content)

    secUid_value = parsed_json['__DEFAULT_SCOPE__']['webapp.user-detail']
    uid = secUid_value['userInfo']['user']['secUid']
    
    
    params = {
    'WebIdLastTime': '1706762654',
    'aid': '1988',
    'app_language': 'id-ID',
    'app_name': 'tiktok_web',
    'browser_language': 'id-ID',
    'browser_name': 'Mozilla',
    'browser_online': 'true',
    'browser_platform': 'Linux x86_64',
    'browser_version': '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'channel': 'tiktok_web',
    'cookie_enabled': 'true',
    'count': '30',
    'device_id': '7330489720444978690',
    'device_platform': 'web_pc',
    'focus_state': 'true',
    'from_page': 'user',
    'history_len': '8',
    'is_fullscreen': 'false',
    'is_page_visible': 'true',
    'maxCursor': '0',
    'minCursor': '0',
    'os': 'linux',
    'priority_region': 'ID',
    'referer': '',
    'region': 'ID',
    'scene': '21',
    'screen_height': '1080',
    'screen_width': '1920',
    'secUid': uid,
    'tz_name': 'Asia/Jakarta',
    'webcast_language': 'id-ID'
}

    response = requests.get('https://www.tiktok.com/api/user/list/', params=params, cookies=cookies, headers=headers)
    json.dump(response.json(), open('sample.json', 'w'), indent=4)
    