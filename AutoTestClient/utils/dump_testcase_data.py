import openpyxl
import pickle

test_case_all=[]

wb=openpyxl.load_workbook('******************************************.xlsx')

sheet=wb['通用网关预测试用例']

test_case = {
    'id':'',
    'level':'',
    'head':'',
    'pre_step':'',
    'step':'',
    'target':'',
    'result':''
}

for row in sheet[11:55]:
    i=0
    for key in test_case:
        if i == 6:
            break
        try:
            test_case[key] = row[:6][i].value.replace('_x000D_','').replace('\n','<br>')
        except:
            test_case[key] = row[:6][i].value
        i = i+1
    print(test_case)
    test_case_all.append(test_case.copy())

with open('data_model/test_case.pickle','wb') as f:
    pickle.dump(test_case_all,f)
