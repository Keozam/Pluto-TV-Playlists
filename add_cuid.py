import os
import re

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for name in files:
        if name.endswith('.m3u') or name.endswith('.m3u8'):
            f = os.path.join(root, name)
            print(f"Encontrando: {f}")
            with open(f, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()

            new_lines = []
            for line in lines:
                # Solo tocamos las #EXTINF
                if line.startswith('#EXTINF'):
                    # Si YA tiene CUID, lo dejamos fijo, NO lo tocamos
                    if 'CUID="' in line:
                        new_lines.append(line)
                        continue

                    # Si NO tiene CUID, lo creamos del tvg-id
                    m = re.search(r'tvg-id="([^"]*)"', line)
                    if m and m.group(1).strip() != "":
                        base = m.group(1).strip()
                        # Limpiamos para que quede fijo, sin espacios ni caracteres raros
                        cuid = re.sub(r'[^a-zA-Z0-9]', '', base)
                        # Lo metemos antes de la coma final
                        # Buscamos la última coma que separa el nombre
                        if ', ' in line:
                            line = line.rsplit(', ', 1)[0] + f' CUID="{cuid}", ' + line.rsplit(', ', 1)[1]
                    new_lines.append(line)
                else:
                    new_lines.append(line)

            with open(f, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
            print("arreglado")

print("CUID fijo aplicado")
