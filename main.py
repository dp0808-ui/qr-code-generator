import argparse
from pathlib import Path
import qrcode
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_qr_code(url: str):
    output_dir = Path("qr_codes")
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_").strip("_") or "qrcode"
    file_path = output_dir / f"{safe_name}.png"

    logging.info(f"Generating QR code for URL: {url}")
    img = qrcode.make(url)
    img.save(file_path)
    logging.info(f"QR code successfully saved to {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="http://github.com/kaw393939")
    args = parser.parse_args()
    generate_qr_code(args.url)