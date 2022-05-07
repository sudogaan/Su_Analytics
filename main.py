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
print(fullmessage)

print("""
-----------------------------------------------------------
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|      {}                                                 |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
|                                                         |
-----------------------------------------------------------
""".format(fullmessage))





from datetime import date
  
today = date.today()
print("Date:", today)


