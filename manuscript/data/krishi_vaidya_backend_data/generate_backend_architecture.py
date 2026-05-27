from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


OUT_DIR = Path(__file__).resolve().parent / "outputs" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def box(ax, x, y, w, h, text, face="#f7f3ea", edge="#2f3a35", size=8.5):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.035",
        linewidth=1.2,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, wrap=True)


def arrow(ax, x1, y1, x2, y2, label=None):
    arr = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=12,
        linewidth=1.0,
        color="#25312c",
        shrinkA=4,
        shrinkB=4,
    )
    ax.add_patch(arr)
    if label:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.025, label, ha="center", va="bottom", fontsize=7.2)


def main():
    fig, ax = plt.subplots(figsize=(12.5, 7.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.patch.set_facecolor("#fbfaf6")
    ax.set_facecolor("#fbfaf6")

    box(ax, 0.03, 0.56, 0.14, 0.17, "Mobile App\nHTTP + multipart image requests", "#e6f0e6")
    box(ax, 0.22, 0.62, 0.16, 0.14, "Express App\n/api/v1\nhealth + Swagger in dev", "#efe6d8")
    box(ax, 0.22, 0.39, 0.16, 0.16, "Middleware\nHelmet, CORS, rate limits,\nJWT auth, multer, validation,\nlogging, errors", "#efe6d8")

    box(ax, 0.44, 0.66, 0.18, 0.13, "Routes + Controllers\nAuth, Users, Scans,\nCrops, Tasks, Notes,\nAdvisories, Diagnose", "#dde9f2")
    box(ax, 0.44, 0.43, 0.18, 0.16, "Services\nAuth, User, Scan, Crop,\nTask, Note, Advisory,\nDiagnosis", "#dde9f2")
    box(ax, 0.44, 0.22, 0.18, 0.12, "Repositories\nMongoose data access\nand ownership filters", "#dde9f2")

    box(ax, 0.70, 0.69, 0.13, 0.11, "MongoDB\nusers, tokens,\nscans, crops,\ntasks, notes,\nadvisories", "#f3e1e1", size=7.8)
    box(ax, 0.70, 0.53, 0.13, 0.10, "Redis\nclient initialized;\nBullMQ-compatible options", "#f3e1e1", size=7.8)
    box(ax, 0.70, 0.37, 0.13, 0.10, "Cloudinary\nscan images,\nprofile pictures,\nnote images", "#f3e1e1", size=7.8)
    box(ax, 0.70, 0.20, 0.13, 0.11, "VLM Inference\n/ready and\n/v1/inference\nBearer/JWT auth", "#f3e1e1", size=7.8)
    box(ax, 0.70, 0.05, 0.13, 0.10, "Google AI Advisory\nJSON schema,\nNepali + English\nadvice, sources", "#f3e1e1", size=7.8)

    box(ax, 0.88, 0.53, 0.10, 0.14, "Configuration\nZod-validated env,\nbackend modes:\ndiagnose, non_ai,\ncomplete", "#f8edc7", size=7.8)

    arrow(ax, 0.17, 0.645, 0.22, 0.69)
    arrow(ax, 0.30, 0.62, 0.30, 0.55)
    arrow(ax, 0.38, 0.47, 0.44, 0.505)
    arrow(ax, 0.53, 0.66, 0.53, 0.59)
    arrow(ax, 0.53, 0.43, 0.53, 0.34)
    arrow(ax, 0.62, 0.28, 0.70, 0.735, "persistent data")
    arrow(ax, 0.62, 0.51, 0.70, 0.58, "runtime client")
    arrow(ax, 0.62, 0.50, 0.70, 0.42, "image assets")
    arrow(ax, 0.62, 0.49, 0.70, 0.255, "VLM prediction")
    arrow(ax, 0.62, 0.485, 0.70, 0.10, "advisory generation")
    arrow(ax, 0.88, 0.60, 0.83, 0.585)
    arrow(ax, 0.88, 0.60, 0.38, 0.69)

    ax.text(
        0.5,
        0.94,
        "Verified Backend Architecture of Krishi Vaidya",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        color="#25312c",
    )
    ax.text(
        0.5,
        0.905,
        "Derived from backend/src application, container, route, service, model, configuration, and middleware files.",
        ha="center",
        va="center",
        fontsize=8.5,
        color="#4f5b55",
    )

    fig.savefig(OUT_DIR / "backend_architecture.pdf", bbox_inches="tight")
    fig.savefig(OUT_DIR / "backend_architecture.png", dpi=220, bbox_inches="tight")


if __name__ == "__main__":
    main()
