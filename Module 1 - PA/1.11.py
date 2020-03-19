#Client name: Professor Laura Atkins
#Programmer name: Brendna Boyle
#PA Purpose: This shows the gradual increase of a given population once the birth, death, and immigrant rates are known.
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

secondsInYear = (60*60*24*365)
birth = (secondsInYear // 7.0)
death = (secondsInYear // 13.0)
immigrant = (secondsInYear // 45.0)
population = (312031486)

yearOnePopulation = (population + birth - death + immigrant)
yearTwoPopulation = (yearOnePopulation + birth - death + immigrant)
yearThreePopulation = (yearTwoPopulation + birth - death + immigrant)
yearFourPopulation = (yearThreePopulation + birth - death + immigrant)
yearFivePopulation = (yearFourPopulation + birth - death + immigrant)

print("Original Population:", population)
print("If someone is born every 7 seconds, someone dies every 13 seconds, and an immigrant arrives every 45 seconds, then the population:")
print("After one year:", yearOnePopulation)
print("After two years:", yearTwoPopulation)
print("After three years:", yearThreePopulation)
print("After four years:", yearFourPopulation)
print("After five years:", yearFivePopulation)


