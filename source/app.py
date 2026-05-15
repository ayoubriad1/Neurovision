import streamlit as st
import matplotlib.pyplot as plt
from brain_regions import get_region_names
from visualization import (
    create_activation_volume,
    plot_brain_surface,
    plot_brain_glass,
    plot_brain_stat,
)

KCAL_MIN = -15.0
KCAL_MAX = -1.0
SURFACE_SIGMA = 12.0
DEFAULT_SIGMA = 6.0

GUIDE_SURFACE = """
| Panel | What you are seeing |
|-------|---------------------|
| **Left — Lateral (Outer Surface)** | Side view of the left hemisphere from the outside. Shows lateral cortex (motor, parietal, temporal areas). |
| **Right — Lateral** | Same as above for the right hemisphere. |
| **Front (Anterior)** | Looking straight at the forehead side of the brain. Shows frontal lobes. |
| **Top (Dorsal)** | Bird's-eye view from above the head. Shows superior cortex. |
| **Bottom (Inferior)** | View from below the head, looking up. Shows orbitofrontal cortex and temporal poles. |

**Color scale** — Gray surface = no activation (below threshold).
Yellow → Orange → Red = increasing binding affinity.
Only regions with ≥ 1 % intensity are colored, matching the style of *Yachou et al. 2025* (Fig. 2–3).
"""

GUIDE_GLASS = """
| Panel | Direction | What you are seeing |
|-------|-----------|---------------------|
| **Left Sagittal** | Looking from the left side | Full projection through the brain left-to-right |
| **Axial (Top-down)** | Looking from above | Full projection top to bottom — like an X-ray from the crown |
| **Right Sagittal** | Looking from the right side | Mirror of the left sagittal panel |
| **Coronal (Front)** | Looking from the front | Full front-to-back projection — shows bilateral activation |

Because each panel is a **full-depth projection** (like an X-ray), deep subcortical regions (thalamus, hippocampus, striatum) are always visible, even if they cannot be seen on the cortical surface.
"""

GUIDE_STAT = """
| Row | What you are seeing |
|-----|---------------------|
| **Axial slices (Row 1)** | Six horizontal cuts through the brain, equally spaced from bottom to top. Each slice is like one layer of an MRI scan. Useful for seeing bilateral and deep structures. |
| **Orthogonal cross-sections (Row 2)** | Three perpendicular slices placed at the coordinates of the **peak activation** in your data: sagittal (left–right cut), coronal (front–back cut), axial (top–bottom cut). The cross-hair marks the exact peak location. |

Use this mode when you need to inspect **subcortical structures** (hippocampus, thalamus, amygdala, basal ganglia) that sit deep inside the brain and may not appear prominently on the cortical surface view.
"""


def kcal_to_normalized(kcal):
    clamped = max(KCAL_MIN, min(KCAL_MAX, kcal))
    return (abs(clamped) - abs(KCAL_MAX)) / (abs(KCAL_MIN) - abs(KCAL_MAX)) * 100.0


# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Neuro-Target Affinity Visualizer", layout="wide")
st.title("Neuro-Target Affinity Visualizer")
st.caption("Visualize protein/target binding affinity across brain regions")

if "regions" not in st.session_state:
    st.session_state.regions = []

# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Add Brain Region")
    region = st.selectbox("Brain Region", get_region_names())
    kcal_score = st.number_input(
        "Binding Affinity (kcal/mol)",
        min_value=-15.0,
        max_value=-0.1,
        value=-7.0,
        step=0.1,
        format="%.1f",
        help="Enter a negative value. More negative = stronger binding. "
             "Typical range: -1 (weak) to -15 (very strong).",
    )

    if st.button("Add Region", use_container_width=True):
        st.session_state.regions.append(
            (region, kcal_score, kcal_to_normalized(kcal_score))
        )
        st.rerun()

    st.divider()
    st.header("Active Regions")

    if not st.session_state.regions:
        st.info("No regions added yet.")
    else:
        to_remove = None
        for i, (name, kcal, norm) in enumerate(st.session_state.regions):
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{name}**  \n{kcal:.1f} kcal/mol ({norm:.0f} %)")
            if col2.button("X", key=f"rm_{i}"):
                to_remove = i

        if to_remove is not None:
            st.session_state.regions.pop(to_remove)
            st.rerun()

        if st.button("Clear All", use_container_width=True):
            st.session_state.regions.clear()
            st.rerun()

# ── View mode selector ─────────────────────────────────────────────────────
view_mode = st.radio(
    "View Mode",
    ["3D Surface", "Glass Brain", "Stat Map (Slices)"],
    horizontal=True,
    help=(
        "3D Surface — realistic cortical mesh from multiple angles (paper style). "
        "Glass Brain — transparent X-ray projection, best for deep structures. "
        "Stat Map — anatomical MRI slices, best for precise anatomical localisation."
    ),
)

# Per-mode guide
if view_mode == "3D Surface":
    with st.expander("How to read the 3D Surface view", expanded=False):
        st.markdown(GUIDE_SURFACE)
elif view_mode == "Glass Brain":
    with st.expander("How to read the Glass Brain view", expanded=False):
        st.markdown(GUIDE_GLASS)
else:
    with st.expander("How to read the Stat Map view", expanded=False):
        st.markdown(GUIDE_STAT)

# ── Main visualization ──────────────────────────────────────────────────────
if st.session_state.regions:
    pairs = [(name, norm) for name, _, norm in st.session_state.regions]

    if view_mode == "3D Surface":
        with st.spinner("Rendering 3D surface — this takes ~20 seconds…"):
            nifti_img = create_activation_volume(pairs, sigma=SURFACE_SIGMA)
            fig = plot_brain_surface(nifti_img)
    elif view_mode == "Glass Brain":
        with st.spinner("Rendering glass brain…"):
            nifti_img = create_activation_volume(pairs, sigma=DEFAULT_SIGMA)
            fig = plot_brain_glass(nifti_img)
    else:
        with st.spinner("Rendering anatomical slices…"):
            nifti_img = create_activation_volume(pairs, sigma=DEFAULT_SIGMA)
            fig = plot_brain_stat(nifti_img)

    st.pyplot(fig)
    plt.close(fig)

    # Summary table
    st.subheader("Summary")
    st.markdown("| Region | kcal/mol | Intensity |")
    st.markdown("|--------|----------|-----------|")
    for name, kcal, norm in st.session_state.regions:
        bar = "█" * int(norm / 5)
        st.markdown(f"| {name} | {kcal:.1f} | {norm:.0f} % {bar} |")

else:
    st.info("Add brain regions from the sidebar to begin visualization.")
