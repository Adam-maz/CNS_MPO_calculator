# CNS_MPO_calculator
Here I provide code that allows users to calculate the MPO CNS score for their molecules based on SMILES and known pKa values. 

CNS MPO is a very useful ADMET filter designed for molecules targeting the central nervous system (CNS). Developed by Wager T. and colleagues [1,2] it is used to test the bioavailability of candidate drugs acting on the CNS.
According to drug design and optimization, the higher (max. 6, min. 1) the CNS MPO score, the more promising the compound.

Here I present 2 Python classes: CNS_MPO_single_molecule() and CNS_MPO_csv_to_df(). First class can calculate the CNS MPO of one or more compounds (lists of SMILES and pKa values ​​are required).
The second class does the same, but as input the code reads a CSV file (mandatory: values ​​separated by a semicolon).

Within this repository I have included: a) cns_mpo_single_molecule code, b) cns_mpo_csv_to_df code, c) example_of_use code which explains how to use each class properly,
d) csv_file with_example_particles and e) csv_file_instruction.

**References:**
1. Wager T. et al. *"Moving beyond Rules: The Development of a Central Nervous System Multiparameter Optimization (CNS MPO) Approach To Enable Alignment of Druglike Properties"*
2. Wager T. et al. *"Central Nervous System Multiparameter Optimization Desirability: Application in Drug Discovery"*
3. RDKit documentation (https://www.rdkit.org/docs/#)
