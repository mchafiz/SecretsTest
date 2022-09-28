# Configuration files are a really frequent source of secrets

'''Common Key Types with obvious names'''

# AWS
## AWS Access Key ID



# Generic api key
ACCESS_TOKEN = '7340ad40-09b3-11eb-adc1-0242ac120002'

'''Generic Credentials with obscure names that flow into password sinks'''

# Generic password
SOURCE_1 = 'GYW2mMmpG327BtrdTnUL'

# Generic weak password
SOURCE_2 = 'redis'

# Generic weak password
SOURCE_3 = 'opensaysme'

# Generic app secret
SOURCE_4 = 'ttn9Jb9ep2U4KvG9hq6e'

# Generic api key
SOURCE_5 = 'SGwJgqnZYzH945UBWnauBuKXKLEhq5Le'

# Generic api key
SOURCE_6 = '897f3b11-72f2-4c6f-9a9d-4750cdc609c6'

# Generic api key
SOURCE_7 = '7340ad40-09b3-11eb-adc1-0242ac120002'


'''False Positives'''

# Github Hashes

## Obvious name
GITHUB_COMMIT_SHA_HASH = '120ba2f7db8affd023e83964e5d8afbd10d20fe8'

## Less obvious name
COMMIT_SHA = '637831c685a5f906c65d6af8389e7988619a3514'

## Obscure name
LATEST = '699865bd61fda628b0bea3080ae73d5f11572a74'

# Public Keys

## SSH RSA public key
PUBLIC_KEY_SSH = 'AAAAB3NzaC1yc2EAAAADAQABAAAAgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0FPqri0cb2JZfXJ/DgYSF6vUpwmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/3j+skZ6UtW+5u09lHNsj6tQ51s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZw=='

## Public key file
PUBLIC_KEY_FILE = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0\nFPqri0cb2JZfXJ/DgYSF6vUpwmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/\n3j+skZ6UtW+5u09lHNsj6tQ51s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZwIDAQAB\n-----END PUBLIC KEY-----'
