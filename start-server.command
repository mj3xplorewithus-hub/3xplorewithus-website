#!/bin/bash
cd "$(dirname "$0")"
echo "Starting 3xploreWithUs local server..."
echo "Open Safari and go to: http://localhost:8080"
echo "Press Ctrl+C to stop."
python3 -m http.server 8080
