message = "Su's Morning Coffee Updates"
myName = "Su Dogan"
fullmessage = "{} {}".format(message, myName)
print(fullmessage)
print(len(fullmessage))

numberofspaces = 51-len(fullmessage)
print(numberofspaces)

endspaces = ""
for x in range(numberofspaces):
	endspaces += " "

endspaces += '|'
fullmessage = fullmessage  + endspaces
#print(fullmessage)

from datetime import datetime
now = datetime.now()
current_time = "THE TIME IS", now.strftime("%H:%M")





print("""
-----------------------------------------------------------
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|      {}                                                 |
|                                                         |
|                                                         |
|      {}                                                 |
|                                                         |
|                                                         |
-----------------------------------------------------------
""".format(fullmessage, current_time))


from datetime import date   
today = date.today()
print("Date:", today)


