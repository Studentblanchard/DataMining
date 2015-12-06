Sentiment Miner
======
## Setup

Run the Makefile from the root folder.

```
$ make
mkdir -p bin
mkdir -p build
clang   -O3 -c src/feal.c -o build/feal.o
clang   -O3 -c src/fealdiff.c -o build/diff.o
clang   -c src/fealrun.c -o build/run.o
clang   build/run.o build/feal.o build/diff.o -o bin/feal
clang  -std=c99 -Wno-int-conversion -c test/fealtest.c -o build/test.o
clang  -std=c99 -Wno-int-conversion build/test.o build/feal.o build/diff.o -o bin/test
clang   -O3 -c src/fealcrack.c -o build/crack.o
clang   -O3 build/diff.o build/feal.o build/crack.o -o bin/crack
```

## Programs

**crack** is the main program that can be run. The usage is as follows (should be run from the ```bin``` folder):

```
$ ./crack -x(optional)
Starting Feal-4 Cryptanalysis
Start time: Sun Nov 29 00:58:01 2015

Actual subkeys to find.
Subkey 0: 0x1002326C
Subkey 1: 0x81C9930D
Subkey 2: 0x39903BC8
Subkey 3: 0x2D2157E0
Subkey 4: 0x93350F7F
Subkey 5: 0x5B9E858B

Finding round 3 subkey...
Found sk3: 0x2D2157E0

Finding round 2 subkey...
Found sk2: 0x39903BC8

Finding round 1 subkey...
Found sk1: 0x0149138D

Finding the rest of the keys...

Subkey[0]: 0x1202326E
Subkey[1]: 0x0149138D
Subkey[2]: 0x39903BC8
Subkey[3]: 0x2D2157E0
Subkey[4]: 0x93350F7F
Subkey[5]: 0x599E8589

Finished Feal-4 Cryptanalysis
End time: Sun Nov 29 00:58:40 2015
Total time: 39 seconds
$
```

#### Options
* -x enables subkeyOptimization. This will limit the subkeys to certain values that allow the true subkeys to always be found in minimal time

**test** runs feal related tests and demonstrations (should be run from the ```bin``` folder):

```
$ ./test
Testing cipher functions...

Testing rotate2 function...

Testing the gbox...

Testing the fbox...

Testing Encrypt/Decrypt...
Tests run: 4

0x7C6446E38A4A2BD4
0x7C6446E38A4A2BD4

0x3D5C211FD1B9D3D3
0x3D5C211FD1B9D3D3
$
```

**feal** runs encrypts a given plaintext (in hex) using the FEAL-4 algorithm (should be run from the ```bin``` folder):

```
$ ./feal
Please enter some plaintext(8 bytes):
1927bd7365dea091
Plaintext: 0x3139323762643733
Ciphertext: 0xB578A1C200BFCBDE
Plaintext (decrypted): 0x3139323762643733
$
```

## Version
* Version 1.0

## Contact
* Authors: Trevor Blanchard, Jessica Sanders
* e-mail: umblanc3@myumanitoba.ca, umsand82@myumanitoba.ca
