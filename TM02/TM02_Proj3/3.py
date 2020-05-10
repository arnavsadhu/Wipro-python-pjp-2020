dic={"Krishna":[22,33,44],"Ram":[33,44,53],"sita":[54,87,44],"Laxman":[88,77,99]}
q_name = input()

print("{0:.2f}".format(round(sum(dic[q_name]) / len(dic[q_name]), 2)))