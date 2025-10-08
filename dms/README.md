# DankMaterialShell (DMS) - Fedora Copr Packaging

RPM packaging for [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) on Fedora via Copr.

Material Design desktop shell for Wayland compositors (niri, Hyprland).

---

## 📦 Packages

This repository contains spec files for building DMS and its dependencies on Fedora Copr.

### Main Packages (dms Copr project)

- **dms** - Stable releases (DMS config + dms-cli binary)
- **dms-git** - Development builds (latest config + built dms-cli from source)
- **material-symbols-fonts** - Google Material Symbols icon font (recommended)

### Dependencies (dgop Copr project - separate)

- **dgop** - System monitoring CLI (required by DMS)
- **dgop-git** - Development builds of dgop

---

## 🚀 Installation

### For Users

```bash
# Enable required Coprs
sudo dnf copr enable purian23/dgop
sudo dnf copr enable purian23/dms
sudo dnf copr enable errornointernet/quickshell

# Install stable DMS
sudo dnf install dms

# OR install development version
sudo dnf install dms-git
```

### For Packagers

See **[SETUP_GUIDE.md](SETUP_GUIDE.md)** for complete build instructions.

---

## 📋 Dependencies

### Required (Auto-installed with dms)

**From Fedora repos:**
- cava, wl-clipboard, brightnessctl
- fira-code-fonts, rsms-inter-fonts
- matugen, cliphist (Fedora 42+, must package yourself for F41)

**From External Copr:**
- quickshell - `copr://errornointernet/quickshell`
- dgop - `copr://purian23/dgop` (your separate project)

### Recommended
- material-symbols-fonts (from your dms Copr)
- NetworkManager, gammastep, qt6ct

---

## 📁 Spec Files

- ✅ `dms.spec` - Main package (stable releases)
- ✅ `dms-git.spec` - Development package (latest commits)
- ✅ `material-symbols-fonts.spec` - Icon font

Located in: `/home/purian23/dms_copr/`

---

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete build & maintenance guide
- **[QUICKSTART_DGOP.md](../QUICKSTART_DGOP.md)** - Building dgop package
- **[SPEC_FIXES_SUMMARY.md](../SPEC_FIXES_SUMMARY.md)** - All spec file fixes applied
- **[CHECKLIST.md](CHECKLIST.md)** - Quick reference checklist

---

## 🔗 Links

- **DMS GitHub**: https://github.com/AvengeMedia/DankMaterialShell
- **dms-cli GitHub**: https://github.com/AvengeMedia/danklinux
- **dgop GitHub**: https://github.com/AvengeMedia/dgop
- **Your Copr**: https://copr.fedorainfracloud.org/coprs/purian23/

---

## 🏗️ Build Status

| Package | Status | Notes |
|---------|--------|-------|
| dgop | ✅ Built | https://copr.fedorainfracloud.org/coprs/purian23/dgop/ |
| dms | 🔨 Ready | All spec files validated and ready to build |
| dms-git | 🔨 Ready | Uses rpkg macros for auto-versioning |
| material-symbols-fonts | 🔨 Ready | Font package for DMS icons |

---

## 📝 Package Details

### dms (Stable) - Recommended for production

- **Source**: Git tags (v0.1.1, v0.2.0, etc.)
- **Binary**: Pre-built dms-cli from danklinux releases
- **Config**: Tagged DMS release
- **Updates**: Manual rebuild when new version released

### dms-git (Development) - For testing

- **Source**: Latest master branch
- **Binary**: Built from danklinux master (Go source)
- **Config**: Latest DMS master
- **Updates**: Can auto-rebuild on commits with webhook

### dgop - System Monitor (Separate Copr)

- **Version**: 0.1.4 (stable)
- **Source**: Pre-built binaries from GitHub releases
- **Purpose**: System monitoring for DMS widgets
- **Copr**: `purian23/dgop`

---

## 🔧 Building Locally

```bash
# Install tools
sudo dnf install fedora-packager mock

# Build SRPM
cd ~/rpmbuild/SPECS
cp /home/purian23/dms_copr/dms/dms.spec .
rpmbuild -bs dms.spec

# Test with mock
mock -r fedora-41-x86_64 ~/rpmbuild/SRPMS/dms-*.src.rpm

# Upload to Copr
copr-cli build dms ~/rpmbuild/SRPMS/dms-*.src.rpm
```

---

## 🎯 Project Structure

```
/home/purian23/dms_copr/
├── dgop/                          # Separate dgop Copr project
│   ├── dgop.spec                  # ✅ Built successfully!
│   ├── dgop-git.spec
│   └── README.md
├── dms/                           # Main DMS Copr project
│   ├── dms.spec                   # ✅ Ready to build
│   ├── dms-git.spec               # ✅ Ready to build
│   ├── SETUP_GUIDE.md
│   └── README.md (this file)
├── fonts/
│   └── material-symbols-fonts.spec # ✅ Ready to build
├── matugen/
│   └── matugen.spec               # ✅ Ready to build
├── cliphist/
│   └── cliphist.spec              # ✅ Ready to build
├── QUICKSTART_DGOP.md
└── SPEC_FIXES_SUMMARY.md
```

---

## 📄 License

These packaging files are licensed under GPL-3.0-only, matching the upstream DMS project.

---

**Ready to build!** See [SETUP_GUIDE.md](SETUP_GUIDE.md) for step-by-step instructions.
