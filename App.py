import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ==================== 1. 資料準備 ====================
# 排除 0% 的水，只留下 10, 20, 30, 40
x_concentration = [10, 20, 30, 40]

# 圖一所需 Y 軸數據：時間 AVG
y_time_avg = [51.11, 69.18, 85.26, 96.62]

# 圖二所需 Y 軸數據：相對黏度 y1 與 絕對黏度 y2
y1_relative_viscosity = [1.220, 1.610, 1.950, 2.163]
y2_absolute_viscosity = [0.9769, 1.289, 1.561, 1.732]


# ==================== 2. 開始畫圖 ====================
# 建立一個包含 1 行 2 列的畫布 (建立左右兩張圖)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))


# ------------------- 左圖 (圖一)：濃度 vs 時間 -------------------
ax1.plot(x_concentration, y_time_avg, marker='o', color='blue', label='Time AVG')
ax1.set_title('Concentration vs Time (Figure 1)')
ax1.set_xlabel('Concentration (%)')
ax1.set_ylabel('Time (sec)')
ax1.set_xticks(x_concentration)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()


# ------------------- 右圖 (圖二)：黏度 vs 濃度 -------------------
# 同時畫上 y1 (相對黏度) 和 y2 (絕對黏度)
ax2.plot(x_concentration, y1_relative_viscosity, marker='s', color='green', label='Relative Viscosity (y1)')
ax2.plot(x_concentration, y2_absolute_viscosity, marker='^', color='orange', label='Absolute Viscosity (y2)')

ax2.set_title('Viscosity vs Concentration (Figure 2)')
ax2.set_xlabel('Concentration (%)')
ax2.set_ylabel('Viscosity')
ax2.set_xticks(x_concentration)

# 【核心控制】設定右圖 Y 軸每隔 0.100 一個刻度，且顯示到小數點後三位
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.100))
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))

ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()


# ==================== 3. 調整並顯示 ====================
plt.tight_layout()  # 自動調整間距，防止圖表擠壓、標籤重疊
plt.show()
