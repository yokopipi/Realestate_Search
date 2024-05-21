def station_serch():
    import pandas as pd
    
    # 空のデータフレームを定義するための列名
    columns = ['station_name', 'main_line', 'ward','time_to_target1', 'time_to_target2','average_rent','num_properties']

    # 空のデータフレームを作成
    df = pd.DataFrame(columns=columns)

    # 追加するサンプルデータ
    sample_data = [
        ["平和島", '京急線', '大田区',30, 20,100000,56],
        ["品川", '京急線', '大田区',30, 20,130000,30],
        ["品川", '京急線', '大田区',30, 20,130000,30],
        ["品川", '京急線', '大田区',30, 20,130000,30],
        ["品川", '京急線', '大田区',30, 20,130000,30],
        ["品川", '京急線', '大田区',30, 20,130000,30],
    ]

    # サンプルデータをデータフレームに追加
    df = pd.DataFrame(sample_data, columns=columns)


    return df