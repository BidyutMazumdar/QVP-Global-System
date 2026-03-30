import csv

WEIGHTS = (0.25, 0.25, 0.25, 0.25)

def qssi_score(pqc, ai, legal, res):
    w1, w2, w3, w4 = WEIGHTS
    return 100 * (w1*pqc + w2*ai + w3*legal + w4*res)

def risk_adjust(score, risk):
    return score * (1 - risk)

def process(input_file, output_file):
    results = []

    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pqc = float(row['PQC'])
            ai = float(row['AI'])
            legal = float(row['LEGAL'])
            res = float(row['RES'])
            risk = float(row['Risk'])

            score = qssi_score(pqc, ai, legal, res)
            adj = risk_adjust(score, risk)

            results.append({
                "Country": row['Country'],
                "QSSI": round(score,2),
                "Adjusted": round(adj,2)
            })

    ranked = sorted(results, key=lambda x: x['Adjusted'], reverse=True)

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Rank","Country","QSSI","Adjusted"])
        writer.writeheader()
        for i, r in enumerate(ranked,1):
            r["Rank"] = i
            writer.writerow(r)

if __name__ == "__main__":
    process("../dataset/qssi_data.csv", "../reports/qssi_ranking.csv")
