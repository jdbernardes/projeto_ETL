from transform import Transform 

if __name__ == "__main__":
    path = '..\..\data\data.jsonl'
    db_path='..\..\data\ml.db'
    transform = Transform(path)
    df = transform.create_dataFrame()
    transform.save_data_DB(df, db_path)
    df.head()