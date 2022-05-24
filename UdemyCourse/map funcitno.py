def sotudent_card(std):
    print(std[0], "Name \t", std[1], "roll")


std_list = [1, 15124, 1292, 40]
print(map(sotudent_card, std_list))
for item in map(sotudent_card, std_list):
    print(item)
