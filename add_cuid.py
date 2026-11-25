import glob, re

for f in glob.glob("*/.m3u*", recursive=True):
    t = open(f, encoding="utf-8", errors="ignore").read()
    t = re.sub(r'#EXTINF:-1 tvg-id="([^"]+)"', r'#EXTINF:-1 CUID="\1" tvg-id="\1"', t)
    open(f, "w", encoding="utf-8").write(t)
