import io
import numpy as np
import nibabel as nib
from nilearn import plotting
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from matplotlib.gridspec import GridSpec
from brain_regions import get_coordinates

MNI_SHAPE = (91, 109, 91)
MNI_AFFINE = np.array([
    [2., 0., 0., -90.],
    [0., 2., 0., -126.],
    [0., 0., 2., -72.],
    [0., 0., 0., 1.],
])


def _mni_to_voxel(x, y, z):
    coord = np.array([x, y, z, 1.0])
    inv_affine = np.linalg.inv(MNI_AFFINE)
    voxel = inv_affine.dot(coord)[:3]
    return np.round(voxel).astype(int)


def create_activation_volume(regions_and_scores, sigma=6.0):
    volume = np.zeros(MNI_SHAPE, dtype=np.float64)
    sigma_vox = sigma / 2.0
    ii, jj, kk = np.mgrid[0:MNI_SHAPE[0], 0:MNI_SHAPE[1], 0:MNI_SHAPE[2]]

    for name, score in regions_and_scores:
        if score <= 0:
            continue
        x, y, z = get_coordinates(name)
        vi, vj, vk = _mni_to_voxel(x, y, z)
        amplitude = score / 100.0
        dist_sq = (ii - vi)**2 + (jj - vj)**2 + (kk - vk)**2
        gaussian = amplitude * np.exp(-dist_sq / (2 * sigma_vox**2))
        volume += gaussian

    volume = np.clip(volume, 0, 1)
    return nib.Nifti1Image(volume, MNI_AFFINE)


# ─────────────────────────────────────────────────────────────────────────────
# Helper: render one surface view to a PNG buffer (used by plot_brain_surface)
# ─────────────────────────────────────────────────────────────────────────────
def _surf_panel(nifti_img, view, hemi, dpi=140):
    fig, axes = plotting.plot_img_on_surf(
        nifti_img,
        surf_mesh="fsaverage5",
        views=[view],
        hemispheres=[hemi],
        colorbar=False,
        cmap="YlOrRd",
        vmin=0.0,
        vmax=1.0,
        threshold=0.01,   # gray brain below threshold, color only where activated
        bg_on_data=True,
        cbar_tick_format="%.1f",
    )
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close(fig)
    buf.seek(0)
    return mpimg.imread(buf)


# ─────────────────────────────────────────────────────────────────────────────
# 3D Surface — paper-style layout (Yachou et al. 2025, Fig. 2C / 3C)
# ─────────────────────────────────────────────────────────────────────────────
def plot_brain_surface(nifti_img):
    """
    Layout matches the paper (Fig. 2C / 3C):
      LEFT  — one large lateral view of the left hemisphere
      RIGHT — four small labeled views stacked: Right Lateral, Front, Top, Bottom
      FAR RIGHT — vertical colorbar (yellow → orange → red)

    The brain surface stays gray where there is no activation;
    color appears only above the 1 % threshold — matching the paper's style.
    """
    # Render the large panel (left hemisphere, lateral/outer side)
    img_large = _surf_panel(nifti_img, "lateral", "left", dpi=160)

    # Render the four small side panels
    small_cfg = [
        ("lateral",  "right", "Right — Lateral"),
        ("anterior", "left",  "Front  (Anterior)"),
        ("dorsal",   "left",  "Top  (Dorsal)"),
        ("ventral",  "left",  "Bottom  (Inferior)"),
    ]
    small_panels = [
        (_surf_panel(nifti_img, view, hemi, dpi=110), label)
        for view, hemi, label in small_cfg
    ]

    # ── Composite figure ──────────────────────────────────────────────────
    fig = plt.figure(figsize=(18, 13), facecolor="white")
    gs = GridSpec(
        4, 3, figure=fig,
        width_ratios=[2.4, 1.0, 0.07],
        wspace=0.04, hspace=0.04,
    )

    # Large panel
    ax_L = fig.add_subplot(gs[:, 0])
    ax_L.imshow(img_large, interpolation="lanczos")
    ax_L.axis("off")
    ax_L.set_title(
        "Left Hemisphere — Lateral  (Outer Surface)",
        fontsize=13, fontweight="bold", pad=8,
    )

    # Small panels
    for i, (img, label) in enumerate(small_panels):
        ax_s = fig.add_subplot(gs[i, 1])
        ax_s.imshow(img, interpolation="lanczos")
        ax_s.axis("off")
        ax_s.set_title(label, fontsize=9, fontweight="bold", pad=3)

    # Vertical colorbar
    cax = fig.add_subplot(gs[:, 2])
    cb = plt.colorbar(
        cm.ScalarMappable(norm=Normalize(vmin=0, vmax=1), cmap="YlOrRd"),
        cax=cax, orientation="vertical",
    )
    cb.set_label("Binding Intensity", fontsize=9, labelpad=10)
    cb.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
    cb.set_ticklabels(["0 %", "25 %", "50 %", "75 %", "100 %"])
    cb.ax.tick_params(labelsize=8)

    fig.suptitle(
        "Brain Region Affinity Map",
        fontsize=16, fontweight="bold", y=1.01,
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# Glass Brain — 4 projection directions with direction labels
# ─────────────────────────────────────────────────────────────────────────────
def plot_brain_glass(nifti_img):
    """
    Shows 4 glass-brain projections in one row:
      [Left sagittal]  [Axial / Top-down]  [Right sagittal]  [Coronal / Front]

    Each panel is a full projection through the brain (like an X-ray),
    so activation deep inside the brain is always visible regardless of depth.
    """
    display = plotting.plot_glass_brain(
        nifti_img,
        display_mode="lzry",   # L sagittal | axial | R sagittal | coronal
        colorbar=True,
        cmap="YlOrRd",
        vmax=1.0,
        vmin=0.0,
        plot_abs=False,
        alpha=0.8,
        title="Brain Region Affinity Map — Glass Brain",
    )

    fig = display.frame_axes.figure
    fig.set_size_inches(18, 5)

    # Add direction labels beneath each projection
    direction_labels = [
        (0.11, 0.01, "◄ L  Sagittal  R ►"),
        (0.37, 0.01, "◄ A  Axial (Top)  P ►"),
        (0.62, 0.01, "◄ L  Sagittal  R ►"),
        (0.87, 0.01, "◄ L  Coronal (Front)  R ►"),
    ]
    for x, y, txt in direction_labels:
        fig.text(x, y, txt, ha="center", va="bottom",
                 fontsize=7.5, color="#555555", style="italic")

    return fig


# ─────────────────────────────────────────────────────────────────────────────
# Stat Map (Slices) — axial strip + orthogonal cross-sections at peak
# ─────────────────────────────────────────────────────────────────────────────
def plot_brain_stat(nifti_img):
    """
    Two-row layout:
      Row 1 — 6 axial slices (horizontal cuts, top to bottom through the brain)
      Row 2 — 3 orthogonal cross-sections (sagittal / coronal / axial)
               placed at the coordinates of peak activation

    Use this mode to inspect deep subcortical structures that may not appear
    on the cortical surface rendering above.
    """
    # Find peak activation coordinate for orthogonal cut placement
    try:
        cut_xyz = plotting.find_xyz_cut_coords(nifti_img, activation_threshold=0.05)
    except Exception:
        cut_xyz = (0, 0, 0)

    stat_kw = dict(cmap="hot", vmax=1.0, black_bg=False)

    # ── Row 1: 6 axial slices ────────────────────────────────────────────
    disp_axial = plotting.plot_stat_map(
        nifti_img,
        display_mode="z",
        cut_coords=6,
        colorbar=True,
        title="Axial Slices  (horizontal cuts, inferior → superior)",
        **stat_kw,
    )
    fig_axial = disp_axial.frame_axes.figure
    fig_axial.set_size_inches(16, 4)

    # ── Row 2: orthogonal views at peak ─────────────────────────────────
    xyz_label = f"x={cut_xyz[0]:.0f}  y={cut_xyz[1]:.0f}  z={cut_xyz[2]:.0f} mm"
    disp_ortho = plotting.plot_stat_map(
        nifti_img,
        display_mode="ortho",
        cut_coords=cut_xyz,
        colorbar=True,
        title=f"Orthogonal Cross-Sections at Peak Activation  [{xyz_label}]",
        **stat_kw,
    )
    fig_ortho = disp_ortho.frame_axes.figure
    fig_ortho.set_size_inches(16, 4)

    # ── Combine both rows into one figure via image buffers ──────────────
    def _to_img(f):
        buf = io.BytesIO()
        f.savefig(buf, format="png", dpi=130, bbox_inches="tight",
                  facecolor="white", edgecolor="none")
        plt.close(f)
        buf.seek(0)
        return mpimg.imread(buf)

    img_axial = _to_img(fig_axial)
    img_ortho = _to_img(fig_ortho)

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(16, 9), facecolor="white",
        gridspec_kw={"hspace": 0.12},
    )

    ax1.imshow(img_axial, interpolation="lanczos")
    ax1.axis("off")
    ax1.set_title(
        "Axial Slices  —  horizontal cuts through the brain (top to bottom)",
        fontsize=10, fontweight="bold", pad=4,
    )

    ax2.imshow(img_ortho, interpolation="lanczos")
    ax2.axis("off")
    ax2.set_title(
        f"Orthogonal Cross-Sections at Peak Activation  [{xyz_label}]",
        fontsize=10, fontweight="bold", pad=4,
    )

    fig.suptitle(
        "Brain Region Affinity Map — Anatomical Slices",
        fontsize=14, fontweight="bold", y=1.01,
    )
    return fig
