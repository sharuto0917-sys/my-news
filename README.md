<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>しゅるのニュース</title>
  <style>
    :root {
      --bg: #f3f7fb;
      --panel: #ffffff;
      --panel-alt: #eef4ff;
      --text: #1e293b;
      --muted: #64748b;
      --border: #dfe7f1;
      --primary: #1d4ed8;
      --primary-soft: #dbeafe;
      --dark: #0f172a;
      --shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      font-family: "Segoe UI", "Hiragino Sans", "Yu Gothic", sans-serif;
      background: linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
      color: var(--text);
    }

    a { color: inherit; }

    header {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: #fff;
      padding: 28px 18px 22px;
    }

    .header-inner {
      max-width: 1180px;
      margin: 0 auto;
    }

    .brand {
      font-size: clamp(2rem, 3vw, 3rem);
      font-weight: 800;
      letter-spacing: 0.04em;
      margin: 0;
    }

    .subtitle {
      margin: 8px 0 0;
      color: rgba(255,255,255,0.8);
      font-size: 1rem;
      letter-spacing: 0.03em;
    }

    .update-time {
      margin-top: 14px;
      font-size: 0.87rem;
      color: rgba(255,255,255,0.8);
    }

    nav {
      position: sticky;
      top: 0;
      z-index: 20;
      background: rgba(255,255,255,0.9);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
    }

    .nav-inner {
      max-width: 1180px;
      margin: 0 auto;
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding: 0 14px;
    }

    .nav-item {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 14px 18px;
      font-weight: 700;
      color: var(--text);
      text-decoration: none;
      white-space: nowrap;
      border-bottom: 3px solid transparent;
      transition: 0.2s ease;
    }

    .nav-item:hover {
      background: #f8fafc;
      border-color: var(--primary);
    }

    main {
      max-width: 1180px;
      margin: 28px auto 40px;
      padding: 0 18px;
    }

    .page-title {
      margin-bottom: 20px;
    }

    .page-title h2 {
      font-size: clamp(1.5rem, 2vw, 2.2rem);
      margin: 0;
    }

    .page-title p {
      margin: 8px 0 0;
      color: var(--muted);
    }

    .top-news {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: var(--shadow);
      padding: 22px 24px;
      margin-bottom: 24px;
    }

    .top-news h2 {
      margin: 0 0 18px;
      padding-bottom: 12px;
      border-bottom: 3px solid var(--dark);
      font-size: 1.45rem;
    }

    .top-article {
      padding: 16px 8px;
      border-bottom: 1px solid var(--border);
    }

    .top-article:last-child {
      border-bottom: none;
    }

    .top-category {
      display: inline-block;
      margin-bottom: 8px;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--muted);
      letter-spacing: 0.04em;
    }

    .top-article a {
      color: var(--primary);
      font-size: 1.06rem;
      font-weight: 700;
      text-decoration: none;
      line-height: 1.7;
    }

    .top-article a:hover {
      text-decoration: underline;
    }

    .search-box {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 16px;
      box-shadow: var(--shadow);
      padding: 18px 20px;
      margin-bottom: 24px;
    }

    .search-box input {
      width: 100%;
      border: 1px solid #cbd5e1;
      border-radius: 10px;
      padding: 14px 16px;
      font-size: 1rem;
      outline: none;
      transition: border-color 0.2s ease;
    }

    .search-box input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.12);
    }

    .category {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: var(--shadow);
      padding: 22px 24px;
      margin-bottom: 22px;
    }

    .category h2 {
      margin: 0 0 18px;
      padding-bottom: 12px;
      border-bottom: 3px solid var(--dark);
      font-size: 1.35rem;
    }

    .news {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 14px 6px;
      border-bottom: 1px solid var(--border);
    }

    .news:last-child {
      border-bottom: none;
    }

    .news-number {
      min-width: 28px;
      color: #94a3b8;
      font-weight: 800;
      padding-top: 2px;
    }

    .news-content {
      flex: 1;
      min-width: 0;
    }

    .news a {
      color: var(--text);
      text-decoration: none;
      font-weight: 600;
      line-height: 1.7;
      display: inline-block;
    }

    .news a:hover {
      color: var(--primary);
      text-decoration: underline;
    }

    .news-meta {
      display: block;
      margin-top: 4px;
      font-size: 0.77rem;
      color: var(--muted);
    }

    .favorite {
      border: none;
      background: transparent;
      font-size: 1.6rem;
      cursor: pointer;
      padding: 4px 2px;
      line-height: 1;
      user-select: none;
    }

    .favorite:hover {
      transform: scale(1.1);
    }

    .no-result,
    .error {
      margin: 0;
      color: var(--muted);
      padding: 10px 0 4px;
    }

    .error {
      background: #fff1f2;
      color: #b91c1c;
      border: 1px solid #fecdd3;
      border-radius: 12px;
      padding: 18px 20px;
    }

    footer {
      text-align: center;
      padding: 20px 16px 36px;
      color: var(--muted);
      font-size: 0.8rem;
    }

    @media (max-width: 640px) {
      .top-news, .category {
        padding: 18px 16px;
      }

      .news {
        gap: 8px;
      }

      .favorite {
        font-size: 1.4rem;
      }
    }
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <h1 class="brand">しゅるのニュース</h1>
      <p class="subtitle">国内政治・国際政治・経済・音楽・テクノロジーをまとめて読む</p>
      <div class="update-time" id="update-time">🕐 ニュースを読み込み中...</div>
    </div>
  </header>

  <nav>
    <div class="nav-inner">
      <a class="nav-item" href="#top">🔥 トップ</a>
      <a class="nav-item" href="#国内政治">🇯🇵 国内政治</a>
      <a class="nav-item" href="#国際政治">🌏 国際政治</a>
      <a class="nav-item" href="#経済">💹 経済</a>
      <a class="nav-item" href="#テクノロジー">💻 テクノロジー</a>
      <a class="nav-item" href="#音楽">🎵 音楽</a>
      <a class="nav-item" href="#エンタメ">🎬 エンタメ</a>
      <a class="nav-item" href="#スポーツ">⚽ スポーツ</a>
    </div>
  </nav>

  <main>
    <div class="page-title">
      <h2>今日の注目ニュース</h2>
      <p>自分向けのニュースを検索して、気になる記事を保存できます。</p>
    </div>

    <section class="top-news" id="top">
      <h2>🔥 トップニュース</h2>
      <div id="top-news-container">
        <p>ニュースを読み込んでいます...</p>
      </div>
    </section>

    <div class="search-box">
      <input id="search" type="text" placeholder="🔎 ニュースを検索（例：政策、円、アーティスト）" />
    </div>

    <div id="news-container">
      <p>ニュースを読み込んでいます...</p>
    </div>
  </main>

  <footer>© しゅるのニュース</footer>

  <script>
    let allNews = {};
    let favorites = JSON.parse(localStorage.getItem("myNewsFavorites") || "[]");

    const icons = {
      "国内政治": "🇯🇵",
      "国際政治": "🌏",
      "経済": "💹",
      "テクノロジー": "💻",
      "音楽": "🎵",
      "エンタメ": "🎬",
      "スポーツ": "⚽"
    };

    async function loadNews() {
      try {
        const response = await fetch("news.json");
        if (!response.ok) throw new Error("news.jsonを取得できませんでした");

        allNews = await response.json();

        const now = new Date();
        const formattedTime = now.toLocaleString("ja-JP", {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
          hour: "2-digit",
          minute: "2-digit"
        });

        document.getElementById("update-time").textContent = `🕐 最終更新: ${formattedTime}`;
        displayTopNews();
        displayNews();
      } catch (error) {
        console.error(error);
        document.getElementById("news-container").innerHTML = '<p class="error">ニュースを読み込めませんでした。news.json を確認してください。</p>';
      }
    }

    function displayTopNews() {
      const container = document.getElementById("top-news-container");
      container.innerHTML = "";

      const entries = Object.entries(allNews).filter(([category, articles]) => Array.isArray(articles) && articles.length > 0);

      entries.slice(0, 5).forEach(([category, articles]) => {
        const article = articles[0];
        const div = document.createElement("div");
        div.className = "top-article";

        const categoryLabel = document.createElement("div");
        categoryLabel.className = "top-category";
        categoryLabel.textContent = `${icons[category] || "📰"} ${category}`;

        const link = document.createElement("a");
        link.href = article.url;
        link.textContent = article.title;
        link.target = "_blank";
        link.rel = "noopener noreferrer";

        div.appendChild(categoryLabel);
        div.appendChild(link);
        container.appendChild(div);
      });
    }

    function displayNews() {
      const container = document.getElementById("news-container");
      const searchWord = document.getElementById("search").value.toLowerCase().trim();
      container.innerHTML = "";

      Object.entries(allNews).forEach(([category, articles]) => {
        if (!Array.isArray(articles)) return;

        const filteredArticles = articles.filter(article =>
          (article.title || "").toLowerCase().includes(searchWord)
        );

        const section = document.createElement("section");
        section.className = "category";
        section.id = category;

        const heading = document.createElement("h2");
        heading.textContent = `${icons[category] || "📰"} ${category}`;
        section.appendChild(heading);

        if (filteredArticles.length === 0) {
          const message = document.createElement("p");
          message.className = searchWord ? "no-result" : "no-result";
          message.textContent = searchWord ? "検索結果がありません。" : "ニュースがありません。";
          section.appendChild(message);
        } else {
          filteredArticles.forEach((article, index) => {
            const div = document.createElement("div");
            div.className = "news";

            const number = document.createElement("span");
            number.className = "news-number";
            number.textContent = `${index + 1}.`;

            const content = document.createElement("div");
            content.className = "news-content";

            const link = document.createElement("a");
            link.href = article.url;
            link.textContent = article.title;
            link.target = "_blank";
            link.rel = "noopener noreferrer";

            const meta = document.createElement("span");
            meta.className = "news-meta";
            meta.textContent = article.source || "ニュースソース";

            content.appendChild(link);
            content.appendChild(meta);

            const favoriteButton = document.createElement("button");
            favoriteButton.className = "favorite";
            const isFavorite = favorites.some(item => item.url === article.url);
            favoriteButton.textContent = isFavorite ? "⭐" : "☆";
            favoriteButton.title = isFavorite ? "お気に入りから削除" : "お気に入りに追加";
            favoriteButton.onclick = () => toggleFavorite(article, favoriteButton);

            div.appendChild(number);
            div.appendChild(content);
            div.appendChild(favoriteButton);
            section.appendChild(div);
          });
        }

        container.appendChild(section);
      });
    }

    function toggleFavorite(article, button) {
      const index = favorites.findIndex(item => item.url === article.url);

      if (index >= 0) {
        favorites.splice(index, 1);
      } else {
        favorites.push(article);
      }

      localStorage.setItem("myNewsFavorites", JSON.stringify(favorites));
      displayNews();
    }

    document.getElementById("search").addEventListener("input", displayNews);
    loadNews();
  </script>
</body>
</html>



























































































































































































































































































"},
"title": "政策議論が再燃、社会保障と税制の調整が焦点", "url": "https://example.com/jp-policy-2", "published": "2026-10-07T09:00:00+09:00", "source": "経済新聞"},{
"title": "地方自治体の新施策が広がる、住民サービスの改善に期待", "url": "https://example.com/jp-policy-3", "published": "2026-10-07T08:45:00+09:00", "source": "朝日新聞"},{
"title": "選挙制度改正を巡る議論、透明性向上が課題", "url": "https://example.com/jp-policy-4", "published": "2026-10-07T08:15:00+09:00", "source": "読売新聞"}
  ],
  "国際政治": [
    {"title": "G7首脳会議で安全保障と経済安定が主要議題に", "url": "https://example.com/world-policy-1", "published": "2026-10-07T09:30:00+09:00", "source": "AFP"},
    {"title": "地域紛争の影響が食料価格に及ぶ、国際支援の必要性が高まる", "url": "https://example.com/world-policy-2", "published": "2026-10-07T09:00:00+09:00", "source": "Reuters"},
    {"title": "主要国で防衛費増額が進展、軍事バランスが変化", "url": "https://example.com/world-policy-3", "published": "2026-10-07T08:20:00+09:00", "source": "BBC"},
    {"title": "国際協調の枠組み再編、エネルギー安定の重要性が増す", "url": "https://example.com/world-policy-4", "published": "2026-10-07T07:50:00+09:00", "source": "時事通信"}
  ],
  "経済": [
    {"title": "円相場が動意づき、輸出企業の利益に注目が集まる", "url": "https://example.com/economy-1", "published": "2026-10-07T10:00:00+09:00", "source": "日本経済新聞"},
    {"title": "国内企業の設備投資計画が改善、成長期待が高まる", "url": "https://example.com/economy-2", "published": "2026-10-07T09:20:00+09:00", "source": "日経"},
    {"title": "インフレ抑制と景気回復のバランスが問われる", "url": "https://example.com/economy-3", "published": "2026-10-07T08:35:00+09:00", "source": "NHK"},
    {"title": "中小企業向け融資制度の見直しが進行、資金繰りに注目", "url": "https://example.com/economy-4", "published": "2026-10-07T07:55:00+09:00", "source": "毎日新聞"}
  ],
  "テクノロジー": [
    {"title": "生成AIの業務活用が進む、企業行動の変化が加速", "url": "https://example.com/tech-1", "published": "2026-10-07T09:45:00+09:00", "source": "ITmedia"},
    {"title": "半導体投資が再加速、国内調達網の強化が課題に", "url": "https://example.com/tech-2", "published": "2026-10-07T09:10:00+09:00", "source": "ZDNet Japan"},
    {"title": "クラウドセキュリティへの関心が高まり、運用モデルの見直しが進む", "url": "https://example.com/tech-3", "published": "2026-10-07T08:30:00+09:00", "source": "TechCrunch"},
    {"title": "AIと教育の接点が広がり、学習支援の新潮流が注目", "url": "https://example.com/tech-4", "published": "2026-10-07T07:45:00+09:00", "source": "ナショナルジオグラフィック"}
  ],
  "音楽": [
    {"title": "新世代アーティストの注目作が続々登場、音楽市場が活況", "url": "https://example.com/music-1", "published": "2026-10-07T09:50:00+09:00", "source": "ナタリー"},
    {"title": "ライブイベントの再編や新規会場開業が音楽消費を後押し", "url": "https://example.com/music-2", "published": "2026-10-07T09:10:00+09:00", "source": "Rolling Stone Japan"},
    {"title": "J-POPの海外展開が進み、世界市場での評価が高まる", "url": "https://example.com/music-3", "published": "2026-10-07T08:20:00+09:00", "source": "音楽新聞"},
    {"title": "アーティストの自主制作が加速、作品の多様化が進む", "url": "https://example.com/music-4", "published": "2026-10-07T07:40:00+09:00", "source": "MUSICMAN"}
  ],
  "エンタメ": [
    {"title": "ドラマ・映画の新作が相次ぎ、配信市場が拡大中", "url": "https://example.com/ent-1", "published": "2026-10-07T09:15:00+09:00", "source": "映画.com"},
    {"title": "人気俳優の舞台公演が再開、観客動員が回復傾向", "url": "https://example.com/ent-2", "published": "2026-10-07T08:40:00+09:00", "source": "スポニチ"},
    {"title": "SNS発のクリエイターが注目を集める、文化の入口が広がる", "url": "https://example.com/ent-3", "published": "2026-10-07T08:00:00+09:00", "source": "デイリースポーツ"},
    {"title": "アニメ作品の海外展開が進み、ファン層が拡大", "url": "https://example.com/ent-4", "published": "2026-10-07T07:10:00+09:00", "source": "アニメイトタイムズ"}
  ],
  "スポーツ": [
    {"title": "国内リーグの新戦略が始動、観客動員と収益改善が課題", "url": "https://example.com/sports-1", "published": "2026-10-07T09:25:00+09:00", "source": "スポーツ紙"},
    {"title": "国際大会で注目選手が活躍、来季の育成計画が加速", "url": "https://example.com/sports-2", "published": "2026-10-07T08:50:00+09:00", "source": "サンケイスポーツ"},
    {"title": "女子スポーツの支援策が拡大、競技人口の増加に期待", "url": "https://example.com/sports-3", "published": "2026-10-07T08:05:00+09:00", "source": "日刊スポーツ"},
    {"title": "施設整備やデータ活用で競技力向上が進む", "url": "https://example.com/sports-4", "published": "2026-10-07T07:35:00+09:00", "source": "Yahoo!スポーツ"}
  ],
  "_meta": {"updated_at": "2026-10-07T00:00:00+09:00"}
}




































































































































































































































































































































































a















































































































































































































































dlc

























































n



































































































































































































































































































n
















n



















29
































































n



n
"},{"title": "経済政策の再検討が進み、成長戦略を模索", "url": "https://example.com/jp-policy-1", "published": "2026-10-07T10:05:00+09:00", "source": "毎日新聞"},




























































"source": "日本経済新聞"}




















































































































































n



n








































n



































n



n



















n

































n

























n



















n










































n









































n












































n








n



n













n












n



















n
























n



n












n










n








n














n



n












n







n












n













n







n












n











n













n

















































n



n


















\n"},{