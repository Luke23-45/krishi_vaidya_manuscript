#!/usr/bin/env python
import os
import sys
import subprocess
from pathlib import Path

def check_and_install_dependencies():
    """State: CheckDependencies - Checks and installs PyMuPDF (fitz) if missing."""
    try:
        import fitz
        print("[+] PyMuPDF (fitz) is already installed.")
    except ImportError:
        print("[!] PyMuPDF (fitz) not found. Attempting automatic installation...")
        try:
            # Install pymupdf using the current python interpreter
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "pymupdf"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # Verify the import works now
            import fitz
            print("[+] PyMuPDF (fitz) successfully installed and verified.")
        except Exception as e:
            print(f"[-] ERROR: Failed to install PyMuPDF automatically.\n"
                  f"    Please install it manually by running: pip install pymupdf\n"
                  f"    Details: {e}", file=sys.stderr)
            sys.exit(1)

def run_pdf_build(build_script_path: Path, root_dir: Path):
    """State: BuildPDF - Invokes the PowerShell build script to compile the PDF."""
    print(f"[*] PDF is missing. Triggering compilation using: {build_script_path.name}")
    try:
        # Run PowerShell build script with Bypass policy
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(build_script_path)],
            cwd=str(root_dir),
            capture_output=True,
            text=True
        )
        
        # Stream output for visibility
        if result.stdout:
            print("[Build Log Output]:")
            print(result.stdout.strip())
        
        if result.returncode != 0:
            if result.stderr:
                print("[Build Log Error]:", file=sys.stderr)
                print(result.stderr.strip(), file=sys.stderr)
            raise RuntimeError(f"PowerShell build script failed with exit code {result.returncode}")
            
        print("[+] PDF built successfully.")
    except Exception as e:
        print(f"[-] ERROR: Failed to run build script.\n    Details: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # 1. State: InitPaths - Resolve paths
    script_dir = Path(__file__).resolve().parent
    menuscripts_dir = script_dir.parent
    root_dir = menuscripts_dir.parent  # C:\Users\Hellx\Documents\Programming\python\Project\iron\bc\GibbsQ
    
    build_script = menuscripts_dir / "scripts" / "build.ps1"
    pdf_path = menuscripts_dir / "build" / "main.pdf"
    output_dir = script_dir / "pdf_images"
    
    print("=== LaTeX PDF to Image State Machine ===")
    print(f"[*] Menuscripts Directory: {menuscripts_dir}")
    print(f"[*] Target PDF Path:       {pdf_path}")
    print(f"[*] Target Images Directory: {output_dir}\n")
    
    # 2. State: CheckDependencies
    check_and_install_dependencies()
    import fitz  # Guaranteed to be available now
    
    # 3. State: VerifyPDF & BuildPDF if missing
    if not pdf_path.exists():
        if not build_script.exists():
            print(f"[-] ERROR: Build script not found at {build_script}", file=sys.stderr)
            sys.exit(1)
        run_pdf_build(build_script, root_dir)
        
        # Double check existence after build attempt
        if not pdf_path.exists():
            print("[-] ERROR: Build completed but main.pdf is still missing.", file=sys.stderr)
            sys.exit(1)
    else:
        print("[+] Existing main.pdf detected. Skipping build step.")
        
    # 4. State: PrepareOutputDir - Clean and recreate output directory
    print(f"\n[*] Preparing output directory: {output_dir}")
    if output_dir.exists():
        print("[*] Completely removing existing output directory to prevent file mixing...")
        try:
            import shutil
            shutil.rmtree(output_dir)
        except Exception as e:
            print(f"[!] Warning: Failed to delete directory directly ({e}). Attempting file-by-file cleaning...")
            for item in output_dir.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                except Exception as inner_e:
                    print(f"[-] WARNING: Could not delete file {item.name}: {inner_e}")
                    
    # Recreate the output directory fresh
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        print("[+] Created fresh output directory.")
    except Exception as e:
        print(f"[-] ERROR: Failed to create output directory.\n    Details: {e}", file=sys.stderr)
        sys.exit(1)
        
    # 5. State: ConvertPages
    print("\n[*] Initializing PDF-to-Image conversion...")
    try:
        doc = fitz.open(str(pdf_path))
        total_pages = len(doc)
        print(f"[+] Successfully opened PDF. Total pages: {total_pages}")
        
        for page_num in range(total_pages):
            page = doc.load_page(page_num)
            
            # Using 150 DPI resolution (matrix scaling factor = 150 / 72 = ~2.08)
            # This keeps image size reasonable while preserving crystal clear math equations
            zoom = 150 / 72
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            page_name = f"page_{page_num + 1:03d}.png"
            output_file = output_dir / page_name
            pix.save(str(output_file))
            print(f"    -> Rendered page {page_num + 1}/{total_pages} as {page_name}")
            
        doc.close()
        print(f"\n[+] SUCCESS: All {total_pages} pages successfully converted to PNG!")
        print(f"[+] Output directory: {output_dir}")
    except Exception as e:
        print(f"[-] ERROR: Page conversion failed.\n    Details: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
