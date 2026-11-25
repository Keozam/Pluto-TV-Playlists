import glob, re

files = glob.glob("output/.m3u") + glob.glob(".m3u")
print("Encontrados:", files)

for f in set(files):
    t = open(f, encoding="utf-8", errors="ignore").read()
    t2 = re.sub(r'#EXTINF:-1 tvg-id="([^"]+)"', r'#EXTINF:-1 CUID="\1" tvg-id="\1"', t)
    open(f, "w", encoding="utf-8").write(t2)
    print("Arreglado:", f)
