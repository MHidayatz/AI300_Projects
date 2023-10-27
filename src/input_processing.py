import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np


# def format_model_inputs(input_dict):
#     contractType = input_dict['contractType']
#     internet_type = input_dict['internetType']
#     payment_method = input_dict['paymentMethod']
#     stream_music = input_dict['streamMusic']
#     paperless_billing = input_dict['paperlessBilling']
#     married = input_dict['married']
#     has_premium_tech_support = input_dict['premiumTechSupport']
#     num_referrals = int(input_dict['numReferrals'])
#     num_dependents = int(input_dict['numDependents'])
#     age = int(input_dict['age'])
#     total_charges_quarter = float(input_dict['totalCharges'])
#     tenure_months = int(input_dict['tenureMonths'])
#     avg_gb_download_monthly = int(input_dict['avgGbDownload'])
#     total_long_distance_fee = float(input_dict['totalLongDistanceFee'])
#     avg_long_distance_fee_monthly = float(input_dict['avgLongDistanceFee'])

#     return [contractType, internet_type, payment_method, stream_music, \
#                  paperless_billing,married, has_premium_tech_support, num_referrals, num_dependents, age, \
#                       total_charges_quarter, tenure_months, avg_gb_download_monthly, \
#                         total_long_distance_fee, avg_long_distance_fee_monthly]

def format_model_inputs(input_dict):
    # Extract values from the input dictionary
    contract_type = input_dict['contractType']
    internet_type = input_dict['internetType']
    payment_method = input_dict['paymentMethod']
    stream_music = input_dict['streamMusic']
    paperless_billing = input_dict['paperlessBilling']
    married = input_dict['married']
    has_premium_tech_support = input_dict['premiumTechSupport']
    num_referrals = int(input_dict['numReferrals'])
    num_dependents = int(input_dict['numDependents'])
    age = int(input_dict['age'])
    total_monthly_fee = float(input_dict['total_monthly_fee'])
    tenure_months = int(input_dict['tenureMonths'])
    avg_gb_download_monthly = int(input_dict['avgGbDownload'])
    total_long_distance_fee = float(input_dict['totalLongDistanceFee'])
    avg_long_distance_fee_monthly = float(input_dict['avgLongDistanceFee'])

    # Create a DataFrame from the features
    df = pd.DataFrame({
        'age': [age],
        'married': [married],
        'num_dependents': [num_dependents],
        'tenure_months': [tenure_months],
        'num_referrals': [num_referrals],
        'internet_type': [internet_type],
        'has_premium_tech_support': [has_premium_tech_support],
        'contract_type': [contract_type],
        'paperless_billing': [paperless_billing],
        'payment_method': [payment_method],
        'avg_long_distance_fee_monthly': [avg_long_distance_fee_monthly],
        'total_long_distance_fee': [total_long_distance_fee],
         'avg_gb_download_monthly': [avg_gb_download_monthly],
        'stream_music': [stream_music],
        'total_monthly_fee': [total_monthly_fee]
              
    })
    
    #print(df)
    #print(df['num_referrals'])


    # Label encode the categorical features
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
    
    # Scale the numerical features
    # numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    # scaler = StandardScaler()
    # df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    # Convert the DataFrame back to a list
    formatted_list = df.values.tolist()[0]

    print(formatted_list)

    return formatted_list