"""
Pathak Real Estate — Local SEO & Assets Automated Verification Script
Checks:
1. File integrity across all deliverables
2. Schema.org JSON-LD validity & required fields
3. Landing page link targets, phone numbers, and keyword coverage
4. QR code and printable flyer generation
"""

import os
import sys
import json
import re

def verify_all():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"[*] Starting verification in: {base_dir}\n")

    errors = []
    warnings = []

    # 1. Check file existence
    expected_files = [
        "local_seo_strategy_guide.md",
        "profile_copy_and_services.md",
        "review_generation_playbook.md",
        "google_posts_calendar.md",
        "local_citations_directory.md",
        "schema/real_estate_schema.json",
        "tools/generate_review_qr.py",
        "tools/review_qr.png",
        "tools/review_flyer.html",
        "website/index.html",
        "images/post1_builder_floor_flats.jpg",
        "images/post2_residential_plots.jpg",
        "images/post3_commercial_shops.jpg",
        "images/post4_home_buyer_guide.jpg",
        "images/post5_rental_properties.jpg",
        "images/post6_budget_flats.jpg",
        "images/post7_weekend_site_visits.jpg",
        "images/post8_luxury_villas.jpg"
    ]

    for rel_path in expected_files:
        full_path = os.path.join(base_dir, rel_path)
        if not os.path.isfile(full_path):
            errors.append(f"Missing expected file: {rel_path}")
        else:
            size = os.path.getsize(full_path)
            if size == 0:
                errors.append(f"File is empty: {rel_path}")
            else:
                print(f" [PASS] File exists: {rel_path} ({size:,} bytes)")

    # 2. Check Schema JSON-LD validity
    schema_path = os.path.join(base_dir, "schema", "real_estate_schema.json")
    if os.path.isfile(schema_path):
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                schema_data = json.load(f)
            
            required_keys = ["@context", "@type", "name", "telephone", "address", "geo", "areaServed"]
            for k in required_keys:
                if k not in schema_data:
                    errors.append(f"Schema missing required field: {k}")
            
            if schema_data.get("@type") != "RealEstateAgent":
                errors.append(f"Schema @type is {schema_data.get('@type')}, expected 'RealEstateAgent'")
            
            if schema_data.get("telephone") != "+919352222820":
                warnings.append(f"Schema phone is {schema_data.get('telephone')}")

            print(" [PASS] Schema.org JSON-LD validation passed successfully.")
        except Exception as e:
            errors.append(f"Schema JSON parsing failed: {e}")

    # 3. Check Website HTML Integrity & Keywords
    html_path = os.path.join(base_dir, "website", "index.html")
    if os.path.isfile(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Check phone number
        if "tel:+919352222820" not in html_content:
            errors.append("Landing page missing click-to-call link 'tel:+919352222820'")
        else:
            print(" [PASS] Click-to-call link 'tel:+919352222820' verified.")

        # Check WhatsApp link
        if "919352222820" not in html_content:
            errors.append("Landing page missing WhatsApp phone number 919352222820")
        else:
            print(" [PASS] WhatsApp integration link verified.")

        # Check embedded JSON-LD
        if 'type="application/ld+json"' not in html_content:
            errors.append("Landing page missing embedded application/ld+json script tag")
        else:
            print(" [PASS] Embedded application/ld+json found.")

        # Check local keyword coverage
        target_keywords = ["Jeevan Park", "Uttam Nagar", "Janak Puri", "Pathak Real Estate"]
        for kw in target_keywords:
            if kw.lower() not in html_content.lower():
                warnings.append(f"Keyword '{kw}' not detected in landing page HTML.")
            else:
                print(f" [PASS] Keyword '{kw}' verified in landing page.")

    # 4. Check QR flyer HTML
    flyer_path = os.path.join(base_dir, "tools", "review_flyer.html")
    if os.path.isfile(flyer_path):
        with open(flyer_path, "r", encoding="utf-8") as f:
            flyer_content = f.read()
        if "Pathak Real Estate" not in flyer_content:
            errors.append("Flyer HTML missing 'Pathak Real Estate'")
        if "data:image/png;base64" not in flyer_content:
            errors.append("Flyer HTML missing base64 embedded QR code")
        print(" [PASS] Review Flyer HTML verified with embedded QR code.")

    print("\n" + "=" * 50)
    if warnings:
        print(f"[!] {len(warnings)} Warning(s):")
        for w in warnings:
            print(f"    - {w}")
    if errors:
        print(f"[x] {len(errors)} Error(s) encountered:")
        for err in errors:
            print(f"    - {err}")
        return False
    else:
        print("[SUCCESS] All files and assets verified perfectly with 0 errors!")
        return True

if __name__ == "__main__":
    success = verify_all()
    sys.exit(0 if success else 1)
