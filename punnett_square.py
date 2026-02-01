def punnett_square(parent1, parent2):
    results = []

    for allele1 in parent1:
        for allele2 in parent2:
            results.append(allele1 + allele2)

    return results


parent1 = "Aa"
parent2 = "Aa"

offspring = punnett_square(parent1, parent2)

print("Punnett Square Results:")
for child in offspring:
    print(child)
