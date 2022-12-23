def main():
  mom = input("Enter mom's alleles ")
  dad = input("Enter dad's alleles ")
  if len(mom) != len(dad):
    print("Mom and dad must have the same amount of alleles")
    return 1
  punnettSquare(mom, dad)

def punnettSquare(mom, dad):
  length = len(mom)
  dadPairs = []
  momPairs = []
  for i in range(0, length, 2):
    momPairs.append(mom[i:i+2])
    dadPairs.append(dad[i:i+2])
  

  halfLength = int(length / 2)
  
  momRow = allStrings(momPairs, "", halfLength, halfLength)
  dadRow = allStrings(dadPairs, "", halfLength, halfLength)

  tableSideLength = len(momRow)

  punnettSquare = [[0 for i in range(tableSideLength)] for j in range(tableSideLength)]
  genotypeRatio = {}
  count = 0

  for momIndex in range(tableSideLength):
    for dadIndex in range(tableSideLength):
      genotype = ""
      for aIndex in range(halfLength):
        momAllele = momRow[momIndex][aIndex]
        dadAllele = dadRow[dadIndex][aIndex]
        firstAllele = momAllele
        secondAllele = dadAllele
        if dadAllele.isupper() and momAllele.islower():
          firstAllele = dadAllele
          secondAllele = momAllele
        genotype += f"{firstAllele}{secondAllele}"
      punnettSquare[momIndex][dadIndex] = genotype
      genotypeRatio[genotype] = genotypeRatio.get(genotype, 0) + 1

  for row in range(tableSideLength):
    for col in range(tableSideLength):
      print(punnettSquare[row][col])
      count += 1
  print(count)

  for (key, value) in genotypeRatio.items():
    print(f"{key}: {value}")
  

def allStrings(sets, string, k, n):
  if k == 0:
    return [string]
  
  returnSet = []
  
  for i in sets[n - k]:
    
    newString = string + i

    returnString = allStrings(sets, newString, k - 1, n)
    returnSet += returnString

  return returnSet

if __name__ == "__main__":
  main()
