#!/bin/bash
## Full OSINT Pipeline Script
# Usage: ./osint_pipeline.sh <target_domain> <company_name>

set -euo pipefail
DOMAIN="${1:?Usage: $0 <domain> <company_name>}"
COMPANY="${2:?Usage: $0 <domain> <company_name>}"
OUTPUT_DIR="./osint_$(echo $DOMAIN | tr '.' '_')_$(date +%Y%m%d)"

echo "========================================="
echo " OSINT Pipeline: $DOMAIN"
echo " Output: $OUTPUT_DIR"
echo "========================================="

mkdir -p "$OUTPUT_DIR"/{employees,emails,subdomains,services,vulns,cloud,report}

echo "[Phase 1] Subdomain Enumeration"
if command -v subfinder &>/dev/null; then
    subfinder -d "$DOMAIN" -all -o "$OUTPUT_DIR/subdomains/subfinder.txt" 2>/dev/null || true
fi

echo "[Phase 2] HTTP Probing"
if command -v httpx &>/dev/null && [ -s "$OUTPUT_DIR/subdomains/subfinder.txt" ]; then
    cat "$OUTPUT_DIR/subdomains/subfinder.txt" | \
        httpx -sc -title -td -server -o "$OUTPUT_DIR/services/httpx_results.txt" 2>/dev/null || true
fi

echo "========================================="
echo " Pipeline Complete. Review $OUTPUT_DIR"
echo "========================================="
