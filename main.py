message = "Su's Morning Coffee Updates"

numberofspaces = 32-len(message)
print(numberofspaces)

endspaces = ""
for x in range(numberofspaces):
	endspaces += " "

endspaces += '|'
fullmessage = message + endspaces
#print(fullmessage)

print("""
----------------------------------------
|                                      |
|                                      |
|                                      |
|                                      |
|      {}                              |
|                                      |
|                                      |
|                                      |
|                                      |
|                                      |
---------------------------------------
""".format(fullmessage))





from datetime import date
  
today = date.today()
print("Date:", today)

#31 bosluk

