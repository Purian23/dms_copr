# DankMaterialShell - Fedora Copr Packages

Fedora RPM packages for [DankMaterialShell](https://github.com/AvengeMedia/DankMaterialShell) and related tools via Copr.

## Available Packages

### Main Package
- **dms** - DankMaterialShell desktop environment
- **dms-git** - Development version

### Standalone Tools
- **dgop** - System monitoring CLI
- **cliphist** - Wayland clipboard manager  
- **matugen** - Material You color generator
- **material-symbols-fonts** - Google Material Symbols icon font

## Installation

```bash
# Install main package (includes all dependencies)
sudo dnf copr enable purian23/dms
sudo dnf install dms

# Or install individual tools
sudo dnf copr enable purian23/dgop && sudo dnf install dgop
sudo dnf copr enable purian23/cliphist && sudo dnf install cliphist
sudo dnf copr enable purian23/matugen && sudo dnf install matugen
sudo dnf copr enable purian23/material-symbols-fonts && sudo dnf install material-symbols-fonts
```

## Copr Repositories

- [purian23/dms](https://copr.fedorainfracloud.org/coprs/purian23/dms/) - Main package
- [purian23/dgop](https://copr.fedorainfracloud.org/coprs/purian23/dgop/) - System monitor
- [purian23/cliphist](https://copr.fedorainfracloud.org/coprs/purian23/cliphist/) - Clipboard manager
- [purian23/matugen](https://copr.fedorainfracloud.org/coprs/purian23/matugen/) - Color generator
- [purian23/material-symbols-fonts](https://copr.fedorainfracloud.org/coprs/purian23/material-symbols-fonts/) - Icon font
