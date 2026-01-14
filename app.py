import random, string, sys

MAX_LEN = 20
POP_SIZE = 200
MUT_RATE = 0.02
ELITE = 0.1

def fitness(target, cand):
    return sum(t == c for t, c in zip(target, cand))

def random_gene(charset, target):
    return ''.join(random.choice(charset) for _ in range(len(target)))

def mutate(gene, charset):
    return ''.join(
        c if random.random() > MUT_RATE else random.choice(charset)
        for c in gene
    )

def crossover(a, b):
    pt = random.randint(1, len(a) - 1)
    return a[:pt] + b[pt:], b[:pt] + a[pt:]

def evolve(target):
    if target.isdigit():
        charset = string.digits
    elif target.isalpha():
        charset = string.ascii_letters
    else:
        charset = string.ascii_letters + string.digits + ' '

    pop = [random_gene(charset, target) for _ in range(POP_SIZE)]
    generation = 0
    
    while True:
        generation += 1
        scored = sorted(pop, key=lambda g: fitness(target, g), reverse=True)
        best = scored[0]
        best_fit = fitness(target, best)

        print(f"Gen {generation:3d} | Best: {best!r} | Fitness: {best_fit}/{len(target)}")

        if best == target:
            return best, generation

        elite_cnt = int(ELITE * POP_SIZE)
        new_pop = scored[:elite_cnt]

        while len(new_pop) < POP_SIZE:
            parent1, parent2 = random.choices(scored[:POP_SIZE // 2], k=2)
            child1, child2 = crossover(parent1, parent2)
            new_pop.append(mutate(child1, charset))
            if len(new_pop) < POP_SIZE:
                new_pop.append(mutate(child2, charset))

        pop = new_pop

if __name__ == "__main__":
    target = input("Enter target (max 20 chars): ")[:MAX_LEN]
    result, gens = evolve(target)
    print(f"\nFound: {result!r} in {gens} generations")