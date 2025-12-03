# 🌸 ScentMatch AI — Your Personal Perfume Concierge

**An ADK-powered intelligent agent that recommends perfumes, finds affordable dupes, and gives usage tips based on your vibe, climate, and budget.**

---

## 🔗 Quick Links

* **📘 Kaggle Notebook:**
  [https://www.kaggle.com/code/abydanielvarghese/scentmatch-ai-your-personal-perfume-recommender](https://www.kaggle.com/code/abydanielvarghese/scentmatch-ai-your-personal-perfume-recommender)
* **🎥 Demo Video:** *(https://drive.google.com/file/d/1mTsPiGsLvM7zjGpsKCqkYSOb63MwKQHK/view?usp=drive_web)*
* **🏆 Kaggle Competition Writeup:**
  *(https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/scentmatch-ai-intelligent-perfume-recommendation)*

---

## 🚀 Overview

Buying fragrances is confusing — performance changes with weather, notes are hard to understand, and prices vary wildly.

**ScentMatch AI** makes fragrance discovery simple by acting as your **AI-powered scent advisor**, helping you pick the perfect perfume instantly.

---

## ✨ Features

### 🔍 Personalized Recommendations

Get perfume suggestions tailored to:

* Hot / cold / humid climate
* Vibe (fresh, woody, sweet, masculine, feminine)
* Budget (affordable → ultra luxury)
* Use case (university, office, date night, gym)

### 🪞 Dupe Finder

Finds **affordable dupes** for expensive designer/niche fragrances.

### 💡 Usage Guide

Practical tips such as:

* Correct spray count
* Longevity expectations
* Where to apply
* When it performs best

---

## 🧠 System Architecture

**Main Components**

* **ChatCompletionAgent** — handles conversation & logic
* **Tools**

  * *preference_input* — gathers and interprets user inputs
  * *dupe_finder_tool* — recommends cheaper similar scents
  * *usage_guide_tool* — provides spray tips + performance insights

**ADK Workflow**

1. User expresses perfume preference
2. Tools run in parallel
3. ADK merges tool outputs into a final clean recommendation

---

## 🛠️ Technologies Used

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| **OpenAI ADK (Agents)** | Core intelligence              |
| **Python**              | Development                    |
| **Jupyter Notebook**    | Demo and evaluation            |
| **Structured Outputs**  | Clean user-friendly formatting |
| **JSON Tools**          | For modular agent actions      |

---

## 🎥 Demo

The Kaggle Notebook walks through:

* Collecting fragrance preferences
* Running all 3 tools
* Producing recommendations + dupes + usage tips
* Outputting structured JSON and final clean text

👉 **Notebook Link again for quick access:**
[https://www.kaggle.com/code/abydanielvarghese/scentmatch-ai-your-personal-perfume-recommender](https://www.kaggle.com/code/abydanielvarghese/scentmatch-ai-your-personal-perfume-recommender)

---

## 📁 Repository Structure

```
ScentMatch-AI/
│── scentmatch-ai-your-personal-perfume-recommender.ipynb
│── README.md
│── /assets (images or diagrams)
│── /images  (optional visuals)
```

---

## 🔮 If I Had More Time

* Add a small UI or web app using Streamlit
* Integrate a large perfume dataset (Fragrantica-like)
* Scent similarity search using embeddings
* Multi-language support
* Personalized “fragrance wardrobe builder”

---

## 👤 Author

**Aby Daniel Varghese**
Built with ❤️ using OpenAI ADK.

---

