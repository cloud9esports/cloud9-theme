import zipfile, os

jar_path = 'cloud9-jetstream-1.0.1.jar'
res_dir = 'resources'

with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(res_dir):
        dirs[:] = [d for d in dirs if d != 'assets']
        for f in files:
            # Explicitly skip .gitignore or other hidden files
            if f == '.gitignore' or f.startswith('.'):
                continue

            full = os.path.join(root, f)
            arcname = os.path.relpath(full, res_dir).replace(os.sep, '/')
            zf.write(full, arcname)

print(f"Successfully built {jar_path} (excluding hidden files).")