stuffinArray = ['car1','car2','car3','car4']
stuffinArray.insert(4,"car5")
stuffinArray.remove('car5')
wordstoputin = '\n Hello \n'
stuffindict = {
    "car1" : "somemake1",
    "car2" : "somemake2",
    "car3" : "somemake3"
    
}
stuffindict["car4"] = 'somemake4'
del stuffindict['car4']
with open('output.txt', 'w') as file:
    file.write(str(stuffinArray))
    file.write(wordstoputin)
    file.write(str(stuffindict))
with open('output.txt', 'r') as file:
    print(file.read())
try:
  print(x)
except:
  print("An exception occurred")