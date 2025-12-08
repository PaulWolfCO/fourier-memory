import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title — placed clearly above everything, no box
plt.text(5, 9.7, 'Figure 4 – Nested Holographic Cascade', 
         ha='center', va='center', fontsize=20, fontweight='bold')

# Layer data: name, neuron count, y-position
layers = [
    ("6-D Cortical Manifold",           "∼10¹⁰ active neurons",   8.6),
    ("Entorhinal Cortex (EC)",          "10⁶ neurons",            7.3),
    ("Dentate Gyrus (DG)",              "10⁶ neurons",            6.0),
    ("CA3",                             "≈ 300 000 neurons",      4.7),
    ("CA1",                             "≈ 400 000 neurons",      3.4),
    ("Subiculum / EC deep",             "≈ 100 000 neurons",      2.1),
]

colors = ['#88c0d0', '#81a1c1', '#5e81ac', '#4c566a', '#434c5e', '#3b4252']

for i, (name, neurons, y) in enumerate(layers):
    width = 8.0 - i * 0.7          # gradually narrower toward the bottom
    height = 1.0
    left = 5 - width / 2
    
    # Colored box
    rect = plt.Rectangle((left, y - height/2), width, height,
                         facecolor=colors[i], edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    
    # Layer name (bold, top line)
    plt.text(5, y + 0.15, name, ha='center', va='center',
             fontsize=16, fontweight='bold')
    
    # Neuron count (middle line)
    plt.text(5, y - 0.05, neurons, ha='center', va='center',
             fontsize=13, style='italic')
    
    # Preserved bits (bottom line — now comfortably fits)
    plt.text(5, y - 0.35, '10⁶ effective bits/trace', ha='center', va='center',
             fontsize=12, color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('Figure_4_Nested_Holographic_Cascade.pdf', dpi=300, bbox_inches='tight')
plt.savefig('Figure_4_Nested_Holographic_Cascade.png', dpi=300, bbox_inches='tight')
plt.show()