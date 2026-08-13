# skills-and-mcp

Claude Code kurulumumda kullandığım **MCP sunucuları, plugin'ler ve skill'lerin** listesi.
Yeni bir makineye geçtiğimde ya da kurulumu sıfırladığımda buradan hızlıca toparlıyorum.

Tüm kayıtlar makine tarafından okunabilir şekilde [`setup.json`](setup.json) içinde tutuluyor.

---

## İçindekiler

- [MCP Sunucuları](#mcp-sunucuları)
- [Plugin & Marketplace](#plugin--marketplace)
- [Skill'ler](#skiller)
- [Kurulum](#kurulum)
- [Maliyet Notları](#maliyet-notları)

---

## MCP Sunucuları

Claude Code'a dış servislere erişim kazandıran sunucular.

| MCP | Ne işe yarar | Kaynak | Ücret |
|-----|--------------|--------|-------|
| **stitch** | Prompt'tan UI tasarımı üretir (Google Stitch). Ekran, varyant, tasarım sistemi. | [stitch.googleapis.com](https://stitch.withgoogle.com/docs/mcp/setup) | Ücretsiz — ~350 üretim/ay |
| **nanobanana** | Gemini ile görsel üretme ve düzenleme (Nano Banana 2). | [YCSE/nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp) | Flash modeli ücretsiz kotada |
| **supabase** | Veritabanı, auth ve storage yönetimi. | [mcp.supabase.com](https://mcp.supabase.com/mcp) | Ücretsiz plan var |
| **github** | Repo, issue, PR işlemleri. | [github/github-mcp-server](https://github.com/github/github-mcp-server) | Ücretsiz |
| **context7** | Kütüphanelerin güncel dokümanlarını çeker — eski API bilgisi sorununu çözer. | [upstash/context7](https://github.com/upstash/context7) | Ücretsiz |
| **markitdown** | PDF, Office ve HTML dosyalarını Markdown'a çevirir. | [microsoft/markitdown](https://github.com/microsoft/markitdown) | Ücretsiz |

> **Not:** Resmi Google sunucusu olan `stitch` dışındakiler üçüncü taraf. `nanobanana` `npx` ile her çalıştığında paketi güncellediği için kaynağına güvenmek gerekiyor.

---

## Plugin & Marketplace

| Plugin | Ne işe yarar | Marketplace |
|--------|--------------|-------------|
| **superpowers** | Brainstorming, sistematik debugging, TDD, plan yazma gibi süreç skill'leri. | [obra/superpowers](https://github.com/obra/superpowers) |
| **ui-ux-pro-max** | 84 UI stili, 192 renk paleti, 74 font eşleşmesi içeren tasarım veritabanı. Logo, banner, slayt, tasarım sistemi üretir. | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| **agent-sdk-dev** | Claude Agent SDK uygulaması kurma ve doğrulama. | [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |

**Ekli marketplace'ler:** `claude-plugins-official`, `anthropic-skills`, `ui-ux-pro-max-skill`

---

## Skill'ler

### Yerleşik (Claude Code ile gelir)

| Skill | Ne işe yarar |
|-------|--------------|
| `update-config` | `settings.json` düzenleme — izinler, hook'lar, env değişkenleri. |
| `keybindings-help` | Klavye kısayollarını özelleştirme. |
| `simplify` | Değişen kodu sadeleştirme ve tekrar kullanım temizliği. |
| `loop` | Bir komutu belirli aralıklarla tekrar çalıştırma. |
| `schedule` | Cron tabanlı zamanlanmış agent'lar. |
| `claude-api` | Model ID'leri, fiyatlandırma, streaming, tool use referansı. |

### Harici skill paketleri

| Skill | Ne işe yarar | Kaynak |
|-------|--------------|--------|
| `focused-fix` | 5 fazlı protokolle bir modülü sistematik onarma. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `review` | Push öncesi yerel inceleme kapısı. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `security-scan` | Push öncesi güvenlik taraması. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `plugin-audit` | Skill dizini için 8 fazlı denetim. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `seo-auditor` | Meta etiket, okunabilirlik, kırık link, sitemap taraması. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `update-docs` | Dokümantasyon dosyalarını güncelleme. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `git/cm` · `git/cp` · `git/pr` · `git/clean` | Conventional commit, push, PR açma, branch temizliği. | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) |
| `ads` | Google, Meta, LinkedIn, TikTok reklam denetimi — 225+ kontrol. | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) |
| `geo-seo-claude` | Lokal / GEO SEO optimizasyonu. | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) |
| `seomachine` | SEO içerik üretim iş akışı. | [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) |
| `awesome-design-systems` | Tasarım sistemi referans koleksiyonu. | [alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems) |

---

## Kurulum

### MCP ekleme

HTTP tabanlı sunucular:

```bash
claude mcp add stitch https://stitch.googleapis.com/mcp --transport http --header "X-Goog-Api-Key: ANAHTARIN" -s user
```

npm paketi olarak çalışanlar:

```bash
claude mcp add nanobanana -s user -e GOOGLE_AI_API_KEY=ANAHTARIN -- npx -y @ycse/nanobanana-mcp
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

- **Ücretsiz kullanılanlar:** stitch (350 üretim/ay), nanobanana (Flash modeli), context7, markitdown, github
- **nanobanana Pro modeli** (`gemini-3-pro-image-preview`) billing gerektirir — görsel başına ücretli. Varsayılan Flash'ta bırakmakta fayda var.
- **Gemini uygulaması aboneliği API'yi kapsamaz.** MCP'ler API anahtarı üzerinden çalışır, abonelik oradan geçmez.
- **fal.ai** denendi, tamamen kullandıkça öde olduğu için kaldırıldı.

---

## Güvenlik

- API anahtarları bu repoda **tutulmaz**. Yukarıdaki komutlarda `ANAHTARIN` yazan yerlere kendi anahtarını koy.
- Anahtarlar `~/.claude.json` içinde saklanır — bu dosyayı paylaşma.
- Üçüncü taraf MCP'ler `npx` ile kendini güncelleyebilir; kaynak repoyu ara ara kontrol et.
