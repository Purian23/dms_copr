# DMS Copr Setup Guide

**Complete instructions for creating, building, and maintaining DMS Copr packages**

---

## 📋 **Prerequisites**

```bash
# Install required tools
sudo dnf install fedora-packager copr-cli rpkg-util git-core golang

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
cp /home/purian23/Copr/dgop/dgop.spec .

# Build SRPM
rpmbuild -bs dgop.spec

# Upload to Copr
copr-cli build dgop ~/rpmbuild/SRPMS/dgop-*.src.rpm
```

### Step 3: Build dgop-git (Optional - Development)

**Option A: Manual Build**
```bash
cp /home/purian23/Copr/dgop/dgop-git.spec ~/rpmbuild/SPECS/
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

## 🏗️ **Part 2: Create dms-shell Copr Project**

### Step 1: Create the Project

```bash
copr-cli create dms-shell \
  --chroot fedora-41-x86_64 \
  --chroot fedora-41-aarch64 \
  --chroot fedora-42-x86_64 \
  --chroot fedora-42-aarch64 \
  --description "DankMaterialShell - Material Design Wayland compositor configuration"
```

### Step 2: Configure External Repositories

Go to Copr web UI → dms-shell project → Settings → **External repositories**

Add these repositories:
```
copr://<your-username>/dgop
copr://errornointernet/quickshell
```

**If using external Coprs for matugen/cliphist, add them here too!**

### Step 3: Handle matugen & cliphist

**Decision Time!** Choose one approach:

#### Option A: Use External Coprs (Faster)
1. Search Copr for up-to-date matugen and cliphist packages
2. Add their Coprs as external repositories in dms-shell project
3. Example:
   ```
   copr://<username>/matugen
   copr://<username>/cliphist
   ```

#### Option B: Package Yourself (Recommended)
1. Create `matugen.spec` (Rust build):
   ```spec
   Name:           matugen
   Version:        2.3.0
   Release:        1%{?dist}
   Summary:        Material You color generation tool
   
   License:        GPL-2.0-or-later
   URL:            https://github.com/InioX/matugen
   Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
   
   BuildRequires:  rust
   BuildRequires:  cargo
   
   %description
   Material You color generation tool for theming.
   
   %prep
   %autosetup
   
   %build
   cargo build --release
   
   %install
   install -Dm755 target/release/matugen %{buildroot}%{_bindir}/matugen
   
   %files
   %{_bindir}/matugen
   ```

2. Create `cliphist.spec` (Go build):
   ```spec
   Name:           cliphist
   Version:        0.5.0
   Release:        1%{?dist}
   Summary:        Wayland clipboard history manager
   
   License:        GPL-3.0-or-later
   URL:            https://github.com/sentriz/cliphist
   Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
   
   BuildRequires:  golang >= 1.21
   BuildRequires:  git-core
   
   %description
   Wayland clipboard manager with support for text and images.
   
   %prep
   %autosetup
   
   %build
   go build -o cliphist
   
   %install
   install -Dm755 cliphist %{buildroot}%{_bindir}/cliphist
   
   %files
   %{_bindir}/cliphist
   ```

3. Build and upload them to dms-shell Copr first

### Step 4: Build material-symbols-fonts

```bash
cd ~/rpmbuild/SPECS
cp /home/purian23/Copr/dms-shell/material-symbols-fonts.spec .

# Build SRPM
rpmbuild -bs material-symbols-fonts.spec

# Upload to Copr
copr-cli build dms-shell ~/rpmbuild/SRPMS/material-symbols-fonts-*.src.rpm
```

### Step 5: Build dms (Stable)

```bash
cp /home/purian23/Copr/dms-shell/dms.spec ~/rpmbuild/SPECS/

# Build SRPM
rpmbuild -bs dms.spec

# Upload to Copr
copr-cli build dms-shell ~/rpmbuild/SRPMS/dms-*.src.rpm
```

### Step 6: Build dms-git (Optional - Development)

**Option A: Manual Build**
```bash
cp /home/purian23/Copr/dms-shell/dms-git.spec ~/rpmbuild/SPECS/
rpmbuild -bs dms-git.spec
copr-cli build dms-shell ~/rpmbuild/SRPMS/dms-git-*.src.rpm
```

**Option B: Auto-Rebuild with GitHub Webhook**
1. Go to Copr web UI → dms-shell project → Packages
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
copr-cli list-builds dms-shell

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
   - Build `dgop.spec` first (stable)
   - Optional: `dgop-git.spec`

2. **dms-shell project:**
   - Build `material-symbols-fonts.spec` (no dependencies)
   - If packaging: Build `matugen.spec` and `cliphist.spec`
   - Build `dms.spec` (depends on dgop + matugen + cliphist)
   - Optional: Build `dms-git.spec`

---

## 👥 **User Installation Instructions**

After building, users install with:

```bash
# Enable repositories
sudo dnf copr enable <your-username>/dgop
sudo dnf copr enable <your-username>/dms-shell
sudo dnf copr enable errornointernet/quickshell

# Install stable version
sudo dnf install dms

# OR install development version
sudo dnf install dms-git
```

---

## 🐛 **Troubleshooting**

### Build Fails: "Nothing provides matugen"
- You forgot to package matugen or add external Copr
- Add matugen Copr to external repositories in dms-shell project

### Build Fails: "Nothing provides dgop"
- You forgot to add dgop Copr as external repository
- Go to dms-shell project settings → External repositories → Add `copr://<username>/dgop`

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
