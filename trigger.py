from curl_cffi import requests

url = "https://like.vn/api/mua-follow-tiktok/order"

payload = {
    "objectId": "https://www.tiktok.com/@food.great.2k",
    "server_order": "5",
    "giftcode": "",
    "amount": "10",
    "note": "",
}

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "api-token": "cac00df160426a80eb1b377dd33268a5",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "dnt": "1",
    "origin": "https://like.vn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://like.vn/mua-follow-tiktok",
    "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "x-csrf-token": "prnpKWpFyy2zVGE5jamWsHPhgR3BEJlpzkOWn5K4",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "_ga=GA1.1.1178009689.1754803296; _gcl_au=1.1.204792198.1754803296.585963872.1754803416.1754803435; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlMyYWFORzVFdzhBUzZTQWh1OU9FWWc9PSIsInZhbHVlIjoibVdsalRPU3ZNb0RMWkRFQ09OOVJzd2dhNlN1WWZiZUNHTXRYeUtQakJkaXZ3TzhSWlJtYU5zbHZweFFrZUxFdmJPVSt4UzMxWmhwd3NCWHF4blZRMUZCSlZTcDJudkgwb1BGQXJrZzNoeklvQUlwc0Q2MVhSU0F2K1ZmNnVNeExRcVFYSnVaUmZlWTMvV3Q2RnZUNXNmeFgzMTNIcnFHR1piQnNONElKT2JNZVU1Si9xbkV6Qi8xZU5pU3pHbG9FS3RYdHRpbXpEc3RKV3liUURGZEcxdThrcnhveU1wck14bGVnLy9EYjR1VT0iLCJtYWMiOiIzYTJjMGI1NWJkN2I5NjY3YmE5YmFmOTUzMzY2Yzc5ZjFlZTljMDgzZDY1ZGRhMGY4YWViMWU3YWIxNzlmMzM3IiwidGFnIjoiIn0%3D; _gcl_aw=GCL.1757238320.CjwKCAjw2vTFBhAuEiwAFaScwotYQspFg16DA8DJEVpt2fOss6sAKPGs2abVMKF9JRBYA-dX2w7-yBoCCKwQAvD_BwE; arcu-closed=1; cf_clearance=pVaDBU4vsIda2oXQSvgs1uexJToJEnAJq87kAQp8K8U-1757310307-1.2.1.1-dapJWwGQ95WeNopHPwkPd8nb2co8afegPcAO7EmmHknKvFCYgB1lSXCpsmIx6SFANdDqADSklx17TyYMf8EYg_PXh.qW.uhhdoeNTNp6LJp6sgm.s0wq2l1piN9mEGphxcwAf_tDD9oxmI4.eUpvUvhvwqGyiqkprahDcePv2iGdAPWq5J0NT2B2jGzsgXEv1AiJaLTraeXtqWRptsVXxP2yEfMIi6_G0h8PjfG7juc; _ga_PVY0H7ZJP0=GS2.1.s1757307946$o8$g1$t1757310322$j41$l0$h0",
}


tasks = [
    {
        "objectId": "https://www.tiktok.com/@food.great.2k",
        "api-token": "cac00df160426a80eb1b377dd33268a5",
        "x-csrf-token": "prnpKWpFyy2zVGE5jamWsHPhgR3BEJlpzkOWn5K4",
        "cookie": "_ga=GA1.1.1178009689.1754803296; _gcl_au=1.1.204792198.1754803296.585963872.1754803416.1754803435; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlMyYWFORzVFdzhBUzZTQWh1OU9FWWc9PSIsInZhbHVlIjoibVdsalRPU3ZNb0RMWkRFQ09OOVJzd2dhNlN1WWZiZUNHTXRYeUtQakJkaXZ3TzhSWlJtYU5zbHZweFFrZUxFdmJPVSt4UzMxWmhwd3NCWHF4blZRMUZCSlZTcDJudkgwb1BGQXJrZzNoeklvQUlwc0Q2MVhSU0F2K1ZmNnVNeExRcVFYSnVaUmZlWTMvV3Q2RnZUNXNmeFgzMTNIcnFHR1piQnNONElKT2JNZVU1Si9xbkV6Qi8xZU5pU3pHbG9FS3RYdHRpbXpEc3RKV3liUURGZEcxdThrcnhveU1wck14bGVnLy9EYjR1VT0iLCJtYWMiOiIzYTJjMGI1NWJkN2I5NjY3YmE5YmFmOTUzMzY2Yzc5ZjFlZTljMDgzZDY1ZGRhMGY4YWViMWU3YWIxNzlmMzM3IiwidGFnIjoiIn0%3D; _gcl_aw=GCL.1757238320.CjwKCAjw2vTFBhAuEiwAFaScwotYQspFg16DA8DJEVpt2fOss6sAKPGs2abVMKF9JRBYA-dX2w7-yBoCCKwQAvD_BwE; arcu-closed=1; cf_clearance=pVaDBU4vsIda2oXQSvgs1uexJToJEnAJq87kAQp8K8U-1757310307-1.2.1.1-dapJWwGQ95WeNopHPwkPd8nb2co8afegPcAO7EmmHknKvFCYgB1lSXCpsmIx6SFANdDqADSklx17TyYMf8EYg_PXh.qW.uhhdoeNTNp6LJp6sgm.s0wq2l1piN9mEGphxcwAf_tDD9oxmI4.eUpvUvhvwqGyiqkprahDcePv2iGdAPWq5J0NT2B2jGzsgXEv1AiJaLTraeXtqWRptsVXxP2yEfMIi6_G0h8PjfG7juc; _ga_PVY0H7ZJP0=GS2.1.s1757307946$o8$g1$t1757310322$j41$l0$h0",
    }
]


for task in tasks:
    try:
        payload["objectId"] = task["objectId"]
        headers["api-token"] = task["api-token"]
        headers["x-csrf-token"] = task["x-csrf-token"]
        headers["cookie"] = task["cookie"]
        resp = requests.post(
            url,
            headers=headers,
            data=payload,
            impersonate="chrome",
        )
        print(resp.status_code)
        print(resp.text)
    except Exception as e:
        print(e)

