# DankMaterialShell - Fedora Copr Packaging

Complete RPM packaging for [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) on Fedora via Copr.

---

## 📦 Projects

This repository contains spec files for **five separate Copr projects**:

### 1. dgop Copr Project
**Location:** `dgop/`  
**Copr:** https://copr.fedorainfracloud.org/coprs/purian23/dgop/

Independent system monitoring CLI tool.

**Packages:**
- `dgop` - Stable releases (pre-built binaries)
- `dgop-git` - Development builds (from source)

### 2. cliphist Copr Project
**Location:** `cliphist/`  
**Copr:** https://copr.fedorainfracloud.org/coprs/purian23/cliphist/

Wayland clipboard history manager (standalone).

**Packages:**
- `cliphist` - Stable releases (built from source with vendored Go dependencies)

### 3. matugen Copr Project
**Location:** `matugen/`  
**Copr:** https://copr.fedorainfracloud.org/coprs/purian23/matugen/

Material You color generation tool (standalone).

**Packages:**
- `matugen` - Stable releases (built from source with vendored Rust dependencies)

### 4. material-symbols-fonts Copr Project
**Location:** `fonts/`  
**Copr:** https://copr.fedorainfracloud.org/coprs/purian23/material-symbols-fonts/

Google Material Symbols icon font (standalone).

**Packages:**
- `material-symbols-fonts` - Latest font from Google (noarch)

### 5. dms Copr Project
**Location:** `dms/`  
**Copr (Stable):** https://copr.fedorainfracloud.org/coprs/purian23/dms/  
**Copr (Git):** https://copr.fedorainfracloud.org/coprs/purian23/dms-git/

Main DankMaterialShell desktop environment.

**Packages:**
- `dms` - Stable DankMaterialShell (includes `dms-cli` sub-package)
- `dms-git` - Development DankMaterialShell (includes `dms-cli-git` sub-package)

---

## 🚀 Quick Start

### For Users (Installation)

```bash
# Enable DMS repository (automatically enables all dependencies)
sudo dnf copr enable purian23/dms

# Install DankMaterialShell
sudo dnf install dms

# Or install development version
sudo dnf install dms-git
```

**Standalone packages** (can be used without DMS):

```bash
# System monitor
sudo dnf copr enable purian23/dgop
sudo dnf install dgop

# Clipboard manager for Wayland
sudo dnf copr enable purian23/cliphist
sudo dnf install cliphist

# Material You color generator
sudo dnf copr enable purian23/matugen
sudo dnf install matugen

# Google Material Symbols icon font
sudo dnf copr enable purian23/material-symbols-fonts
sudo dnf install material-symbols-fonts
```

### For Packagers (Building)

See the README files in each subdirectory:
- **[dgop/README.md](dgop/README.md)** - Build dgop packages
- **[dms/README.md](dms/README.md)** - Build dms packages

---

## 📁 Repository Structure

```
dms_copr/
├── dgop/                       # dgop Copr project
│   ├── dgop.spec              # Stable (pre-built binaries)
│   ├── dgop-git.spec          # Development (source build)
│   └── README.md
│
├── cliphist/                   # cliphist Copr project
│   ├── cliphist.spec          # Go build with vendored deps
│   └── README.md (coming soon)
│
├── matugen/                    # matugen Copr project
│   ├── matugen.spec           # Rust build with vendored deps
│   └── README.md (coming soon)
│
├── fonts/                      # material-symbols-fonts Copr project
│   ├── material-symbols-fonts.spec
│   └── README.md (coming soon)
│
├── dms/                        # dms Copr project (main)
│   ├── dms.spec               # Stable DMS
│   ├── dms-git.spec           # Development DMS
│   ├── README.md
│   ├── SUMMARY.md
│   ├── SETUP_GUIDE.md         # Complete build instructions
│   └── CHECKLIST.md
│
├── LICENSE                     # GPL-3.0-only
├── README.md                   # This file
└── .gitignore
```

---

## 🏗️ Build Order

**Important:** Build in this order to satisfy dependencies!

1. **Create and build dgop Copr** ✅ (independent, pre-built binaries)
   ```bash
   copr-cli create dgop --chroot fedora-41-x86_64 ...
   # Build dgop.spec
   ```

2. **Create and build standalone dependencies** ✅ (can be parallel):
   - **cliphist** - Wayland clipboard manager (Go with vendored deps)
   - **matugen** - Material You color generator (Rust with vendored deps)
   - **material-symbols-fonts** - Google icon font (direct download)

3. **Create and build dms Copr** ✅ (depends on above)
   ```bash
   copr-cli create dms --chroot fedora-41-x86_64 ...
   copr-cli create dms-git --chroot fedora-41-x86_64 ...
   # Add external repos: dgop, cliphist, matugen, material-symbols-fonts, quickshell
   # Build dms.spec (stable)
   # Build dms-git.spec (development)
   ```

See **[dms/SETUP_GUIDE.md](dms/SETUP_GUIDE.md)** for complete step-by-step instructions including vendoring dependencies.

---

## 📋 Package Overview

| Package | Type | Description | Copr Project | Status |
|---------|------|-------------|--------------|--------|
| **dgop** | Stable | System monitoring CLI | purian23/dgop | ✅ Built |
| **dgop-git** | Development | Latest dgop commits | purian23/dgop | ✅ Built |
| **cliphist** | Stable | Wayland clipboard manager | purian23/cliphist | ✅ Built |
| **matugen** | Stable | Material You color generator | purian23/matugen | ✅ Built |
| **material-symbols-fonts** | Font | Google Material Symbols | purian23/material-symbols-fonts | ✅ Built |
| **dms** | Stable | DankMaterialShell config + CLI | purian23/dms | ✅ Built |
| **dms-cli** | Sub-package | Dank Linux installer (stable) | purian23/dms | ✅ Built |
| **dms-git** | Development | Latest DMS commits | purian23/dms-git | ✅ Built |
| **dms-cli-git** | Sub-package | Dank Linux installer (dev) | purian23/dms-git | ✅ Built |

---

## 🔗 Important Links

- **DankMaterialShell:** https://github.com/AvengeMedia/DankMaterialShell
- **dgop:** https://github.com/AvengeMedia/dgop
- **danklinux (dms CLI):** https://github.com/AvengeMedia/danklinux
- **Fedora Copr:** https://copr.fedorainfracloud.org/
- **Packaging Guidelines:** https://docs.fedoraproject.org/en-US/packaging-guidelines/

---

## 📝 License

GPL-3.0-only - Same as DankMaterialShell upstream project.

---

## 🔮 Future Plans

- **Unified spec file**: Refactor to single `dms.spec` with conditional logic (like niri compositor pattern)
- **Webhook automation**: Set up GitHub webhooks for automatic rebuilds on releases/pushes
- **AvengeMedia Copr**: Migrate production packages to AvengeMedia organization account
- **Standalone packages**: Keep cliphist, matugen, material-symbols-fonts under personal account

---

## 🤝 Contributing

Improvements to the packaging are welcome! Please:
1. Test changes locally with mock
2. Verify on clean Fedora installation
3. Update changelog in spec files
4. Submit pull request

---

**See [dms/SETUP_GUIDE.md](dms/SETUP_GUIDE.md) for complete build instructions!**
