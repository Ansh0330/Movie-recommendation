"""
style.py — Premium Dark Emerald CSS module
==========================================
All custom CSS for the Movie Recommendation System.
Imported by main.py and injected via st.markdown().

Design System:
  Background:        #090909
  Secondary BG:      #141414
  Cards:             #1B1F1D
  Primary Accent:    #0F5C4A  (Deep Emerald)
  Secondary Accent:  #157A63  (Forest Emerald)
  Luxury Highlight:  #D8C28F  (Champagne Gold)
  Primary Text:      #F7F7F7
  Secondary Text:    #B9B9B9
  Muted Text:        #8D8D8D
  Border:            rgba(215, 194, 143, 0.12)
"""


def get_css() -> str:
    """Return the complete CSS string for injection via st.markdown()."""
    return """
<style>

/* ============================================================
   DESIGN TOKENS
   ============================================================ */
:root {
    --bg:            #090909;
    --bg-secondary:  #141414;
    --bg-card:       #1B1F1D;
    --accent:        #0F5C4A;
    --accent-light:  #157A63;
    --gold:          #D8C28F;
    --gold-dim:      rgba(216, 194, 143, 0.35);
    --text-primary:  #F7F7F7;
    --text-secondary:#B9B9B9;
    --text-muted:    #8D8D8D;
    --border:        rgba(216, 194, 143, 0.10);
    --border-hover:  rgba(216, 194, 143, 0.28);
    --shadow:        0 4px 32px rgba(0, 0, 0, 0.55);
    --shadow-hover:  0 12px 48px rgba(0, 0, 0, 0.70);
    --radius:        14px;
    --radius-sm:     8px;
    --transition:    250ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
}


/* ============================================================
   GLOBAL RESETS & BASE
   ============================================================ */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background-color: var(--bg) !important;
}

/* Import Google Font — Inter */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap');

body, .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-primary) !important;
    background-color: var(--bg) !important;
}

/* Make Streamlit header transparent — do NOT zero its height
   because it hosts the sidebar expand/collapse toggle button */
[data-testid="stHeader"] {
    background: transparent !important;
    border-bottom: none !important;
}

/* Hide only the hamburger menu and footer — NOT the header itself */
#MainMenu, footer {
    visibility: hidden !important;
    height: 0 !important;
}

/* Always keep the sidebar collapse/expand button visible */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999 !important;
}

/* Remove top-padding Streamlit adds by default */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 4rem !important;
    max-width: 1280px !important;
}


/* ============================================================
   CUSTOM SCROLLBAR
   ============================================================ */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: var(--bg-secondary);
}
::-webkit-scrollbar-thumb {
    background: var(--accent);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--accent-light);
}


/* ============================================================
   SIDEBAR
   ============================================================ */
/* Remove Streamlit's stacked top padding — brings logo flush to top */
[data-testid="stSidebar"] {
    background-color: var(--bg-secondary) !important;
    border-right: 1px solid var(--border) !important;
    padding-top: 0 !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 0.5rem 1.25rem 1.5rem !important;
}

/* Streamlit's inner scrollable content wrapper */
[data-testid="stSidebarContent"],
section[data-testid="stSidebar"] > div > div {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

/* Sidebar logo area */
.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.5rem;
}
.sidebar-logo-icon {
    font-size: 1.5rem;
    line-height: 1;
}
.sidebar-logo-text {
    font-family: 'Playfair Display', serif;
    font-size: 0.95rem;
    font-weight: 500;
    color: var(--gold);
    letter-spacing: 0.02em;
    line-height: 1.3;
}
.sidebar-logo-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.68rem;
    font-weight: 400;
    color: var(--text-muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* Sidebar section headings */
.sidebar-section-title {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.6rem;
    margin-top: 1.5rem;
}

/* Sidebar body text */
.sidebar-body {
    font-size: 0.78rem;
    color: var(--text-secondary);
    line-height: 1.65;
}

/* Tech pills in sidebar */
.tech-pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    background: rgba(15, 92, 74, 0.20);
    border: 1px solid rgba(21, 122, 99, 0.30);
    color: var(--accent-light);
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    margin: 3px 2px;
}

/* GitHub button */
.github-btn {
    display: block;
    text-align: center;
    padding: 9px 16px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-hover);
    background: transparent;
    color: var(--gold) !important;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-decoration: none !important;
    transition: background var(--transition), border-color var(--transition);
    margin-top: 1rem;
}
.github-btn:hover {
    background: rgba(216, 194, 143, 0.08);
    border-color: var(--gold);
    text-decoration: none !important;
}

/* Sidebar divider */
.sidebar-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.25rem 0;
}

/* Sidebar dataset info */
.sidebar-dataset {
    font-size: 0.70rem;
    color: var(--text-muted);
    line-height: 1.6;
    padding: 0.75rem;
    border-radius: var(--radius-sm);
    background: rgba(255,255,255,0.02);
    border: 1px solid var(--border);
}


/* ============================================================
   HERO SECTION
   ============================================================ */
.hero {
    text-align: center !important;
    padding: 1.25rem 2rem 1.5rem;
    position: relative;
    width: 100%;
}

/* Streamlit markdown container wrapping the hero — force full width + center */
[data-testid="stMarkdownContainer"]:has(.hero) {
    width: 100% !important;
    text-align: center !important;
}


.hero-eyebrow {
    font-size: 0.70rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 1.1rem;
    opacity: 0.9;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 500;
    color: var(--text-primary);
    letter-spacing: -0.01em;
    line-height: 1.12;
    margin-bottom: 1.25rem;
}

.hero-title span {
    color: var(--gold);
}

.hero-subtitle {
    font-size: clamp(0.88rem, 1.5vw, 1.0rem);
    font-weight: 400;
    color: var(--text-secondary);
    line-height: 1.8;
    max-width: 580px;
    margin: 0 auto 2.5rem !important;
    text-align: center !important;
    display: block;
}

/* Thin gold rule */
.hero-rule {
    width: 48px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 0 auto;
    opacity: 0.7;
}

/* Force Streamlit's markdown wrapper to not interfere with hero centering */
.hero p,
.hero div,
.hero h1,
.hero span {
    text-align: center !important;
}

/* Streamlit wraps st.markdown output in stMarkdown — override that too */
[data-testid="stMarkdownContainer"] .hero,
[data-testid="stMarkdownContainer"] .hero * {
    text-align: center !important;
}

/* Also center the stMarkdownContainer itself when it's inside the hero flow */
[data-testid="stMarkdownContainer"]:has(.hero) {
    text-align: center !important;
}


/* ============================================================
   SELECTOR CARD
   ============================================================ */
.selector-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2.25rem 2.5rem;
    max-width: 680px;
    margin: 2rem auto;
    box-shadow: var(--shadow);
    transition: border-color var(--transition);
}
.selector-card:hover {
    border-color: var(--border-hover);
}
.selector-card-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
    display: block;
}
.selector-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
}
.selector-card-desc {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
    line-height: 1.6;
}


/* ============================================================
   STREAMLIT SELECTBOX OVERRIDE
   ============================================================ */
[data-testid="stSelectbox"] > div > div {
    background-color: var(--bg-secondary) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-primary) !important;
    font-size: 0.9rem !important;
    padding: 0.2rem 0.4rem !important;
    transition: border-color var(--transition) !important;
}
[data-testid="stSelectbox"] > div > div:focus-within,
[data-testid="stSelectbox"] > div > div:hover {
    border-color: var(--accent-light) !important;
    box-shadow: 0 0 0 1px var(--accent) !important;
}
/* Dropdown option list */
[data-baseweb="popover"] {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
}
[role="option"]:hover {
    background-color: rgba(21, 122, 99, 0.15) !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */
/* Primary recommend button */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%) !important;
    color: #F7F7F7 !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.65rem 2.2rem !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.10em !important;
    text-transform: uppercase !important;
    transition: transform var(--transition), box-shadow var(--transition), opacity var(--transition) !important;
    box-shadow: 0 4px 20px rgba(15, 92, 74, 0.35) !important;
    width: 100% !important;
    margin-top: 1rem !important;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) scale(1.01) !important;
    box-shadow: 0 8px 32px rgba(15, 92, 74, 0.55) !important;
    opacity: 0.95 !important;
}
[data-testid="stButton"] > button:active {
    transform: translateY(0px) scale(0.99) !important;
}


/* ============================================================
   SPINNER OVERRIDE
   ============================================================ */
[data-testid="stSpinner"] > div {
    color: var(--text-muted) !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.06em !important;
}
[data-testid="stSpinner"] svg {
    stroke: var(--accent-light) !important;
    color: var(--accent-light) !important;
}


/* ============================================================
   RECOMMENDATIONS HEADER
   ============================================================ */
.reco-header {
    text-align: center;
    padding: 2.5rem 0 2rem;
}
.reco-eyebrow {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.6rem;
}
.reco-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3vw, 2.1rem);
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}
.reco-subtitle {
    font-size: 0.8rem;
    color: var(--text-muted);
}


/* ============================================================
   MOVIE CARD
   ============================================================ */
.movie-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    transition:
        transform var(--transition),
        border-color var(--transition),
        box-shadow var(--transition);
    box-shadow: var(--shadow);
    height: 100%;
    display: flex;
    flex-direction: column;
    animation: fadeInUp 0.4s ease both;
}
.movie-card:hover {
    transform: translateY(-6px);
    border-color: var(--border-hover);
    box-shadow: var(--shadow-hover);
}

/* Staggered animation delays */
.movie-card:nth-child(1) { animation-delay: 0.05s; }
.movie-card:nth-child(2) { animation-delay: 0.10s; }
.movie-card:nth-child(3) { animation-delay: 0.15s; }
.movie-card:nth-child(4) { animation-delay: 0.20s; }
.movie-card:nth-child(5) { animation-delay: 0.25s; }

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(16px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Poster wrapper */
.card-poster-wrap {
    overflow: hidden;
    position: relative;
    aspect-ratio: 2/3;
    background: var(--bg-secondary);
}
.card-poster-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 350ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
.movie-card:hover .card-poster-wrap img {
    transform: scale(1.05);
}

/* Card body */
.card-body {
    padding: 1rem 0.9rem 1.1rem;
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    flex: 1;
}

/* Title */
.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 0.92rem;
    font-weight: 500;
    color: var(--text-primary);
    line-height: 1.3;
    letter-spacing: 0.005em;
}

/* Rating badge */
.rating-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(216, 194, 143, 0.12);
    border: 1px solid rgba(216, 194, 143, 0.25);
    border-radius: 5px;
    padding: 2px 8px;
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--gold);
    letter-spacing: 0.04em;
    width: fit-content;
}
.rating-badge .star-icon {
    font-size: 0.65rem;
    opacity: 0.9;
}

/* Meta row: year + runtime */
.meta-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}
.meta-item {
    font-size: 0.70rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 3px;
}
.meta-dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: var(--text-muted);
    opacity: 0.5;
}

/* Genre pills */
.genre-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    margin-top: 0.1rem;
}
.genre-pill {
    padding: 2px 9px;
    border-radius: 20px;
    background: rgba(15, 92, 74, 0.18);
    border: 1px solid rgba(21, 122, 99, 0.25);
    color: rgba(21, 122, 99, 0.95);
    font-size: 0.63rem;
    font-weight: 500;
    letter-spacing: 0.04em;
    white-space: nowrap;
}

/* Plot */
.card-plot {
    font-size: 0.75rem;
    color: var(--text-secondary);
    line-height: 1.7;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-top: 0.1rem;
    flex: 1;
}

/* Divider inside card */
.card-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 0.2rem 0;
}


/* ============================================================
   EXPANDER (Read More)
   ============================================================ */
[data-testid="stExpander"] {
    border: none !important;
    background: transparent !important;
    padding: 0 !important;
}
[data-testid="stExpander"] summary {
    font-size: 0.70rem !important;
    color: var(--accent-light) !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    padding: 0 !important;
    padding-left: 0.9rem !important;
    cursor: pointer !important;
    transition: color var(--transition) !important;
}
[data-testid="stExpander"] summary:hover {
    color: var(--gold) !important;
}
[data-testid="stExpander"] > details > div {
    padding: 0.5rem 0.9rem 0.6rem !important;
    font-size: 0.73rem !important;
    color: var(--text-secondary) !important;
    line-height: 1.65 !important;
}


/* ============================================================
   COLUMNS SPACING
   ============================================================ */
/* Reduce gap between st.columns */
[data-testid="stHorizontalBlock"] {
    gap: 1.1rem !important;
    align-items: stretch !important;
}


/* ============================================================
   ERROR / INFO STATES
   ============================================================ */
.empty-state {
    text-align: center;
    padding: 3rem 2rem;
    color: var(--text-muted);
}
.empty-state-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    opacity: 0.4;
}
.empty-state-text {
    font-size: 0.85rem;
    line-height: 1.6;
}


/* ============================================================
   SECTION DIVIDER
   ============================================================ */
.section-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 2rem auto;
    max-width: 900px;
}


/* ============================================================
   FOOTER
   ============================================================ */
.app-footer {
    text-align: center;
    padding: 3rem 1rem 1.5rem;
    color: var(--text-muted);
    font-size: 0.70rem;
    letter-spacing: 0.08em;
}
.app-footer a {
    color: var(--accent-light);
    text-decoration: none;
}
.app-footer a:hover {
    color: var(--gold);
}


/* ============================================================
   RESPONSIVE GRID HELPERS
   ============================================================ */
/* On tablet — columns auto-stack (Streamlit handles this natively) */
@media (max-width: 900px) {
    .hero { padding: 3rem 1rem 2rem; }
    .selector-card { padding: 1.5rem 1.25rem; }
    .card-body { padding: 0.75rem 0.7rem 0.9rem; }
}
@media (max-width: 600px) {
    .hero-title { font-size: 1.8rem; }
    .selector-card { margin: 1rem; padding: 1.25rem 1rem; }
}


/* ============================================================
   HIDE STREAMLIT BRANDING / CHROME
   ============================================================ */
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

/* Suppress default st.title / st.header styling */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 500 !important;
    color: var(--text-primary) !important;
}

</style>
"""


def get_sidebar_html() -> str:
    """Return sidebar content HTML."""
    return """
<div class="sidebar-logo">
    <span class="sidebar-logo-icon">🎬</span>
    <div>
        <div class="sidebar-logo-text">CineMatch</div>
        <div class="sidebar-logo-sub">Film Discovery Engine</div>
    </div>
</div>

<div class="sidebar-section-title">About this Project</div>
<div class="sidebar-body">
    A content-based movie recommendation engine that analyses film metadata
    using Natural Language Processing to surface films you'll love.
</div>

<hr class="sidebar-divider">

<div class="sidebar-section-title">Recommendation Algorithm</div>
<div class="sidebar-body">
    Vectorises movie metadata (overview, genres, cast, keywords) using
    <strong style="color:#D8C28F;">TF-IDF</strong> and computes
    <strong style="color:#D8C28F;">Cosine Similarity</strong> scores to rank
    recommendations from a corpus of 45,000+ films.
</div>

<hr class="sidebar-divider">

<div class="sidebar-section-title">Built With</div>
<div>
    <span class="tech-pill">Python</span>
    <span class="tech-pill">Streamlit</span>
    <span class="tech-pill">Scikit-Learn</span>
    <span class="tech-pill">TF-IDF</span>
    <span class="tech-pill">Pandas</span>
    <span class="tech-pill">OMDb API</span>
    <span class="tech-pill">NumPy</span>
</div>

<a href="https://github.com/Ansh0330/Movie-recommendation"
   target="_blank"
   class="github-btn">
    ⭐ &nbsp; View on GitHub
</a>

<hr class="sidebar-divider">

<div class="sidebar-section-title">Dataset</div>
<div class="sidebar-dataset">
    <strong style="color:#B9B9B9;">TMDB 5000 Movies</strong><br>
    45,466 films · metadata + credits<br>
    Source: The Movie Database (TMDB)<br>
    Enriched via OMDb API
</div>
"""


def render_movie_card_html(movie: dict) -> str:
    """
    Build the HTML for a single movie card.

    Args:
        movie: dict with keys title, year, poster, rating, runtime, genre, plot

    Returns:
        Stripped HTML string for the card — no leading whitespace so
        st.markdown() never interprets it as a markdown code block.
    """
    title   = movie.get("title", "Unknown")
    year    = movie.get("year", "N/A")
    poster  = movie.get("poster", "")
    rating  = movie.get("rating", "N/A")
    runtime = movie.get("runtime", "N/A")
    genre   = movie.get("genre", "Unknown")
    plot    = movie.get("plot", "No description available.")

    # Build genre pills (max 3)
    genres = [g.strip() for g in genre.split(",") if g.strip() and genre != "Unknown"]
    genre_pills_html = "".join(
        f'<span class="genre-pill">{g}</span>' for g in genres[:3]
    )
    if not genre_pills_html:
        genre_pills_html = '<span class="genre-pill">Film</span>'

    # Poster — only use remote URLs; local paths show emoji placeholder
    poster_src = poster if poster and poster.startswith("http") else ""
    if not poster_src:
        poster_block = '<div class="card-poster-wrap" style="display:flex;align-items:center;justify-content:center;"><span style="font-size:2.5rem;opacity:0.2;">🎬</span></div>'
    else:
        poster_block = f'<div class="card-poster-wrap"><img src="{poster_src}" alt="poster" loading="lazy" /></div>'

    # Escape user-controlled strings for HTML safety
    safe_title = title.replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
    safe_plot  = plot.replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
    rating_val = rating if rating != 'N/A' else '&mdash;'

    # Build card — NO leading whitespace so markdown won't treat it as a code block
    card_html = (
        f'<div class="movie-card">'
        f'{poster_block}'
        f'<div class="card-body">'
        f'<div class="card-title">{safe_title}</div>'
        f'<div class="rating-badge"><span class="star-icon">★</span> {rating_val}&nbsp;IMDb</div>'
        f'<div class="meta-row">'
        f'<span class="meta-item">📅 {year}</span>'
        f'<span class="meta-dot"></span>'
        f'<span class="meta-item">⏱ {runtime}</span>'
        f'</div>'
        f'<div class="genre-pills">{genre_pills_html}</div>'
        f'<hr class="card-divider">'
        f'<p class="card-plot">{safe_plot}</p>'
        f'</div>'
        f'</div>'
    )
    return card_html
