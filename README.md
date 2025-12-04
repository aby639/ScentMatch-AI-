# 🌸 ScentMatch AI — Your Personal Perfume Concierge

**An ADK-powered intelligent agent that recommends perfumes, finds dupes, and gives usage tips based on vibe, climate, and budget.**

---

## 🔗 Quick Links

**📘 Kaggle Notebook:**
[https://www.kaggle.com/code/abydanielvarghese/scentmatch-ai-your-personal-perfume-recommender](https://www.kaggle.com/code/abydanielvarghese/scentmatch-ai-your-personal-perfume-recommender)

**🎥 Demo Video:**
*Google Drive link (https://drive.google.com/file/d/1mTsPiGsLvM7zjGpsKCqkYSOb63MwKQHK/view)*

**🏆 Kaggle Competition Submission:**
[https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/scentmatch-ai-intelligent-perfume-recommendation](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/scentmatch-ai-intelligent-perfume-recommendation)

---

## 🚀 Overview

Perfume shopping is confusing — hundreds of fragrances, changing performance, and overpriced designers.

**ScentMatch AI solves this.**

It acts as your **AI-powered fragrance advisor**, helping you instantly discover the perfect scent based on:

* Climate (hot, humid, cold, winter)
* Vibe (fresh, woody, sweet, masculine/feminine)
* Occasion (university, party, gym, date night)
* Budget (affordable → luxury)
* Extra needs like longevity or projection

The agent also suggests **dupes** for expensive perfumes and gives **spray tips** & usage guidance.

---

## ✨ Features

### 🔍 Intelligent Recommendations

Understands your profile and picks scents that match your:

* Weather
* Season
* Gender
* Usage scenario
* Budget
* Preferred vibe

---

### 🪞 **Dupe Finder Tool**

Get **cheaper alternatives** to designer and niche fragrances.
E.g., recommends Club de Nuit Intense Man instead of Creed Aventus.

---

### 💡 **Usage Guide Tool**

Gives actionable advice:

* Correct spray count
* Longevity + projection expectation
* Works best in which season
* Where to apply on the body

---

## 🧠 System Architecture

### Core Components

* **ChatCompletionAgent** → main brain that handles conversation
* **Tools:**

  * `preference_input` → interprets user preferences
  * `dupe_finder_tool` → suggests affordable alternatives
  * `usage_guide_tool` → spray & performance guidance

### ADK Flow

1. User asks for a fragrance
2. Tools run in parallel
3. ADK merges tool outputs
4. Produces a final structured + clean recommendation

---

## 🛠 Technologies Used

| Tech                          | Purpose                             |
| ----------------------------- | ----------------------------------- |
| **OpenAI ADK**                | Multi-tool agent structure          |
| **Python**                    | Development                         |
| **Jupyter Notebook (Kaggle)** | Demo, evaluation                    |
| **Structured Outputs**        | Clean JSON formatting               |
| **Tool Calling**              | Modular dupe & usage tool execution |

---

## 📁 Repository Structure

```
ScentMatch-AI/
│── scentmatch-ai-your-personal-perfume-recommender.ipynb
│── README.md
│── /assets          # (optional) images, banners
│── /images          # (optional) visuals
```

---

## 📀 How to Use (Kaggle Notebook)

1. Open the Kaggle notebook.
2. Add your OpenAI API key in the sidebar → “Secrets”.
3. Run all cells.
4. Interact with ScentMatch AI using:

   ```
   await run_session(runner, "Your question here", session_name="live-chat")
   ```
5. Ask natural questions like:

   * “Suggest a daily fragrance for hot climate.”
   * “Give me cheaper alternatives to Dior Sauvage.”
   * “What’s good for a winter party date night?”

---

## 🧪 Example Sessions

### **1. Hot-climate daily fragrance**

“I'm a guy in a hot climate, budget level cheap designer, want fresh + clean vibe.”
→ Recommends **Nautica Voyage** or **Mont Blanc Explorer**

### **2. Cheaper alternatives to Creed Aventus**

→ Suggests **Armaf CDNIM**, **Mont Blanc Explorer**, etc.

### **3. Winter date night scent**

→ Suggests **Lattafa Asad**, **CDNIM**, etc.

---

## 🧭 Future Improvements

If developed into a full consumer product, the agent can be extended with:

* Web UI (Streamlit / Next.js)
* Large fragrance dataset (Fragrantica-style)
* Embedding-based similarity search
* User fragrance wardrobe tracking
* Multi-language support
* API endpoint for mobile apps

---

## 👤 Author

**Aby Daniel Varghese**
Built with ❤️ during the **5-Day OpenAI × Kaggle Agents Intensive**.

