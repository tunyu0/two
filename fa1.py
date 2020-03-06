# 密碼是s03131047
# 最多3次機會

time = 3
while time > 0:
    password = input("請輸入密碼:")
    if password == 's03131047':
        print("登入成功")
        break
    else:
        time = time - 1
        print("密碼錯誤! 還有", time, "次機會")

