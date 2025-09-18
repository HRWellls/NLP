import matplotlib.pyplot as plt
import numpy as np


prompt_lengths = [5, 7, 10,29]  # 三个提示词的长度
accuracy_rates = [0.6, 0.44, 0.44,0.34]  # 对应的模型准确率

# 创建图表
plt.figure(figsize=(8, 6))

# 绘制折线图
plt.plot(prompt_lengths, accuracy_rates, 
         marker='o',  # 数据点标记为圆形
         linestyle='-',  # 实线连接
         color='b',  # 蓝色线条
         linewidth=2,  # 线宽
         markersize=8)  # 标记大小

# 添加标题和标签
plt.title('Prompt Length vs Model Accuracy', fontsize=14)
plt.xlabel('Prompt Length ', fontsize=12)
plt.ylabel('Accuracy Rate', fontsize=12)

# 设置坐标轴范围
plt.xlim(min(prompt_lengths)-5, max(prompt_lengths)+5)
plt.ylim(min(accuracy_rates)-0.05, max(accuracy_rates)+0.05)

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 在每个数据点添加准确率标签
for x, y in zip(prompt_lengths, accuracy_rates):
    plt.text(x, y+0.01, f'{y:.2f}', 
             ha='center', 
             va='bottom',
             fontsize=10)

# 显示图表
plt.tight_layout()
plt.show()