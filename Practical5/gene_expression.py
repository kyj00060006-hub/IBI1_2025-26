import matplotlib.pyplot as plt

#create dictionary
gene_expr={"TP53": 12.4,"EGFR": 15.1,"BRCA1": 8.2,"PTEN": 5.3,"ESR1": 10.7}
print("=== Gene Expression Dictionary ===")
print(gene_expr)

#add MYC
gene_expr["MYC"] = 11.6
print("\nAfter adding MYC:")
print(gene_expr)

#bar chart
plt.figure(figsize=(8, 4))
plt.bar(gene_expr.keys(), gene_expr.values(), color='skyblue')
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()

#calculate average
avg_expr = sum(gene_expr.values()) / len(gene_expr)
print(f"\nAverage gene expression: {avg_expr:.2f}")

#query gene of interest
while True:
    gene_of_interest =input('your gene of interest:')
    if gene_of_interest in gene_expr:
        print(f"Expression: {gene_expr[gene_of_interest]}")
        break
    else:
        print(f"Error: Gene '{gene_of_interest}' not found in the database.")
