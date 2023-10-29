def factorize_number(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors


def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            n = int(line.strip())
            if n > 1:
                factors = factorize_number(n)
                if len(factors) >= 2:
                    p, q = factors[0], factors[1]
                    outfile.write(f"{n}={p}*{q}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "factorizations.txt"
    main(input_file, output_file)
