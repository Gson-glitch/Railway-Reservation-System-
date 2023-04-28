from datetime import datetime
from utils import calculate_age
import pandas as pd

# LOADING THE DATASETS
booked_df = pd.read_csv("./datasets/booked-1.csv")
booked_df.columns = [col_name.strip() for col_name in booked_df.columns]

passenger_df = pd.read_csv("./datasets/Passenger-1.csv")
passenger_df.columns = [col_name.strip() for col_name in passenger_df.columns]
passenger_df["full_names"] = passenger_df[['first_name', 'last_name']].agg(' '.join, axis=1) # creating a new column with both names
passenger_df.insert(2, 'full_names', passenger_df.pop('full_names'))  # rearrange the columns so that the fullt_names column is right next to last_name column
passenger_df["bdate"] = passenger_df["bdate"].apply(lambda x: str(datetime.strptime(x, "%m/%d/%Y")))
passenger_df["age"] = passenger_df["bdate"].apply(lambda x: calculate_age(x))

train_status_df = pd.read_csv("./datasets/Train_status.csv")
train_status_df.columns = [col_name.strip() for col_name in train_status_df.columns]
train_status_df["TrainDate"] = train_status_df["TrainDate"].apply(lambda x: str(datetime.strptime(x, "%d/%m/%Y")))

train_df = pd.read_csv("./datasets/Train.csv")
train_df.loc[0, ("AvailableOn")] = "(Monday, Tuesday, Wednesday, Thursday, Friday)"
train_df.columns = [col_name.strip() for col_name in train_df.columns]

# print(booked_df.head())
data = {
    "book": booked_df,
    "passenger": passenger_df,
    "train_status": train_status_df,
    "train": train_df,
}


def load_data(data_frame):
    if data_frame not in data.keys():
        return f"No data frame with the name: {data_frame} from {list(data.keys())}"
    return data[data_frame]


# print(load_data("passenger"))
