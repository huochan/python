import logging
import pickle
import pandas as pd
import re
## 导入模型
with open('./file', 'rb') as f:
    rf = pickle.load(f)


for i in range(10000):
    print("输入 # 退出预测！")

    input_X = input("请按顺序依次输入变量数值（年龄、BMI、血小板、黄体生成素、雌二醇、获卵数），以空格分割：")
    ## 35 18.95 174	4.45 862.30	5   (1)
    ## 41 21.45 319 3.43 757.8 3 (0)
    if "#" not in input_X:
            data={}
            data_list=[]
            data["age_rkxzl"]=input_X.split(" ")[0]
            data["BMI_rkxzl"]=input_X.split(" ")[1]
            data["pltores_xcg"]=input_X.split(" ")[2]
            data["LHores_sysjc"]=input_X.split(" ")[3]
            data["E2ores_sysjc"]=input_X.split(" ")[4]
            data["hls_lczl"]=input_X.split(" ")[5]
            data_list.append(data)
            new_X = pd.DataFrame(data_list )
            preds = rf.predict(new_X)


            print("预测结果：",preds[0])

    else:
        break