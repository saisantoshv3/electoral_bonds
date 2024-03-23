import pandas as pd

parties=pd.read_csv("/Users/apple/Desktop/projects/electoral_bonds/encashed.csv",index_col=False)

companies=pd.read_csv("/Users/apple/Desktop/projects/electoral_bods/purchased.csv",index_col=False)

final_dataset=parties.merge(companies,how="outer",left_on=['Prefix','Bond Number'],right_on=['Prefix','Bond Number'])

renamed_columns={'Date of Encashment':'date_of_encashment','Name of the Political Party':'political_party_name','Prefix':'prefix',
                                'Bond Number':'bond_number','Denominations_x':'amount', 'Pay Branch Code':'pay_branch_code',
       'Reference No (URN)':'reference_number_URN', 'Journal Date':'journam_date', 'Date of Purchase':'date_of_purchase',
       'Date of Expiry':'date_of_expiry', 'Name of the Purchaser':'purchaser_name',
       'Issue Branch Code':'issue_branch_code', 'Status':'status'}

final_dataset=final_dataset.rename(columns=renamed_columns)

final_columns=['date_of_encashment','political_party_name','prefix','bond_number','amount','pay_branch_code',
     'reference_number_URN','journam_date','date_of_purchase','date_of_expiry','purchaser_name',
     'issue_branch_code','status']

final_dataset=final_dataset.sort_values(by='date_of_encashment')
print(final_dataset[final_columns].to_csv("/Users/apple/Desktop/projects/electoral_bonds/final.csv",index=0))