import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
    fig, ax= plt.subplots()
    ax.bar(labels,values)
    ax.tick_params(axis='x', rotation=45)
    plt.savefig('./img/bar.png')
    plt.close()

def generate_pie_chart(labels,values):
    fig, ax= plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.xticks(rotation=20)
    plt.savefig('./img/chart_pie.png')
    plt.close() 