import numpy as np
import matplotlib.pyplot as plt

CHART_TITLE = "My First Chart"  # เปลี่ยนชื่อ chart ตรงนี้ที่เดียว

np.random.seed(19680801)

fig, axs = plt.subplots(3, 3, figsize=(13, 11))
fig.suptitle(CHART_TITLE, fontsize=18, fontweight="bold")


def label(ax, title, xlabel, ylabel):
    """กำหนด Title, X, Y label ให้ทุก graph"""
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(xlabel, fontsize=8)
    ax.set_ylabel(ylabel, fontsize=8)


# ---------------- แถวที่ 1 ----------------
# 1) Scatter + colormap + colorbar
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
ax = axs[0, 0]
sc = ax.scatter(x, y, c=colors, cmap="viridis", s=10)
fig.colorbar(sc, ax=ax, label="Color Value")
label(ax, "Scatter with Colormap", "X value", "Y value")

# 2) Scatter bubbles (size + alpha) + colorbar
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)
ax = axs[0, 1]
sc = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap="nipy_spectral")
fig.colorbar(sc, ax=ax, label="Color Value")
label(ax, "Scatter Size and Alpha", "X value", "Y value")

# 3) Horizontal bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
ax = axs[0, 2]
ax.barh(x, y, height=0.1, color="darkblue")
label(ax, "Horizontal Bars", "Value", "Category")

# ---------------- แถวที่ 2 ----------------
# 4) Line + grid
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
ax = axs[1, 0]
ax.plot(x, y)
ax.grid(color="green", linestyle="--", linewidth=0.5)
label(ax, "Sports Watch Data", "Average Pulse", "Calorie Burnage")

# 5) Two lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
ax = axs[1, 1]
ax.plot(y1, label="Line 1")
ax.plot(y2, label="Line 2")
ax.legend(fontsize=7)
label(ax, "Two Lines", "Index", "Value")

# 6) Line + markers
ypoints = np.array([3, 8, 1, 10])
ax = axs[1, 2]
ax.plot(ypoints, marker="o", ms=8, mec="r", mfc="r", color="purple")
label(ax, "Line with Markers", "Index", "Value")

# ---------------- แถวที่ 3 ----------------
# 7) Histogram
x = np.random.normal(170, 10, 250)
ax = axs[2, 0]
ax.hist(x, bins=10, edgecolor="white")
label(ax, "Histogram of Heights", "Height (cm)", "Frequency")

# 8) Pie + explode
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
ax = axs[2, 1]
ax.pie(y, labels=mylabels, explode=[0.2, 0, 0, 0], startangle=90)
label(ax, "Pie Chart with Explode", "Fruit", "Share")

# 9) Pie + legend
ax = axs[2, 2]
ax.pie(y, labels=mylabels, startangle=90)
ax.legend(title="Four Fruits:", fontsize=6, loc="upper right", bbox_to_anchor=(1.25, 1.15))
label(ax, "Pie Chart with Legend", "Fruit", "Share")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("my_first_chart.png", dpi=120)
plt.show()
