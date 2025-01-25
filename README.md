<h1 align="center">ransomware</h1>

<h4 align="center">A simple ransomware program that encrypts just one file</h4>

<h4 align="center">Terminal lauch | bash</h4>


```
openssl genrsa -out keys.key 1024 # generating a key pair
openssl rsa -in keys.key -pubout -out public.key # extract public key
echo "Simple text" > file.txt # create a file that will later be encrypted

# running the script
# python3 ransomware.py <filename>

python3 ransomware.py file.txt

# now your file has been mercilessly encrypted >:)
```
