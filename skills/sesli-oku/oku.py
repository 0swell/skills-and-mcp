"""Metni parça parça seslendirir. Kullanım:
  oku.py --dosya metin.txt [--ses emel|ahmet] [--hiz -20%] [--devam]
  oku.py --dur
Parçalar boş satırla ayrılır. Durum state.json'da tutulur, --devam kaldığı yerden okur.
"""
import argparse, asyncio, ctypes, json, os, subprocess, sys, tempfile, threading
from pathlib import Path

import edge_tts

KOK = Path(__file__).parent
STATE = KOK / "state.json"
SESLER = {"emel": "tr-TR-EmelNeural", "ahmet": "tr-TR-AhmetNeural"}
mci = ctypes.windll.winmm.mciSendStringW


def durum_oku():
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def durum_yaz(d):
    STATE.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")


def dur():
    d = durum_oku()
    pid = d.get("pid")
    if pid:
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], capture_output=True)
        d["pid"] = None
        durum_yaz(d)
    mci("close all", None, 0, None)
    print(f"durdu, kalinan parca: {d.get('index', 0) + 1}/{d.get('toplam', '?')}")


def uret(metin, ses, hiz, yol):
    asyncio.run(edge_tts.Communicate(metin, ses, rate=hiz).save(yol))


def cal(yol):
    mci("close s", None, 0, None)
    mci(f'open "{yol}" type mpegvideo alias s', None, 0, None)
    mci("play s wait", None, 0, None)
    mci("close s", None, 0, None)


def oku(dosya, ses, hiz, devam):
    parcalar = [p.strip() for p in Path(dosya).read_text(encoding="utf-8").split("\n\n") if p.strip()]
    d = durum_oku()
    bas = d.get("index", 0) if devam and d.get("dosya") == str(Path(dosya).resolve()) else 0
    if devam and d:
        ses, hiz = d.get("ses", ses), d.get("hiz", hiz)
    d = {"pid": os.getpid(), "dosya": str(Path(dosya).resolve()), "index": bas,
         "toplam": len(parcalar), "ses": ses, "hiz": hiz}
    durum_yaz(d)
    tmp = Path(tempfile.mkdtemp(prefix="sesli-oku-"))
    yol = lambda i: str(tmp / f"{i}.mp3")
    if bas < len(parcalar):
        uret(parcalar[bas], ses, hiz, yol(bas))
    for i in range(bas, len(parcalar)):
        t = None
        if i + 1 < len(parcalar):
            t = threading.Thread(target=uret, args=(parcalar[i + 1], ses, hiz, yol(i + 1)))
            t.start()
        d["index"] = i
        durum_yaz(d)
        cal(yol(i))
        if t:
            t.join()
    d.update(pid=None, index=len(parcalar))
    durum_yaz(d)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--dosya")
    a.add_argument("--ses", default="emel")
    a.add_argument("--hiz", default="-20%")
    a.add_argument("--devam", action="store_true")
    a.add_argument("--dur", action="store_true")
    g = a.parse_args()
    if g.dur:
        dur()
    elif g.dosya:
        dur() if durum_oku().get("pid") else None
        oku(g.dosya, SESLER.get(g.ses, g.ses), g.hiz, g.devam)
    else:
        a.print_help()
        sys.exit(1)
