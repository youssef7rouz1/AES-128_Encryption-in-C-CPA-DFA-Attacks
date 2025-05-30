import numpy as np
import matplotlib.pyplot as plt

# Charger les données
# Si vos fichiers sont au format .npz, remplacez np.load par np.load(...)['arr_0'] ou la clé appropriée.
traces = np.load("traces.npy")                     # Traces mesurées (N x T)
P = np.load("prediction_matrix_octet4.npy")        # Matrice de prédiction pour l'octet 4 (N x 256)

# Dimensions des données
num_traces, num_points = traces.shape    # N x T
_, num_keys = P.shape                     # N x 256

# Initialiser une matrice pour stocker les corrélations
correlations = np.zeros((num_keys, num_points), dtype=float)

# Calculer la corrélation pour chaque clé hypothétique et point temporel
for key_guess in range(num_keys):
    for time_point in range(num_points):
        # np.corrcoef renvoie la matrice de corrélation 2x2
        correlations[key_guess, time_point] = np.corrcoef(
            P[:, key_guess],
            traces[:, time_point]
        )[0, 1]

# Tracer les courbes de corrélation pour toutes les hypothèses de clé
plt.figure(figsize=(10, 6))
for key_guess in range(num_keys):
    plt.plot(correlations[key_guess, :], linewidth=0.5)

plt.xlabel("Points temporels")
plt.ylabel("Corrélation")
plt.title("Corrélations pour l'octet 4")
plt.grid(True)
plt.tight_layout()

# Sauvegarder le graphique
plt.savefig("correlation_curves_octet4.png", dpi=300)
plt.close()

print("Corrélations calculées et graphique enregistré sous 'correlation_curves_octet4.png'")
