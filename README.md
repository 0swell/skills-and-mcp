# skills-and-mcp

Claude Code kurulumumda kullandığım **MCP sunucuları, plugin'ler ve skill'lerin** listesi.
Yeni bir makineye geçtiğimde ya da kurulumu sıfırladığımda buradan hızlıca toparlıyorum.

Tüm kayıtlar makine tarafından okunabilir şekilde [`setup.json`](setup.json) içinde tutuluyor.

---

> Etiketler: `MCP` dış servise bağlanır · `Skill` Claude'a iş akışı öğretir · `Plugin` skill/agent paketi

## 🎨 Tasarım & UI

- **[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)** `Plugin`: Cebindeki tasarım ajansı. 84 stil, 192 palet, 74 font eşleşmesi; "AI yaptı" belli olmayan arayüzler.
- **[stitch](https://stitch.withgoogle.com/docs/mcp/setup)** `MCP`: Bir cümle yaz, Google komple ekranı çizsin. Figma'yı açmadan tasarım sistemi ve varyantlar hazır. *(Ücretsiz, ~350 üretim/ay)*
- **[21st](https://21st.dev)** `MCP`: shadcn/ui + Tailwind component'leri tek prompt'la. Hazır kütüphaneden çek, kodu direkt projene düşsün. *(100 kredi/ay, hızlı biter)*
- **[nanobanana](https://github.com/YCSE/nanobanana-mcp)** `MCP`: Gemini'nin görsel motoru terminalinde. Logo, mockup, asset üret ya da mevcut görseli düzenle. *(Flash ücretsiz kotada)*
- **[awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** `Skill`: Dünyanın en iyi tasarım sistemleri tek yerde; ilham ve referans.

## 🎬 Video (Remotion)

- **[remotion-documentation](https://www.npmjs.com/package/@remotion/mcp)** `MCP`: Remotion'ın resmi doküman beyni. Video kodu yazarken API'yi tahmin etme, sor. *(Ücretsiz)*
- **[`remotion-best-practices`](https://github.com/remotion-dev/skills)** `Skill`: React ile video yapmanın resmi rehberi. Hangi skill'i seçeceğini bilmiyorsan buradan başla.
- **`remotion-create`** `Skill`: "Plak dükkanı için promo video yap" de, proje ve composition hazır.
- **`remotion-markup` · `remotion-interactivity`** `Skill`: Animasyon, efekt ve yerleşimde Remotion ekibinin kuralları; sonradan düzenlenebilir kurgu.
- **`remotion-captions`** `Skill`: Sesi yazıya dök, altyazıyı TikTok tarzı animasyonla ekrana bas.
- **`remotion-studio` · `remotion-render`** `Skill`: Canlı önizle, sonra MP4'e dök; local ya da Lambda, ayar derdi yok.
- **`remotion-maps`** `Skill`: Harita animasyonları; rota çiz, şehirden şehre uç.
- **`remotion-multimedia`** `Skill`: Mediabunny ile video/ses dosyalarını oku, kes, dönüştür.
- **`remotion-saas` · `remotion-upgrade` · `remotion-docs`** `Skill`: Remotion üstüne SaaS kur, paketleri güvenle güncelle, dokümanda anında ara.

## 🛠️ Geliştirme & Kod Kalitesi

- **[superpowers](https://github.com/obra/superpowers)** `Plugin`: Claude'a kıdemli mühendis disiplini aşılar. Brainstorm, plan, TDD, sistematik debug; rastgele kod yazmaya son.
- **[`ponytail`](https://github.com/DietrichGebert/ponytail)** `Skill`: Odadaki en tembel kıdemli dev gibi düşünür. En iyi kod hiç yazılmayan koddur; YAGNI, stdlib, tek satır.
- **`ponytail-review` · `ponytail-audit`** `Skill`: Değişikliği ya da tüm repoyu sade dille inceler: bug, güvenlik, yük altında ne kırılır, ne silinebilir.
- **`ponytail-debt` · `ponytail-gain` · `ponytail-help`** `Skill`: Ertelenen kısayolların borç defteri, ölçülmüş tasarruf ve hızlı referans.
- **[`focused-fix`](https://github.com/alirezarezvani/claude-skills)** `Skill`: Bozuk modülü 5 fazlı protokolle onarır; yama değil kök neden.
- **[`review` · `security-scan`](https://github.com/alirezarezvani/claude-skills)** `Skill`: Push'tan önce son kapı; hatayı ve sızan anahtarı CI'dan önce sen gör.
- **[`git/cm` · `git/cp` · `git/pr` · `git/clean`](https://github.com/alirezarezvani/claude-skills)** `Skill`: Conventional commit, push, PR, branch temizliği; git ritüeli tek komut.
- **[`update-docs` · `plugin-audit`](https://github.com/alirezarezvani/claude-skills)** `Skill`: Kod değişti, doküman da güncellensin; skill/plugin dizinine 8 fazlı denetim.
- **`simplify`** `Skill`: Değişen kodu tarar, tekrarı ve gereksiz karmaşayı budar. Kod incelir, okunur olur.
- **[github](https://github.com/github/github-mcp-server)** `MCP`: Repo, issue ve PR'lar Claude'un elinde. Tarayıcıya geçmeden review, merge, triage. *(Ücretsiz)*
- **[context7](https://github.com/upstash/context7)** `MCP`: Eskimiş API bilgisine son. Kütüphanenin bugünkü dokümanını anında çeker, halüsinasyon kodu bitirir. *(Ücretsiz)*
- **[supabase](https://mcp.supabase.com/mcp)** `MCP`: Veritabanı, auth ve storage'ı sohbetten yönet. Dashboard'a girmeden tablo kur, sorgu at. *(Ücretsiz plan)*
- **[markitdown](https://github.com/microsoft/markitdown)** `MCP`: PDF, Word, Excel, HTML ne verirsen temiz Markdown'a çevirir. Belge okutmanın en kısa yolu. *(Ücretsiz)*

## 📈 Dijital Pazarlama

### SEO · GEO · AEO

- **[geo-optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill)** `MCP` `Skill`: ChatGPT, Perplexity, AI Overviews sitene atıf yapıyor mu? Princeton'ın 47 yöntemiyle GEO/AEO karnesi; llms.txt, bot erişimi, schema. *(Ücretsiz)*
- **[gsc](https://github.com/AminForou/mcp-gsc)** `MCP`: Search Console verisi sohbette. Hangi sorgu geliyor, hangi sayfa düşüyor, indeksleme neden takıldı; tahmin değil gerçek veri. *(Ücretsiz, Google OAuth)*
- **[openseo](https://github.com/every-app/open-seo)** `MCP`: Semrush/Ahrefs'in açık kaynak alternatifi. Kelime, rakip, backlink ve YZ görünürlüğü verisi agent'ının elinde. *(DataForSEO kullandıkça öde)*
- **[`seo-audit` · `keyword-research` · `keyword-clustering`](https://github.com/every-app/open-seo)** `Skill`: Veriye dayalı SEO denetimi, kelime fırsatları ve sayfa-kelime haritası; cannibalization'a son.
- **[`competitor-analysis` · `competitive-landscape` · `link-prospecting`](https://github.com/every-app/open-seo)** `Skill`: Rakibin trafiğini nereden aldığını çöz, boşluğu bul, backlink adaylarına outreach taslağı hazırla.
- **[`ai-visibility-audit` · `ai-prompt-research`](https://github.com/every-app/open-seo)** `Skill`: YZ neden rakibini öneriyor? İnsanların ChatGPT'ye ne sorduğunu ve kimin alıntılandığını gör.
- **[`local-seo`](https://github.com/every-app/open-seo)** `Skill`: Google İşletme Profili denetimi ve Maps görünürlük haritası.
- **[`seo-report` · `seo-coach` · `seo-project-setup` · `setup-openseo`](https://github.com/every-app/open-seo)** `Skill`: Tek sayfalık HTML rapor, rehber mod ve OpenSEO kurulum/proje bağlamı.
- **[`seo-auditor`](https://github.com/alirezarezvani/claude-skills)** `Skill`: Meta etiket, okunabilirlik, kırık link, sitemap; tek taramada SEO karnesi.
- **[`geo-seo-claude`](https://github.com/zubair-trabzada/geo-seo-claude)** `Skill`: Google'da değil, ChatGPT/Perplexity cevaplarında da çık; GEO optimizasyonu.
- **[`seomachine`](https://github.com/TheCraigHewitt/seomachine)** `Skill`: Anahtar kelimeden yayına SEO içerik fabrikası.

### Reklam & Sosyal Medya

- **[meta-ads](https://github.com/pipeboard-co/meta-ads-mcp)** `MCP`: Facebook + Instagram reklamlarını sohbetten yönet. Kampanya aç, bütçe değiştir, performansı analiz et. *(Pipeboard, free plan)*
- **[`ads`](https://github.com/AgriciDaniel/claude-ads)** `Skill`: Google, Meta, LinkedIn, TikTok reklam hesaplarına 225+ kontrollü denetim. Boşa giden bütçeyi bulur.
- **[`ig-reel`](https://github.com/Jakeschincariol/instagram-agent-skill)** `Skill`: Ham fikirden çekime hazır Reel. 26 skorlanmış hook formülü, script, ekran yazısı, zamanlı beat sheet.
- **`ig-viral`** `Skill`: Nişindeki şu an patlayan reel'leri bulur, hook'unu çözer, sana swipe file çıkarır.
- **`ig-caption` · `ig-carousel` · `ig-story`** `Skill`: "... devamı"ndan sağ çıkan caption, kaydırtan carousel, DM'e taşıyan story dizisi.
- **`ig-plan` · `ig-repurpose`** `Skill`: Haftalık içerik takvimi; tek YouTube videosundan bir haftalık reel + carousel.
- **`ig-profile` · `ig-audit`** `Skill`: Profilini 100 üzerinden puanlar, insights'ını okur: ne tuttu, neden battı.
- **`ig-dm` · `ig-comment` · `ig-reply`** `Skill`: Cevap alan DM, bot gibi olmayan yorum, hater'dan lead'e öncelikli cevap.
- **`ig-human`** `Skill`: Taslaktaki AI izini siler; em dash, slop kelimeler, görünmez karakterler gider.

## 🤖 Claude İçi İşlevsel

### Token & Model Yönetimi

- **[omniroute](https://github.com/diegosouzapw/OmniRoute)** `MCP`: 370+ sağlayıcı, 150+ ücretsiz tier tek endpoint'te. Kota biterse otomatik başka modele geçer, kodlama hiç durmaz. *(MIT, ücretsiz)*
- **`omni-*` · `cli-*` · `config-codex-cli`** `Skill`: OmniRoute'un tamamı Claude'un elinde (44 skill): sağlayıcı, routing, bütçe, cache, sıkıştırma, A2A; API'den de terminalden de.
- **[headroom](https://github.com/headroomlabs-ai/headroom)** `MCP`: Tool çıktısını, log'ları, JSON'u LLM'e gitmeden sıkıştırır. Aynı cevap, %20-95 daha az token. *(Ücretsiz)*

### Prompt & Agent

- **[`prompt-master`](https://github.com/nidhinjs/prompt-master)** `Skill`: Her AI aracı için nokta atışı prompt; Midjourney'den Cursor'a. Boşa kredi yakma.
- **[`task-observer`](https://github.com/rebelytics/one-skill-to-rule-them-all)** `Skill`: "One Skill to Rule Them All". Çalışmanı izler, düzeltmelerini yakalar, diğer skill'lerini senin onayınla geliştirir.
- **[agent-sdk-dev](https://github.com/anthropics/claude-plugins-official)** `Plugin`: Kendi Claude agent'ını dakikalar içinde ayağa kaldır ve best practice'e göre doğrulat.
- **`claude-api`** `Skill`: Model ID, fiyat, streaming, tool use. Claude ile uygulama yazarken ezbere değil, doğru bilgiyle.

### Ayar & Otomasyon

- **`update-config`** `Skill`: "Bundan sonra her seferinde..." de, hook'u ve izni o yazsın. settings.json'a elle dokunma.
- **`loop` · `schedule`** `Skill`: Komutu aralıklarla tekrar çalıştır ya da bulutta cron'la agent koştur; sen uyurken rapor hazır.
- **`keybindings-help`** `Skill`: Kısayolları kendi parmaklarına göre yeniden bağla, chord'lar dahil.

**Ekli marketplace'ler:** `claude-plugins-official`, `anthropic-skills`, `ui-ux-pro-max-skill`

> **Not:** Resmi Google sunucusu olan `stitch` dışındaki MCP'ler üçüncü taraf. `npx` ile çalışanlar her açılışta paketi güncellediği için kaynağına güvenmek gerekiyor.

---

## Kurulum

### Plugin ekleme

```bash
claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
```

```bash
claude plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

---

## Maliyet Notları

- **Ücretsiz kullanılanlar:** stitch (350 üretim/ay), nanobanana (Flash modeli), context7, markitdown, github, remotion, omniroute, headroom, geo-optimizer, gsc
- **21st** free planında 100 kredi/ay veriyor — birkaç component üretimine denk geliyor, hızlı tükeniyor.
- **meta-ads** Pipeboard'un free planıyla çalışıyor; ilk kullanımda OAuth ile Meta hesabı bağlanıyor.
- **openseo** DataForSEO API'si üzerinden çalışır, istek başına ücret; hosted sürüm %28 ekler. Kullanmadan önce bütçe kararı ver.
- **gsc** ücretsiz ama Google Cloud'da OAuth (Desktop app) client oluşturmak gerekiyor.
- **nanobanana Pro modeli** (`gemini-3-pro-image-preview`) billing gerektirir — görsel başına ücretli. Varsayılan Flash'ta bırakmakta fayda var.
- **Gemini uygulaması aboneliği API'yi kapsamaz.** MCP'ler API anahtarı üzerinden çalışır, abonelik oradan geçmez.
- **fal.ai** denendi, tamamen kullandıkça öde olduğu için kaldırıldı.

