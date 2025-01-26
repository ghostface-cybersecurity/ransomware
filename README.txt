 ######     ##     ##   ##   #####    #####   ##   ##  ##   ##    ##     ######   #######
  ##  ##   ####    ###  ##  ##   ##  ##   ##  ### ###  ##   ##   ####     ##  ##   ##   #
  ##  ##  ##  ##   #### ##  #        ##   ##  #######  ##   ##  ##  ##    ##  ##   ## #
  #####   ##  ##   ## ####   #####   ##   ##  #######  ## # ##  ##  ##    #####    ####
  ## ##   ######   ##  ###       ##  ##   ##  ## # ##  #######  ######    ## ##    ## #
  ##  ##  ##  ##   ##   ##  ##   ##  ##   ##  ##   ##  ### ###  ##  ##    ##  ##   ##   #
 #### ##  ##  ##   ##   ##   #####    #####   ##   ##  ##   ##  ##  ##   #### ##  #######

_________________________________________________________________________________________
                                          ABOUT
_________________________________________________________________________________________
Description: A simple ransomware program that encrypts just one file
Program: Ransomware
Languages: Python 3.12.7
Tested on: Linux 6.11.2
Author: ghostface-cybersecurity

_________________________________________________________________________________________
                                     PROGRAM LAUNCH
_________________________________________________________________________________________
# generating keys
openssl genrsa -out keys.key 1024 # generating a key pair
openssl rsa -in keys.key -pubout -out public.key # extract public key
echo "Simple text" > file.txt # create a file that will later be encrypted

# running the script
# python3 ransomware.py <filename>

python3 ransomware.py file.txt

__________________________________________________________________________________________
                                      LEGAL STATEMENT
__________________________________________________________________________________________
By downloading, modifying, redistributing, and/or executing python-network-tools, the
user agrees to the contained LEGAL.txt statement found in this repository.

I, ghostface-cybersecurity, the creator, take no legal responsibility for unlawful actions
caused/stemming from this program. 

Use responsibly and ethically!
