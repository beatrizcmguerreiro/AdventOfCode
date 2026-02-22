# day 12 (part 2)

# TUDO NUMA LINHA SÓ PQ O PYTHON É LENTO E EU QUERO O RESULTADO NÃO AGUENTO MAIS 
print(sum(map(lambda l:7*sum(map(int,l[6:].split()))<int(l[:2])*int(l[3:5]),list(open("2025/day12/input.txt"))[30:])))