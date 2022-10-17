# 松田雄飛
# gmail:sansctipt0550@gmail.com

# python selection.py or python3 selection.py
print("--------input type--------")
print("sometime starttime endtime")
print("exsample: 3 22 5")
print("--------------------------")
some_time, start_time, end_time = map(int, input().split()) # ある時刻と、時間の範囲(開始時刻と終了時刻)を受け取る

if start_time < end_time: # 開始時刻が22時で終了時刻が5時、というような指定をされても動作する
    if start_time <= some_time < end_time: # 範囲指定は、開始時刻を含み、終了時刻は含まない
        print('ある時刻を含みます')
    else:
        print('ある時刻を含みません')
else: # 開始時刻が5時で終了時刻が22時、というような指定をされても動作する
    if start_time <= some_time or some_time < end_time:
        print('ある時刻を含みます')
    else:
        print('ある時刻を含みません')