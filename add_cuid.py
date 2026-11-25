import os, re

for root, dirs, files in os.walk("."):
    if ".git" in root:
        continue
    for name in files:
        if name.endswith(".m3u") or name.endswith(".m3u8"):
            f = os.path.join(root, name)
            print("Encontrado:", f)
            t = open(f, encoding="utf-8", errors="ignore").read()
            t2 = re.sub(r'#EXTINF:-1 tvg-id="([^"]+)"', r'#EXTINF:-1 CUID="\1" tvg-id="\1"', t)
            open(f, "w", encoding="utf-8").write(t2)
            print("Arreglado:", f)
