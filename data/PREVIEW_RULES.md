Build a one-page preview website for a real small auto business, as a sales mockup from the web agency "Shopfront Sites".

Rules:
- Output ONE self-contained HTML file at /home/claude/shopfront-sites/preview/<SLUG>/index.html (inline CSS/JS; Google Fonts link allowed; no other external assets; no images — use CSS/SVG shapes and color instead).
- FIRST read the two reference previews named in your task fully and match their structure and quality: sticky header, hero with CTA, services, pricing, reviews, about/service area, quote form, footer, and the "Website preview by Shopfront Sites" banner linking to https://shopfrontsites.org. Also copy the `<meta name="robots" content="noindex, nofollow">` tag they carry.
- Use the shop's REAL name, phone (tel: links), city/service area, and services from the lead JSON. Quote 2–3 of their real Google reviews (trim to 1–2 sentences each, attribute as "Google review"). Show the real rating and review count. Link their Instagram/Facebook if present. Use the owner's first name if present.
- Pricing: "Starting at $X" ranges realistic for this trade in Tampa Bay, with the note "Example pricing — we'll put in your real numbers." Never invent certifications, warranties, film brands, or years in business.
- Quote form: fields name, phone, vehicle, what you need; submit opens an SMS to the shop's number with fields prefilled (href="sms:+1...?&body=..." built by JS), same as the references.
- Mobile-first, 16px side gutters, no horizontal scroll at 390px, dark-mode aware like the references.
- Pick a DISTINCT color palette and font pairing that fits this specific business — do NOT reuse the palette of either reference.
- Do NOT run git commands. Do NOT edit any other file.

When finished, reply with ONLY: the file path, the palette (3 hex codes), and the headline. Nothing else.

EXTRA RULES (learned from earlier batches):
- At 390px wide the sticky header MUST NOT overflow: keep the brand text short, let the header wrap, and give the call button `white-space:nowrap` with a small font. Check this mentally before finishing.
- Navy+amber, teal/aqua, and coal+ember palettes are overused already — choose something else.
