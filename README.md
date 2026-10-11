# skills-and-mcp

Claude Code kurulumumda kullandığım **MCP sunucuları, plugin'ler ve skill'lerin** listesi.

Tüm kayıtlar makine tarafından okunabilir şekilde [`setup.json`](setup.json) içinde tutuluyor.

---

> Etiketler: `MCP` dış servise bağlanır · `Skill` Claude'a iş akışı öğretir · `Plugin` skill/agent paketi · `Yerleşik` Claude Code ile gelir

## 🎨 Tasarım & UI

- **[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** `Plugin`: Cebindeki tasarım ajansı. 84 stil, 192 palet, 74 font eşleşmesi; "AI yaptı" belli olmayan arayüzler.
- **[stitch](https://stitch.withgoogle.com/docs/mcp/setup)** `MCP`: Bir cümle yaz, Google komple ekranı çizsin. Figma'yı açmadan tasarım sistemi ve varyantlar hazır. *(Ücretsiz, ~350 üretim/ay)*
- **[21st](https://21st.dev)** `MCP`: shadcn/ui + Tailwind component'leri tek prompt'la. Hazır kütüphaneden çek, kodu direkt projene düşsün. *(100 kredi/ay, hızlı biter)*
- **[nanobanana](https://github.com/YCSE/nanobanana-mcp)** `MCP`: Gemini'nin görsel motoru terminalinde. Logo, mockup, asset üret ya da mevcut görseli düzenle. *(Flash ücretsiz kotada)*
- **[awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** `Skill`: Dünyanın en iyi tasarım sistemleri tek yerde; ilham ve referans.
- **[fal.ai](https://fal.ai)** `MCP`: Flux, Recraft, Kling gibi yüzlerce görsel ve video modeli tek API'de. Nanobanana yetmediğinde profesyonel kalite. *(💰 Ücretli, tamamen kullandıkça öde)*

## 🎬 Video

- **[Remotion MCP](https://www.npmjs.com/package/@remotion/mcp)** `MCP`: Remotion'ın resmi doküman beyni. Video kodu yazarken API'yi tahmin etme, sor. *(Ücretsiz)*
- **[Remotion Skills](https://github.com/remotion-dev/skills)** `Skill`: React ile kodla video üret. Remotion ekibinin 12 resmi skill'i fikirden MP4'e tüm yolu kapsıyor.

  <details>
  <summary>12 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `remotion-best-practices` | Hepsinin yönlendiricisi; hangisini seçeceğini bilmiyorsan buradan başla |
  | `remotion-create` | "Plak dükkanı için promo video yap" de, proje ve composition hazır |
  | `remotion-markup` | Animasyon, efekt ve yerleşimde Remotion ekibinin kuralları |
  | `remotion-interactivity` | Sonradan düzenlenebilir, interaktif kurgu |
  | `remotion-captions` | Sesi yazıya dök, TikTok tarzı animasyonlu altyazı |
  | `remotion-studio` | Render beklemeden canlı önizleme |
  | `remotion-render` | MP4'e dök; local ya da Lambda |
  | `remotion-maps` | Harita animasyonu; rota çiz, şehirden şehre uç |
  | `remotion-multimedia` | Mediabunny ile video/ses oku, kes, dönüştür |
  | `remotion-saas` | Remotion üstüne video üreten SaaS kur |
  | `remotion-upgrade` | Remotion paketlerini güvenle güncelle |
  | `remotion-docs` | Dokümanda anında arama |

  </details>

## 🛠️ Geliştirme & Kod Kalitesi

- **[superpowers](https://github.com/obra/superpowers)** `Plugin`: Claude'a kıdemli mühendis disiplini aşılar. Brainstorm, plan, TDD, sistematik debug; rastgele kod yazmaya son.
- **[Ponytail](https://github.com/DietrichGebert/ponytail)** `Skill`: Odadaki en tembel kıdemli dev gibi düşünür. En iyi kod hiç yazılmayan koddur; YAGNI, stdlib, tek satır.

  <details>
  <summary>6 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `ponytail` | En küçük değişiklikle tam çözüm; lite / full / ultra seviyeleri |
  | `ponytail-review` | Değişikliği sade dille inceler: mantık, güvenlik, yük, test, gereksiz satır |
  | `ponytail-audit` | Tüm repoya kalite denetimi; bug, güvenlik açığı, silinecek kod |
  | `ponytail-debt` | Ertelenen `shortcut:` yorumlarının borç defteri |
  | `ponytail-gain` | Benchmark'tan ölçülmüş tasarruf (kod, maliyet, hız) |
  | `ponytail-help` | Seviye, skill ve komutlar için hızlı referans |

  </details>

- **[claude-skills](https://github.com/alirezarezvani/claude-skills)** `Skill`: Push öncesi kalite kapıları ve git ritüeli tek komutta. Hata CI'a, sızan anahtar repoya ulaşmadan yakalanır.

  <details>
  <summary>9 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `focused-fix` | Bozuk modülü 5 fazlı protokolle onarır; yama değil kök neden |
  | `review` | Push öncesi yerel inceleme kapısı |
  | `security-scan` | Push öncesi güvenlik taraması |
  | `git/cm` | Conventional Commit oluşturur |
  | `git/cp` | Stage, commit, push tek komut |
  | `git/pr` | Mevcut branch'ten PR açar |
  | `git/clean` | Merge edilmiş branch'leri temizler |
  | `update-docs` | Kod değişince dokümanları günceller |
  | `plugin-audit` | Skill/plugin dizinine 8 fazlı denetim |

  </details>

- **`simplify`** `Yerleşik`: Değişen kodu tarar, tekrarı ve gereksiz karmaşayı budar. Kod incelir, okunur olur.
- **[github](https://github.com/github/github-mcp-server)** `MCP`: Repo, issue ve PR'lar Claude'un elinde. Tarayıcıya geçmeden review, merge, triage. *(Ücretsiz)*
- **[context7](https://github.com/upstash/context7)** `MCP`: Eskimiş API bilgisine son. Kütüphanenin bugünkü dokümanını anında çeker, halüsinasyon kodu bitirir. *(Ücretsiz)*
- **[supabase](https://mcp.supabase.com/mcp)** `MCP`: Veritabanı, auth ve storage'ı sohbetten yönet. Dashboard'a girmeden tablo kur, sorgu at. *(Ücretsiz plan)*
- **[markitdown](https://github.com/microsoft/markitdown)** `MCP`: PDF, Word, Excel, HTML ne verirsen temiz Markdown'a çevirir. Belge okutmanın en kısa yolu. *(Ücretsiz)*

## 📈 Dijital Pazarlama

### SEO · GEO · AEO

- **[geo-optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill)** `MCP` `Skill`: ChatGPT, Perplexity, AI Overviews sitene atıf yapıyor mu? Princeton'ın 47 yöntemiyle GEO/AEO karnesi; llms.txt, bot erişimi, schema. *(Ücretsiz)*
- **[gsc](https://github.com/AminForou/mcp-gsc)** `MCP`: Search Console verisi sohbette. Hangi sorgu geliyor, hangi sayfa düşüyor, indeksleme neden takıldı; tahmin değil gerçek veri. *(Ücretsiz, Google OAuth)*
- **[OpenSEO](https://github.com/every-app/open-seo)** `MCP` `Skill`: Semrush/Ahrefs'in açık kaynak alternatifi. Kelime, rakip, backlink ve YZ görünürlüğü verisi agent'ının elinde. *(DataForSEO kullandıkça öde)*

  <details>
  <summary>13 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `seo-audit` | Veriye dayalı site denetimi; trafiği en çok büyütecek birkaç değişiklik |
  | `keyword-research` | Kelime fırsatları, metrikler, SERP analizi |
  | `keyword-clustering` | Kelimeleri niyete göre kümeler, sayfalara eşler; cannibalization'a son |
  | `competitor-analysis` | Tek rakibin organik ayak izi, kelimeleri, backlink'leri |
  | `competitive-landscape` | Pazar liderleri, kazanan içerik temaları, stratejik boşluklar |
  | `link-prospecting` | Backlink adayları, iletişim yolu, outreach taslağı |
  | `ai-visibility-audit` | Markan YZ cevaplarında nasıl görünüyor; alıntılanmak için ne yapmalı |
  | `ai-prompt-research` | İnsanlar ChatGPT'ye ne soruyor, kim alıntılanıyor |
  | `local-seo` | Google İşletme Profili denetimi, Maps görünürlük haritası |
  | `seo-report` | Tek sayfalık HTML rapor |
  | `seo-coach` | Rehber mod; sıradaki adımı önerir |
  | `seo-project-setup` | Proje bağlamı: hedef, rakip, ana sayfalar, Search Console |
  | `setup-openseo` | OpenSEO plugin, MCP ve skill kurulumu |

  </details>

- **[`seo-auditor`](https://github.com/alirezarezvani/claude-skills)** `Skill`: Meta etiket, okunabilirlik, kırık link, sitemap; tek taramada SEO karnesi.
- **[`geo-seo-claude`](https://github.com/zubair-trabzada/geo-seo-claude)** `Skill`: Google'da değil, ChatGPT/Perplexity cevaplarında da çık; GEO optimizasyonu.
- **[`seomachine`](https://github.com/TheCraigHewitt/seomachine)** `Skill`: Anahtar kelimeden yayına SEO içerik fabrikası.

### Reklam & Sosyal Medya

- **[meta-ads](https://github.com/pipeboard-co/meta-ads-mcp)** `MCP`: Facebook + Instagram reklamlarını sohbetten yönet. Kampanya aç, bütçe değiştir, performansı analiz et. *(Pipeboard, free plan)*
- **[`ads`](https://github.com/AgriciDaniel/claude-ads)** `Skill`: Google, Meta, LinkedIn, TikTok reklam hesaplarına 225+ kontrollü denetim. Boşa giden bütçeyi bulur.
- **[Instagram Agent Skills](https://github.com/Jakeschincariol/instagram-agent-skill)** `Skill`: Instagram hesabını baştan sona yöneten 13 skill. Viral hook'lu Reel'den DM'e kadar her şey; API anahtarı yok, hesap bağlamak yok.

  <details>
  <summary>13 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `ig-reel` | Ham fikirden çekime hazır Reel; 26 skorlanmış hook formülü, script, beat sheet |
  | `ig-viral` | Nişinde şu an patlayan reel'leri bulur, hook'unu çözer, swipe file çıkarır |
  | `ig-caption` | "... devamı"ndan sağ çıkan, lint'li, 3 hashtag'li caption |
  | `ig-carousel` | Kaydırtan kapak, slayt slayt metin, 1080x1350 dosyalar |
  | `ig-story` | Günün story dizisi; hangi sticker nerede, DM'e nasıl taşınır |
  | `ig-plan` | Haftalık içerik takvimi ve etkileşim listesi |
  | `ig-repurpose` | Tek YouTube videosu ya da podcast'ten bir haftalık reel + carousel |
  | `ig-profile` | Profili 100 üzerinden puanlar, bio/highlight/grid'i yeniden yazar |
  | `ig-audit` | Insights'ı okur: ne tuttu, neden battı, neyi bırakmalı |
  | `ig-dm` | Cevap alan DM; ilk mesaj, collab pitch, iki takip |
  | `ig-comment` | Bot gibi değil, fikri olan biri gibi yorum |
  | `ig-reply` | Kendi yorumlarına öncelik sırasıyla cevap; hater'dan lead'e |
  | `ig-human` | Taslaktaki AI izini siler; em dash, slop kelime, görünmez karakter |

  </details>

## 🤖 Claude İçi İşlevsel

### Token & Model Yönetimi

- **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** `MCP` `Skill`: 370+ sağlayıcı, 150+ ücretsiz tier tek endpoint'te. Kota biterse otomatik başka modele geçer, kodlama hiç durmaz. *(MIT, ücretsiz)*

  <details>
  <summary>45 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `omni-*` (25) | API tarafı: sağlayıcı, routing combo, bütçe, cache, sıkıştırma, MCP, A2A, webhook, tunnel, yedek |
  | `cli-*` (19) | Aynısı terminalden: sunucuyu başlat, sağlayıcı ekle, maliyeti izle, eval koştur |
  | `config-codex-cli` | Codex CLI'yi OmniRoute'a bağlar; config ve 7 profil hazır |

  </details>

- **[headroom](https://github.com/headroomlabs-ai/headroom)** `MCP`: Tool çıktısını, log'ları, JSON'u LLM'e gitmeden sıkıştırır. Aynı cevap, %20-95 daha az token. *(Ücretsiz)*

### Prompt & Agent

- **[`prompt-master`](https://github.com/nidhinjs/prompt-master)** `Skill`: Her AI aracı için nokta atışı prompt; Midjourney'den Cursor'a. Boşa kredi yakma.
- **[`task-observer`](https://github.com/rebelytics/one-skill-to-rule-them-all)** `Skill`: "One Skill to Rule Them All". Çalışmanı izler, düzeltmelerini yakalar, diğer skill'lerini senin onayınla geliştirir.
- **[agent-sdk-dev](https://github.com/anthropics/claude-plugins-official)** `Plugin`: Kendi Claude agent'ını dakikalar içinde ayağa kaldır ve best practice'e göre doğrulat.
- **`claude-api`** `Yerleşik`: Model ID, fiyat, streaming, tool use. Claude ile uygulama yazarken ezbere değil, doğru bilgiyle.

### Ayar & Otomasyon

- **[Claude Code yerleşik skill'leri](https://code.claude.com/docs/en/skills)** `Yerleşik`: Kurulum gerektirmez, Claude Code ile gelir. Ayarı, zamanlamayı ve kısayolları sohbetten yönet.

  <details>
  <summary>4 skill'in içinde ne var?</summary>

  | Skill | Ne yapar |
  |-------|----------|
  | `update-config` | "Bundan sonra her seferinde..." de, hook'u ve izni o yazsın |
  | `loop` | Komutu aralıklarla tekrar çalıştırır; deploy'u, CI'ı o izler |
  | `schedule` | Bulutta cron'la çalışan agent'lar; sen uyurken rapor hazır |
  | `keybindings-help` | Kısayolları yeniden bağla, chord'lar dahil |

  </details>

**Ekli marketplace'ler:** `claude-plugins-official`, `anthropic-skills`, `ui-ux-pro-max-skill`

> **Not:** Resmi Google sunucusu olan `stitch` dışındaki MCP'ler üçüncü taraf. `npx` ile çalışanlar her açılışta paketi güncellediği için kaynağına güvenmek gerekiyor.

---

## Maliyet Notları

- **Ücretsiz kullanılanlar:** stitch (350 üretim/ay), nanobanana (Flash modeli), context7, markitdown, github, remotion, omniroute, headroom, geo-optimizer, gsc
- **21st** free planında 100 kredi/ay veriyor — birkaç component üretimine denk geliyor, hızlı tükeniyor.
- **meta-ads** Pipeboard'un free planıyla çalışıyor; ilk kullanımda OAuth ile Meta hesabı bağlanıyor.
- **openseo** DataForSEO API'si üzerinden çalışır, istek başına ücret; hosted sürüm %28 ekler. Kullanmadan önce bütçe kararı ver.
- **gsc** ücretsiz ama Google Cloud'da OAuth (Desktop app) client oluşturmak gerekiyor.
- **nanobanana Pro modeli** (`gemini-3-pro-image-preview`) billing gerektirir — görsel başına ücretli. Varsayılan Flash'ta bırakmakta fayda var.
- **Gemini uygulaması aboneliği API'yi kapsamaz.** MCP'ler API anahtarı üzerinden çalışır, abonelik oradan geçmez.
- **fal.ai** ücretli: ücretsiz kota yok, tamamen kullandıkça öde. Kullanmadan önce bütçe kararı ver.

