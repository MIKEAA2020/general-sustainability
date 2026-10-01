# Restore the exact compiler used for the paper 2 family check

The x86_64 static Tectonic 0.15.0 binary is preserved as `tectonic-0.15.0-x86_64-static.tar.gz` in this directory on the `e2-v3-source-year` Git branch. The archive is a single `tectonic` executable, not a live-workspace requirement. Tested by extracting it and comparing bytes against the working binary before removing that local duplicate.

```bash
git clone -b e2-v3-source-year https://github.com/MIKEAA2020/general-sustainability.git repo
cd 'repo/arena agent 1/agent workspace'
sha256sum tools/tectonic-0.15.0-x86_64-static.tar.gz
# expected: b00fcaf562798fcaf92d4ee8391080bb0728b2309cea84f94efa06949417d450
tar -xzf tools/tectonic-0.15.0-x86_64-static.tar.gz -C tools
sha256sum tools/tectonic
# expected: 4df19452c202c5bef9f0a1f73b70b4fe1bffbc9837f6
chmod u+x tools/tectonic
tools/tectonic --version
python3 content_audit/claim_alignment/compile_drafts.py
```

The TeX bundle may download external packages on first run. The archived binary is for x86_64 Linux; a different architecture needs an appropriate compiler. A successful TeX build is not a Lean build or a scientific validation.
