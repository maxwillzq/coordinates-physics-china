import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Constants
    lambda_c = 2.426  # Compton wavelength in pm
    
    # Angles to plot
    angles_deg = [0, 45, 90, 135]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    # Wavelength shift range (pm)
    x = np.linspace(-1.5, 6.0, 1000)
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    
    # Offset between successive plots for visual clarity
    offset_step = 1.2
    
    for i, theta in enumerate(angles_deg):
        theta_rad = np.radians(theta)
        shift_mod = lambda_c * (1 - np.cos(theta_rad))
        
        # Unmodified peak (centered at 0)
        # Intensity of unmodified peak decreases with scattering angle
        amp_unmod = 0.8 * np.exp(-theta / 90.0) if theta > 0 else 1.0
        width_unmod = 0.25
        y_unmod = amp_unmod * np.exp(-0.5 * (x / width_unmod)**2)
        
        # Modified peak (centered at shift_mod)
        # Intensity of modified peak increases relative to unmodified peak as angle increases
        if theta > 0:
            amp_mod = 0.8 * (1 - np.exp(-theta / 45.0))
            width_mod = 0.35 + 0.001 * theta
            y_mod = amp_mod * np.exp(-0.5 * ((x - shift_mod) / width_mod)**2)
        else:
            y_mod = np.zeros_like(x)
            
        y_total = y_unmod + y_mod
        
        # Offset for waterfall display
        y_display = y_total + i * offset_step
        
        # Plot curve
        ax.plot(x, y_display, label=rf"$\theta = {theta}^\circ$", color=colors[i], linewidth=2.0)
        
        # Add labels for unmodified and modified peaks
        # For theta = 0, there is only one peak at 0
        if theta == 0:
            ax.text(0, i * offset_step + 1.1, "Primary", ha='center', va='bottom', fontsize=9, color=colors[i])
        else:
            ax.text(0, i * offset_step + amp_unmod + 0.05, "Unmodified", ha='center', va='bottom', fontsize=8, color=colors[i], alpha=0.8)
            ax.text(shift_mod, i * offset_step + amp_mod + 0.05, "Modified", ha='center', va='bottom', fontsize=8, color=colors[i])
            
            # Draw line/arrow indicating the shift
            ax.annotate('', xy=(shift_mod, i * offset_step - 0.1), xytext=(0, i * offset_step - 0.1),
                        arrowprops=dict(arrowstyle="<->", color=colors[i], linestyle="--", alpha=0.7))
            ax.text(shift_mod / 2, i * offset_step - 0.05, rf"$\Delta\lambda \approx {shift_mod:.2f}$ pm", 
                    ha='center', va='bottom', fontsize=8, color=colors[i])

    # Title and labels
    ax.set_title("Compton Scattering Wavelength Shift", fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel(r"Wavelength Shift $\Delta\lambda = \lambda' - \lambda_0$ (pm)", fontsize=12, labelpad=10)
    ax.set_ylabel("Intensity (Arbitrary Units, Offset)", fontsize=12, labelpad=10)
    
    # Custom ticks and styling
    ax.set_xlim(-1.5, 6.0)
    ax.set_ylim(-0.3, len(angles_deg) * offset_step + 0.5)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')
    
    ax.set_yticks([])  # Hide y-axis absolute scale as it's arbitrary/offset
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    
    # Legend
    ax.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none', shadow=True, fontsize=10)
    
    # Save output
    output_dir = "/Users/johnqiangzhang/Documents/projects/coordinates-physics-china/website/static/img"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "compton_scattering_fit.png")
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Successfully generated and saved plot to {output_path}")

if __name__ == "__main__":
    main()
