smthn = [("abbyy",3),("ray",10),("thatguy",2)]
def check(smthn):
    current_best = 0
    current_best_holder = ""
    for employee,decades in smthn:
        if decades > current_best:
            current_best = decades
            current_best_holder = employee
        else:
            pass
    print(current_best,current_best_holder)