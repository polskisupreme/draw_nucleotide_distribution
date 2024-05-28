import matplotlib.pyplot as plt

def load_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def compute_cumulative_percentage(sequence, nucleotide):
    cumulative_counts = []
    count = 0
    for index, char in enumerate(sequence):
        if char == nucleotide:
            count += 1
        cumulative_counts.append((count / (index + 1)) * 100)
    return cumulative_counts

def draw_nucleotide_distribution(sequence, nucleotide):
    cumulative_percentages = compute_cumulative_percentage(sequence, nucleotide)
    positions = range(1, len(sequence) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(positions, cumulative_percentages, marker='o', linestyle='-', color='blue', label=f'Percentage {nucleotide}')
    plt.xlabel('Position in Sequence')
    plt.ylabel(f'Percentage of {nucleotide}')
    plt.title(f'Cumulative Percentage Distribution of {nucleotide} in DNA Sequence')
    plt.legend()
    plt.grid(True)
    plt.savefig('cumulative_distribution.png')
    plt.show()

# Main execution
file_path = 'sequence.txt'
nucleotide_to_analyze = "A"  # Options: A, T, C, G

sequence_data = load_sequence(file_path)
draw_nucleotide_distribution(sequence_data, nucleotide_to_analyze)