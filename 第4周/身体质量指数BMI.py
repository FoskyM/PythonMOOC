height, weight = eval(input())
bmi = weight / pow(height, 2)
print("BMI数值为:{:.2f}".format(bmi))

internation, nation = "", ""

if bmi < 18.5:
    internation, nation = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    internation, nation = "正常", "正常"
elif 24 <= bmi < 25:
    internation, nation = "正常", "偏胖"
elif 25 <= bmi < 28:
    internation, nation = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    internation, nation = "偏胖", "肥胖"
else:
    internation, nation = "偏胖", "肥胖"
print("BMI指标为:国际'{0}',国内'{1}'".format(internation, nation))