# AES-128 Encryption and Cryptanalysis

## Overview
This repository contains the implementation of AES-128 encryption and two cryptanalysis techniques: CPA (Correlation Power Analysis) and DFA (Differential Fault Analysis) attacks. These attacks were conducted as part of a school project on a ATxmega128D4 microcontroller on a ChipWhisperer-Lite card 

## Repository Structure
```
|-- AES Code C/                          # AES-128 encryption implementation in C
|   |-- aes.c                            # AES encryption source code
|   |-- aes.h                            # Header file for AES functions
|   |-- main.c                           # Test file for AES encryption process
|
|-- CPA Attack/                          # CPA (Correlation Power Analysis) attack
|   |-- traces.npy                       # Power consumption traces (NumPy format)
|   |-- correlation figures/             # Correlation figures obtained during attack
|   |-- prediction matrices/             # Prediction matrices for attack analysis
|   |-- attack_code/                      # Attack implementation
|       |-- CPA Attack code full key  guess.py              # Python script to calculate the recovered key
|       |-- GenerateAll16PredictionMatrices.jl       # Julia script to generate prediction matrices
|       |-- PlotAll16Correlations.jl          # Julia script to plot correlation figures
|
|-- DFA Attack/                           # DFA (Differential Fault Analysis) attack
|   |-- DFA Attack code.py                     # Python script for DFA attack
|   |-- reverse key schedule.py           # Script to compute the master key
|   |-- entropy figures/                   # Entropy figures generated during attack
|   |-- ciphered-faulty-npy/                # Correct and faulty ciphertexts (NumPy format)
|


## AES-128 Implementation
The `AES Code C/` folder contains an implementation of AES-128 encryption in C. The implementation includes core functions such as:

- Key expansion
- SubBytes
- ShiftRows
- MixColumns
- AddRoundKey

### How to Compile and Run AES-128

```bash
cd "AES Code C"
gcc -o aes main.c aes.c -lm
./aes
```

## CPA Attack
The `CPA Attack/` folder contains the implementation of the Correlation Power Analysis attack. This attack exploits the correlation between power consumption and the Hamming Weight (HW) of intermediate values in the first SubBytes operation of the first AES round.

### CPA Attack Steps:
1. Collect power traces during encryption (provided as `traces.npy`).
2. Use the provided Julia scripts to generate prediction matrices and correlation figures.
3. Recover the AES key using the Python script.

### How to Run CPA Attack

```bash
cd "CPA Attack/attack_code"
python key_recovery.py
```

## DFA Attack
The `DFA Attack/` folder contains the implementation of the Differential Fault Analysis attack. This attack is based on Shannon entropy analysis applied to the last SubBytes operation of the final AES round, recovering the last round key and using the reverse key schedule to compute the master key.

### DFA Attack Steps:
1. Inject faults and analyze correct vs faulty ciphertexts.
2. Compute entropy to deduce the last round key.
3. Use the reverse key schedule script to derive the master key.

### How to Run DFA Attack

```bash
cd "DFA Attack"
python dfa_attack.py
python reverse_key_schedule.py
```

## Prerequisites
Ensure the following dependencies are installed before running the code:

- GCC compiler (for AES C code)
- Python (for attack scripts)
- Julia (for CPA attack analysis)
- NumPy and Matplotlib libraries
- Adapt the python and julia codes to have the correct directory of their inputs (traces,prediction matrices , etc.)
  


## Contact
For any questions or issues, feel free to reach out via GitHub Issues or contact the repository maintainer.

---
**Disclaimer:** This project is intended for educational and research purposes only. Please use responsibly and within legal guidelines.

