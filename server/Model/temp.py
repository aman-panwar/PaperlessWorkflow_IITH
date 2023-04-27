
def show(d, indent =0 ):
    if(isinstance(d,list)):
        for x in d:
            print('')
            print("    "*indent + f">{x}:", end=' ')
            if isinstance(x, dict):
                print('')
                show(x, indent=indent+1)
            elif isinstance(x, list):
                print('')
                print("    "*indent+ '[')
                for i ,ele in enumerate(x):
                    print('    '*indent,'>', f"ele {i} {type(ele)}")
                    show(ele, indent=indent+1)
                print("    "*indent+ ']')
    elif(isinstance(d,dict)):
        for x in d:
            print("    "*indent + f">{x} {type(d[x])}:", end=' ')
            if isinstance(d[x], dict):
                print('')
                show(d[x], indent=indent+1)
            elif isinstance(d[x], list):
                print('')
                print("    "*indent+ '[')
                for i ,ele in enumerate(d[x]):
                    print('    '*indent,'>', f"ele {i} {type(ele)}")
                    show(ele, indent=indent+1)
                print("    "*indent+ ']')
            else: print(d[x])
    else:
        print('    '*indent, '>',d)


# from Model.form import *
# from Model.data import *
# F = Form('644957e16158406dd10333b3')
# # F.applicant_id = 'i_want_to_sleep.com'
# # my_f = Dropdown("dfdf", ['sdfsd', 'kkkkk'],"SDFsd")
# # F.data.append_field(time.time(), "sdf", 4, 34, my_f)
# # F.save_to_db()


# d = F.to_dict()
# show(d)
