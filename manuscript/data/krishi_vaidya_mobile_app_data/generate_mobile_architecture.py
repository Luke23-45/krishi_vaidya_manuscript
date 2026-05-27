from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def add_box(ax, x, y, w, h, text, fc, ec="#24422a", fs=8.2):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.035,rounding_size=0.025",
        linewidth=1.15,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color="#102015")
    return patch


def arrow(ax, start, end, label=None):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=1.0,
            color="#31543a",
            connectionstyle="arc3,rad=0.02",
        )
    )
    if label:
        x = (start[0] + end[0]) / 2
        y = (start[1] + end[1]) / 2
        ax.text(x, y + 0.025, label, ha="center", va="bottom", fontsize=7, color="#31543a")


def main():
    fig, ax = plt.subplots(figsize=(12.5, 8.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.patch.set_facecolor("#f7f4ed")
    ax.set_facecolor("#f7f4ed")

    ax.text(
        0.5,
        0.965,
        "Krishi Vaidya Mobile Application Architecture",
        ha="center",
        va="top",
        fontsize=17,
        fontweight="bold",
        color="#15351d",
    )
    ax.text(
        0.5,
        0.925,
        "Generated from the implemented Expo Router, provider, repository, offline, API, and ML source structure",
        ha="center",
        va="top",
        fontsize=9,
        color="#455b48",
    )

    add_box(ax, 0.04, 0.78, 0.18, 0.105, "Expo App Shell\napp.config.ts\nRoot layout", "#dff0d9")
    add_box(ax, 0.29, 0.78, 0.18, 0.105, "Root Providers\nTheme, ErrorBoundary\nSyncStatus, Services\nRepositories", "#dff0d9")
    add_box(ax, 0.54, 0.78, 0.18, 0.105, "Expo Router\nOnboarding, Tabs\nScan Stack, Crops\nSettings, History", "#dff0d9")
    add_box(ax, 0.79, 0.78, 0.17, 0.105, "Feature Views\nHome, Scan, Result\nCrops, History\nSettings", "#dff0d9")

    add_box(ax, 0.06, 0.56, 0.19, 0.12, "View Models\nCapture, Preview\nAnalysis, Result\nCrops, Settings", "#eaf5c8")
    add_box(ax, 0.31, 0.56, 0.19, 0.12, "Domain Services\nCamera, Network\nNotifications, Haptics\nLocation, Voice", "#eaf5c8")
    add_box(ax, 0.56, 0.56, 0.19, 0.12, "Repositories\nScans, Crops\nTasks, Notes\nCatalog", "#eaf5c8")
    add_box(ax, 0.79, 0.56, 0.17, 0.12, "State Stores\nApp settings\nScan history\nCrop and notification\nUI caches", "#eaf5c8")

    add_box(ax, 0.05, 0.34, 0.18, 0.12, "Capture and Quality\nVisionCamera\nGallery fallback\nImage quality gate", "#d7edf1")
    add_box(ax, 0.29, 0.34, 0.18, 0.12, "On-device Inference\nTFLite assets\nint8, fp16, fp32\nGPU with CPU fallback", "#d7edf1")
    add_box(ax, 0.53, 0.34, 0.18, 0.12, "Cloud Diagnosis\n/api/v1/diagnose\nmultipart image\nretry and timeout", "#d7edf1")
    add_box(ax, 0.77, 0.34, 0.18, 0.12, "Result Actions\nTreatment timeline\nPDF export\nFeedback\nReminders", "#d7edf1")

    add_box(ax, 0.05, 0.13, 0.21, 0.12, "SQLite Local Data\nscans, offline_queue\nsync_queue, plots\ntasks, notes, advisories", "#f3e3bf")
    add_box(ax, 0.31, 0.13, 0.18, 0.12, "Offline Sync\nNetwork monitor\n5-minute periodic sync\nbatch size 10", "#f3e3bf")
    add_box(ax, 0.55, 0.13, 0.18, 0.12, "Configuration\nAPI base URL, API key\nweather key, flags\nsecure-store plugin", "#f3e3bf")
    add_box(ax, 0.78, 0.13, 0.17, 0.12, "Localization and UX\nNepali fallback\nEnglish support\naccessibility settings", "#f3e3bf")

    arrow(ax, (0.22, 0.835), (0.29, 0.835))
    arrow(ax, (0.47, 0.835), (0.54, 0.835))
    arrow(ax, (0.72, 0.835), (0.79, 0.835))
    arrow(ax, (0.875, 0.78), (0.155, 0.68), "screen actions")
    arrow(ax, (0.155, 0.56), (0.14, 0.46))
    arrow(ax, (0.155, 0.56), (0.385, 0.46))
    arrow(ax, (0.405, 0.56), (0.62, 0.46))
    arrow(ax, (0.655, 0.56), (0.15, 0.25))
    arrow(ax, (0.655, 0.56), (0.40, 0.25))
    arrow(ax, (0.625, 0.34), (0.64, 0.25))
    arrow(ax, (0.86, 0.34), (0.865, 0.25))
    arrow(ax, (0.40, 0.34), (0.62, 0.34), "optional cloud step")
    arrow(ax, (0.71, 0.40), (0.77, 0.40))

    ax.text(
        0.5,
        0.035,
        "Evidence source: mobile_app/app source files. The figure documents implemented application structure, not runtime performance.",
        ha="center",
        va="bottom",
        fontsize=7.5,
        color="#55645a",
    )

    fig.savefig(OUT / "mobile_app_architecture.pdf", bbox_inches="tight")
    fig.savefig(OUT / "mobile_app_architecture.png", dpi=220, bbox_inches="tight")


if __name__ == "__main__":
    main()
