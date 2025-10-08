# DankMaterialShell - Fedora Copr Packaging# DankMaterialShell Copr Project# DankMaterialShell - Fedora Copr Packaging# DankMaterialShell - Fedora Copr Packaging



RPM packaging for [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) on Fedora via Copr.



---Material Design desktop shell for Wayland compositors (niri, Hyprland).



## 📦 What This Project Builds



**Two separate Copr projects:**## 📦 PackagesRPM packaging for [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) on Fedora via Copr.This repository contains RPM spec files and documentation for packaging [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) for Fedora via Copr.



1. **dgop** (your project) - `dgop`, `dgop-git`

2. **dms-shell** (your project) - `dms`, `dms-git`, `material-symbols-fonts`

- **dms-shell** - Stable releases (DMS config + dms binary)

---

- **dms-shell-git** - Development builds (latest config + built dms)

## 🚀 Quick Start

- **material-symbols-fonts** - Google Material Symbols icon font## 📦 What Gets Built## 🚀 Status: Ready to Build!

### For Users (Installation)



```bash

# Enable Coprs## 📋 Dependencies

sudo dnf copr enable <your-username>/dgop

sudo dnf copr enable <your-username>/dms-shell

sudo dnf copr enable errornointernet/quickshell

This project depends on external Coprs:You will package **4-6 packages** in your Copr project:**✅ All 4 spec files complete and validated!**  

# Install DMS

sudo dnf install dms



# Or development version- **dgop** - `copr://<your-username>/dgop` (your separate dgop project)**✅ All dependencies verified in Fedora repos or Copr!**

sudo dnf install dms-git

```- **quickshell** - `copr://errornointernet/quickshell`



### For Packagers (Building)1. **dms-shell** - Main DMS package (stable releases)



**Step 1:** Review **[SUMMARY.md](SUMMARY.md)** - Project overviewAdd these in Copr project settings → External repositories.



**Step 2:** Follow **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete build instructions2. **dms-shell-git** - Development version (latest commits)  See **[BUILD_SUMMARY.md](BUILD_SUMMARY.md)** for complete overview! 🎉



**Step 3:** Use **[CHECKLIST.md](CHECKLIST.md)** - Track your progress## 🚀 Building



---3. **dgop** - System monitor (REQUIRED dependency)



## 📁 StructureSee `QUICK_START.md` for detailed build instructions.



```4. **material-symbols-fonts** - Google Material Symbols (recommended)## Quick Start

/home/purian23/Copr/

├── dgop/                   # Separate dgop Copr projectSee `COPR_ARCHITECTURE.md` for complete project structure.

│   ├── dgop.spec

│   └── dgop-git.spec5. **matugen** - Auto-theming (REQUIRED - build yourself or use external Copr)

│

└── dms-shell/              # Main DMS Copr project## 📥 Installation

    ├── dms.spec

    ├── dms-git.spec6. **cliphist** - Clipboard manager (REQUIRED - build yourself or use external Copr)### For Users

    ├── material-symbols-fonts.spec

    ├── README.md           # This file```bash

    ├── SUMMARY.md          # Overview

    ├── SETUP_GUIDE.md      # How to build# Enable all required Coprs

    └── CHECKLIST.md        # Quick reference

```sudo dnf copr enable <your-username>/dgop



---sudo dnf copr enable <your-username>/dms-shell## 📚 Documentation (Cleaned Up!)Install DankMaterialShell on Fedora:



## 📋 Dependenciessudo dnf copr enable errornointernet/quickshell



**Required (automatically installed):**

- `dgop` - From your dgop Copr

- `quickshell` - From `copr://errornointernet/quickshell`# Install DMS

- `cava, wl-clipboard, brightnessctl` - Fedora repos

- `matugen, cliphist` - ⚠️ **YOU MUST PROVIDE** (package yourself or use external Copr)sudo dnf install dms-shell- **[README.md](README.md)** - This file```bash



**Recommended:**

- `material-symbols-fonts` - Icon font (your dms-shell Copr)

- Various fonts and utilities from Fedora repos# Or development version- **[QUICK_START.md](QUICK_START.md)** - Build and upload instructions# Enable repositories



---sudo dnf install dms-shell-git



## ⚠️ Important Notes```- **[COPR_SETUP_GUIDE.md](COPR_SETUP_GUIDE.md)** - Detailed Copr configuration and maintenance  sudo dnf copr enable <username>/dms-shell



### Binary Sources (CRITICAL!)

- **dgop binary** → https://github.com/AvengeMedia/dgop

- **dms CLI** → https://github.com/AvengeMedia/danklinux (NOT DankMaterialShell!)## 🔗 Links- **[CHECKLIST.md](CHECKLIST.md)** - Setup checklistsudo dnf copr enable errornointernet/quickshell

- **DMS config** → https://github.com/AvengeMedia/DankMaterialShell



### Two Separate Coprs Required

1. Create `dgop` Copr first (independent)- **DMS GitHub**: https://github.com/AvengeMedia/DankMaterialShell

2. Create `dms-shell` Copr second (depends on dgop)

3. Add external repos to `dms-shell`: your `dgop` + `errornointernet/quickshell`- **dms binary**: https://github.com/AvengeMedia/danklinux



### Package Names (Simplified)- **Copr**: https://copr.fedorainfracloud.org/coprs/<your-username>/dms-shell## 📋 Dependencies Status# Install stable version

- `dms` (not dms-shell) - Main package

- `dms-git` (not dms-shell-git) - Development package



---## 📁 Documentationsudo dnf install dms-shell quickshell



## 📚 Documentation



- **[SUMMARY.md](SUMMARY.md)** - Project overview, current status- `README.md` - This file### YOU MUST PACKAGE (Required by dms-shell)

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete build & maintenance guide

- **[CHECKLIST.md](CHECKLIST.md)** - Quick reference checklist- `COPR_ARCHITECTURE.md` - **Complete project structure** (2 Copr projects)



---- `QUICK_START.md` - Build instructions# Or install development version



## 🔗 Links- `COPR_SETUP_GUIDE.md` - Detailed Copr configuration



- **DMS**: https://github.com/AvengeMedia/DankMaterialShell- `CHECKLIST.md` - Setup checklist| Package | Have Spec? | Decision |sudo dnf install dms-shell-git quickshell-git

- **dgop**: https://github.com/AvengeMedia/dgop

- **danklinux**: https://github.com/AvengeMedia/danklinux- `BINARY_SOURCES.md` - Where binaries come from

- **Your Copr**: https://copr.fedorainfracloud.org/coprs/\<username\>/dms-shell/

- `FINAL_STATUS.md` - Current status|---------|------------|----------|

---



**See [SETUP_GUIDE.md](SETUP_GUIDE.md) for complete instructions!**| **dgop** | ✅ Yes | Build from `dgop.spec` |# Optional: Install dgop for system monitoring


| **matugen** | ❌ No | Build yourself OR add `copr://heus-sueh/matugen` (verify up-to-date first) |sudo dnf install dgop

| **cliphist** | ❌ No | Build yourself OR add `copr://alternateved/cliphist` or `copr://wef/cliphist` |```

| **material-symbols-fonts** | ✅ Yes | Build from `material-symbols-fonts.spec` (recommended, not required) |

### For Packagers

### EXTERNAL DEPENDENCIES (Add to Copr settings)

**🎉 START HERE:** [BUILD_SUMMARY.md](BUILD_SUMMARY.md) - Complete verified overview

| Package | Source | Status |

|---------|--------|--------|**📋 Current Status:** [STATUS.md](STATUS.md) - Build order and quick start

| **quickshell** | `copr://errornointernet/quickshell` | ✅ Add as external repo |

**📋 Dependencies:** [DEPENDENCY_STATUS.md](DEPENDENCY_STATUS.md) - All verified dependencies

### FEDORA REPOS (Auto-available)

**📚 Complete Guide:** [COPR_SETUP_GUIDE.md](COPR_SETUP_GUIDE.md) - Detailed walkthrough

| Package | Status |

|---------|--------|**✅ Setup Checklist:** [CHECKLIST.md](CHECKLIST.md) - Interactive checklist

| cava, wl-clipboard, brightnessctl | ✅ In Fedora repos |

| google-noto-sans-fonts, fira-code-fonts, rsms-inter-fonts | ✅ In Fedora repos |**📦 Package Details:** [PACKAGES.md](PACKAGES.md) - What each package does

| NetworkManager, gammastep, qt5ct, qt6ct | ✅ In Fedora repos |

## Contents

## 🚀 Quick Start

### Spec Files (Ready to Build) ✅

1. **Read**: [QUICK_START.md](QUICK_START.md)- **`dms-shell.spec`** - Stable releases from git tags (v0.1.1+)

2. **Setup Copr**: [COPR_SETUP_GUIDE.md](COPR_SETUP_GUIDE.md)- **`dms-shell-git.spec`** - Development builds from master branch

3. **Build packages** in order (see QUICK_START.md)- **`dgop.spec`** - System monitoring CLI (v0.1.4)

- **`material-symbols-fonts.spec`** - Google Material Symbols icon font

## 📁 Spec Files

### Documentation

- ✅ `dms-shell.spec` - Main package (stable)- **`BUILD_SUMMARY.md`** - 🔥 **COMPLETE OVERVIEW** - Everything verified and ready!

- ✅ `dms-shell-git.spec` - Development package- **`DEPENDENCY_STATUS.md`** - ✅ All dependencies verified in Fedora/Copr

- ✅ `dgop.spec` - System monitor (REQUIRED)- **`STATUS.md`** - Build status and quick start guide

- ✅ `material-symbols-fonts.spec` - Icon font (recommended)- **`PACKAGES.md`** - Complete package overview and build instructions

- **`COPR_SETUP_GUIDE.md`** - Detailed Copr setup walkthrough

## 🔗 Links- **`CHECKLIST.md`** - Interactive setup checklist

- **`WORKFLOW.md`** - Local workflow guide

- **DMS**: https://github.com/AvengeMedia/DankMaterialShell- **`SUMMARY.md`** - Original packaging strategy notes

- **dgop**: https://github.com/AvengeMedia/dgop- **`README.md`** - This file - Quick reference

- **matugen**: https://github.com/InioX/matugen

- **cliphist**: https://github.com/sentriz/cliphist## Packages Overview


### dms-shell (Stable) ⭐ Recommended
- **Source**: Git tags (v0.1.1, v0.2.0, etc.)
- **Binary**: Pre-built from danklinux releases
- **Updates**: Auto-rebuilds on new GitHub releases
- **Use Case**: Production/daily use

### dms-shell-git (Development) 🔥 Bleeding Edge
- **Source**: Latest master branch commits
- **Binary**: Built from Go source
- **Updates**: Auto-rebuilds on every commit
- **Use Case**: Testing and development

### dgop (System Monitor) 📊 Recommended
- **Version**: 0.1.4
- **Binary**: Pre-built from GitHub releases
- **Use Case**: System monitoring (recommended for DMS)

### material-symbols-fonts (Icon Font) 🎨 Recommended
- **Source**: Google Material Design Icons
- **Font**: Variable font with all Material Symbols
- **Use Case**: DMS UI icons

## Building Locally

```bash
# Install tools
sudo dnf install @development-tools fedpkg mock
sudo usermod -a -G mock $USER

# Build SRPM
cd ~/rpmbuild/SPECS
cp /path/to/dms-shell.spec .
rpmbuild -bs dms-shell.spec

# Test in mock
mock -r fedora-40-x86_64 ~/rpmbuild/SRPMS/dms-shell-*.src.rpm
```

## Upstream Project

- **Source**: https://github.com/AvengeMedia/DankMaterialShell
- **License**: GPL-3.0-only
- **Language**: QML (Quickshell framework)

## Dependencies

### Required (Auto-installed when you install dms-shell)

**From Fedora repos:**
- **cava** - Audio visualizer ✅
- **wl-clipboard** - Wayland clipboard ✅
- **brightnessctl** - Backlight control ✅
- **matugen** - Auto-theming ✅ (Fedora 42+)
- **cliphist** - Clipboard manager ✅ (Fedora 42+)
- **google-noto-sans-fonts** ✅
- **fira-code-fonts** ✅
- **rsms-inter-fonts** ✅

**From External Copr:**
- **quickshell** - From `copr://errornointernet/quickshell` ✅

### Recommended (Auto-installed but can be removed)

**From Your Copr (separate packages you build):**
- **dgop** - System monitor 🔨
- **material-symbols-fonts** - UI icons 🔨

**From Fedora repos:**
- NetworkManager, gammastep, qt5ct, qt6ct

See [PACKAGING_STRATEGY.md](PACKAGING_STRATEGY.md) for complete packaging architecture.

## Contributing

Improvements to packaging are welcome! Please:
1. Test changes locally with mock
2. Verify on clean Fedora installation
3. Update changelog in spec files
4. Submit pull request

## Links

- **Copr Project**: https://copr.fedorainfracloud.org/coprs/<username>/dms-shell/
- **DMS GitHub**: https://github.com/AvengeMedia/DankMaterialShell
- **Copr Docs**: https://docs.pagure.org/copr.copr/
- **Fedora Packaging**: https://docs.fedoraproject.org/en-US/packaging-guidelines/

## License

These packaging files are licensed under GPL-3.0-only, matching the upstream project.
