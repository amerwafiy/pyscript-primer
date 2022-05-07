import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = (18,15)
plt.rcParams.update({'font.size': 14})

df = pd.read_csv('vax_malaysia.csv')
df = pd.DataFrame(df.groupby(pd.PeriodIndex(df['date'], freq="M"))['daily'].sum().reset_index())
df['date'] = df['date'].astype(str)
df = df[:-1]

fig, ax = plt.subplots()
x = ['Feb 21', 'Mac 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21',
     'Dec 21', 'Jan 22', 'Feb 22', 'Mac 22', 'Apr 22', 'May 22']
plt.plot(x, df['daily'], marker='o', linestyle='--', color='r')
ax.ticklabel_format(useOffset=False, style='plain', axis = 'y')

for i, v in enumerate(df['daily']):
    ax.text(i, v+200000, "%d" %v, ha="center", size ='large')

plt.ylim(-100, 15000000)
plt.ylabel('Total vaccine dosses administered',size = 'x-large')
plt.title('MONTHLY VACCINE DOSES ADMINISTERED', size = 'x-large', weight ='bold' )
fig
