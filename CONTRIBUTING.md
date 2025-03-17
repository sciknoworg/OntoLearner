# Contribution Guidelines
Welcome to **OntoLearner**!



### 1. Commit Guidelines

For efficient code review, *`make one commit per logical change`* and keep changes small to speed up the process and simplify troubleshooting. Avoid mixing whitespace changes with functional updates, and separate unrelated functional changes into distinct commits. Use the imperative mood in commit messages (e.g., "Add preprocessing step") and keep the subject concise, ideally under 60 characters. Focus on what the change does, not how it’s done, and format references to issues or PRs like "Add LLaMA-3.2 [#2]". Optionally, use emoji codes for clarity.


**This is an Optional** but feel free to use the following emoji codes in your message.

| Code           | Emoji | Use for                        |
|----------------|-------|--------------------------------|
| `:fire:`       | 🔥    | Remove code or files           |
| `:bug:`        | 🐛    | Fix a bug or issue             |
| `:sparkles:`   | ✨    | Add feature or improvements    |
| `:memo:`       | 📝    | Add or update documentation    |
| `:tada:`       | 🎉    | Start a project                |
| `:recycle:`    | ♻️    | Refactor code                  |
| `:pencil2:`    | ✏️    | Minor changes   or improvement |
| `:bookmark:`   | 🔖    | Version release                |
| `:adhesive_bandage:` | 🩹 | Non-critical fix               |
| `:test_tube:`  | 🧪    | Test-related changes           |
| `:boom:`       | 💥    | Introduce breaking changes     |

## 3. How to Submit a Pull Request (PR)

To contribute changes to the library, please follow these steps:

1. Clone the repository.
```bash
git clone git@github.com:sciknoworg/OntoLearner.git
cd OntoLearner
```
2. Create a virtual environment with python>=3.9, activate it, install the required dependencies and install the pre-commit configuration:
```bash
conda create -n my_env python=3.9
conda activate my_env
pip install -r requirements.txt
pre-commit install
```
3. Create a branch and commit your changes:
```bash
git switch -c <name-your-branch>
# do your changes
git add .
git commit -m "your commit msg"
git push
```
4. Ensure your code adheres to the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
5. Format the code using `ruff check --fix .`.
6. Open a pull request with your changes to the `dev` branch.
7. Be responsive to feedback during the review process.
