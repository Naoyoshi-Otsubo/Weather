import plotly.graph_objects as go
import pandas as pd 

#入力データ 
in_file = "data.csv" 

#トリミング後のデータ 
out_file = "osaka.csv" 

# CSVファイルを一行ずつ読み込み 
with open(in_file, "rt", encoding="Shift_JIS") as fr:
    lines = fr.readlines() 

# デフォルトのヘッダを削除して、新たなヘッダを作成 
headers = ["年","月","日","気温","1","2","降水量","3","4","5"]
body = []
for line in lines[5:]:
    line = line.strip().replace('/',',').split(',')
    datas = []
    for data in line:
        datas.append(float(data))
    body.append(datas)

df = pd.DataFrame(body, columns=headers)

"""
header = [",".join(headers)+"\n"]
lines = header + lines[5:]
lines = map(lambda v: v.replace('/', ','), lines) 
result = "".join(lines).strip()
# 結果をファイルへ出力 
with open(out_file, "wt", encoding="Shift_JIS") as fw: 
    fw.write(result)
print("saved.")
#df = pd.read_csv('osaka.csv', encoding="Shift_JIS") 
"""

fig = go.Figure(data=go.Scatter(x=(df['年'],df['月']), y=df['気温'], mode='markers')) 
fig.show()
