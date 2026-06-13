import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Magnetic field range (Tesla)
    B = np.linspace(0.5, 35, 1000)
    
    # Sigmoid parameters for R_xy steps
    # We want plateaus at:
    # nu = 2   => R_xy = 0.5 (around B = 5T)
    # nu = 1   => R_xy = 1.0 (around B = 10T)
    # nu = 2/3 => R_xy = 1.5 (around B = 15T)
    # nu = 1/3 => R_xy = 3.0 (around B = 30T)
    
    # Transition centers (B_k) and widths (w_k)
    transitions = [
        {"center": 3.5,  "width": 0.6, "step": 0.5},  # to nu = 2 (R_xy = 0.5)
        {"center": 7.5,  "width": 0.8, "step": 0.5},  # to nu = 1 (R_xy = 1.0)
        {"center": 12.5, "width": 0.8, "step": 0.5},  # to nu = 2/3 (R_xy = 1.5)
        {"center": 22.0, "width": 2.5, "step": 1.5}   # to nu = 1/3 (R_xy = 3.0)
    ]
    
    # Calculate R_xy
    R_xy = np.zeros_like(B)
    for trans in transitions:
        R_xy += trans["step"] * 0.5 * (1 + np.tanh((B - trans["center"]) / trans["width"]))
    
    # Calculate R_xx (proportional to dR_xy/dB + small background at low fields)
    R_xx = np.zeros_like(B)
    for trans in transitions:
        # Derivative of 0.5 * (1 + tanh(u)) is 0.5 * sech^2(u) = 0.5 * (1 - tanh^2(u))
        u = (B - trans["center"]) / trans["width"]
        sech2 = 1.0 / (np.cosh(u)**2)
        R_xx += (trans["step"] / (2 * trans["width"])) * sech2
        
    # Scale R_xx for visualization and add a tiny noise/background
    R_xx = R_xx * 2.0
    
    # Add some SdH-like oscillations at very low B (below 5T)
    sdh_envelope = 0.4 * np.exp(-B / 4.0)
    sdh_oscillations = sdh_envelope * (1.0 + np.sin(2.0 * np.pi * 5.0 / B))
    R_xx += sdh_oscillations
    
    # Clean up R_xx near B=0 to prevent division by zero or weird artifacts
    R_xx[B < 1.0] = R_xx[B < 1.0] * (B[B < 1.0] - 0.5) / 0.5
    R_xx[R_xx < 0] = 0
    
    # Setup plot with dual y-axis
    fig, ax1 = plt.subplots(figsize=(9, 6), dpi=300)
    
    color_xy = '#1f77b4'
    color_xx = '#d62728'
    
    # Plot R_xy on ax1
    ax1.plot(B, R_xy, color=color_xy, linewidth=2.5, label=r'$R_{xy}$')
    ax1.set_xlabel('Magnetic Field $B$ (T)', fontsize=12, labelpad=10)
    ax1.set_ylabel(r'Hall Resistance $R_{xy}$ ($h/e^2$)', color=color_xy, fontsize=12, labelpad=10)
    ax1.tick_params(axis='y', labelcolor=color_xy)
    ax1.set_ylim(-0.1, 3.5)
    
    # Plot R_xx on ax2
    ax2 = ax1.twinx()
    ax2.plot(B, R_xx, color=color_xx, linewidth=1.8, linestyle='-', label=r'$R_{xx}$')
    ax2.set_ylabel(r'Longitudinal Resistivity $R_{xx}$ (a.u.)', color=color_xx, fontsize=12, labelpad=10)
    ax2.tick_params(axis='y', labelcolor=color_xx)
    ax2.set_ylim(-0.05, 1.5)
    
    # Annotate plateaus and filling factors
    # nu = 2 (R_xy = 0.5)
    ax1.annotate(r'$\nu = 2$', xy=(5.0, 0.5), xytext=(5.0, 0.8),
                 arrowprops=dict(arrowstyle="->", color=color_xy),
                 fontsize=11, fontweight='bold', color=color_xy, ha='center')
    
    # nu = 1 (R_xy = 1.0)
    ax1.annotate(r'$\nu = 1$', xy=(10.0, 1.0), xytext=(10.0, 1.3),
                 arrowprops=dict(arrowstyle="->", color=color_xy),
                 fontsize=11, fontweight='bold', color=color_xy, ha='center')
                 
    # nu = 2/3 (R_xy = 1.5)
    ax1.annotate(r'$\nu = 2/3$', xy=(15.0, 1.5), xytext=(15.0, 1.8),
                 arrowprops=dict(arrowstyle="->", color=color_xy),
                 fontsize=11, fontweight='bold', color=color_xy, ha='center')
                 
    # nu = 1/3 (R_xy = 3.0)
    ax1.annotate(r'$\nu = 1/3$', xy=(30.0, 3.0), xytext=(30.0, 2.6),
                 arrowprops=dict(arrowstyle="->", color=color_xy),
                 fontsize=11, fontweight='bold', color=color_xy, ha='center')
                 
    # Title and grids
    plt.title("Integer & Fractional Quantum Hall Effect Plateaus", fontsize=14, fontweight='bold', pad=15)
    ax1.grid(True, which='both', linestyle=':', alpha=0.5)
    
    # Spines
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.spines['left'].set_color(color_xy)
    ax1.spines['right'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax2.spines['right'].set_color(color_xx)
    
    # Save output
    output_dir = "/Users/johnqiangzhang/Documents/projects/coordinates-physics-china/website/static/img"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fractional_quantum_hall.png")
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Successfully generated and saved plot to {output_path}")

if __name__ == "__main__":
    main()
