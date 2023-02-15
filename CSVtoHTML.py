import pandas as pd

df = pd.read_csv('data.csv')

html_string = df.to_html()

print("-------------- Start of HTML format --------------")
print(html_string)
print("-------------- End of HTML format --------------")
