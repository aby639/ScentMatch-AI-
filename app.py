import os
import asyncio
from typing import List, Dict, Any, Optional

import streamlit as st
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool

# =========================
# 0. API KEY CHECK
# =========================

if "GOOGLE_API_KEY" not in os.environ or not os.environ["GOOGLE_API_KEY"]:
    st.error("❌ GOOGLE_API_KEY environment variable is not set.")
    st.stop()

# =========================
# 1. PERFUME CATALOG
# =========================

Perfume = Dict[str, Any]

PERFUMES: List[Perfume] = [
    {
        "name": "Creed Aventus",
        "brand": "Creed",
        "gender": "masculine",
        "season": ["spring", "summer", "autumn"],
        "occasion": ["date", "party", "special"],
        "vibe": ["fruity", "smoky", "boss", "attention-grabbing"],
        "strength": "eau de parfum",
        "longevity": "8-10h",
        "projection": "strong",
        "price_level": "luxury",
        "price_estimate_usd": 350,
        "link": "https://www.creedboutique.com/products/aventus",
    },
    {
        "name": "Armaf Club de Nuit Intense Man",
        "brand": "Armaf",
        "gender": "masculine",
        "season": ["spring", "autumn", "winter"],
        "occasion": ["party", "night out"],
        "vibe": ["fruity", "smoky", "beast-mode", "aventus-style"],
        "strength": "eau de toilette",
        "longevity": "7-9h",
        "projection": "strong",
        "price_level": "budget",
        "price_estimate_usd": 45,
        "link": "https://www.armafperfume.com/",
    },
    {
        "name": "Dior Sauvage EDT",
        "brand": "Dior",
        "gender": "masculine",
        "season": ["all"],
        "occasion": ["daily", "date", "office"],
        "vibe": ["fresh", "clean", "mass-appeal", "blue"],
        "strength": "eau de toilette",
        "longevity": "6-8h",
        "projection": "moderate-strong",
        "price_level": "designer",
        "price_estimate_usd": 120,
        "link": "https://www.dior.com/",
    },
    {
        "name": "Nautica Voyage",
        "brand": "Nautica",
        "gender": "masculine",
        "season": ["spring", "summer"],
        "occasion": ["daily", "casual"],
        "vibe": ["fresh", "aquatic", "soapy", "cheap-gem"],
        "strength": "eau de toilette",
        "longevity": "4-6h",
        "projection": "moderate",
        "price_level": "budget",
        "price_estimate_usd": 25,
        "link": "https://www.nautica.com/",
    },
    {
        "name": "Jean Paul Gaultier Le Male Le Parfum",
        "brand": "Jean Paul Gaultier",
        "gender": "masculine",
        "season": ["autumn", "winter"],
        "occasion": ["date", "party", "club"],
        "vibe": ["sweet", "vanilla", "sexy", "warm"],
        "strength": "eau de parfum",
        "longevity": "8-10h",
        "projection": "strong",
        "price_level": "designer",
        "price_estimate_usd": 120,
        "link": "https://www.jeanpaulgaultier.com/",
    },
    {
        "name": "Bleu de Chanel EDT",
        "brand": "Chanel",
        "gender": "masculine",
        "season": ["all"],
        "occasion": ["office", "daily", "date"],
        "vibe": ["fresh", "blue", "clean", "mass-appeal"],
        "strength": "eau de toilette",
        "longevity": "6-8h",
        "projection": "moderate",
        "price_level": "designer",
        "price_estimate_usd": 150,
        "link": "https://www.chanel.com/",
    },
    {
        "name": "Prada Luna Rossa Carbon",
        "brand": "Prada",
        "gender": "masculine",
        "season": ["all"],
        "occasion": ["daily", "office", "gym"],
        "vibe": ["fresh", "clean", "metallic", "modern"],
        "strength": "eau de toilette",
        "longevity": "6-7h",
        "projection": "moderate",
        "price_level": "designer",
        "price_estimate_usd": 110,
        "link": "https://www.prada.com/",
    },
    {
        "name": "Versace Dylan Blue",
        "brand": "Versace",
        "gender": "masculine",
        "season": ["all"],
        "occasion": ["daily", "party"],
        "vibe": ["fresh", "blue", "sexy", "clean"],
        "strength": "eau de toilette",
        "longevity": "6-8h",
        "projection": "moderate",
        "price_level": "designer",
        "price_estimate_usd": 95,
        "link": "https://www.versace.com/",
    },
    {
        "name": "Burberry Hero EDT",
        "brand": "Burberry",
        "gender": "masculine",
        "season": ["spring", "summer"],
        "occasion": ["daily", "casual"],
        "vibe": ["fresh", "woody", "light", "clean"],
        "strength": "eau de toilette",
        "longevity": "4-6h",
        "projection": "moderate",
        "price_level": "designer",
        "price_estimate_usd": 90,
        "link": "https://us.burberry.com/",
    },
    {
        "name": "Lattafa Asad",
        "brand": "Lattafa",
        "gender": "masculine",
        "season": ["autumn", "winter"],
        "occasion": ["date", "party"],
        "vibe": ["vanilla", "spicy", "warm", "sexy"],
        "strength": "eau de parfum",
        "longevity": "8-12h",
        "projection": "strong",
        "price_level": "budget",
        "price_estimate_usd": 25,
        "link": "https://www.lattafa.com/",
    },
    {
        "name": "Lattafa Yara",
        "brand": "Lattafa",
        "gender": "feminine",
        "season": ["all"],
        "occasion": ["daily", "date"],
        "vibe": ["sweet", "vanilla", "fruity", "creamy"],
        "strength": "eau de parfum",
        "longevity": "6-10h",
        "projection": "moderate-strong",
        "price_level": "budget",
        "price_estimate_usd": 30,
        "link": "https://www.lattafa.com/",
    },
    {
        "name": "Carolina Herrera Bad Boy",
        "brand": "Carolina Herrera",
        "gender": "masculine",
        "season": ["autumn", "winter"],
        "occasion": ["party", "date"],
        "vibe": ["sweet", "sexy", "warm", "amber"],
        "strength": "eau de toilette",
        "longevity": "7-9h",
        "projection": "moderate-strong",
        "price_level": "designer",
        "price_estimate_usd": 110,
        "link": "https://www.carolinaherrera.com/",
    },
    {
        "name": "Mont Blanc Explorer",
        "brand": "Mont Blanc",
        "gender": "masculine",
        "season": ["all"],
        "occasion": ["daily", "office", "casual"],
        "vibe": ["fresh", "fruity", "aventus-style"],
        "strength": "eau de parfum",
        "longevity": "6-8h",
        "projection": "moderate",
        "price_level": "designer",
        "price_estimate_usd": 85,
        "link": "https://www.montblanc.com/",
    },
    {
        "name": "Jean Paul Gaultier Le Male Elixir Absolu",
        "brand": "Jean Paul Gaultier",
        "gender": "masculine",
        "season": ["autumn", "winter", "night"],
        "occasion": ["date", "night-out", "party", "club"],
        "vibe": ["sweet", "spicy", "vanilla", "warm", "sexy"],
        "strength": "eau de parfum",
        "longevity": "9-11h",
        "projection": "strong-beast",
        "price_level": "designer",
        "price_estimate_usd": 130,
        "link": "https://www.jeanpaulgaultier.com",
    },
    {
        "name": "Mancera Cedrat Boise",
        "brand": "Mancera",
        "gender": "masculine",
        "season": ["all"],
        "occasion": ["daily", "office", "casual", "date"],
        "vibe": ["fresh", "citrus", "woody", "versatile"],
        "strength": "eau de parfum",
        "longevity": "8-9h",
        "projection": "moderate-strong",
        "price_level": "high",
        "price_estimate_usd": 195,
        "link": "https://www.mancera-paris.com",
    },
]

# =========================
# 2. METRICS
# =========================

AGENT_METRICS = {
    "tool_calls": {
        "recommend_perfumes": 0,
        "find_alternative": 0,
        "get_usage_tips": 0,
        "describe_perfume": 0,
    },
    "fallback_count": 0,
    "error_count": 0,
}

# =========================
# 3. HELPERS
# =========================

def _normalize(s: Optional[str]) -> str:
    return s.strip().lower() if isinstance(s, str) else ""


def _matches_pref(value: Optional[str], options: Optional[list[str]]) -> bool:
    """
    Check if a preference fits a list.
    - Accepts comma-, slash-, or space-separated input ("fresh, clean long lasting")
    - Case-insensitive and partial matching.
    """
    if not value:
        return True
    if not options:
        return True

    value = _normalize(value)
    raw = value.replace("/", " ").replace(",", " ")
    tokens = [t.strip() for t in raw.split() if t.strip()]
    options_norm = [_normalize(o) for o in options]
    return any(tok in opt for tok in tokens for opt in options_norm)


def _price_level_key(level: str) -> int:
    """
    Simple ranking for price_level. Lower = cheaper.
    """
    order = {
        "budget": 0,
        "designer": 1,
        "high": 2,
        "niche": 3,
        "luxury": 4,
    }
    return order.get(_normalize(level), 2)

# =========================
# 4. TOOLS
# =========================


def recommend_perfumes(
    gender: Optional[str] = None,
    occasion: Optional[str] = None,
    season: Optional[str] = None,
    vibe: Optional[str] = None,
    budget_level: Optional[str] = None,
) -> dict:
    """
    Recommend perfumes based on user preferences.
    """
    AGENT_METRICS["tool_calls"]["recommend_perfumes"] += 1

    try:
        g = _normalize(gender)
        b = _normalize(budget_level)

        matches: List[Perfume] = []
        for p in PERFUMES:
            # gender check (allow "all" or "unisex")
            if g:
                pg = _normalize(p.get("gender", ""))
                if pg not in ("all", "unisex"):
                    if g not in pg:
                        continue

            # season / occasion / vibe checks
            if season and not _matches_pref(season, p.get("season")):
                continue
            if occasion and not _matches_pref(occasion, p.get("occasion")):
                continue
            if vibe and not _matches_pref(vibe, p.get("vibe")):
                continue

            # budget check (soft): keep perfumes <= requested level
            if b:
                if _price_level_key(p.get("price_level", "")) > _price_level_key(b):
                    continue

            matches.append(p)

        if not matches:
            AGENT_METRICS["fallback_count"] += 1
            fallback = sorted(
                PERFUMES,
                key=lambda x: x.get("price_estimate_usd", 9999),
            )[:5]
            return {
                "status": "fallback",
                "note": (
                    "I couldn't find a perfect match, so here are some popular "
                    "everyday options instead."
                ),
                "data": fallback,
            }

        projection_rank = {
            "soft": 0,
            "moderate": 1,
            "moderate-strong": 2,
            "strong": 3,
            "strong-beast": 4,
        }

        matches_sorted = sorted(
            matches,
            key=lambda x: (
                x.get("price_estimate_usd", 9999),
                -projection_rank.get(_normalize(x.get("projection", "")), 1),
            ),
        )

        return {"status": "success", "data": matches_sorted[:5]}
    except Exception as e:
        AGENT_METRICS["error_count"] += 1
        return {"status": "error", "error_message": str(e)}


def find_alternative(
    reference_name: str,
    max_price_level: Optional[str] = None,
) -> dict:
    """
    Find cheaper / similar alternatives for a reference perfume.
    """
    AGENT_METRICS["tool_calls"]["find_alternative"] += 1

    try:
        ref_name_norm = _normalize(reference_name)
        max_level_norm = _normalize(max_price_level)

        ref = None
        for p in PERFUMES:
            if ref_name_norm in _normalize(p["name"]):
                ref = p
                break

        if not ref:
            AGENT_METRICS["fallback_count"] += 1
            fallback = sorted(
                PERFUMES,
                key=lambda x: x.get("price_estimate_usd", 9999),
            )[:3]
            return {
                "status": "fallback",
                "error_message": (
                    "That exact perfume is not in my small catalog. "
                    "Here are some popular, affordable options instead."
                ),
                "reference_name": reference_name,
                "data": fallback,
            }

        ref_vibes = set(_normalize(v) for v in ref.get("vibe", []))

        candidates = []
        for p in PERFUMES:
            if p["name"] == ref["name"]:
                continue

            overlap = ref_vibes.intersection(
                _normalize(v) for v in p.get("vibe", [])
            )
            if not overlap:
                continue

            if p.get("price_estimate_usd", 9999) >= ref.get(
                "price_estimate_usd", 9999
            ):
                continue

            if max_level_norm:
                if _price_level_key(p.get("price_level", "")) > _price_level_key(
                    max_level_norm
                ):
                    continue

            saving = ref.get("price_estimate_usd", 0) - p.get(
                "price_estimate_usd", 0
            )
            candidates.append((len(overlap), saving, p))

        if not candidates:
            return {
                "status": "no_results",
                "reference": ref,
                "error_message": "No cheaper alternatives found in this tiny demo list.",
            }

        candidates_sorted = [
            c[-1] for c in sorted(candidates, key=lambda x: (-x[0], -x[1]))
        ]

        return {
            "status": "success",
            "reference": ref,
            "data": candidates_sorted[:3],
        }

    except Exception as e:
        AGENT_METRICS["error_count"] += 1
        return {"status": "error", "error_message": str(e)}


def get_usage_tips(
    perfume_name: str,
    sprays_per_day: Optional[int] = None,
    climate: Optional[str] = None,
) -> dict:
    """
    Give practical usage tips for a perfume.
    """
    AGENT_METRICS["tool_calls"]["get_usage_tips"] += 1

    try:
        search_name = _normalize(perfume_name)

        p = None
        for item in PERFUMES:
            if search_name in _normalize(item["name"]):
                p = item
                break

        if not p:
            AGENT_METRICS["fallback_count"] += 1
            return {
                "status": "no_results",
                "error_message": (
                    "That perfume is not in my small catalog yet. "
                    "Try another one or ask for a recommendation first."
                ),
            }

        projection = _normalize(p.get("projection", "moderate"))
        if projection in ["strong", "strong-beast", "moderate-strong"]:
            default_sprays = 4
        elif projection == "soft":
            default_sprays = 6
        else:
            default_sprays = 5

        climate_norm = _normalize(climate)
        if "hot" in climate_norm:
            recommended_sprays = max(2, default_sprays - 2)
        elif "cold" in climate_norm:
            recommended_sprays = default_sprays + 1
        else:
            recommended_sprays = default_sprays

        if sprays_per_day is None:
            sprays_per_day = recommended_sprays

        estimated_days = round(1000 / max(1, sprays_per_day))

        tips = {
            "perfume": p["name"],
            "brand": p["brand"],
            "recommended_sprays": recommended_sprays,
            "user_sprays": sprays_per_day,
            "projection": p["projection"],
            "longevity": p["longevity"],
            "estimated_days_for_100ml": estimated_days,
            "note": (
                "These are rough community-style estimates based on projection and climate, "
                "not exact lab measurements."
            ),
        }

        return {"status": "success", "data": tips}

    except Exception as e:
        AGENT_METRICS["error_count"] += 1
        return {"status": "error", "error_message": str(e)}


def describe_perfume(name: str) -> dict:
    """
    Return a catalog-backed description of a perfume:
    - basic profile (brand, vibe, season, occasion)
    - when to wear it
    - rough price band
    """
    AGENT_METRICS["tool_calls"]["describe_perfume"] += 1

    try:
        search = _normalize(name)
        match = None
        for p in PERFUMES:
            if search in _normalize(p["name"]):
                match = p
                break

        if not match:
            AGENT_METRICS["fallback_count"] += 1
            return {
                "status": "no_results",
                "error_message": (
                    "That perfume is not in my small catalog yet. "
                    "Try another one from the list or ask for a recommendation."
                ),
            }

        data = {
            "name": match["name"],
            "brand": match["brand"],
            "vibe": match.get("vibe", []),
            "season": match.get("season", []),
            "occasion": match.get("occasion", []),
            "strength": match.get("strength"),
            "projection": match.get("projection"),
            "longevity": match.get("longevity"),
            "price_level": match.get("price_level"),
            "price_estimate_usd": match.get("price_estimate_usd"),
            "link": match.get("link"),
        }
        return {"status": "success", "data": data}
    except Exception as e:
        AGENT_METRICS["error_count"] += 1
        return {"status": "error", "error_message": str(e)}

# =========================
# 5. AGENT + RUNNER
# =========================

perfume_tools = [
    FunctionTool(func=recommend_perfumes),
    FunctionTool(func=find_alternative),
    FunctionTool(func=get_usage_tips),
    FunctionTool(func=describe_perfume),
]

# Sub-agent that polishes answers (same idea as notebook)
coach_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="coach_agent",
    description=(
        "You are a senior fragrance coach. "
        "When asked by other agents, you refine their draft answer to be clearer, "
        "friendlier, and more helpful, without changing the underlying facts."
    ),
)

scentmatch_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite"),
    name="scentmatch_ai",
    description=(
        "You are ScentMatch AI, a friendly but honest perfume expert. "
        "Always use the tools to look up data from the PERFUMES catalog instead of guessing. "
        "For any recommendation, alternative, usage-tip, or description question, "
        "first call the appropriate tool, then turn its structured JSON result into a "
        "short, clear answer with bullet points. "
        "Ask clarifying questions when needed (especially about gender, season, vibe, and budget). "
        "If the matches are only partial or fallback suggestions, say that clearly. "
        "You may ask 'coach_agent' to polish your final reply."
    ),
    tools=perfume_tools,
    sub_agents=[coach_agent],
)

APP_NAME = "scentmatch_app"
USER_ID = "streamlit-user"

runner = InMemoryRunner(
    app_name=APP_NAME,
    agent=scentmatch_agent,
)

# =========================
# 6. ASYNC CALL HANDLER (with proper ADK session)
# =========================

async def _ensure_session(session_name: str) -> str:
    """Create or get an ADK session (same logic as in the notebook)."""
    app_name = runner.app_name
    session_service = runner.session_service

    try:
        session = await session_service.create_session(
            app_name=app_name,
            user_id=USER_ID,
            session_id=session_name,
        )
    except Exception:
        session = await session_service.get_session(
            app_name=app_name,
            user_id=USER_ID,
            session_id=session_name,
        )
    return session.id


async def _ask_agent_async(query: str, session_name: str) -> str:
    session_id = await _ensure_session(session_name)

    content = types.Content(role="user", parts=[types.Part(text=query)])
    chunks: list[str] = []

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=content,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                txt = getattr(part, "text", None)
                if txt and txt != "None":
                    chunks.append(txt)

    return "\n".join(chunks).strip()


def ask_agent(query: str, session_name: str = "streamlit-chat") -> str:
    return asyncio.run(_ask_agent_async(query, session_name))

# =========================
# 7. STREAMLIT UI
# =========================

st.set_page_config(
    page_title="ScentMatch AI",
    page_icon="🌸",
    layout="centered",
)

st.title("🌸 ScentMatch AI")
st.caption("Your personal perfume recommender — powered by Google ADK + Gemini")

with st.expander("ℹ️ Examples"):
    st.markdown(
        """
- *“Daily perfume for hot climate, budget designer.”*  
- *“Cheaper alternative to Creed Aventus.”*  
- *“Sweet sexy winter scent for dates.”*  
- *“Explain Versace Dylan Blue and when to wear it.”*  
- *“How many sprays of Lattafa Asad in winter?”*  
"""
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# replay chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something about perfumes...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                reply = ask_agent(user_input)
            except Exception as e:
                reply = f"⚠️ Error: `{e}`"

        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# Sidebar metrics (same spirit as notebook summary)
st.sidebar.title("📊 Metrics")
st.sidebar.write("Tool calls:")
for name, count in AGENT_METRICS["tool_calls"].items():
    st.sidebar.write(f"- `{name}`: {count}")

st.sidebar.write(f"\nFallbacks: {AGENT_METRICS['fallback_count']}")
st.sidebar.write(f"Errors (tool level): {AGENT_METRICS['error_count']}")
