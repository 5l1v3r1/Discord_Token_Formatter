
loop = True
while loop:
 tokold = input('Token: \n')

 res = tokold.rpartition(':')[-1]
 toknew = open('newtokens.txt', 'a')
 toknew.write(f"{res}" + "\n")
 toknew.close()
 print('Ок')
 