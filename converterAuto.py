L = []
F = []

#FUNCTIONS:
def listToMatrx(x,stat):    # Convert a list in a matrix
  mat = []
  i = 0
  while x != []:
   mat.append(x[:stat+1]) ####BUG FIX: ESTAVA SÓ STAT E ERA PARA SER STAT+1
   x = x[stat+1:]
   i += 1
  return mat

def dupliREM(sam_list):
    result = []
    for i in sam_list:
        if i not in result:
            result.append(i)
    return result

def statInMat(x,a,stat):  # Verify if the state is already in the matrix or not
  i = 0
  for j in range(stat):
    if a == x[i][0]:
      return 1
    i += 1
  return 0


def vall(x,rw,cm,val):  # Get the value in some state
    for i in range(rw):
        if(x[i][0] == val):
            if x[i][cm] == '-':   # when it's NULL
                return ''
            else:
                return x[i][cm]

def newRow(aux,cam,st,MRT):
    sqr = []
    NRw = []
    NRw.append(aux)
    sqr = aux.split(",")

    for j in range(cam):
        j += 1
        desc = []
        for i in range(len(sqr)):
            if(vall(MRT,st,j,sqr[i]) != ''):
                desc.append(vall(MRT,st,j,sqr[i]))

        for bb in range(len(desc)):
            Fnl = ','.join(desc)
        NRw.append(Fnl)

    ### Sorting the first column
    for ii in range(len(NRw)):
        sr = []
        sr = NRw[ii].split(",")
        sr.sort()
        rss = ','.join(dupliREM(sr))
        NRw[ii] = rss
    #######
    return NRw


#READ FILE
NameF = input("Qual o nome do arquivo? ")

with open(NameF, 'r') as file:
    for line in file:
      for word in line.split():
        L.append(word)

#Defining main variables
NumCam = int(L[0])
NumSTates = int(L[1])
FinalStates = L[2]
for i in range(3):  # Delete all, beside the content table
  L.pop(0)

# Now L is just the matrix, But it is still a list so
LMTR = listToMatrx(L,NumCam)  ####BUG FIX: ESTAVA NUMSTATES E ERA PARA PASSAR NUMCAM

F.append(LMTR[0])  # Fist line of our deterministic automata ( starting the new automata)

cont = 1        # keep the loop while it's needed ( While new states are added)
hy = 0

while hy != cont:    # MAIN:::::
    for j in range(NumCam):
        j += 1
        aux  = []
        if(statInMat(F,F[hy][j],cont) == 0):
            aux = F[hy][j]
            F.append(newRow(aux,NumCam,NumSTates,LMTR))
            cont += 1
    hy += 1


#print("REsult: ",F)

# Getting all final states
allFin = []
auxD = []
auxFin = FinalStates.split(",")
for hhg in range(len(F)):
    auxD = F[hhg][0].split(",")
    for hhgg in range(len(auxFin)):
        for gghh in range(len(auxD)):
            if auxFin[hhgg] == auxD[gghh]:
                allFin.append(F[hhg][0])

##

# WRITE THE NEW FILE
file1 = open('DeterministicAUTOMATA.txt', 'w')
file1.write("Qtd letters: "+str(NumCam)+'\n')  # qt letters
file1.write("Number of states: "+str(len(F))+'\n')  # Number of states
file1.write("FinalStates: "+str(allFin)+'\n')
for jj in range(len(F)):  # the matrix
    file1.write(str(F[jj])+'\n')
file1.close()

print("DONE :)")
print("Check in the directory for DeterministicAUTOMATA.txt")
