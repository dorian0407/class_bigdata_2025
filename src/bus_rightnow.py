import requests
import json

url = 'https://2384.tainan.gov.tw/IMP/jsp/rwd_api/ajax_routeinfo_pathattr.jsp?id=10451&Lang=cht'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://2384.tainan.gov.tw/newtnbusweb/ebusInfo.html?Lang=cht',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    try:
        outer = response.json()
        data = outer.get("data", [])  # ⬅️ 正確地從外層 dict 拿出資料

        print("\n✅ 即時站點資訊如下：\n")

        has_data = False
        for stop in data:
            car_no = stop.get("carNo", "")
            stop_name = stop.get("stopInfo", "未知站名")
            car_dist = stop.get("carDist", "未知距離")
            if car_no:
                print(f"🚌 車牌：{car_no} ➜ 即將到達 🚏 {stop_name}（距離 {car_dist} 公尺）")
                has_data = True

        if not has_data:
            print("⚠️ 目前無任何即將進站的車輛")
    except Exception as e:
        print("⚠️ JSON 處理失敗：", str(e))
else:
    print("❌ 抓取失敗，狀態碼：", response.status_code)
