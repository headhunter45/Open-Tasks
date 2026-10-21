#!/usr/bin/env sh
# Open Tasks (ot) Installer Script
# Installs standalone Open Tasks (.zipapp) from GitHub Releases
set -eu

REPO="headhunter45/opentasks"
DEFAULT_INSTALL_DIR="${HOME}/.local/bin"
INSTALL_DIR="${OT_INSTALL_DIR:-$DEFAULT_INSTALL_DIR}"
VERSION="${OT_VERSION:-latest}"
BINARY_NAME="ot"

# Text styles
BOLD="\033[1m"
GREEN="\033[32m"
BLUE="\033[34m"
YELLOW="\033[33m"
RED="\033[31m"
RESET="\033[0m"

info() {
    printf "${BLUE}==>${RESET} ${BOLD}%s${RESET}\n" "$1"
}

success() {
    printf "${GREEN}✔${RESET} ${BOLD}%s${RESET}\n" "$1"
}

warn() {
    printf "${YELLOW}▲${RESET} %s\n" "$1"
}

error() {
    printf "${RED}✖ Error:${RESET} %s\n" "$1" >&2
    exit 1
}

# 1. Check Python installation
info "Checking host Python environment..."
if ! command -v python3 >/dev/null 2>&1; then
    error "python3 is required to run Open Tasks, but was not found in PATH."
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PY_MAJOR=$(echo "$PY_VER" | cut -d. -f1)
PY_MINOR=$(echo "$PY_VER" | cut -d. -f2)

if [ "$PY_MAJOR" -lt 3 ] || { [ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]; }; then
    error "Python 3.10 or higher is required (found Python $PY_VER)."
fi
success "Found Python $PY_VER"

# 2. Determine download URL
if [ "$VERSION" = "latest" ]; then
    DOWNLOAD_URL="https://github.com/${REPO}/releases/latest/download/ot.zipapp"
    SUMS_URL="https://github.com/${REPO}/releases/latest/download/SHA256SUMS"
    DISPLAY_VER="latest release"
else
    # Strip leading v if provided
    CLEAN_VER="${VERSION#v}"
    DOWNLOAD_URL="https://github.com/${REPO}/releases/download/v${CLEAN_VER}/ot-${CLEAN_VER}.zipapp"
    SUMS_URL="https://github.com/${REPO}/releases/download/v${CLEAN_VER}/SHA256SUMS"
    DISPLAY_VER="v${CLEAN_VER}"
fi

# 3. Create target directory
mkdir -p "$INSTALL_DIR"
DEST_FILE="${INSTALL_DIR}/${BINARY_NAME}"

# 4. Download artifact to temporary file
TMP_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'ot-install')
trap 'rm -rf "$TMP_DIR"' EXIT INT TERM

TMP_BIN="${TMP_DIR}/ot.zipapp"
TMP_SUMS="${TMP_DIR}/SHA256SUMS"

info "Downloading Open Tasks ($DISPLAY_VER)..."
if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$DOWNLOAD_URL" -o "$TMP_BIN"
    curl -fsSL "$SUMS_URL" -o "$TMP_SUMS" 2>/dev/null || true
elif command -v wget >/dev/null 2>&1; then
    wget -qO "$TMP_BIN" "$DOWNLOAD_URL"
    wget -qO "$TMP_SUMS" "$SUMS_URL" 2>/dev/null || true
else
    error "Neither curl nor wget was found. Please install one of them."
fi

# 5. Checksum verification if SHA256SUMS was downloaded
if [ -s "$TMP_SUMS" ]; then
    info "Verifying SHA-256 integrity..."
    TARGET_NAME=$(basename "$DOWNLOAD_URL")
    EXPECTED_SHA=$(grep -E "${TARGET_NAME}|ot\.zipapp" "$TMP_SUMS" | head -n 1 | awk '{print $1}')

    if [ -n "$EXPECTED_SHA" ]; then
        if command -v sha256sum >/dev/null 2>&1; then
            ACTUAL_SHA=$(sha256sum "$TMP_BIN" | awk '{print $1}')
        elif command -v shasum >/dev/null 2>&1; then
            ACTUAL_SHA=$(shasum -a 256 "$TMP_BIN" | awk '{print $1}')
        else
            ACTUAL_SHA=""
        fi

        if [ -n "$ACTUAL_SHA" ]; then
            if [ "$EXPECTED_SHA" != "$ACTUAL_SHA" ]; then
                error "SHA-256 verification failed (expected: $EXPECTED_SHA, got: $ACTUAL_SHA)"
            fi
            success "Checksum verified: ${ACTUAL_SHA:0:16}..."
        fi
    fi
fi

# 6. Install executable binary
mv "$TMP_BIN" "$DEST_FILE"
chmod +x "$DEST_FILE"
success "Installed Open Tasks to $DEST_FILE"

# 7. Verify installed launcher
INSTALLED_VER=$("$DEST_FILE" version 2>/dev/null | head -n 1 || true)
if [ -n "$INSTALLED_VER" ]; then
    success "$INSTALLED_VER"
fi

# 8. Path check
case ":$PATH:" in
    *":$INSTALL_DIR:"*) ;;
    *)
        echo ""
        warn "Note: $INSTALL_DIR is not currently in your PATH."
        printf "To use 'ot' anywhere, add this to your shell profile (~/.bashrc, ~/.zshrc):\n\n"
        printf "    export PATH=\"%s:\$PATH\"\n\n" "$INSTALL_DIR"
        ;;
esac

echo ""
printf "${GREEN}${BOLD}Open Tasks installation complete!${RESET}\n"
printf "Run ${BOLD}ot init${RESET} in any repository to get started.\n"
