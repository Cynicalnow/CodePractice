import pandas as pd
user=pd.read_csv(r"C:\Users\Cynical\Desktop\ml-100k\u.user",sep="|",names=["User_id","Age","Gender","Occupation","Zip_code"])
print(user.dtypes)
