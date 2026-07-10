import zipfile, os, xml.etree.ElementTree as ET

res_dir = 'resources'

plugin_xml = os.path.join(res_dir, 'META-INF', 'plugin.xml')
version = ET.parse(plugin_xml).getroot().findtext('version')
jar_path = f'cloud9-jetstream-{version}.jar'

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