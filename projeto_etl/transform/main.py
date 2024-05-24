from transform import Transform 

if __name__ == "__main__":
    path = '..\..\data\data.jsonl'
    transform = Transform(path)
    df = transform.create_dataFrame()
    print(df)