from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def add_box(ax, x, y, w, h, text, face, edge="#263f2d", fs=8.0):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.025,rounding_size=0.025",
        linewidth=1.1,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color="#142217")
    return patch


def add_arrow(ax, start, end):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.0,
            color="#31543a",
        )
    )


def main():
    fig, ax = plt.subplots(figsize=(12.6, 8.2))
    fig.patch.set_facecolor("#f8f4ea")
    ax.set_facecolor("#f8f4ea")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.965,
        "Krishi Vaidya Testing and Validation Coverage",
        ha="center",
        va="top",
        fontsize=17,
        fontweight="bold",
        color="#14351c",
    )
    ax.text(
        0.5,
        0.925,
        "Evidence-backed validation layers from datasets and models through API contracts, mobile workflow checks, and final evidence gaps",
        ha="center",
        va="top",
        fontsize=8.6,
        color="#455b48",
    )

    colors = {
        "strong": "#dff0d9",
        "model": "#eaf5c8",
        "api": "#d7edf1",
        "partial": "#f3e3bf",
        "gap": "#f5d0c8",
    }

    add_box(ax, 0.045, 0.74, 0.17, 0.12, "YOLO Validation\ntraining metrics\nthreshold sweep\nrobust validation\nquantized latency", colors["strong"])
    add_box(ax, 0.295, 0.74, 0.17, 0.12, "VLM Validation\ndataset scanner\nprediction metrics\nconfusion matrix\nparse diagnostics", colors["model"])
    add_box(ax, 0.545, 0.74, 0.17, 0.12, "Backend Tests\nscan service unit\nscan route integration\nMongo memory server\nowner scoping", colors["api"])
    add_box(ax, 0.795, 0.74, 0.16, 0.12, "VLM API Tests\nhealth/ready\nauth and scope\ninvalid image\nrate limits", colors["api"])

    add_box(ax, 0.045, 0.49, 0.17, 0.12, "Mobile Checks\nsource inspection\nONNX harness\nno full executed\napp workflow suite yet", colors["partial"])
    add_box(ax, 0.295, 0.49, 0.17, 0.12, "Integration Checks\nroute contracts\nvalidation boundaries\nschema contracts\noffline branches", colors["partial"])
    add_box(ax, 0.545, 0.49, 0.17, 0.12, "Reliability Controls\ninput validation\nJWT/bearer auth\ntimeouts/retries\nschema validation", colors["partial"])
    add_box(ax, 0.795, 0.49, 0.16, 0.12, "Missing Evidence\nlive E2E run\nscreenshots\nlatency\nmodel alignment", colors["gap"])

    add_box(ax, 0.16, 0.21, 0.20, 0.13, "Validated Claims\nmodel metrics, dataset integrity,\nscan-domain backend behavior,\nVLM API contract behavior", "#e6efe0")
    add_box(ax, 0.40, 0.21, 0.20, 0.13, "Cautious Claims\nmobile and integration structure\nare source-verified but need\nruntime demonstration", "#fff0cc")
    add_box(ax, 0.64, 0.21, 0.20, 0.13, "Not Yet Claimed\nproduction readiness, full\nmobile device performance,\ncomplete sync and full API coverage", "#f7d8d2")

    for x in [0.13, 0.38, 0.63, 0.875]:
        add_arrow(ax, (x, 0.74), (x, 0.61))
    add_arrow(ax, (0.13, 0.49), (0.26, 0.34))
    add_arrow(ax, (0.38, 0.49), (0.50, 0.34))
    add_arrow(ax, (0.63, 0.49), (0.50, 0.34))
    add_arrow(ax, (0.875, 0.49), (0.74, 0.34))

    ax.text(
        0.5,
        0.065,
        "Interpretation rule: the manuscript separates quantitative validation, automated test coverage, source-verified architecture, and missing runtime evidence.",
        ha="center",
        va="center",
        fontsize=7.6,
        color="#55645a",
    )

    fig.savefig(OUT / "validation_coverage.pdf", bbox_inches="tight")
    fig.savefig(OUT / "validation_coverage.png", dpi=220, bbox_inches="tight")


if __name__ == "__main__":
    main()
