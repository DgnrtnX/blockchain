from backend.util.crypto_hash import crypto_hash
HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex):
    binary = ''

    for char in hex:
        binary += HEX_TO_BINARY_CONVERSION_TABLE[char]

    return binary

def main():
    # number = 295
    # print(number)
    # hex_num = hex(number)[2:]
    # print(f'hex number: {hex_num}')
    #
    # bin_num = hex_to_binary(hex_num)
    # print(f'Binary number: {bin_num}')
    #
    # oginum = int(bin_num, 2)
    # print(oginum)

    crypto_hash_binary = hex_to_binary(crypto_hash('test-data'))

    print(f'Crypto hash binary: {crypto_hash_binary}')

if __name__ == "__main__":
    main()
