import sys
def lines_to_dict(lines):
    out = {}
    for line in lines:
        ls = line.split()
        ls[0] = int(str(ls[0].replace("_","")))
        if len(ls)>1:
            out[ls[0]] = ls[1]
    return out
def my_scoring_function(ref,res):
    try:
        refdic = lines_to_dict(open(ref).readlines())
        resdic = lines_to_dict(open(res).readlines())
    except:
        print("Could not read the solution files")
    truepos = 0.0
    trueneg = 0.0
    totalpos = 0.0
    totalpreds = 0.0
    for key in refdic.keys():
        if str(refdic[key]) != '0':
            totalpos +=1
            if key in resdic.keys():
                if str(resdic[key]) ==  str(refdic[key]):
                    truepos+=1
                    totalpreds+=1
        else:
            if key in resdic.keys():
                if str(resdic[key]) !=  str(refdic[key]):
                    totalpreds+=1
                else:
                    trueneg+=1
    pre = 0.0
    rec = 0.0
    if totalpreds == 0:
        pre = 0.0
    else:
        pre = truepos/totalpreds

    if totalpos == 0:
        rec =1
    else :
        rec = truepos/totalpos
    f1 = 2 * (pre*rec) / (pre+rec)

    return pre,rec,f1

def task12_eval(solution_file,prediction_file):
    pre,rec,f1 = my_scoring_function(solution_file,prediction_file)
    print("Precision : %0.4f" %pre)
    print("Recall : %0.4f" %rec)
    print("F1 : %0.4f" %f1)

if __name__ == "__main__":
    args = sys.argv
    if args[1] == '-h':
        print("Run the script as follows:\n")
        print("python task3_eval.py [solution_file_path] [predict_file_path]")
        exit()
    if len(args)!=3:
        raise IOError('Missing arguments ')
    task12_eval(args[1],args[2])
