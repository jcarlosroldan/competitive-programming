from re import findall

# see https://oeis.org/search?q=1%2C+11%2C+21%2C+1211%2C+111221&language=english&go=Search
describe = lambda n: "".join([str(len(f+o))+f for f,o in findall(r"(\d)(\1*)", n)])
x = "1"
for _ in range(30): x = describe(x)
print(len(x))