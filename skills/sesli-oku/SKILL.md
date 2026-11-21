---
name: sesli-oku
description: Metni veya PDF'in istenen kısımlarını Türkçe sesle yüksek sesle okur (edge-tts, ücretsiz). "sesli oku", "seslendir", "oku bana", "dur", "devam et" denince kullan.
---

# Sesli oku

Python: `C:\Users\osman\.claude\skills\sesli-oku\.venv\Scripts\python.exe` (edge-tts kurulu). Script: `oku.py` (aynı klasör).

## Okut
1. Kaynağı çıkar: PDF ise markitdown MCP veya pdf skill ile metni al, sadece istenen kısımları seç (ör. "yapıldı" olan maddeler, belli sayfalar).
2. Sesli okumaya uygun hale getir: kısaltmaları aç ("TL" → "lira", "vb." → "ve benzeri"), tablo/markdown işaretlerini at, tarih ve sayıları okunur yaz. Her okunacak parçayı boş satırla ayır (madde başına bir parça).
3. Metni scratchpad'e `.txt` (UTF-8) olarak yaz.
4. Arka planda başlat (konuşma bloklanmasın):
   ```powershell
   Start-Process -WindowStyle Hidden "C:\Users\osman\.claude\skills\sesli-oku\.venv\Scripts\python.exe" -ArgumentList '"C:\Users\osman\.claude\skills\sesli-oku\oku.py"','--dosya','"<txt yolu>"','--hiz','-20%'
   ```
   - Ses: `--ses emel` (varsayılan) veya `--ses ahmet`.
   - Hız: "yavaş" → `-30%`, normal → `-20%` (varsayılan), "hızlı" → `+0%`.
5. Kullanıcıya tek cümleyle kaç parça okunacağını söyle.

## Komutlar
- "dur" → `python oku.py --dur` (çıktıda kalınan parça yazar).
- "devam" → aynı dosyayla `--devam` ekleyerek yukarıdaki Start-Process komutu.
- "baştan" → `--devam` olmadan başlat.
- Yeni okuma başlatmak eskisini otomatik durdurur.
