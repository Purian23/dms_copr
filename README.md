# DankMaterialShell - Fedora Copr Packaging

Complete RPM packaging for [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) on Fedora via Copr.

---

## 📦 Projects

This repository contains spec files for **two separate Copr projects**:

### 1. dgop Copr Project
**Location:** `dgop/`

Independent system monitoring CLI tool.

**Packages:**
- `dgop` - Stable releases
- `dgop-git` - Development builds

### 2. dms Copr Project
**Location:** `dms/`

Main DankMaterialShell desktop environment.

**Packages:**
- `dms` - Stable DankMaterialShell (includes `dms-cli` sub-package)
- `dms-git` - Development DankMaterialShell (includes `dms-cli-git` sub-package)
- `material-symbols-fonts` - Google Material Symbols icon font

---

## 🚀 Quick Start

### For Users (Installation)

```bash
# Enable repositories
sudo dnf copr enable <your-username>/dgop
sudo dnf copr enable <your-username>/dms
sudo dnf copr enable errornointernet/quickshell

# Install DankMaterialShell
sudo dnf install dms

# Or install development version
sudo dnf install dms-git
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
│   ├── dgop.spec
│   ├── dgop-git.spec
│   └── README.md
│
├── dms/                        # dms Copr project
│   ├── dms.spec
│   ├── dms-git.spec
│   ├── material-symbols-fonts.spec
│   ├── README.md
│   ├── SUMMARY.md
│   ├── SETUP_GUIDE.md
│   └── CHECKLIST.md
│
├── LICENSE                     # GPL-3.0-only
├── README.md                   # This file
└── .gitignore
```

---

## 🏗️ Build Order

**Important:** Build in this order to satisfy dependencies!

1. **Create and build dgop Copr** (independent)
   ```bash
   copr-cli create dgop --chroot fedora-40-x86_64 ...
   # Build dgop.spec
   ```

2. **Create and build dms Copr** (depends on dgop)
   ```bash
   copr-cli create dms --chroot fedora-40-x86_64 ...
   # Add external repos: your dgop + errornointernet/quickshell
   # Build material-symbols-fonts.spec, then dms.spec
   ```

See **[dms/SETUP_GUIDE.md](dms/SETUP_GUIDE.md)** for complete instructions.

---

## 📋 Package Overview

| Package | Type | Description | Copr Project |
|---------|------|-------------|--------------|
| **dgop** | Stable | System monitoring CLI | dgop |
| **dgop-git** | Development | Latest dgop commits | dgop |
| **dms** | Stable | DankMaterialShell config + CLI | dms |
| **dms-cli** | Sub-package | Dank Linux installer (stable) | dms |
| **dms-git** | Development | Latest DMS commits | dms |
| **dms-cli-git** | Sub-package | Dank Linux installer (dev) | dms |
| **material-symbols-fonts** | Support | Icon font | dms |

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

## 🤝 Contributing

Improvements to the packaging are welcome! Please:
1. Test changes locally with mock
2. Verify on clean Fedora installation
3. Update changelog in spec files
4. Submit pull request

---

**See [dms/SETUP_GUIDE.md](dms/SETUP_GUIDE.md) for complete build instructions!**
