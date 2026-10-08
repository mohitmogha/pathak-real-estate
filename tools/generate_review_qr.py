"""
Pathak Real Estate — Direct Google Review QR Code & Standee Flyer Generator
Generates:
1. review_qr.png (High-resolution PNG QR Code)
2. review_flyer.html (Printable Countertop Standee / Desk Flyer with Embedded QR Code)
"""

import os
import sys
import base64
from io import BytesIO

try:
    import qrcode
    from PIL import Image
except ImportError:
    print("Required packages missing. Please install with: pip install qrcode pillow")
    sys.exit(1)

def generate_qr_and_flyer(
    business_name="Pathak Real Estate",
    review_url="https://share.google/Zm8GaUdHTM4IsPYNA",
    phone="+91 9352222820",
    locality="Jeevan Park, Uttam Nagar, Janak Puri, West Delhi",
    output_dir=None
):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Generate High-Res QR Code Image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=2,
    )
    qr.add_data(review_url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="#1a365d", back_color="#ffffff")
    
    png_path = os.path.join(output_dir, "review_qr.png")
    qr_img.save(png_path)
    print(f"[+] Saved high-resolution QR code to: {png_path}")

    # Convert image to base64 for embedding directly inside the HTML flyer
    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # 2. Generate Beautiful Printable Standee / Flyer HTML
    flyer_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{business_name} - Google Review Standee Flyer</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    body {{
      background: #f1f5f9;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }}

    .standee {{
      background: #ffffff;
      width: 100%;
      max-width: 440px;
      padding: 40px 32px;
      border-radius: 24px;
      box-shadow: 0 20px 40px rgba(15, 23, 42, 0.12);
      border: 2px solid #e2e8f0;
      text-align: center;
      position: relative;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #eff6ff;
      color: #1d4ed8;
      font-weight: 700;
      font-size: 13px;
      padding: 6px 16px;
      border-radius: 9999px;
      margin-bottom: 20px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .business-title {{
      font-size: 28px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
      margin-bottom: 6px;
    }}

    .tagline {{
      font-size: 14px;
      color: #64748b;
      margin-bottom: 24px;
    }}

    .stars {{
      color: #f59e0b;
      font-size: 30px;
      letter-spacing: 4px;
      margin-bottom: 8px;
    }}

    .cta-text {{
      font-size: 20px;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 20px;
    }}

    .qr-container {{
      background: #ffffff;
      padding: 16px;
      border-radius: 20px;
      display: inline-block;
      border: 3px solid #e2e8f0;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.04);
      margin-bottom: 24px;
    }}

    .qr-image {{
      width: 220px;
      height: 220px;
      display: block;
    }}

    .instructions {{
      font-size: 13px;
      color: #475569;
      background: #f8fafc;
      padding: 12px 16px;
      border-radius: 12px;
      margin-bottom: 24px;
      line-height: 1.5;
    }}

    .footer {{
      border-top: 1px dashed #cbd5e1;
      padding-top: 20px;
    }}

    .contact-item {{
      font-size: 13px;
      color: #334155;
      font-weight: 600;
      margin-bottom: 4px;
    }}

    .location {{
      font-size: 12px;
      color: #64748b;
    }}

    .print-btn {{
      margin-top: 24px;
      background: #2563eb;
      color: white;
      border: none;
      padding: 12px 24px;
      font-size: 15px;
      font-weight: 600;
      border-radius: 10px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    }}

    .print-btn:hover {{
      background: #1d4ed8;
    }}

    @media print {{
      body {{
        background: white;
        padding: 0;
      }}
      .standee {{
        box-shadow: none;
        border: 2px solid #000;
        margin: 0 auto;
      }}
      .print-btn {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <div class="standee">
    <div class="badge">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
      </svg>
      Google Verified Business
    </div>

    <h1 class="business-title">{business_name}</h1>
    <p class="tagline">Plots • Builder Floors • Commercial • Rentals</p>

    <div class="stars">★★★★★</div>
    <div class="cta-text">Love Our Service? Leave a Review!</div>

    <div class="qr-container">
      <img src="data:image/png;base64,{qr_base64}" alt="Scan to Review on Google" class="qr-image">
    </div>

    <div class="instructions">
      📸 <strong>How to Review:</strong><br>
      Open your mobile camera or Google Lens & scan the QR code above to share your feedback directly on Google Maps.
    </div>

    <div class="footer">
      <div class="contact-item">📞 Direct Assistance: {phone}</div>
      <div class="location">📍 {locality}</div>
    </div>

    <button onclick="window.print()" class="print-btn">🖨️ Print Standee / Flyer</button>
  </div>

</body>
</html>
"""
    flyer_path = os.path.join(output_dir, "review_flyer.html")
    with open(flyer_path, "w", encoding="utf-8") as f:
        f.write(flyer_html)
    print(f"[+] Saved printable standee flyer to: {flyer_path}")
    return png_path, flyer_path

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    generate_qr_and_flyer(output_dir=current_dir)
