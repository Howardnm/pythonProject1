TempStr = input()
if TempStr[0:3] in ['RMB']:
    USD = eval(TempStr[3:])/6.78
    print("USD{:.2f}".format(USD))
elif TempStr[0:3] in ['USD']:
    RMB = eval(TempStr[3:])*6.78
    print("RMB{:.2f}".format(RMB))
