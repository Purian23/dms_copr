# AvengeMedia Source Repository Spec Files

This folder contains spec files that belong in the **AvengeMedia source repositories** for Copr SCM builds with webhook support.

## Structure

- `dgop/dgop.spec` - Spec file for dgop-git builds (add to https://github.com/AvengeMedia/dgop)
- `DankMaterialShell/dms.spec` - Spec file for dms-git builds (add to https://github.com/AvengeMedia/DankMaterialShell)

## Usage

These spec files use rpkg git macros and are designed for Copr SCM builds:

1. Copy the spec file to the root of the corresponding AvengeMedia repository
2. For DMS, also add `danklinux-vendor.tar.gz` to the repository
3. Configure the Copr `-git` project to use SCM build method
4. Enable webhooks for automatic builds on push

## Differences from Unified Specs

The unified specs in `dms/dms.spec` and `dgop/dgop.spec` support both stable and git builds using conditionals, but cannot be used with Copr SCM/webhook builds.

These spec files in `avenge_media/` are git-only and use rpkg macros (`{{{ git_dir_version }}}`, etc.) for automatic version detection and changelog generation from git commits.

## Copr Configuration

For SCM builds in Copr:
- **Source Type:** Build from an SCM repository
- **SCM type:** git
- **Clone URL:** https://github.com/AvengeMedia/<repo>
- **Committish:** master (or main)
- **Build SRPM with:** rpkg
- **Webhook rebuild:** Yes
