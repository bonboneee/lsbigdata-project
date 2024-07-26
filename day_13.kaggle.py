import pandas as pd
house_df = pd.read_csv("data/house price/train.csv")
house_df.shape

price_mean = house_df['SalePrice'].mean()
price_mean

sub_df = pd.read_csv("data/house price/sample_submission.csv")
sub_df


sub_df['SalePrice'] =  price_mean
sub_df

sub_df.to_csv("./data/housepricesample_submission.csv", index = False)


