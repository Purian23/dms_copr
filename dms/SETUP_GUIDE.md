# DMS Copr Setup Guide

**Complete instructions for creating, building, and maintaining DMS Copr packages**

---

## 📋 **Prerequisites**

```bash
# Install required tools
sudo dnf install fedora-packager copr-cli rpkg-util git-core golang rpkg

# Configure Copr CLI
copr-cli --help  # Follow setup if not configured
```

---

## 🏗️ **Part 1: Create dgop Copr Project**

### Step 1: Create the Project

```bash
copr-cli create dgop \
  --chroot fedora-41-x86_64 \
  --chroot fedora-41-aarch64 \
  --chroot fedora-42-x86_64 \
  --chroot fedora-42-aarch64 \
  --description "dgop - System monitoring CLI for DankMaterialShell"
```

### Step 2: Build dgop (Stable)

```bash
cd ~/rpmbuild/SPECS
cp /home/purian23/dms_copr/dgop/dgop.spec .

# Build SRPM
rpmbuild -bs dgop.spec

# Upload to Copr
copr-cli build dgop ~/rpmbuild/SRPMS/dgop-*.src.rpm
```

### Step 3: Build dgop-git (Optional - Development)

**Option A: Manual Build**
```bash
cp /home/purian23/dms_copr/dgop/dgop-git.spec ~/rpmbuild/SPECS/
rpmbuild -bs dgop-git.spec
copr-cli build dgop ~/rpmbuild/SRPMS/dgop-git-*.src.rpm
```

**Option B: Auto-Rebuild with GitHub Webhook**
1. Go to Copr web UI → dgop project → Packages
2. Click "New Package" → Type: **SCM**
3. Fill in:
   - **Clone URL:** `https://github.com/AvengeMedia/dgop.git`
   - **Subdirectory:** (leave empty)
   - **Spec file:** `dgop-git.spec`
   - **Type:** git
   - **Branch:** master
4. Enable "Auto-rebuild"
5. Add webhook to dgop GitHub repo settings

---

## 🏗️ **Part 2: Build Standalone Dependencies**

Before creating the DMS project, we need to build the standalone dependency packages that DMS requires. These are independent Copr repositories that anyone can use.

### Step 1: Build cliphist (Wayland Clipboard Manager)

```bash
# Create Copr project
copr-cli create cliphist \
  --chroot fedora-41-x86_64 \
  --chroot fedora-41-aarch64 \
  --chroot fedora-42-x86_64 \
  --chroot fedora-42-aarch64 \
  --description "cliphist - Wayland clipboard history manager with support for text and images"

# Vendor Go dependencies locally
cd /tmp
wget https://github.com/sentriz/cliphist/archive/refs/tags/v0.6.1.tar.gz -O cliphist-0.6.1.tar.gz
tar xzf cliphist-0.6.1.tar.gz
cd cliphist-0.6.1
go mod vendor
tar czf ~/rpmbuild/SOURCES/cliphist-0.6.1-vendor.tar.gz vendor/

# Download source
cd ~/rpmbuild/SOURCES
wget https://github.com/sentriz/cliphist/archive/refs/tags/v0.6.1/cliphist-0.6.1.tar.gz

# Build and upload
cd ~/rpmbuild/SPECS
cp /home/purian23/dms_copr/cliphist/cliphist.spec .
rpmbuild -bs cliphist.spec
copr-cli build cliphist ~/rpmbuild/SRPMS/cliphist-*.src.rpm
```

### Step 2: Build matugen (Material You Color Generator)

```bash
# Create Copr project
copr-cli create matugen \
  --chroot fedora-41-x86_64 \
  --chroot fedora-41-aarch64 \
  --chroot fedora-42-x86_64 \
  --chroot fedora-42-aarch64 \
  --description "matugen - Material You color generation tool for theming"

# Vendor Rust dependencies locally
cd /tmp
wget https://github.com/InioX/matugen/archive/refs/tags/v2.4.1.tar.gz -O matugen-2.4.1.tar.gz
tar xzf matugen-2.4.1.tar.gz
cd matugen-2.4.1
cargo vendor
tar czf ~/rpmbuild/SOURCES/matugen-2.4.1-vendor.tar.gz vendor/

# Download source
cd ~/rpmbuild/SOURCES
wget https://github.com/InioX/matugen/archive/refs/tags/v2.4.1.tar.gz -O matugen-2.4.1.tar.gz

# Build and upload (takes ~5-6 minutes)
cd ~/rpmbuild/SPECS
cp /home/purian23/dms_copr/matugen/matugen.spec .
rpmbuild -bs matugen.spec
copr-cli build matugen ~/rpmbuild/SRPMS/matugen-*.src.rpm
```

### Step 3: Build material-symbols-fonts (Google Icon Font)

```bash
# Create Copr project
copr-cli create material-symbols-fonts \
  --chroot fedora-41-x86_64 \
  --chroot fedora-41-aarch64 \
  --chroot fedora-42-x86_64 \
  --chroot fedora-42-aarch64 \
  --description "Material Symbols variable font by Google - Required for DankMaterialShell UI icons"

# Download font file (13.91MB)
cd ~/rpmbuild/SOURCES
wget 'https://github.com/google/material-design-icons/raw/master/variablefont/MaterialSymbolsRounded[FILL,GRAD,opsz,wght].ttf' -O MaterialSymbolsRounded.ttf

# Build and upload
cd ~/rpmbuild/SPECS
cp /home/purian23/dms_copr/fonts/material-symbols-fonts.spec .
rpmbuild -bs material-symbols-fonts.spec
copr-cli build material-symbols-fonts ~/rpmbuild/SRPMS/material-symbols-fonts-*.src.rpm
```

**Important Notes:**
- **Go packages** require vendored dependencies because Copr build environments have no network access
- **Rust packages** also require vendored dependencies for the same reason
- **Font packages** work with direct file downloads as long as the filename is simple

---

## 🏗️ **Part 3: Create dms Copr Project**

### Step 1: Create the Project

```bash
copr-cli create dms \
  --chroot fedora-41-x86_64 \
  --chroot fedora-41-aarch64 \
  --chroot fedora-42-x86_64 \
  --chroot fedora-42-aarch64 \
  --description "DankMaterialShell - Material Design Wayland compositor configuration"
```

### Step 2: Configure External Repositories

Go to Copr web UI → dms project → Settings → **External repositories**

Add these repositories:
```
copr://purian23/dgop
copr://purian23/cliphist
copr://purian23/matugen
copr://purian23/material-symbols-fonts
copr://errornointernet/quickshell
```

### Step 3: Build dms (Stable)

```bash
cp /home/purian23/dms_copr/dms/dms.spec ~/rpmbuild/SPECS/

# Build SRPM
rpmbuild -bs dms.spec

# Upload to Copr
copr-cli build dms ~/rpmbuild/SRPMS/dms-*.src.rpm
```

### Step 4: Build dms-git (Optional - Development)

**Option A: Manual Build**
```bash
cp /home/purian23/dms_copr/dms/dms-git.spec ~/rpmbuild/SPECS/
rpmbuild -bs dms-git.spec
copr-cli build dms ~/rpmbuild/SRPMS/dms-git-*.src.rpm
```

**Option B: Auto-Rebuild with GitHub Webhook**
1. Go to Copr web UI → dms project → Packages
2. Click "New Package" → Type: **SCM**
3. Fill in:
   - **Clone URL:** `https://github.com/AvengeMedia/DankMaterialShell.git`
   - **Subdirectory:** (leave empty)
   - **Spec file:** `dms-git.spec`
   - **Type:** git
   - **Branch:** master
4. **Important:** In "Additional repo files" or "Buildroot packages", add: `rpkg-util`
5. Enable "Auto-rebuild"
6. Add webhook to DankMaterialShell GitHub repo settings

---

## 🔄 **Maintenance**

### Updating Stable Packages (dgop, dms)

When a new release is published:

1. **Update version in spec file:**
   ```bash
   # Edit dgop.spec or dms.spec
   # Change: Version: 0.1.5
   # Update Source URLs if needed
   # Update SHA256 checksums for dgop.spec
   ```

2. **Rebuild:**
   ```bash
   rpmbuild -bs <package>.spec
   copr-cli build <project> ~/rpmbuild/SRPMS/<package>-*.src.rpm
   ```

### Updating Development Packages (dgop-git, dms-git)

If using GitHub webhooks:
- **Automatic!** Pushes to master trigger rebuilds

If manual:
```bash
# Just rebuild - version auto-updates from git
rpmbuild -bs <package>-git.spec
copr-cli build <project> ~/rpmbuild/SRPMS/<package>-git-*.src.rpm
```

### Monitoring Builds

```bash
# List builds
copr-cli list-builds dgop
copr-cli list-builds dms

# Get build details
copr-cli build-status dgop <build-id>

# Cancel a build
copr-cli cancel <build-id>
```

---

## 🧪 **Testing Locally Before Upload**

### Mock Build (Simulates Copr Environment)

```bash
# Install mock
sudo dnf install mock
sudo usermod -a -G mock $USER
newgrp mock

# Build in mock
mock -r fedora-41-x86_64 ~/rpmbuild/SRPMS/dms-*.src.rpm

# Check results
ls /var/lib/mock/fedora-41-x86_64/result/
```

### Local Install Test

```bash
# Install built RPM
sudo dnf install /var/lib/mock/fedora-41-x86_64/result/dms-*.rpm

# Test
dms --version
```

---

## 📊 **Build Order Summary**

**Critical order to avoid dependency failures:**

1. **dgop project:**
   - Build `dgop.spec` (stable) ✅
   - Optional: `dgop-git.spec`

2. **Standalone dependency projects** (can be built in parallel):
   - Build `cliphist.spec` in purian23/cliphist project ✅
   - Build `matugen.spec` in purian23/matugen project ✅
   - Build `material-symbols-fonts.spec` in purian23/material-symbols-fonts project ✅

3. **dms project:**
   - Create project and add external repositories (dgop, cliphist, matugen, material-symbols-fonts, quickshell)
   - Build `dms.spec` (stable)
   - Optional: Build `dms-git.spec`

**Note:** The standalone packages (cliphist, matugen, material-symbols-fonts) are now in their own Copr projects so they can be used by anyone, not just DMS users.

---

## 👥 **User Installation Instructions**

After building, users install with:

```bash
# Enable repositories (all dependencies are automatically pulled in)
sudo dnf copr enable purian23/dms

# Install stable version
sudo dnf install dms

# OR install development version
sudo dnf install dms-git
```

**Note:** The dms Copr has external repositories configured, so enabling just `purian23/dms` will automatically enable all the dependency Coprs (dgop, cliphist, matugen, material-symbols-fonts, quickshell).

Alternatively, users can enable individual packages:

```bash
# For individual packages
sudo dnf copr enable purian23/dgop
sudo dnf copr enable purian23/cliphist
sudo dnf copr enable purian23/matugen
sudo dnf copr enable purian23/material-symbols-fonts

sudo dnf install dgop              # System monitor
sudo dnf install cliphist          # Clipboard manager
sudo dnf install matugen           # Color generator
sudo dnf install material-symbols-fonts  # Icon font
```

---

## 🐛 **Troubleshooting**

### Build Fails: "Nothing provides matugen" or "Nothing provides cliphist"
- You forgot to add the external Copr repositories to the dms project
- Go to dms project settings → External repositories → Add:
  - `copr://purian23/cliphist`
  - `copr://purian23/matugen`
  - `copr://purian23/material-symbols-fonts`

### Build Fails: "Nothing provides dgop"
- You forgot to add dgop Copr as external repository
- Go to dms project settings → External repositories → Add `copr://purian23/dgop`

### Go build fails: "cannot find package" or network errors
- Go packages need vendored dependencies in Copr (no network access during build)
- Create vendor tarball locally: `go mod vendor && tar czf vendor.tar.gz vendor/`
- Add as Source1 in spec and extract in %prep
- Build with `--offline` or `-mod=vendor` flag

### Rust build fails: "failed to download dependencies"
- Rust packages need vendored dependencies in Copr (no network access during build)
- Create vendor tarball locally: `cargo vendor && tar czf vendor.tar.gz vendor/`
- Add as Source1 in spec and configure `.cargo/config.toml` to use vendor directory
- Build with `cargo build --release --offline`

### Font package fails: "Can't download file"
- Use URL fragment `#/filename` to simplify source filename
- Example: `Source0: https://.../%5Bencoded%5D.ttf#/SimpleFilename.ttf`
- This avoids issues with special characters in filenames

### rpkg macros not working in dms-git.spec
- Make sure `rpkg-util` is in buildroot packages
- In Copr web UI when setting up SCM build, add it to "Additional packages"

### SHA256 mismatch in dgop.spec
- dgop released a new binary
- Download new binary, calculate checksum: `sha256sum dgop-linux-amd64.gz`
- Update SHA256SUM_AMD64 or SHA256SUM_ARM64 in spec

---

## 📚 **Additional Resources**

- **Fedora Packaging Guidelines:** https://docs.fedoraproject.org/en-US/packaging-guidelines/
- **Copr Documentation:** https://docs.pagure.org/copr.copr/
- **rpkg-util Guide:** https://pagure.io/rpkg-util
- **Mock Documentation:** https://rpm-software-management.github.io/mock/

---

**See CHECKLIST.md for a quick reference!**
