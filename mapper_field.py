import pandas as pd 

df1 = pd.read_csv('master_file.csv')
df2 = pd.read_csv('slave_file.csv')

nick_name = df2.loc[:, 'nick_name']
gender = df2.loc[:, 'gender']

output_name = pd.concat([df1.loc[:, 'name'],nick_name]).reset_index(drop=True)
output_sex  = pd.concat([df1.loc[:, 'sex'],gender]).reset_index(drop=True)
output_age  = pd.concat([df1.loc[:, 'age'],gender]).reset_index(drop=True)

df = pd.concat([output_name, output_sex, output_age], axis = 1)
header = list(df1.columns.values)
df.columns = header

output = df.to_csv('output.csv', index=False)