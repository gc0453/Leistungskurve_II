import matplotlib.pyplot as plt
import os

def plot_line_power(data):

    x_raw = data.iloc[:,0]
    y = data.iloc[:,1]
    
    # Zeit umrechnen
    x_pos = range(len(x_raw))
    x_labels = []
    for t in x_raw:

        if t < 60:
            x_labels.append(f"{t}s")

        else:
            x_labels.append(f"{t/60:.0f}min")
    
    plt.figure(figsize=(10,5))
    plt.plot(x_pos, y)
    
    plt.title("Leistungskurve")
    plt.xlabel("Zeit (s)")
    plt.ylabel("Leistung (W)")

    plt.xscale("linear")
    plt.xticks(x_pos, x_labels, rotation=45)
    plt.grid(True)
    # Unterordner erstellen
    output_dir = "screenshot"
    os.makedirs(output_dir, exist_ok=True)

    # Screenshot speichern
    plt.savefig(f"{output_dir}/leistungskurve.png", dpi=300)
    plt.show()


