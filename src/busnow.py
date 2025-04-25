import requests

# 使用者輸入要查的站名
stop_name = input("請輸入站牌名稱（完整或部分，例如：文化中心）：")

# PTX API（台南市所有公車即時預估到站資料）
url = "https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Tainan?$format=JSON"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    found = False
    print(f"\n📍 找到以下即將抵達『{stop_name}』的公車：\n")
    for item in data:
        stop = item.get("StopName", {}).get("Zh_tw", "")
        if stop_name in stop and item.get("EstimateTime") is not None:
            route = item.get("RouteName", {}).get("Zh_tw", "未知路線")
            plate = item.get("PlateNumb", "未提供")
            seconds = item["EstimateTime"]
            minutes = seconds // 60
            remain_sec = seconds % 60
            print(f"🚌 路線：{route}｜車牌：{plate}｜預估抵達：{minutes} 分 {remain_sec} 秒後")
            found = True

    if not found:
        print("⚠️ 沒有找到即將進站的公車或站名錯誤")
else:
    print("❌ 無法取得即時資料，狀態碼：", response.status_code)
