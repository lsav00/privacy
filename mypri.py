import csv
import os
import pandas as pd







play=True
while(play==True):
	print("Enter your knowledge:")
	print()
	old_pri=pd.read_csv("users.csv")
	da_key=input("Key: ")
	da_val=input("Value: ")

	my_pri=pd.DataFrame({"mykey":[da_key], "myvalue":[da_val]})

	new_pri=old_pri.append(my_pri)

	print(new_pri)

	new_pri.to_csv("users.csv", index=False)

	os.system("cls")
