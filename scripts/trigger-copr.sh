#!/usr/bin/env bash
# Trigger COPR builds for updated packages
set -euo pipefail

COPR_OWNER="avengemedia"
COPR_PROJECT="danklinux"

echo "🚀 Triggering COPR builds..."

# Check if copr-cli is available
if ! command -v copr-cli &> /dev/null; then
    echo "❌ copr-cli not found. Skipping COPR builds."
    echo "   Install with: sudo dnf install copr-cli"
    exit 0
fi

# Check if COPR config exists
if [[ ! -f ~/.config/copr ]]; then
    echo "⚠️  COPR configuration not found at ~/.config/copr"
    echo "   Skipping COPR builds."
    exit 0
fi

# Function to trigger build for a package
trigger_build() {
    local package_name="$1"

    echo ""
    echo "📦 Building $package_name..."

    if copr-cli build-package "$COPR_OWNER/$COPR_PROJECT" \
        --name "$package_name" \
        --timeout 7200 \
        --nowait; then
        echo "   ✓ Build triggered successfully"
        return 0
    else
        echo "   ❌ Build trigger failed"
        return 1
    fi
}

# Determine which packages to build based on git changes
CHANGED_FILES=$(git diff HEAD~1 --name-only 2>/dev/null || echo "")

# Package build flags
BUILD_QUICKSHELL=false
BUILD_QUICKSHELL_GIT=false
BUILD_DGOP=false
BUILD_CLIPHIST=false
BUILD_MATUGEN=false
BUILD_HYPRPICKER=false
BUILD_BREAKPAD=false

# Check which specs changed
if echo "$CHANGED_FILES" | grep -q "quickshell/quickshell.spec"; then
    BUILD_QUICKSHELL=true
fi

if echo "$CHANGED_FILES" | grep -q "quickshell/quickshell-git.spec"; then
    BUILD_QUICKSHELL_GIT=true
fi

if echo "$CHANGED_FILES" | grep -q "dgop/dgop.spec"; then
    BUILD_DGOP=true
fi

if echo "$CHANGED_FILES" | grep -q "cliphist/cliphist.spec"; then
    BUILD_CLIPHIST=true
fi

if echo "$CHANGED_FILES" | grep -q "matugen/matugen.spec"; then
    BUILD_MATUGEN=true
fi

if echo "$CHANGED_FILES" | grep -q "hyprpicker/hyprpicker.spec"; then
    BUILD_HYPRPICKER=true
fi

if echo "$CHANGED_FILES" | grep -q "breakpad/breakpad.spec"; then
    BUILD_BREAKPAD=true
fi

# If no git history, check for uncommitted changes
if [[ -z "$CHANGED_FILES" ]]; then
    echo "ℹ️  No git history found, checking for uncommitted changes..."
    UNCOMMITTED=$(git diff --name-only 2>/dev/null || echo "")

    echo "$UNCOMMITTED" | grep -q "quickshell/quickshell.spec" && BUILD_QUICKSHELL=true
    echo "$UNCOMMITTED" | grep -q "quickshell/quickshell-git.spec" && BUILD_QUICKSHELL_GIT=true
    echo "$UNCOMMITTED" | grep -q "dgop/dgop.spec" && BUILD_DGOP=true
    echo "$UNCOMMITTED" | grep -q "cliphist/cliphist.spec" && BUILD_CLIPHIST=true
    echo "$UNCOMMITTED" | grep -q "matugen/matugen.spec" && BUILD_MATUGEN=true
    echo "$UNCOMMITTED" | grep -q "hyprpicker/hyprpicker.spec" && BUILD_HYPRPICKER=true
    echo "$UNCOMMITTED" | grep -q "breakpad/breakpad.spec" && BUILD_BREAKPAD=true
fi

# Trigger builds
BUILDS_TRIGGERED=0

if [[ "$BUILD_QUICKSHELL" == true ]]; then
    trigger_build "quickshell" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

if [[ "$BUILD_QUICKSHELL_GIT" == true ]]; then
    trigger_build "quickshell-git" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

if [[ "$BUILD_DGOP" == true ]]; then
    trigger_build "dgop" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

if [[ "$BUILD_CLIPHIST" == true ]]; then
    trigger_build "cliphist" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

if [[ "$BUILD_MATUGEN" == true ]]; then
    trigger_build "matugen" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

if [[ "$BUILD_HYPRPICKER" == true ]]; then
    trigger_build "hyprpicker" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

if [[ "$BUILD_BREAKPAD" == true ]]; then
    trigger_build "breakpad" && BUILDS_TRIGGERED=$((BUILDS_TRIGGERED + 1))
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [[ $BUILDS_TRIGGERED -gt 0 ]]; then
    echo "✅ Triggered $BUILDS_TRIGGERED COPR build(s)"
    echo "📊 View builds: https://copr.fedorainfracloud.org/coprs/$COPR_OWNER/$COPR_PROJECT/builds/"
else
    echo "ℹ️  No builds triggered (no package changes detected)"
fi
