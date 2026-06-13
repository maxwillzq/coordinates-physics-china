import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Temperature range (K)
    T = np.linspace(0, 150, 1000)
    
    # Model parameters for YBCO
    Tc = 93.0  # Transition temperature in K
    w = 0.6    # Transition width parameter
    
    # Normal state resistance (linear with T, normalized to 1.0 at 100K)
    # R_normal(T) = A + B*T
    # R_normal(100) = 1.0 => A + 100*B = 1.0
    # Let's assume R_normal(0) would be 0.05 (residual resistivity if normal)
    # B = (1.0 - 0.05) / 100 = 0.0095
    # A = 0.05
    A = 0.05
    B = 0.0095
    R_normal = A + B * T
    
    # Transition function (Sigmoid-like)
    f_transition = 1.0 / (1.0 + np.exp(-(T - Tc) / w))
    
    # Normalized Resistance
    R_normalized = R_normal * f_transition
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    
    # Plot YBCO curve
    ax.plot(T, R_normalized, color='#d62728', linewidth=2.5, label='YBCO (High-$T_c$)')
    
    # Add transition temperature Tc annotation
    ax.axvline(x=Tc, color='gray', linestyle='--', alpha=0.7)
    ax.plot(Tc, 0.5 * (A + B * Tc), 'o', color='#d62728', markersize=6)
    ax.annotate(r'$T_c \approx 93$ K', xy=(Tc, 0.3), xytext=(Tc + 5, 0.2),
                arrowprops=dict(arrowstyle="->", color='#d62728'),
                fontsize=11, color='#d62728', fontweight='bold')
    
    # Shaded region for BCS McMillan Limit (30K - 40K)
    ax.axvspan(30, 40, color='#1f77b4', alpha=0.15, label='BCS McMillan Limit (30 K - 40 K)')
    ax.text(35, 0.65, 'Conventional BCS\nMcMillan Limit\n(30 K - 40 K)', 
            color='#1f77b4', fontsize=9, ha='center', va='center', rotation=0,
            bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.3', edgecolor='#1f77b4', lw=0.5))
    
    # Title and Labels
    ax.set_title("Superconducting Transition: YBCO vs. BCS Limit", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Temperature $T$ (K)", fontsize=12, labelpad=10)
    ax.set_ylabel(r"Normalized Resistance $R(T)/R(100\text{ K})$", fontsize=12, labelpad=10)
    
    # Grid and spines
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')
    
    # Limits and Ticks
    ax.set_xlim(0, 150)
    ax.set_ylim(-0.02, 1.5)
    ax.set_xticks(np.arange(0, 151, 20))
    # Explicitly include critical values on x-axis
    ticks = list(ax.get_xticks())
    if 93 not in ticks:
        ticks.append(93)
        ticks.sort()
    ax.set_xticks(ticks)
    
    # Legend
    ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none', shadow=True, fontsize=10)
    
    # Save output
    output_dir = "/Users/johnqiangzhang/Documents/projects/coordinates-physics-china/website/static/img"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "superconductor_transition.png")
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Successfully generated and saved plot to {output_path}")

if __name__ == "__main__":
    main()
