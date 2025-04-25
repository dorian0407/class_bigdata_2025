import requests
import csv
import io

url = "https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=7F6BE616-8CE6-449E-8620-5F627C22AA0D"

response = requests.get(url)

if response.status_code == 200:
    # 用 io.StringIO 把 response.text 當作檔案來讀
    csv_file = io.StringIO(response.text)
    reader = csv.reader(csv_file)

    for row in reader:
        if row[0].isdigit():  # 確保是資料列，不是標題
            report_date = row[1]
            line_id = row[2]
            print(f"通報日期: {report_date}  |  Line ID: {line_id}")
else:
    print("下載失敗")
