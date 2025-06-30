# LegalDoc Assistant – Full-Stack Challenge

## 1 · Mission

Build a tiny web tool that lets a user:

1. Upload one contract file (PDF **or** DOCX, ≤&nbsp;10&nbsp;MB).
2. Receive structured data (JSON) for a handful of key fields.
3. Get a short plain-English summary.
4. Ask follow-up questions about the document via a chat box.

You pick the exact approach, libraries, and deployment method—just stay within the tech stack below.

---

## 2 · Tech Stack (baseline)

* **Frontend** React + Next.js with **TypeScript**.
* **Backend** Python (**FastAPI** preferred) **OR** just use Next.js API routes (TypeScript).
* **Database** MongoDB (free tier).
* **LLM / NLP** Any model or service you can run for free or behind an env-var key.
* **Hosting** Deploy the frontend (e.g. Vercel) and backend (e.g. Fly.io, Railway, Render, or Docker on any VM). If using Next.js only, just deploy to Vercel.

---

## 3 · Minimal Requirements

| Area | What we must see |
|------|------------------|
| **Upload** | Single-file upload ≤ 10 MB. |
| **Extraction** | Produce a JSON object with these fields: `parties`, `effective_date`, `termination_clause`, `governing_law`, `payment_terms`. |
| **Summary** | ≤ 150-word paragraph in plain English. |
| **Chat** | Endpoint that answers questions about the uploaded contract. |
| **Type Safety** | TypeScript **strict** throughout. If using Python backend, include type hints. |
| **Testing** | One happy-path unit test **per backend route**. |
| **Deployment** | Public URL(s) for your app, plus a health check endpoint. |

---

## 4 · Deliverables

1. **GitHub repo** with clean commit history.
2. **README** (≤ 2-min setup) containing:
   * Project overview
   * How to run tests
   * How to deploy (env vars, commands)
3. **Live demo links** (frontend + backend).
4. *Optional:* 2–3-minute screen recording that shows **upload ➜ extraction ➜ chat**.

---

## 5 · Evaluation Rubric (0–5 each)

* **Code Quality**
* **Architectural Soundness**
* **Testing Discipline**
* **Documentation Clarity**
* **UX / Polish**
* **Autonomy & Problem-Solving**

Passing = **≥ 18** total **and** at least **3** in *Code Quality*.

---

## 6 · Timeline

Aim to spend **8–12 focused hours** and deliver within **5 calendar days** of receiving the docs.

---

Good luck — surprise us with clear code, concise docs, and a smooth demo. 