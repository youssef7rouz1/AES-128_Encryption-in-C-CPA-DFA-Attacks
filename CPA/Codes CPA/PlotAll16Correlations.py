import numpy as np
import matplotlib.pyplot as plt

# Charger les traces
# Si votre fichier est un .npz, utilisez np.load("traces.npz")["arr_name"]
traces = np.load("traces.npy")               # Traces mesurées (N x T)
num_traces, num_points = traces.shape        # N = nombre de traces, T = points temporels

# Boucle sur les 16 octets
for octet_index in range(1, 17):
    # Charger la matrice de prédiction pour l'octet courant
    P = np.load(f"prediction_matrix_octet{octet_index}.npy")  # (N x 256)
    _, num_keys = P.shape                                    # 256 hypothèses de clé

    # Initialiser la matrice de corrélations (256 clés × T points)
    correlations = np.zeros((num_keys, num_points), dtype=float)

    # Calculer la corrélation pour chaque hypothèse de clé et chaque point temporel
    for key_guess in range(num_keys):
        # On extrait une fois la colonne P[:, key_guess]
        pred_col = P[:, key_guess]
        for t in range(num_points):
            # np.corrcoef renvoie une matrice 2×2, dont l'élément [0,1] est la corrélation
            correlations[key_guess, t] = np.corrcoef(pred_col, traces[:, t])[0, 1]

    # Tracer toutes les courbes de corrélation (une par clé)
    plt.figure(figsize=(10, 6))
    for key_guess in range(num_keys):
        plt.plot(correlations[key_guess, :], linewidth=0.5)
    plt.xlabel("Points temporels")
    plt.ylabel("Corrélation")
    plt.title(f"Corrélations pour l'octet {octet_index}")
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarder le graphique
    plot_file = f"correlation_curves_octet{octet_index}.png"
    plt.savefig(plot_file, dpi=300)
    plt.close()

    print(f"Octet {octet_index:d} : corrélations calculées et graphique sauvegardé sous '{plot_file}'")
