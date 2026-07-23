import streamlit as st
import requests
import base64
import urllib.parse

st.set_page_config(page_title="carpe diem", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Playfair+Display:ital@0;1&display=swap');

* { font-family: 'DM Sans', sans-serif; }

/* hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 2rem !important; max-width: 560px !important; margin: 0 auto !important; }

/* ── rəngli fon ── */
.stApp {
    background: linear-gradient(160deg, #c8f0e0 0%, #e8f8f2 40%, #d4eee4 70%, #b8e8d4 100%) !important;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #a8dfc8 0%, #c8f0e0 100%) !important;
    min-width: 220px !important;
    max-width: 220px !important;
}
/* bağlama düyməsini gizlət */
button[data-testid="collapsedControl"],
button[kind="header"] { display: none !important; }
div[data-testid="stSidebarCollapseButton"] { display: none !important; }

/* ── palette ── */
:root {
    --tq:      #1D9E75;
    --tq-lt:   #E1F5EE;
    --tq-mid:  #5DCAA5;
    --tq-dk:   #0F6E56;
    --ink:     #1a1f1e;
    --muted:   #6b7875;
    --surface: #f6faf8;
    --border:  #d4ebe2;
}

/* ── top bar ── */
.topbar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 1.1rem 0 0.9rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
}
.topbar-logo {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.6rem;
    color: var(--tq);
    letter-spacing: -0.5px;
}
.topbar-tag {
    font-size: 0.72rem;
    color: var(--muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── section labels ── */
.section-label {
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    margin: 1.5rem 0 0.6rem;
    font-weight: 500;
}

/* ── post card ── */
.post-card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.6);
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 1rem;
}
.post-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.85rem 1rem 0.6rem;
}
.post-avatar {
    width: 34px; height: 34px; border-radius: 50%;
    background: var(--tq-lt);
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 0.78rem; font-weight: 500; color: var(--tq-dk);
    margin-right: 8px; flex-shrink: 0;
}
.post-name { font-size: 0.88rem; font-weight: 500; color: var(--ink); }
.post-date { font-size: 0.75rem; color: var(--muted); }
.post-caption {
    padding: 0.5rem 1rem 0.9rem;
    font-size: 0.88rem; color: var(--ink); line-height: 1.55;
}
.owner-badge {
    font-size: 0.68rem; color: var(--tq);
    border: 1px solid var(--tq-mid); border-radius: 20px;
    padding: 2px 8px;
}

/* ── login ── */
.login-hero {
    text-align: center; padding: 2.5rem 0 1.8rem;
}
.login-hero-logo {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 3rem; color: var(--tq);
    line-height: 1;
    margin-bottom: 0.4rem;
}
.login-hero-sub {
    font-size: 0.85rem; color: var(--muted);
    letter-spacing: 0.03em;
}

/* ── upload zone ── */
.upload-hint {
    background: var(--tq-lt);
    border: 1.5px dashed var(--tq-mid);
    border-radius: 14px;
    padding: 1.8rem 1rem;
    text-align: center;
    color: var(--tq-dk);
    font-size: 0.88rem;
    margin-bottom: 0.8rem;
}
.upload-hint strong { display: block; font-size: 1rem; margin-bottom: 4px; }

/* ── sidebar ── */
.sidebar-user {
    background: var(--tq-lt);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1rem;
    font-size: 0.85rem;
    color: var(--tq-dk);
}
.sidebar-user strong { display: block; font-size: 0.95rem; color: var(--tq-dk); }

/* ── primary button override ── */
div.stButton > button[kind="primary"] {
    background: var(--tq) !important;
    border: none !important; border-radius: 10px !important;
    color: white !important; font-weight: 500 !important;
    padding: 0.55rem 1.2rem !important;
}
div.stButton > button[kind="primary"]:hover {
    background: var(--tq-dk) !important;
}
div.stButton > button[kind="secondary"] {
    border: 1px solid var(--tq) !important; border-radius: 10px !important;
    color: var(--tq) !important; background: transparent !important;
    font-weight: 500 !important;
}
div.stButton > button[kind="secondary"]:hover {
    background: var(--tq-lt) !important;
}

/* ── text inputs ── */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    font-size: 0.9rem !important;
    background: rgba(255,255,255,0.8) !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: var(--tq) !important;
    box-shadow: 0 0 0 3px rgba(29,158,117,0.12) !important;
}

/* ── divider ── */
hr { border-color: var(--border) !important; margin: 0.5rem 0 !important; }

/* ── image radius ── */
div[data-testid="stImage"] img {
    border-radius: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────────────────────
if 'token' not in st.session_state:
    st.session_state.token = None
if 'user' not in st.session_state:
    st.session_state.user = None

BASE_URL = 'https://fastapi-project-66ph.onrender.com'


def get_headers():
    if st.session_state.token:
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}


def encode_text_for_overlay(text):
    if not text:
        return ""
    return urllib.parse.quote(base64.b64encode(text.encode('utf-8')).decode('utf-8'))


def create_transformed_url(original_url, transformation_params, caption=None):
    if caption:
        encoded_caption = encode_text_for_overlay(caption)
        transformation_params = f"l-text,ie-{encoded_caption},ly-N20,lx-20,fs-100,co-white,bg-000000A0,l-end"
    if not transformation_params:
        return original_url
    parts = original_url.split("/")
    base_url = "/".join(parts[:4])
    file_path = "/".join(parts[4:])
    return f"{base_url}/tr:{transformation_params}/{file_path}"


def initials(email):
    parts = email.split("@")[0].split(".")
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    return email[:2].upper()





# ══════════════════════════════════════════════════════════════════════════════
# LOGIN PAGE
# ══════════════════════════════════════════════════════════════════════════════
def login_page():
    st.markdown("""
    <div class="login-hero">
        <div class="login-hero-logo">carpe diem</div>
        <div class="login-hero-sub">anda qal</div>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input("E-poçt", placeholder="siz@mail.com", label_visibility="collapsed")
    password = st.text_input("Şifrə", type="password", placeholder="••••••••", label_visibility="collapsed")

    if email and password:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Daxil ol", type="primary", use_container_width=True):
                resp = requests.post(
                    f"{BASE_URL}/auth/jwt/login",
                    data={"username": email, "password": password}
                )
                if resp.status_code == 200:
                    st.session_state.token = resp.json()["access_token"]
                    me = requests.get(f"{BASE_URL}/users/me", headers=get_headers())
                    if me.status_code == 200:
                        st.session_state.user = me.json()
                        st.rerun()
                    else:
                        st.error("İstifadəçi məlumatı alınmadı.")
                else:
                    st.error("E-poçt və ya şifrə yanlışdır.")
        with col2:
            if st.button("Qeydiyyat", type="secondary", use_container_width=True):
                resp = requests.post(
                    f"{BASE_URL}/auth/register",
                    json={"email": email, "password": password}
                )
                if resp.status_code == 201:
                    st.success("Hesab yaradıldı! İndi daxil ol.")
                else:
                    detail = resp.json().get("detail", "Qeydiyyat uğursuz oldu.")
                    st.error(f"Xəta: {detail}")
    else:
        st.markdown("""
        <div style="text-align:center; color:#6b7875; font-size:0.82rem; padding:0.8rem 0;">
            Yuxarıda e-poçt və şifrəni daxil et
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FEED PAGE
# ══════════════════════════════════════════════════════════════════════════════
def feed_page():
    st.markdown('<div class="section-label">axın</div>', unsafe_allow_html=True)

    resp = requests.get(f"{BASE_URL}/feed", headers=get_headers())
    if resp.status_code != 200:
        st.error("Axın yüklənmədi.")
        return

    posts = resp.json().get("posts", [])
    if not posts:
        st.markdown("""
        <div style="text-align:center; padding:3rem 1rem; color:#6b7875;">
            <div style="font-size:2rem; margin-bottom:0.5rem;">🌿</div>
            Hələ heç bir an paylaşılmayıb.<br>
            <span style="font-size:0.82rem;">İlk sən ol!</span>
        </div>
        """, unsafe_allow_html=True)
        return

    for post in posts:
        ini = initials(post["email"])
        is_owner = post.get("is_owner", False)
        caption = post.get("caption", "")
        date_str = post["created_at"][:10]

        owner_badge = '<span class="owner-badge">sənin</span>' if is_owner else ""

        st.markdown(f"""
        <div class="post-card">
            <div class="post-meta">
                <div style="display:flex;align-items:center;">
                    <div class="post-avatar">{ini}</div>
                    <div>
                        <div class="post-name">{post['email'].split('@')[0]}</div>
                        <div class="post-date">{date_str}</div>
                    </div>
                </div>
                {owner_badge}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # media
        if post["file_type"] == "image":
            url = create_transformed_url(post["url"], "", caption)
            st.image(url, use_container_width=True)
        else:
            video_url = create_transformed_url(post["url"], "w-480,h-270,cm-pad_resize,bg-blurred")
            st.video(video_url)

        if caption:
            st.markdown(f"""
            <div class="post-caption">
                <strong>{post['email'].split('@')[0]}</strong> {caption}
            </div>
            """, unsafe_allow_html=True)

        if is_owner:
            if st.button("Sil", key=f"del_{post['id']}"):
                del_resp = requests.delete(
                    f"{BASE_URL}/posts/{post['id']}", headers=get_headers()
                )
                if del_resp.status_code == 200:
                    st.success("Post silindi.")
                    st.rerun()
                else:
                    st.error("Silinmədi.")

        st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# UPLOAD PAGE
# ══════════════════════════════════════════════════════════════════════════════
def upload_page():
    st.markdown('<div class="section-label">yeni an</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="upload-hint">
        <strong>📎 Şəkil və ya video seç</strong>
        PNG · JPG · MP4 · AVI · MOV · WEBM
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Fayl",
        type=["png", "jpg", "jpeg", "mp4", "avi", "mov", "mkv", "webm"],
        label_visibility="collapsed"
    )

    caption = st.text_area(
        "Başlıq",
        placeholder="Bu anda nə hiss edirsən?",
        max_chars=300,
        label_visibility="collapsed"
    )

    if uploaded:
        if st.button("Paylaş", type="primary", use_container_width=True):
            with st.spinner("Yüklənir..."):
                files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
                data = {"caption": caption}
                resp = requests.post(
                    f"{BASE_URL}/upload",
                    files=files, data=data,
                    headers=get_headers()
                )
                if resp.status_code == 200:
                    st.success("An paylaşıldı! 🌿")
                    st.rerun()
                else:
                    st.error("Yükləmə uğursuz oldu.")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.user is None:
    login_page()
else:
    user = st.session_state.user
    ini = initials(user["email"])

    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-user">
            <div style="font-size:1.5rem;margin-bottom:4px;">{ini}</div>
            <strong>{user['email'].split('@')[0]}</strong>
            <div style="font-size:0.75rem;opacity:0.7;">{user['email']}</div>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio(
            "Səhifə",
            ["🏠  Axın", "📎  Paylaş"],
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Çıxış", type="secondary", use_container_width=True):
            st.session_state.user = None
            st.session_state.token = None
            st.rerun()

    if page == "🏠  Axın":
        feed_page()
    else:
        upload_page()