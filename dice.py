import random
#import plotly.express as px 
import plotly.figure_factory as ff

dice_result = []
#count = []

for I in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
 #   count.append(I)

#fig = px.bar(x = dice_result, y = count)
fig = ff.create_distplot([dice_result], ["Result"])
fig.show()