# TRM-Ace Master Playbook
_Auto-generated from Seed Data_

## Buffer Overflow
_Memory corruption attacks._

### EIP Overwrite
- **ID**: `pwn_bof_eip_01`
- **Triggers**: Segfault at offset, Checksec: NX Disabled
- **Technique**: Overwrite Return Address to redirect flow.
- **Payload**: `Cyclic Pattern: Aa0Aa1...`
- **Expected Output**: Program crashes with EIP = 0xdeadbeef

## RSA Attacks
_Exploiting weak key generation._

### Small Public Exponent (e=3)
- **ID**: `crypto_rsa_small_e_01`
- **Triggers**: Public Key e=3, No Padding (OAEP)
- **Technique**: If m^e < n, calculate the eth root of ciphertext.
- **Payload**: `gmpy2.iroot(c, 3)`
- **Expected Output**: Cube root yields plaintext integer.

### Common Modulus Attack
- **ID**: `crypto_rsa_common_modulus_01`
- **Triggers**: Same 'n' used with different 'e', Two ciphertexts captured
- **Technique**: Recover plaintext using Extended Euclidean Algorithm on exponents.
- **Payload**: `Find a,b s.t. a*e1 + b*e2 = 1`
- **Expected Output**: Mathematical cancellation reveals message 'm'.

## XOR Encryption
_Bitwise cipher breaking._

### Single-Byte XOR Brute Force
- **ID**: `crypto_xor_brute_01`
- **Triggers**: Ciphertext has repeating patterns, Key length likely 1 byte
- **Technique**: XOR every byte with 0-255.
- **Payload**: `for k in range(256): print(xor(c, k))`
- **Expected Output**: Output contains readable flag format (e.g. 'flag{').

## PCAP Analysis
_Network traffic inspection._

### HTTP Object Extraction
- **ID**: `forensics_pcap_export_01`
- **Triggers**: HTTP traffic present, Large file transfer detected
- **Technique**: Extract files transferred over unencrypted HTTP.
- **Payload**: `Wireshark: File -> Export Objects -> HTTP`
- **Expected Output**: Extraction yields 'malware.exe' or 'flag.pdf'.

### DNS Tunneling Detection
- **ID**: `forensics_dns_tunnel_01`
- **Triggers**: High volume of DNS TXT records, Long subdomains
- **Technique**: Analyze protocol hierarchy for anomalous DNS volume.
- **Payload**: `Statistics -> Protocol Hierarchy`
- **Expected Output**: DNS traffic accounts for >50% of bandwidth.

## SQL Injection
_Database query manipulation._

### Union-Based Extraction
- **ID**: `web_sqli_union_01`
- **Triggers**: Input reflected in error, Database dump visible
- **Technique**: Combine results of original query with injected query.
- **Payload**: `' UNION SELECT username, password FROM users --`
- **Expected Output**: Application displays data from 'users' table.

### Boolean Blind SQLi
- **ID**: `web_sqli_boolean_01`
- **Triggers**: Page content changes on True/False, No error message
- **Technique**: Infer data by asking True/False questions.
- **Payload**: `' AND 1=1 -- vs ' AND 1=2 --`
- **Expected Output**: True payload shows content; False payload hides it.

## Command Injection
_OS Command Execution._

### Command Chaining
- **ID**: `web_cmdi_separator_01`
- **Triggers**: Input used in shell command, Ping/Echo functionality
- **Technique**: Use separators (; | &&) to inject commands.
- **Payload**: `127.0.0.1; cat /etc/passwd`
- **Expected Output**: Response includes content of /etc/passwd.

