import matplotlib.pyplot as plt

# Data
labels = ["ГБ", "Стенокардия", "Инфаркт миокарда", "Желудочковая экстрасистолия", "Мерцательная аритмия",
          "ХСН", "НК"]
sizes = [10, 9, 8, 1, 1, 10, 6]

colors = ['#506D2F', '#2a2922', '#f3ebdd', '#7d5642']
# Plot
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(sizes, startangle=-40, colors=colors)

# Inner circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add labels
ax.legend(wedges, labels,
          title="болезни",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(texts, size=12, weight="bold")
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%')
ax.set_title("imt")

plt.show()

# plt.pie(sizes, labels=labels, colors=colors,
#         autopct='%1.1f%%')
#
# plt.axis('equal')
# plt.show()
