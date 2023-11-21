# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 5
Version: v0.1.0
"""

import pandas as pd

file_path = "./data/466920.csv"
df = pd.read_csv(file_path)
"""
-9991 儀器故障待修無資料,
-9996 資料累計於後,
-9997 因不明原因或故障等因素無資料,
-9998 雨跡(Trace),
-9999 未觀測而無資料
"""

df = df.replace(-9991, 0)
df = df.replace(-9996, 0)
df = df.replace(-9997, 0)
df = df.replace(-9998, 0)
df = df.replace(-9999, 0)

df_2017 = df[df['year'] == 2017]

year_avg_temp = df_2017['TX01'].mean()
year_total_prep = df_2017['PP01'].sum()

month_avg_temp = df_2017.groupby('month')['TX01'].mean()
month_total_prep = df_2017.groupby('month')['PP01'].sum()

year_max_temp = df_2017['TX01'].max()
year_max_temp_time = df_2017[df_2017['TX01'] == year_max_temp]['yyyymmddhh'].iloc[0]
year_min_temp = df_2017['PP01'].min()
year_min_temp_time = df_2017[df_2017['PP01'] == year_min_temp]['yyyymmddhh'].iloc[0]

month_max_temp = df_2017.groupby('month')['TX01'].max()
month_min_temp = df_2017.groupby('month')['TX01'].min()

import os
import matplotlib.pyplot as plt

# Check if 'imgs' directory exists, if not, create it
if not os.path.exists("./imgs"):
    os.makedirs("./imgs")

x_month = [*range(1, 13, 1)]

fig, ax1 = plt.subplots(figsize=(8, 6))

ax1.plot(x_month, month_max_temp.values, "-o")
ax1.plot(x_month, month_avg_temp.values, "-o")
ax1.plot(x_month, month_min_temp.values, "-o")

ax1.set_ylabel("Temperature (°C)")


ax2 = ax1.twinx()
ax2.bar(x_month, month_total_prep.values, alpha=0.5)

ax2.set_ylabel("Precipitation (mm)")

ax1.legend(
    ["max temp", "avg temp", "min temp"], 
    loc ="upper left",
)
ax2.legend(
    ["total prepicitation"], 
    loc="upper right",
)

plt.xlim(0, 13)
plt.grid()
ax1.set_xticks(x_month)
ax1.set_xlabel("Month")
plt.title("Total precipitation and Temperature diversity in 2017 by TA")

plt.savefig("./imgs/q05_plot.jpg", dpi=300)
plt.show()
