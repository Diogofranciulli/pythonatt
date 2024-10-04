a = [12,68,95,41,25,71]

print(a)

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)


def traducao_rnaM(rna):
    rna_to_amino = {
        "UUU": "Phe",
        "CUU": "Leu",
        "UUA": "Leu",
        "AAG": "Lisina",
        "UCU": "Ser",
        "UAU": "Tyr",
        "CAA": "Gln"
    }


    proteina = []

    # Iterate through the RNA string in steps of 3
    for i in range(0, len(rna), 3):
        triplet = rna[i:i + 3]
        if triplet in rna_to_amino:
            proteina.append(rna_to_amino[triplet])

    # Join the list of amino acids with hyphens
    return "-".join(proteina)


# Example usage
print(traducao_rnaM("UUU"
                    "UUAUCU"))  # Output: Phe-Leu-Ser
