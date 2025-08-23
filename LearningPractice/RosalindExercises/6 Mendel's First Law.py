import matplotlib.pyplot as plt

def mendel_prob(k, m, n):
    """
    Calculate probability of dominant phenotype in offspring.
    
    k = homozygous dominant (AA)
    m = heterozygous (Aa)
    n = homozygous recessive (aa)-
    """
    N = k + m + n  # total population
    
    # Probabilities of each parental pairing (without replacement)
    P_AA_AA = (k/N) * ((k-1)/(N-1))
    P_AA_Aa = (k/N) * (m/(N-1)) + (m/N) * (k/(N-1))
    P_AA_aa = (k/N) * (n/(N-1)) + (n/N) * (k/(N-1))
    P_Aa_Aa = (m/N) * ((m-1)/(N-1))
    P_Aa_aa = (m/N) * (n/(N-1)) + (n/N) * (m/(N-1))
    P_aa_aa = (n/N) * ((n-1)/(N-1))
    
    # Multiply by probability offspring shows dominant trait
    prob = (1.0 * P_AA_AA +
            1.0 * P_AA_Aa +
            1.0 * P_AA_aa +
            0.75 * P_Aa_Aa +
            0.5 * P_Aa_aa +
            0.0 * P_aa_aa)
    
    return prob

def visualize_mendel(k, m, n):
    N = k + m + n
    
    # Probabilities of each pair
    probs = {
        "AA×AA": (k/N) * ((k-1)/(N-1)),
        "AA×Aa": (k/N) * (m/(N-1)) + (m/N) * (k/(N-1)),
        "AA×aa": (k/N) * (n/(N-1)) + (n/N) * (k/(N-1)),
        "Aa×Aa": (m/N) * ((m-1)/(N-1)),
        "Aa×aa": (m/N) * (n/(N-1)) + (n/N) * (m/(N-1)),
        "aa×aa": (n/N) * ((n-1)/(N-1))
    }
    
    # Probability offspring shows dominant trait for each cross
    dom_probs = {
        "AA×AA": 1.0,
        "AA×Aa": 1.0,
        "AA×aa": 1.0,
        "Aa×Aa": 0.75,
        "Aa×aa": 0.5,
        "aa×aa": 0.0
    }
    
    # Contribution of each cross to final probability
    contributions = {cross: probs[cross] * dom_probs[cross] for cross in probs}
    
    # Plot
    plt.figure(figsize=(8,5))
    plt.bar(contributions.keys(), contributions.values(), color="skyblue")
    plt.title(f"Contributions to Dominant Offspring Probability (k={k}, m={m}, n={n})")
    plt.ylabel("Probability Contribution")
    plt.xlabel("Mating Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Total probability
    total_prob = sum(contributions.values())
    print(f"Total probability of dominant phenotype = {total_prob:.5f}")
    return total_prob

# --- Example Usage ---
k, m, n = 17, 16, 15
print("Computed probability:", mendel_prob(k, m, n))
visualize_mendel(k, m, n)


