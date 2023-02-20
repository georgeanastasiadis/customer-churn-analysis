import pandas as pd

df = pd.read_csv(r'Telco-Customer-Churn.csv')

#Label Encoding for categorical variables that contain only two unique values

gender = {'Female': 0, 'Male': 1}
partner = {'No': 0, 'Yes': 1}
dependents = {'No': 0, 'Yes': 1}
phone_service = {'No': 0, 'Yes': 1}
paperless_billing = {'No':0, 'Yes':1}
churn = {'No': 0, 'Yes': 1}

for key, value in df.iteritems():
    df['gender'] = df['gender'].apply(lambda x: gender.get(x,x))
    df['Partner'] = df['Partner'].apply(lambda x: partner.get(x, x))
    df['Dependents'] = df['Dependents'].apply(lambda x: dependents.get(x, x))
    df['PhoneService'] = df['PhoneService'].apply(lambda x: phone_service.get(x, x))
    df['PaperlessBilling'] = df['PaperlessBilling'].apply(lambda x: paperless_billing.get(x, x))
    df['Churn'] = df['Churn'].apply(lambda x: churn.get(x, x))

'''We are dropping customerID column because it won't give us information
   in the learning process'''
df = df.drop('customerID', axis=1)

df = pd.get_dummies(df, drop_first=True)

#remove duplicate rows cause they are of no use
df = df.drop_duplicates()

df.to_csv('Telco.csv', index=False)
