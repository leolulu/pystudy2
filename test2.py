list1 = [0,1,2,3,4]

core_list = [{'orig_num':i} for i in list1]

for sn,i in enumerate(core_list):
    print(sn)
    try:
        if i['orig_num'] == 2:
            raise threeNum()
        i['result_num'] = i['orig_num'] + 10
        print(sn)
    except Exception as e:
        print(e)
        core_list.remove(i)
        print(sn)

print(core_list)