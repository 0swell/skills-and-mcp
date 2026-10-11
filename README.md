# skills-and-mcp

Claude Code kurulumumda kullandığım **MCP sunucuları, plugin'ler ve skill'lerin** listesi.
Yeni bir makineye geçtiğimde ya da kurulumu sıfırladığımda buradan hızlıca toparlıyorum.

Tüm kayıtlar makine tarafından okunabilir şekilde [`setup.json`](setup.json) içinde tutuluyor.

---

## MCP Sunucuları

- **[stitch](https://stitch.withgoogle.com/docs/mcp/setup)**: Bir cümle yaz, Google komple ekranı çizsin. Figma'yı açmadan tasarım sistemi ve varyantlar hazır. *(Ücretsiz, ~350 üretim/ay)*
- **[nanobanana](https://github.com/YCSE/nanobanana-mcp)**: Gemini'nin görsel motoru terminalinde. Logo, mockup, asset üret ya da mevcut görseli düzenle. *(Flash ücretsiz kotada)*
- **[21st](https://21st.dev)**: shadcn/ui + Tailwind component'leri tek prompt'la. Hazır kütüphaneden çek, kodu direkt projene düşsün. *(100 kredi/ay, hızlı biter)*
- **[supabase](https://mcp.supabase.com/mcp)**: Veritabanı, auth ve storage'ı sohbetten yönet. Dashboard'a girmeden tablo kur, sorgu at. *(Ücretsiz plan)*
- **[github](https://github.com/github/github-mcp-server)**: Repo, issue ve PR'lar Claude'un elinde. Tarayıcıya geçmeden review, merge, triage. *(Ücretsiz)*
- **[context7](https://github.com/upstash/context7)**: Eskimiş API bilgisine son. Kütüphanenin bugünkü dokümanını anında çeker, halüsinasyon kodu bitirir. *(Ücretsiz)*
- **[markitdown](https://github.com/microsoft/markitdown)**: PDF, Word, Excel, HTML ne verirsen temiz Markdown'a çevirir. Belge okutmanın en kısa yolu. *(Ücretsiz)*
- **[remotion-documentation](https://www.npmjs.com/package/@remotion/mcp)**: Remotion'ın resmi doküman beyni. Video kodu yazarken API'yi tahmin etme, sor. *(Ücretsiz)*
- **[omniroute](https://github.com/diegosouzapw/OmniRoute)**: 370+ sağlayıcı, 150+ ücretsiz tier tek endpoint'te. Kota biterse otomatik başka modele geçer, kodlama hiç durmaz. *(MIT, ücretsiz)*
- **[headroom](https://github.com/headroomlabs-ai/headroom)**: Tool çıktısını, log'ları, JSON'u LLM'e gitmeden sıkıştırır. Aynı cevap, %20-95 daha az token. *(Ücretsiz)*
- **[meta-ads](https://github.com/pipeboard-co/meta-ads-mcp)**: Facebook + Instagram reklamlarını sohbetten yönet. Kampanya aç, bütçe değiştir, performansı analiz et. *(Pipeboard, free plan)*
- **[geo-optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill)**: ChatGPT, Perplexity ve Google AI Overviews sitene atıf yapıyor mu? Tek komutla GEO/AEO karnesi ve düzeltme listesi. *(MIT, ücretsiz)*
- **[gsc](https://github.com/AminForou/mcp-gsc)**: Search Console verisi sohbette. Hangi sorgu geliyor, hangi sayfa düşüyor, indeksleme neden takıldı; tahmin değil gerçek veri. *(Ücretsiz, Google OAuth)*
- **[openseo](https://github.com/every-app/open-seo)**: Semrush/Ahrefs'in açık kaynak alternatifi. Anahtar kelime, rakip, backlink ve YZ görünürlüğü verisi agent'ının elinde. *(DataForSEO kullandıkça öde)*

> **Not:** Resmi Google sunucusu olan `stitch` dışındakiler üçüncü taraf. `npx` ile çalışanlar her açılışta paketi güncellediği için kaynağına güvenmek gerekiyor.

---

## Plugin & Marketplace

- **[superpowers](https://github.com/obra/superpowers)**: Claude'a kıdemli mühendis disiplini aşılar. Brainstorm, plan, TDD, sistematik debug; rastgele kod yazmaya son.
- **[ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)**: Cebindeki tasarım ajansı. 84 stil, 192 palet, 74 font eşleşmesi; "AI yaptı" belli olmayan arayüzler.
- **[agent-sdk-dev](https://github.com/anthropics/claude-plugins-official)**: Kendi Claude agent'ını dakikalar içinde ayağa kaldır ve best practice'e göre doğrulat.

**Ekli marketplace'ler:** `claude-plugins-official`, `anthropic-skills`, `ui-ux-pro-max-skill`

---

## Skill'ler

### Yerleşik (Claude Code ile gelir)

- **`update-config`**: "Bundan sonra her seferinde..." de, hook'u ve izni o yazsın. settings.json'a elle dokunma.
- **`keybindings-help`**: Kısayolları kendi parmaklarına göre yeniden bağla, chord'lar dahil.
- **`simplify`**: Değişen kodu tarar, tekrarı ve gereksiz karmaşayı budar. Kod incelir, okunur olur.
- **`loop`**: Bir komutu aralıklarla tekrar çalıştırır. Deploy'u, CI'ı sen izleme, o izlesin.
- **`schedule`**: Bulutta cron'la çalışan agent'lar. Sen uyurken rapor hazır.
- **`claude-api`**: Model ID, fiyat, streaming, tool use. Claude ile uygulama yazarken ezbere değil, doğru bilgiyle.

### Video: Remotion ([remotion-dev/skills](https://github.com/remotion-dev/skills))

- **`remotion-best-practices`**: React ile video yapmanın resmi rehberi. Hangi skill'i seçeceğini bilmiyorsan buradan başla.
- **`remotion-create`**: "Plak dükkanı için promo video yap" de, proje ve composition hazır.
- **`remotion-markup`**: Animasyon, efekt ve içerik yerleşiminde Remotion ekibinin kendi kuralları.
- **`remotion-captions`**: Sesi yazıya dök, altyazıyı TikTok tarzı animasyonla ekrana bas.
- **`remotion-render`**: Videoyu MP4'e dök; local ya da Lambda, ayar derdi yok.
- **`remotion-studio`**: Studio'da canlı önizleme; render beklemeden sonucu gör.
- **`remotion-docs`**: Remotion dokümanında anında arama.
- **`remotion-interactivity`**: Markup'ı sonradan düzenlenebilir, interaktif olacak şekilde kurgula.
- **`remotion-maps`**: Harita animasyonları; rota çiz, şehirden şehre uç.
- **`remotion-multimedia`**: Mediabunny ile video/ses dosyalarını oku, kes, dönüştür.
- **`remotion-saas`**: Remotion üstüne video üreten bir SaaS kur.
- **`remotion-upgrade`**: Remotion ve bağlı paketleri tek hamlede güvenle güncelle.

### Instagram ([Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill))

- **`ig-reel`**: Ham fikirden çekime hazır Reel. 26 skorlanmış hook formülü, script, ekran yazısı, zamanlı beat sheet.
- **`ig-viral`**: Nişindeki şu an patlayan reel'leri bulur, hook'unu çözer, sana swipe file çıkarır.
- **`ig-caption`**: "... devamı" kesiminden sağ çıkan caption; lint'li, 3 hashtag'li.
- **`ig-carousel`**: Kaydırtan kapak, slayt slayt metin ve 1080x1350 dosyalar.
- **`ig-story`**: Günün story dizisi; hangi sticker nerede, DM'e nasıl taşınır.
- **`ig-plan`**: Haftalık içerik takvimi ve etkileşim listesi. "Ne paylaşsam" derdi biter.
- **`ig-profile`**: Profilini 100 üzerinden puanlar, puan kaybettiren bio/highlight/grid'i yeniden yazar.
- **`ig-audit`**: Insights'ını okur: ne tuttu, neden battı, neyi bırakmalısın.
- **`ig-repurpose`**: Tek YouTube videosu ya da podcast'ten bir haftalık reel + carousel.
- **`ig-dm`**: Cevap alan DM'ler; ilk mesaj, collab pitch, iki takip.
- **`ig-comment`**: Bot gibi değil, fikri olan biri gibi yorum.
- **`ig-reply`**: Kendi yorumlarına öncelik sırasıyla cevap; hater'dan lead'e.
- **`ig-human`**: Taslaktaki AI izini siler; em dash, slop kelimeler, görünmez karakterler gider.

### OmniRoute ([diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute))

- **`omni-*` (25 skill)**: OmniRoute API'sinin tamamı Claude'un elinde: sağlayıcılar, routing combo'ları, bütçe, cache, sıkıştırma, MCP, A2A, webhook, tunnel.
- **`cli-*` (19 skill)**: Aynı gücü terminalden: sunucuyu başlat, sağlayıcı ekle, maliyeti izle, eval koştur.
- **`config-codex-cli`**: Codex CLI'yi OmniRoute'a bağlar; config ve 7 profil hazır.

### Kod kalitesi

- **[`ponytail`](https://github.com/DietrichGebert/ponytail)**: Odadaki en tembel kıdemli dev gibi düşünür. En iyi kod hiç yazılmayan koddur; YAGNI, stdlib, tek satır.
- **`ponytail-review` · `ponytail-audit`**: Değişikliği ya da tüm repoyu sade dille inceler: bug, güvenlik, yük altında ne kırılır, ne silinebilir.
- **`ponytail-debt` · `ponytail-gain` · `ponytail-help`**: Ertelenen kısayolların borç defteri, ölçülmüş tasarruf ve hızlı referans.
- **[`focused-fix`](https://github.com/alirezarezvani/claude-skills)**: Bozuk modülü 5 fazlı protokolle onarır; yama değil kök neden.
- **[`review`](https://github.com/alirezarezvani/claude-skills)**: Push'tan önce son kapı. Hatayı CI'dan önce sen gör.
- **[`security-scan`](https://github.com/alirezarezvani/claude-skills)**: Push öncesi güvenlik taraması; sızan anahtar repoya girmesin.
- **[`plugin-audit`](https://github.com/alirezarezvani/claude-skills)**: Skill/plugin dizinine 8 fazlı denetim.
- **[`git/cm` · `git/cp` · `git/pr` · `git/clean`](https://github.com/alirezarezvani/claude-skills)**: Conventional commit, push, PR, branch temizliği; git ritüeli tek komut.
- **[`update-docs`](https://github.com/alirezarezvani/claude-skills)**: Kod değişti, doküman da güncellensin.

### Prompt & meta

- **[`prompt-master`](https://github.com/nidhinjs/prompt-master)**: Her AI aracı için nokta atışı prompt; Midjourney'den Cursor'a. Boşa kredi yakma.
- **[`task-observer`](https://github.com/rebelytics/one-skill-to-rule-them-all)**: "One Skill to Rule Them All". Çalışmanı izler, düzeltmelerini yakalar, diğer skill'lerini senin onayınla geliştirir.

### Pazarlama & SEO

- **[`ads`](https://github.com/AgriciDaniel/claude-ads)**: Google, Meta, LinkedIn, TikTok reklam hesaplarına 225+ kontrollü denetim. Boşa giden bütçeyi bulur.
- **[`seo-auditor`](https://github.com/alirezarezvani/claude-skills)**: Meta etiket, okunabilirlik, kırık link, sitemap; tek taramada SEO karnesi.
- **[`geo-seo-claude`](https://github.com/zubair-trabzada/geo-seo-claude)**: Google'da değil, ChatGPT/Perplexity cevaplarında da çık; GEO optimizasyonu.
- **[`seomachine`](https://github.com/TheCraigHewitt/seomachine)**: Anahtar kelimeden yayına SEO içerik fabrikası.
- **[`geo-optimizer`](https://github.com/Auriti-Labs/geo-optimizer-skill)**: Princeton araştırmasına dayalı 47 yöntemle sayfanı YZ'nin alıntılayacağı hale getirir; llms.txt, bot erişimi, schema.
- **[`seo-audit` · `keyword-research` · `keyword-clustering`](https://github.com/every-app/open-seo)**: Veriye dayalı SEO denetimi, kelime fırsatları ve sayfa-kelime haritası; cannibalization'a son.
- **[`competitor-analysis` · `competitive-landscape` · `link-prospecting`](https://github.com/every-app/open-seo)**: Rakibin trafiğini nereden aldığını çöz, boşluğu bul, backlink adaylarına outreach taslağı hazırla.
- **[`ai-visibility-audit` · `ai-prompt-research`](https://github.com/every-app/open-seo)**: YZ neden rakibini öneriyor? İnsanların ChatGPT'ye ne sorduğunu ve kimin alıntılandığını gör.
- **[`local-seo`](https://github.com/every-app/open-seo)**: Google İşletme Profili denetimi ve Maps görünürlük haritası.
- **[`seo-report` · `seo-coach` · `seo-project-setup` · `setup-openseo`](https://github.com/every-app/open-seo)**: Tek sayfalık HTML rapor, rehber mod ve OpenSEO kurulum/proje bağlamı.
- **[`awesome-design-systems`](https://github.com/alexpate/awesome-design-systems)**: Dünyanın en iyi tasarım sistemleri tek yerde; ilham ve referans.

---

## Kurulum

### Skill ekleme ([skills CLI](https://skills.sh))

```bash
npx skills add remotion-dev/skills -g -a claude-code -y
```

Aynı komutla: `Jakeschincariol/instagram-agent-skill`, `diegosouzapw/OmniRoute`, `DietrichGebert/ponytail`, `nidhinjs/prompt-master`, `rebelytics/one-skill-to-rule-them-all --skill task-observer`, `every-app/open-seo --skill seo-audit keyword-research ...`.

`geo-optimizer` skill'i frontmatter'sız geldiği için CLI ile kurulmuyor: repodaki `SKILL.md` + `references/` elle `~/.claude/skills/geo-optimizer/` altına kopyalanır.

### MCP ekleme

HTTP tabanlı sunucular:

```bash
claude mcp add stitch https://stitch.googleapis.com/mcp --transport http --header "X-Goog-Api-Key: ANAHTARIN" -s user
```

```bash
claude mcp add --transport http meta-ads -s user https://meta-ads.mcp.pipeboard.co/
```

npm paketi olarak çalışanlar:

```bash
claude mcp add nanobanana -s user -e GOOGLE_AI_API_KEY=ANAHTARIN -- npx -y @ycse/nanobanana-mcp
```

```bash
claude mcp add remotion-documentation -s user -- npx -y @remotion/mcp@latest
```

Önce CLI'si kurulması gerekenler:

```bash
npm install -g omniroute && claude mcp add omniroute -s user -- omniroute --mcp
```

```bash
uv tool install --python 3.13 "headroom-ai[all]" && headroom mcp install --agent claude
```

```bash
uv tool install --python 3.13 "geo-optimizer-skill[mcp]" --with "mcp<2" && claude mcp add geo-optimizer -s user -- geo-mcp
```

```bash
claude mcp add gsc -s user -e GSC_OAUTH_CLIENT_SECRETS_FILE=/path/to/client_secrets.json -- uvx mcp-search-console
```

```bash
claude mcp add --transport http openseo -s user https://app.openseo.so/mcp
```

Doğrulama:

```bash
claude mcp list
```

### Plugin ekleme

```bash
claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
```

```bash
claude plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### Scope seçimi

| Scope | Kapsam |
|-------|--------|
| `-s user` | Tüm projelerde geçerli |
| `-s local` | Sadece bulunduğun proje klasöründe |
| `-s project` | `.mcp.json` ile takıma paylaşılır |

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

---

## Güvenlik

- API anahtarları bu repoda **tutulmaz**. Yukarıdaki komutlarda `ANAHTARIN` yazan yerlere kendi anahtarını koy.
- Anahtarlar `~/.claude.json` içinde saklanır — bu dosyayı paylaşma.
- Üçüncü taraf MCP'ler `npx` ile kendini güncelleyebilir; kaynak repoyu ara ara kontrol et.
- `omniroute` ve `headroom` yerel proxy olarak çalışır; Claude Code'u onlardan geçirmek (`ANTHROPIC_BASE_URL`) isteğe bağlı, varsayılan kurulumda yönlendirme yok.
