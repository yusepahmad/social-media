import requests
import json

cookies = {
    'ig_did': 'AFF8FDF9-5545-4824-9D95-865E92FD1C06',
    'datr': '9WG7ZafAMkU4j0eaPZb3pjFo',
    'ps_n': '0',
    'ps_l': '0',
    'ig_nrcb': '1',
    'fbm_124024574287414': 'base_domain=.instagram.com',
    'ds_user_id': '13073668454',
    'shbid': '"17905\\05413073668454\\0541740452063:01f7234e70825ccb6ac34733758e57bf2e191fafeb3eeaa3e883b53b5197a88586b81558"',
    'shbts': '"1708916063\\05413073668454\\0541740452063:01f781726678fc0dd21ec3f2612d8bfd4ff07050dae6b34fc1f9b77a5c80a88687f655c7"',
    'csrftoken': 'O1pCFGlzGih73q3Ujc93Ua41i8CirbQw',
    'mid': 'Zd2ZMwAEAAF4RErJu7pcRwjLwSr_',
    'sessionid': '13073668454%3AEni0gdCzQqHuDp%3A3%3AAYedHJ-lz3-DaHisfHARa_tI8OCKV-oe9OLzOHUuMw',
    'fbsr_124024574287414': '4iPL3RKMkVGN-1ukHX_ts-efw376dFBIxMojqqcWxGs.eyJ1c2VyX2lkIjoiMTAwMDM2ODYyODQzODA3IiwiY29kZSI6IkFRREZVbURZa3dxUDJpNU1zV1hyYkV6WHBRNmRoVUFQcWpONU15Z0M1cklCUVVoT0E1TExwODBEMGR6TXVYS1FyNHdmOHFYUnlpRjRUcl9jM3VPSUJxdFVzRVE3UHVVN3pJd01GcTExYnVfUHRQczlhZ1lweTBJOXFLdjV4OThuczdyU0dWUk0wbmY2VUJqN01SeWlrOWs5SGt5WHpfOFlDQkVZa0ZwT05zbnVYakk4RWZmZkRaTy1vcmk1X0JUcXNNSEZzb0NDay1DUzk4YUpTY1AwNlVBdjU4NmpoamtXSUVfeGZ0VDRGX0lRTjBnUXlnMFRPM1IxSFd6UFF0QV9lRzlITHNScTJWdWIzTkJxUnlZYW52d0dWUHFZU3g1UUFfTXZ0QW5iaERaLUZaZ1JnUm9adlc2RGEtcUFGQWNGYVJpV1F1Y2M1ZkI1MWhQcUlMOWtmaFVlIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzBlbEJmd1RjYjc4cERaQXozdHF2RnFJaUNPYWdLMTVJZ3ZHS2RlR1BjQ2hKRWIyYlpCWXBGSm9HaW1BdkRRWkNwWUh2T3Vpa1VBdG1aQWpyUmFnWFFkcmF4c1dKZm04MTVudnZjZmZJZFdUWkN3aUVHUWJOTmhHNldIam1qalJrUFE1Z1RvbERJSGowWkJLRWVtRG5UcnhIYW04ZDc4NERSdHdhZkI2WkNaQVJQbDU3d1pEWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcwOTExNDQ5M30',
    'fbsr_124024574287414': 'j4jx5dDOiSCX9VnYTXU3wOMjSU3f9BASrSDcJdqDte4.eyJ1c2VyX2lkIjoiMTAwMDM2ODYyODQzODA3IiwiY29kZSI6IkFRQWlZeGhsdTlibXJfNUo4QkFFaEQ1Ny1WUi1Ec0xjM19wYVFfc1A1Ul9QMk5JcDhBZEIza2h3MjhrUmd2c1hBcTdCY0FFNW9CYmRuWEJmcnJreGw2dmtrZEtlandRSWNFS3NlcTZ1aTNjT3czcG5nWDhvTjhMT1AxV1ZZaml3c29RXy14QmRodG52a09GZVVrT1Z4NUNPRUlUY2liazJlUVdrckxSb21meGhxakpCM2RoMURaUkZfdDhpQ01jRHZfbmtlcmtRRlNMY0REWVRsRVJJTU5lemI3b3c5SldmbmE2ejJwRFpCeWFmZVFwQ1lWOGFjMDZMNEVNWDJGLTZERWhsbkFXSk1yaF8wSWZsX3FIUjB6NEU5amFiam8tLTNSY3BNZDI1LTNzZ3pRVF9NVzR4ZE8wNTQ2c2h6bzdEY1dnLTlUc0pIa0VXNmJhcW1yWkR3SW9uIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzNZYlpDeWdObzN4UFM5RjdRRnhYTldFM0h1MGFaQ01Ia1luTUZCd2RCZnJYRlJaQkJrenR0UWJZZUc0b0NnQmdES254SlhySHVVOVhBSFpBODhLOFpBSWVnVVJ4WkFaQ052ZEg2RFgzaWFMOGJJYmJndUtHZHhMbHFaQjlCaUtJTXhHYThFOG5JRnZ5UHZBMEdSMXVMaE1CcGpZNnlZTmFjU2FjSHZ3Mmd6NmdXYVpDa2daRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MDkxMTUyMDd9',
    'rur': '"CCO\\05413073668454\\0541740651211:01f70d520977894c61ee7e1eda35e4c16d2859194c6026f17c4135b253f43ceb4b632369"',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'ig_did=AFF8FDF9-5545-4824-9D95-865E92FD1C06; datr=9WG7ZafAMkU4j0eaPZb3pjFo; ps_n=0; ps_l=0; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=13073668454; shbid="17905\\05413073668454\\0541740452063:01f7234e70825ccb6ac34733758e57bf2e191fafeb3eeaa3e883b53b5197a88586b81558"; shbts="1708916063\\05413073668454\\0541740452063:01f781726678fc0dd21ec3f2612d8bfd4ff07050dae6b34fc1f9b77a5c80a88687f655c7"; csrftoken=O1pCFGlzGih73q3Ujc93Ua41i8CirbQw; mid=Zd2ZMwAEAAF4RErJu7pcRwjLwSr_; sessionid=13073668454%3AEni0gdCzQqHuDp%3A3%3AAYedHJ-lz3-DaHisfHARa_tI8OCKV-oe9OLzOHUuMw; fbsr_124024574287414=4iPL3RKMkVGN-1ukHX_ts-efw376dFBIxMojqqcWxGs.eyJ1c2VyX2lkIjoiMTAwMDM2ODYyODQzODA3IiwiY29kZSI6IkFRREZVbURZa3dxUDJpNU1zV1hyYkV6WHBRNmRoVUFQcWpONU15Z0M1cklCUVVoT0E1TExwODBEMGR6TXVYS1FyNHdmOHFYUnlpRjRUcl9jM3VPSUJxdFVzRVE3UHVVN3pJd01GcTExYnVfUHRQczlhZ1lweTBJOXFLdjV4OThuczdyU0dWUk0wbmY2VUJqN01SeWlrOWs5SGt5WHpfOFlDQkVZa0ZwT05zbnVYakk4RWZmZkRaTy1vcmk1X0JUcXNNSEZzb0NDay1DUzk4YUpTY1AwNlVBdjU4NmpoamtXSUVfeGZ0VDRGX0lRTjBnUXlnMFRPM1IxSFd6UFF0QV9lRzlITHNScTJWdWIzTkJxUnlZYW52d0dWUHFZU3g1UUFfTXZ0QW5iaERaLUZaZ1JnUm9adlc2RGEtcUFGQWNGYVJpV1F1Y2M1ZkI1MWhQcUlMOWtmaFVlIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzBlbEJmd1RjYjc4cERaQXozdHF2RnFJaUNPYWdLMTVJZ3ZHS2RlR1BjQ2hKRWIyYlpCWXBGSm9HaW1BdkRRWkNwWUh2T3Vpa1VBdG1aQWpyUmFnWFFkcmF4c1dKZm04MTVudnZjZmZJZFdUWkN3aUVHUWJOTmhHNldIam1qalJrUFE1Z1RvbERJSGowWkJLRWVtRG5UcnhIYW04ZDc4NERSdHdhZkI2WkNaQVJQbDU3d1pEWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcwOTExNDQ5M30; fbsr_124024574287414=j4jx5dDOiSCX9VnYTXU3wOMjSU3f9BASrSDcJdqDte4.eyJ1c2VyX2lkIjoiMTAwMDM2ODYyODQzODA3IiwiY29kZSI6IkFRQWlZeGhsdTlibXJfNUo4QkFFaEQ1Ny1WUi1Ec0xjM19wYVFfc1A1Ul9QMk5JcDhBZEIza2h3MjhrUmd2c1hBcTdCY0FFNW9CYmRuWEJmcnJreGw2dmtrZEtlandRSWNFS3NlcTZ1aTNjT3czcG5nWDhvTjhMT1AxV1ZZaml3c29RXy14QmRodG52a09GZVVrT1Z4NUNPRUlUY2liazJlUVdrckxSb21meGhxakpCM2RoMURaUkZfdDhpQ01jRHZfbmtlcmtRRlNMY0REWVRsRVJJTU5lemI3b3c5SldmbmE2ejJwRFpCeWFmZVFwQ1lWOGFjMDZMNEVNWDJGLTZERWhsbkFXSk1yaF8wSWZsX3FIUjB6NEU5amFiam8tLTNSY3BNZDI1LTNzZ3pRVF9NVzR4ZE8wNTQ2c2h6bzdEY1dnLTlUc0pIa0VXNmJhcW1yWkR3SW9uIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzNZYlpDeWdObzN4UFM5RjdRRnhYTldFM0h1MGFaQ01Ia1luTUZCd2RCZnJYRlJaQkJrenR0UWJZZUc0b0NnQmdES254SlhySHVVOVhBSFpBODhLOFpBSWVnVVJ4WkFaQ052ZEg2RFgzaWFMOGJJYmJndUtHZHhMbHFaQjlCaUtJTXhHYThFOG5JRnZ5UHZBMEdSMXVMaE1CcGpZNnlZTmFjU2FjSHZ3Mmd6NmdXYVpDa2daRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MDkxMTUyMDd9; rur="CCO\\05413073668454\\0541740651211:01f70d520977894c61ee7e1eda35e4c16d2859194c6026f17c4135b253f43ceb4b632369"',
    'dpr': '1',
    'referer': 'https://www.instagram.com/ntaxily__/following/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.184", "Chromium";v="121.0.6167.184"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"6.5.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'viewport-width': '973',
    'x-asbd-id': '129477',
    'x-csrftoken': 'O1pCFGlzGih73q3Ujc93Ua41i8CirbQw',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3b5sutWQJ0RtD5ImsEYu4u5CY8PUiN4oAW992lYDh8wAfv',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'count': 100,
    'max_id': 0,
}


def data(username, params, cookies, headers):
    response1 = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}',
        params=params,
        cookies=cookies,
        headers=headers,).json()

    response2 = []
    while True:
        res = requests.get(
            f'https://www.instagram.com/api/v1/friendships/{response1["data"]["user"]["id"]}/following/',
            params=params,
            cookies=cookies,
            headers=headers,
        ).json()
        response2.extend(res['users'])
        if len(res['users']) == 0:
            break;
        params['max_id'] += params['count']
        
    params = {
        'count': 100,
        'max_id': 0,
    }

    response3 = []
    while True:
        res = requests.get(
            f'https://www.instagram.com/api/v1/friendships/{response1["data"]["user"]["id"]}/followers/',
            params=params,
            cookies=cookies,
            headers=headers,
        ).json()
        response3.extend(res['users'])
        if len(res['users']) == 0:
            break;
        params['max_id'] += params['count']



    response = {
        'user': response1['data']['user'],
        'following': response2,
        'followers': response3
    }
    return response

# json.dump(response, open('sample.json', 'w'), indent=4)