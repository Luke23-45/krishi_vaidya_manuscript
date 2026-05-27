from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def box(ax, xy, wh, text, face, edge="#24422a", fs=8.1):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.025,rounding_size=0.025",
        linewidth=1.15,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color="#102015")
    return patch


def arrow(ax, start, end, label=None, rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.05,
            color="#31543a",
            connectionstyle=f"arc3,rad={rad}",
        )
    )
    if label:
        ax.text(
            (start[0] + end[0]) / 2,
            (start[1] + end[1]) / 2 + 0.018,
            label,
            ha="center",
            va="bottom",
            fontsize=6.9,
            color="#31543a",
        )


def main():
    fig, ax = plt.subplots(figsize=(13.2, 8.6))
    fig.patch.set_facecolor("#f8f4ea")
    ax.set_facecolor("#f8f4ea")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.965,
        "Krishi Vaidya Integrated Diagnosis Workflow",
        ha="center",
        va="top",
        fontsize=17,
        fontweight="bold",
        color="#14351c",
    )
    ax.text(
        0.5,
        0.927,
        "Source-backed flow across mobile app, backend API, VLM inference gateway, Google AI advisory generation, and local persistence",
        ha="center",
        va="top",
        fontsize=8.8,
        color="#455b48",
    )

    # Mobile stage.
    box(ax, (0.035, 0.76), (0.16, 0.105), "Mobile Capture\nVisionCamera or gallery\ncrop hint optional", "#dff0d9")
    box(ax, (0.035, 0.58), (0.16, 0.105), "Mobile Review\nquality check\nimage editor\nanalysis state machine", "#dff0d9")
    box(ax, (0.035, 0.40), (0.16, 0.105), "Network-aware\nDiagnosis Hook\nonline / slow / offline", "#dff0d9")
    box(ax, (0.035, 0.20), (0.16, 0.105), "Local Persistence\nscan history\noffline queue\nsync queue", "#f3e3bf")

    # Backend stage.
    box(ax, (0.285, 0.70), (0.18, 0.115), "Backend API\nPOST /api/v1/diagnose\nmultipart field image", "#d7edf1")
    box(ax, (0.285, 0.51), (0.18, 0.115), "Validation Layer\ncrop_name check\nJPEG / PNG / WEBP\n64-4096 px, size limit", "#d7edf1")
    box(ax, (0.285, 0.31), (0.18, 0.115), "Diagnosis Service\nrequest_id\nprocessing timer\nresponse assembly", "#d7edf1")

    # VLM stage.
    box(ax, (0.555, 0.70), (0.17, 0.115), "VLM Readiness\nGET /ready\nvLLM connected", "#eaf5c8")
    box(ax, (0.555, 0.51), (0.17, 0.115), "VLM Inference\nPOST /v1/inference\nbase64 image\nJWT / bearer auth", "#eaf5c8")
    box(ax, (0.555, 0.31), (0.17, 0.115), "Prediction Parsing\nJSON extraction\nraw text preserved\nconfidence fields", "#eaf5c8")

    # Advisory/result stage.
    box(ax, (0.805, 0.66), (0.16, 0.13), "Advisory Generation\nGoogle AI Studio\nstrict JSON schema\noptional grounding", "#f5dfc8")
    box(ax, (0.805, 0.45), (0.16, 0.13), "Structured Response\ndisease, crop, tier\nsymptoms, advisory\nsources, model version", "#f5dfc8")
    box(ax, (0.805, 0.23), (0.16, 0.13), "Mobile Result UI\ntreatment timeline\nreminders, feedback\nPDF, history, voice", "#f5dfc8")

    # Main path arrows.
    arrow(ax, (0.115, 0.76), (0.115, 0.685))
    arrow(ax, (0.115, 0.58), (0.115, 0.505))
    arrow(ax, (0.195, 0.455), (0.285, 0.755), "online cloud request", rad=0.05)
    arrow(ax, (0.115, 0.40), (0.115, 0.305), "offline/failed")
    arrow(ax, (0.465, 0.755), (0.555, 0.755))
    arrow(ax, (0.64, 0.70), (0.64, 0.625))
    arrow(ax, (0.64, 0.51), (0.64, 0.425))
    arrow(ax, (0.465, 0.365), (0.555, 0.565), "VLM request", rad=0.06)
    arrow(ax, (0.725, 0.365), (0.805, 0.725), "parsed VLM + image", rad=0.08)
    arrow(ax, (0.885, 0.66), (0.885, 0.58))
    arrow(ax, (0.805, 0.515), (0.465, 0.365), "validated JSON", rad=-0.12)
    arrow(ax, (0.285, 0.365), (0.195, 0.455), "200 response", rad=-0.08)
    arrow(ax, (0.195, 0.455), (0.805, 0.295), "final report view", rad=-0.12)

    # Backend internal arrows.
    arrow(ax, (0.375, 0.70), (0.375, 0.625))
    arrow(ax, (0.375, 0.51), (0.375, 0.425))

    ax.text(
        0.50,
        0.075,
        "Important boundary: source inspection verifies the implemented integration structure. Final manuscript still needs live mobile-to-backend request examples, latency measurements, and device screenshots before claiming production runtime performance.",
        ha="center",
        va="center",
        fontsize=7.5,
        color="#55645a",
        wrap=True,
    )

    fig.savefig(OUT / "integration_workflow.pdf", bbox_inches="tight")
    fig.savefig(OUT / "integration_workflow.png", dpi=220, bbox_inches="tight")


if __name__ == "__main__":
    main()
