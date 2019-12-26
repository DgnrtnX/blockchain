import hashlib, json

def crypto_hash(*args):
    string_coded = sorted(map(lambda data: json.dumps(data), args))

    joined_data = "".join(string_coded)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash: {crypto_hash('one', 2, [3])}")

if __name__ == "__main__":
    main()