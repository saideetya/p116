#Uploading the csv
from google.colab import files
data_to_load = files.upload()

import pandas as pd
import plotly.express as px

df = pd.read_csv("Admission_Predict.csv")

toefl_score = df["TOEFL Score"].tolist()
result = df["Chance of admit"].tolist()



fig = px.scatter(x=toefl_score, y=result)
fig.show()