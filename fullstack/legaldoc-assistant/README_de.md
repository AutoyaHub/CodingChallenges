# LegalDoc Assistant – Full-Stack Challenge

## 1 · Mission

Erstelle ein kleines Web-Tool, das einem Benutzer folgende Funktionen bietet:

1. Upload einer Vertragsdatei (PDF **oder** DOCX, ≤&nbsp;10&nbsp;MB).
2. Strukturierte Daten (JSON) für eine Handvoll Schlüsselfelder erhalten.
3. Eine kurze Zusammenfassung in verständlichem Deutsch.
4. Nachfragen zum Dokument über eine Chat-Box stellen.

Du wählst den genauen Ansatz, die Bibliotheken und die Deployment-Methode—bleibe nur innerhalb des unten aufgeführten Tech-Stacks.

---

## 2 · Tech Stack (Baseline)

* **Frontend** React + Next.js mit **TypeScript**.
* **Backend** Python (**FastAPI** bevorzugt) **ODER** verwende einfach Next.js API Routes (TypeScript).
* **Datenbank** MongoDB (kostenlose Stufe).
* **LLM / NLP** Jedes Modell oder jeder Service, den du kostenlos ausführen kannst oder hinter einem env-var Schlüssel.
* **Hosting** Deploy das Frontend (z.B. Vercel) und Backend (z.B. Fly.io, Railway, Render, oder Docker auf einer beliebigen VM). Bei Verwendung von nur Next.js, einfach auf Vercel deployen.

---

## 3 · Mindestanforderungen

| Bereich | Was wir sehen müssen |
|---------|---------------------|
| **Upload** | Einzeldatei-Upload ≤ 10 MB. |
| **Extraktion** | Erzeuge ein JSON-Objekt mit diesen Feldern: `parties`, `effective_date`, `termination_clause`, `governing_law`, `payment_terms`. |
| **Zusammenfassung** | ≤ 150-Wort Absatz in verständlichem Deutsch. |
| **Chat** | Endpoint, der Fragen zum hochgeladenen Vertrag beantwortet. |
| **Type Safety** | TypeScript **strict** durchgängig. Bei Verwendung eines Python-Backends, Type Hints verwenden. |
| **Testing** | Ein Happy-Path Unit-Test **pro Backend-Route**. |
| **Deployment** | Öffentliche URL(s) für deine App, plus einen Health Check Endpoint. |

---

## 4 · Deliverables

1. **GitHub Repository** mit sauberer Commit-Historie.
2. **README** (≤ 2-min Setup) mit folgendem Inhalt:
   * Projektübersicht
   * Wie man Tests ausführt
   * Wie man deployed (env vars, Befehle)
3. **Live Demo Links** (Frontend + Backend).
4. *Optional:* 2–3-minütige Bildschirmaufnahme, die **Upload ➜ Extraktion ➜ Chat** zeigt.

---

## 5 · Bewertungsrubrik (0–5 jeweils)

* **Code-Qualität**
* **Architektonische Solidität**
* **Test-Disziplin**
* **Dokumentations-Klarheit**
* **UX / Polierung**
* **Autonomie & Problemlösung**

Bestehen = **≥ 18** gesamt **und** mindestens **3** in *Code-Qualität*.

---

## 6 · Zeitrahmen

Plane **8–12 fokussierte Stunden** und liefere innerhalb von **5 Kalendertagen** nach Erhalt der Dokumente.

---

Viel Erfolg — überrasche uns mit klarem Code, prägnanter Dokumentation und einer reibungslosen Demo.