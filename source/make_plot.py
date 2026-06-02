import matplotlib.pyplot as plt
import os

def plot_line_power(data):

    x = data.iloc[:,0]
    y = data.iloc[:,1]
    # Leistung
    plt.figure(figsize=(10,5))
    plt.plot(x,y)
    
    plt.title("Leistungskurve")
    plt.xlabel("Zeit (s)")
    plt.ylabel("Leistung (W)")

    plt.xscale("log")
    plt.grid(True)
    # Unterordner erstellen
    output_dir = "screenshots"
    os.makedirs(output_dir, exist_ok=True)

    # Screenshot speichern
    plt.savefig(f"{output_dir}/leistungskurve.png", dpi=300)
    plt.show()


