import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-recommendation-project-1-u6sx.onrender.com"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="🎬 HopeMatch — Movie Recommender", page_icon="🎬", layout="wide")

# =============================
# PREMIUM STYLES
# =============================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

/* ===== GLOBAL ===== */
.stApp {
    background: linear-gradient(160deg, #0b0b1a 0%, #121228 40%, #1a1a3e 70%, #0f1629 100%);
    font-family: 'Inter', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header[data-testid="stHeader"] {
    background: rgba(11,11,26,0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255,255,255,0.04);
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

/* ===== HERO ===== */
.hero-container {
    text-align: center;
    padding: 30px 0 10px;
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #ff6b6b, #e94560, #c23616, #e94560, #ff6b6b);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient-flow 5s ease infinite;
    letter-spacing: -2px;
    margin-bottom: 0;
    line-height: 1.1;
}

@keyframes gradient-flow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-subtitle {
    color: #6b7b9e;
    font-size: 0.95rem;
    font-weight: 400;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 6px;
}

.hero-glow {
    width: 200px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #e94560, transparent);
    margin: 18px auto 10px;
    border-radius: 2px;
    animation: glow-pulse 2.5s ease-in-out infinite;
}

@keyframes glow-pulse {
    0%, 100% { opacity: 0.4; width: 120px; }
    50% { opacity: 1; width: 250px; }
}

/* ===== SECTION HEADERS ===== */
.section-header {
    font-family: 'Outfit', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #e0e6f0;
    margin: 35px 0 20px;
    padding-left: 16px;
    border-left: 4px solid #e94560;
    letter-spacing: -0.3px;
}

.section-header-icon {
    margin-right: 8px;
}

/* ===== MOVIE CARDS ===== */
.movie-card-wrapper {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    background: linear-gradient(160deg, rgba(25,25,50,0.95), rgba(15,15,35,0.98));
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    transition: all 0.45s cubic-bezier(0.23, 1, 0.32, 1);
    margin-bottom: 6px;
}

.movie-card-wrapper:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0 24px 48px rgba(233,69,96,0.18), 0 0 0 1px rgba(233,69,96,0.3);
    border-color: rgba(233,69,96,0.4);
}

.movie-card-wrapper img {
    width: 100%;
    aspect-ratio: 2/3;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.movie-card-wrapper:hover img {
    transform: scale(1.08);
}

.movie-card-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to top, rgba(10,10,26,0.97) 0%, rgba(10,10,26,0.7) 50%, transparent 100%);
    padding: 50px 14px 14px;
    transition: all 0.4s ease;
}

.movie-card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #f0f4ff;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-bottom: 4px;
}

.movie-card-year {
    font-size: 0.75rem;
    color: #7a8bb5;
    font-weight: 400;
}

.movie-card-rating {
    position: absolute;
    top: 12px;
    right: 12px;
    background: linear-gradient(135deg, #e94560, #c23616);
    color: white;
    padding: 4px 10px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 0.72rem;
    box-shadow: 0 4px 12px rgba(233,69,96,0.4);
    letter-spacing: 0.3px;
    z-index: 2;
}

/* ===== SEARCH INPUT ===== */
.stTextInput > div > div > input {
    background: rgba(20,20,45,0.85) !important;
    border: 2px solid rgba(233,69,96,0.15) !important;
    border-radius: 16px !important;
    color: #e6f1ff !important;
    font-size: 1.05rem !important;
    padding: 15px 22px !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.35s ease !important;
    backdrop-filter: blur(10px);
}

.stTextInput > div > div > input:focus {
    border-color: #e94560 !important;
    box-shadow: 0 0 25px rgba(233,69,96,0.12), 0 0 0 1px rgba(233,69,96,0.3) !important;
}

.stTextInput > div > div > input::placeholder {
    color: #4a5a80 !important;
}

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(135deg, #e94560, #c23616) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 8px 22px !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    transition: all 0.35s ease !important;
    letter-spacing: 0.3px !important;
    box-shadow: 0 4px 15px rgba(233,69,96,0.25) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 30px rgba(233,69,96,0.35) !important;
}

/* ===== SELECTBOX ===== */
.stSelectbox > div > div {
    background: rgba(20,20,45,0.85) !important;
    border-color: rgba(233,69,96,0.15) !important;
    border-radius: 12px !important;
    color: #e6f1ff !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d24 0%, #151535 100%);
    border-right: 1px solid rgba(233,69,96,0.08);
}

section[data-testid="stSidebar"] .stMarkdown h2 {
    color: #e0e6f0 !important;
    font-family: 'Outfit', sans-serif;
}

/* ===== DETAIL PAGE ===== */
.detail-card {
    background: linear-gradient(160deg, rgba(25,25,55,0.9), rgba(15,15,40,0.95));
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}

.detail-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #f0f4ff;
    letter-spacing: -0.5px;
    margin-bottom: 8px;
}

.detail-meta {
    color: #7a8bb5;
    font-size: 0.9rem;
    margin-bottom: 4px;
}

.detail-overview {
    color: #a0aecf;
    font-size: 0.95rem;
    line-height: 1.85;
    margin-top: 12px;
}

.genre-pill {
    display: inline-block;
    background: rgba(233,69,96,0.12);
    color: #e94560;
    padding: 5px 16px;
    border-radius: 25px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 3px 5px 3px 0;
    border: 1px solid rgba(233,69,96,0.25);
    transition: all 0.3s ease;
}

.genre-pill:hover {
    background: rgba(233,69,96,0.25);
    transform: translateY(-1px);
}

/* ===== DIVIDER ===== */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(233,69,96,0.25), rgba(99,102,241,0.15), transparent);
    margin: 35px 0;
    border: none;
}

/* ===== CATEGORY CHIPS ===== */
.category-chip-container {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
    margin: 15px 0 25px;
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,0.02); }
::-webkit-scrollbar-thumb { background: rgba(233,69,96,0.2); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(233,69,96,0.4); }

/* ===== LOADING ===== */
.stSpinner > div { color: #e94560 !important; }

/* ===== INFO/WARNING BOXES ===== */
.stAlert { border-radius: 12px !important; }

/* ===== BACKDROP IMAGE ===== */
.backdrop-img {
    width: 100%;
    max-height: 380px;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.5);
    margin-bottom: 24px;
}

/* ===== FOOTER ===== */
.app-footer {
    text-align: center;
    padding: 40px 0 20px;
    color: #3a4568;
    font-size: 0.8rem;
    letter-spacing: 1px;
}
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING (single-file pages)
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"  # home | details
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=30)
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


# =============================
# PREMIUM POSTER GRID
# =============================
def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")
            year = (m.get("release_date") or "")[:4]
            rating = m.get("vote_average")

            rating_html = ""
            if rating and float(rating) > 0:
                rating_html = f'<div class="movie-card-rating">⭐ {float(rating):.1f}</div>'

            with colset[c]:
                if poster:
                    st.markdown(f"""
                    <div class="movie-card-wrapper">
                        {rating_html}
                        <img src="{poster}" alt="{title}" loading="lazy"/>
                        <div class="movie-card-overlay">
                            <div class="movie-card-title" title="{title}">{title}</div>
                            <div class="movie-card-year">{year}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="movie-card-wrapper" style="aspect-ratio:2/3;display:flex;align-items:center;justify-content:center;background:rgba(20,20,45,0.9);">
                        <div style="text-align:center;color:#4a5a80;">
                            <div style="font-size:2rem;margin-bottom:8px;">🎬</div>
                            <div class="movie-card-title">{title}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                if st.button("🎬 Details", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}", use_container_width=True):
                    if tmdb_id:
                        goto_details(tmdb_id)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                    "vote_average": tmdb.get("vote_average"),
                    "release_date": tmdb.get("release_date"),
                }
            )
    return cards


# =============================
# Robust TMDB search parsing
# =============================
def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()

    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                    "vote_average": m.get("vote_average"),
                }
            )
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                    "vote_average": m.get("vote_average"),
                }
            )
    else:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [
        {
            "tmdb_id": x["tmdb_id"],
            "title": x["title"],
            "poster_url": x["poster_url"],
            "vote_average": x.get("vote_average"),
            "release_date": x.get("release_date"),
        }
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.markdown("## 🎬 HopeMatch")
    st.markdown('<div style="color:#5a6a8a;font-size:0.8rem;margin-bottom:20px;">AI Movie Recommender</div>', unsafe_allow_html=True)

    if st.button("🏠 Home", use_container_width=True):
        goto_home()

    st.markdown("---")
    st.markdown("### 📂 Category")
    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
        label_visibility="collapsed",
    )
    st.markdown("### 🔲 Grid")
    grid_cols = st.slider("Columns", 4, 8, 6, label_visibility="collapsed")

# =============================
# HERO HEADER
# =============================
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🎬 HopeMatch</div>
    <div class="hero-subtitle">AI-Powered Movie Recommendations</div>
    <div class="hero-glow"></div>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    # Search bar
    _, search_col, _ = st.columns([1, 3, 1])
    with search_col:
        typed = st.text_input(
            "Search movies",
            placeholder="🔍  Search any movie... Inception, Batman, Avengers...",
            label_visibility="collapsed",
        )

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)

    # SEARCH MODE
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters for suggestions.")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(
                    data, typed.strip(), limit=24
                )

                # Inline suggestion chips (instead of dropdown)
                if suggestions:
                    st.markdown("""
                    <div style="color:#7a8bb5;font-size:0.8rem;margin:8px 0 6px;font-weight:500;letter-spacing:0.5px;">
                        🎯 SUGGESTIONS — click to view details
                    </div>
                    """, unsafe_allow_html=True)

                    # Show suggestions as buttons in a row
                    chip_cols = st.columns(min(len(suggestions), 5))
                    for i, (label, sid) in enumerate(suggestions[:5]):
                        with chip_cols[i]:
                            if st.button(label, key=f"sug_{i}_{sid}", use_container_width=True):
                                goto_details(sid)

                    # Show remaining suggestions in next row if more than 5
                    if len(suggestions) > 5:
                        chip_cols2 = st.columns(min(len(suggestions) - 5, 5))
                        for i, (label, sid) in enumerate(suggestions[5:10]):
                            with chip_cols2[i]:
                                if st.button(label, key=f"sug2_{i}_{sid}", use_container_width=True):
                                    goto_details(sid)

                st.markdown('<div class="section-header">🔍 Search Results</div>', unsafe_allow_html=True)
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    # HOME FEED
    category_labels = {
        "trending": "🔥 Trending Now",
        "popular": "⭐ Popular",
        "top_rated": "🏆 Top Rated",
        "now_playing": "🎬 Now Playing",
        "upcoming": "🔮 Coming Soon",
    }
    label = category_labels.get(home_category, home_category)
    st.markdown(f'<div class="section-header">{label}</div>', unsafe_allow_html=True)

    with st.spinner(""):
        home_cards, err = api_get_json(
            "/home", params={"category": home_category, "limit": 24}
        )

    if err or not home_cards:
        st.error(f"Home feed failed: {err or 'Unknown error'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")

    # Footer
    st.markdown('<div class="app-footer">Powered by TMDB API & TF-IDF Engine • HopeMatch 2026 • Built by Asha Bakshi</div>', unsafe_allow_html=True)

# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    # Top bar
    col_a, col_b = st.columns([4, 1])
    with col_b:
        if st.button("← Back to Home", use_container_width=True):
            goto_home()

    # Fetch details
    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    # Backdrop
    if data.get("backdrop_url"):
        st.markdown(f'<img src="{data["backdrop_url"]}" class="backdrop-img" />', unsafe_allow_html=True)

    # Layout: Poster + Info
    left, right = st.columns([1, 2.5], gap="large")

    with left:
        if data.get("poster_url"):
            st.markdown(f"""
            <div style="border-radius:20px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,0.5);">
                <img src="{data['poster_url']}" style="width:100%;display:block;" />
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="aspect-ratio:2/3;background:rgba(20,20,45,0.9);border-radius:20px;display:flex;align-items:center;justify-content:center;">
                <span style="font-size:3rem;">🎬</span>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown(f'<div class="detail-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-title">{data.get("title", "")}</div>', unsafe_allow_html=True)

        release = data.get("release_date") or ""
        year = release[:4]
        if year:
            st.markdown(f'<div class="detail-meta">📅 {release}</div>', unsafe_allow_html=True)

        # Genre pills
        genres = data.get("genres", [])
        if genres:
            genre_html = "".join(
                f'<span class="genre-pill">{g["name"]}</span>' for g in genres
            )
            st.markdown(f'<div style="margin:12px 0;">{genre_html}</div>', unsafe_allow_html=True)

        # Overview
        overview = data.get("overview") or "No overview available."
        st.markdown(f'<div class="detail-overview">{overview}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Recommendations
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">✨ Recommendations</div>', unsafe_allow_html=True)

    title = (data.get("title") or "").strip()
    if title:
        with st.spinner("Finding similar movies..."):
            bundle, err2 = api_get_json(
                "/movie/search",
                params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
            )

        if not err2 and bundle:
            tfidf_cards = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            if tfidf_cards:
                st.markdown('<div class="section-header">🤖 AI Similar Movies (TF-IDF)</div>', unsafe_allow_html=True)
                poster_grid(tfidf_cards, cols=grid_cols, key_prefix="details_tfidf")

            genre_cards = bundle.get("genre_recommendations", [])
            if genre_cards:
                st.markdown('<div class="section-header">🎭 More Like This (Genre)</div>', unsafe_allow_html=True)
                poster_grid(genre_cards, cols=grid_cols, key_prefix="details_genre")
        else:
            st.info("Showing genre recommendations (fallback).")
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")

    # Footer
    st.markdown('<div class="app-footer">Powered by TMDB API & TF-IDF Engine • HopeMatch 2026 • Built by Asha Bakshi</div>', unsafe_allow_html=True)