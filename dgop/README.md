# dgop Copr Project

Dank Linux Stateless System monitoring CLI for Linux systems.

## 📦 Packages

- **dgop** - Stable releases (pre-built binaries from GitHub)
- **dgop-git** - Development builds (built from master source)

## 🔗 Links

- **GitHub**: https://github.com/AvengeMedia/dgop
- **Copr**: https://copr.fedorainfracloud.org/coprs/purian23/dgop

## 🚀 Building

### dgop (stable)
```bash
cd ~/rpmbuild/SOURCES
wget https://github.com/AvengeMedia/dgop/releases/download/v0.1.4/dgop-linux-amd64.gz
wget https://github.com/AvengeMedia/dgop/releases/download/v0.1.4/dgop-linux-amd64.gz.sha256
wget https://github.com/AvengeMedia/dgop/releases/download/v0.1.4/dgop-linux-arm64.gz
wget https://github.com/AvengeMedia/dgop/releases/download/v0.1.4/dgop-linux-arm64.gz.sha256

cd ~/rpmbuild/SPECS
cp /home/purian23/Copr/dgop/dgop.spec .
rpmbuild -bs dgop.spec
copr-cli build dgop ~/rpmbuild/SRPMS/dgop-*.src.rpm
```

### dgop-git (development - auto-updates)
Configure as SCM build in Copr web UI:
- Package type: SCM
- Git URL: https://github.com/AvengeMedia/dgop.git
- Spec file: dgop-git.spec
- Enable auto-rebuild with GitHub webhook

## 📥 Installation

```bash
sudo dnf copr enable purian23/dgop
sudo dnf install dgop

# Or development version
sudo dnf install dgop-git
```

## 🔧 Files

- `dgop.spec` - Stable package (uses pre-built binaries)
- `dgop-git.spec` - Git package (builds from source)
- `README.md` - This file
