# Example of CNS_MPO_single_molecule() use
x = CNS_MPO_single_molecule(
    smiles_list=[
        "C(C=1CCN(C5)CCC(C5)c(n4)c(c3o4)ccc(c3)F)(=O)N(C2)C(CCC2)=NC1C",
        "C1CNCC(C1C2=CC=C(C=C2)F)COC3=CC4=C(C=C3)OCO4",
    ],
    pKa_list=[8.765, 9.365],
)
print(x)


# Example of CNS_MPO_csv_to_df() use
filepath = 'path_to_CSV_files'
x = CNS_MPO_csv_to_df(csv_file=filepath)
print(x[1:3][['Id','MW']])  #1 user can specify columns and rows with slicing, which can enable him to get desired output
print(x[1:3]['Id'])  #2
print(x[1:3])  #3
print(x)  #4 but also user can get whole object

