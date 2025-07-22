# 🧠 Interactive Resume (Streamlit)

[![Made with Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)](https://streamlit.io/)
[![Live Demo](https://img.shields.io/badge/Demo-Available-brightgreen)](#demo)

Welcome to my interactive resume, built using **Python** and the **Streamlit** framework. This project allows users to explore my professional experience, skills, and education dynamically — beyond a static PDF.

---

## 🚀 Features

- 📄 **Multi-page interactive resume**
- 🔍 **Search & filter** by:
  - Skills
  - Roles
  - Companies
- 📊 **Dashboard view** with visual insights
- 🔗 JSON-powered data — easy to maintain and extend
- 🌐 Built using [Streamlit](https://streamlit.io/) for fast, shareable web apps

---

## 📁 Repository Structure
```
├── data/
│ ├── introduction.json
│ ├── education.json
│ └── professional_experience.json
├── pages/
│ ├── 1_Experience.py
│ ├── 2_Skills.py
│ └── 3_Education.py
├── About.py
├── requirements.txt
└── README.md
```

- `data/`: Contains all structured resume data in JSON format
- `pages/`: Individual Streamlit pages (Experience, Skills, Dashboard)
- `About.py`: Main landing page / app controller
- `requirements.txt`: Python dependencies

---

## 📦 Installation

To run the project locally:

```bash
# Clone the repo
git clone https://github.com/FARVE14/FaisalAhmedResume.git
cd FaisalAhmedResume

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run About.py
```
--- 

🌐 Demo

Want to see it in action?

👉  [Live Demo](https://faisalahmed.streamlit.app/)

--- 
📊 How it works

All resume data is stored in JSON files under the data/ folder

Pages are generated dynamically using Streamlit's multi-page app support

Users can explore experiences based on tags like "Python", "Data Science", "AWS", etc.

The Dashboard aggregates insights on roles, tenure, and company types

---


🙋‍♂️ About Me

I'm Faisal Ahmed, a passionate developer with experience in building data-driven applications.

📧 faisalg2006@gmail.com

🔗 [LinkedIn](https://www.linkedin.com/in/faisalahmed92/)

---


## 🤝 Contributing

We welcome contributions to improve and expand this project!

### How to Contribute

1. **Fork the repository**  
2. **Create a new branch** for your changes  
3. **Commit** your updates with clear messages  
4. **Push** your branch to your fork  
5. **Create a Pull Request** with a description of your changes

### Ideas for Contributions

- Add new performance metrics
- Improve graphing and visualizations
- Support additional browser configurations
- Enhance reporting and email formatting
- Add dashboard or web interface

Please ensure all code follows good practices and is tested before submission.

For major feature ideas or questions, feel free to open an issue first to discuss.

---

Looking forward to your contributions! ⭐

---

## 📜 Contribution Rules

To maintain the quality and security of this project, we kindly ask all contributors to follow these rules when submitting pull requests:

### ✅ Pull Request Requirements

- Use **descriptive branch names** (e.g., `fix/load-time-bug`, `feature/add-dashboard`)
- Ensure your code is **well-documented and tested**
- Pull Requests must be **linked to an open issue** if applicable
- All PRs should pass existing **CI workflows** and **linter checks**
- Avoid committing directly to `main` or `master`

### 🔐 Signed Commits

We require **signed commits** to ensure the authenticity of contributions.  
To sign a commit:

```bash
git commit -S -m "Your commit message"
```

Make sure you’ve [set up GPG signing](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) in your GitHub account.

---

Thank you for helping keep this project high quality and secure!
