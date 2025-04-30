# leetcode-practice

This repository serves as a centralized LeetCode study log, combining Zenn article drafts and multi-language code solutions in a structured monorepo.

---

## Repository Structure

```
leetcode-practice/
├── README.md
├── articles/                   # Zenn article drafts (Markdown) and assets
│   └── two-sum.md
├── problems/                   # LeetCode problems organized by slug
│   └── two-sum/                # Problem #1: Two Sum
│       ├── python/             # Python implementation & tests
│       │   ├── solution.py
│       │   ├── tests.py
│       │   └── README.md       # Problem statement, constraints, solution summary
│       ├── javascript/         # JavaScript implementation (coming soon)
│       └── cpp/                # C++ implementation (coming soon)
└── .gitignore
```

---

## Getting Started

### Prerequisites

- **Python** (3.x)  
- **Node.js & npm** (future)  
- **C++ compiler & CMake** (future)  

### Python Setup

```bash
cd problems/two-sum/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

---

## Zenn Article Workflow

1. Edit or create article drafts under `articles/` (e.g., `two-sum.md`).  
2. Copy-paste Markdown into Zenn or deploy using Zenn CLI.  

---

## Adding a New Problem

1. Create a new folder under `problems/` named by the problem slug (e.g., `problems/two-sum/`).  
2. Within it, add language-specific subfolders (`python/`, `javascript/`, `cpp/`).  
3. Add `solution.*`, `tests.*`, and a `README.md` summarizing the problem and solution.  
4. Draft or update the corresponding Zenn article in `articles/<problem-slug>.md`.  

---

## License

This project is licensed under the MIT License.

---

# 日本語版

## このリポジトリについて

このリポジトリは、Zenn記事の草稿（Markdown）と多言語のコードソリューションを構造化されたモノレポとして一元管理する LeetCode 学習ログリポジトリです。

---

## リポジトリ構成

```
leetcode-practice/
├── README.md
├── articles/                   # Zenn記事の草稿（Markdown）とアセット
│   └── two-sum.md
├── problems/                   # LeetCode問題をスラッグ単位で整理
│   └── two-sum/                # 問題 #1: Two Sum
│       ├── python/             # Python実装＆テスト
│       │   ├── solution.py
│       │   ├── tests.py
│       │   └── README.md       # 問題文、制約、解法概要
│       ├── javascript/         # JavaScript実装（近日対応予定）
│       └── cpp/                # C++実装（近日対応予定）
└── .gitignore
```

---

## はじめに

### 前提条件

- **Python** (3.x)  
- **Node.js と npm** (今後)  
- **C++コンパイラ & CMake** (今後)  

### Python セットアップ

```bash
cd problems/two-sum/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

---

## Zenn記事ワークフロー

1. `articles/` 以下で記事の草稿を編集または作成（例：`two-sum.md`）。  
2. Markdown をコピーして Zenn に貼り付けるか、Zenn CLI でデプロイ。  

---

## 新しい問題の追加

1. `problems/` 下に問題のスラッグ名（例：`problems/two-sum/`）でフォルダを作成。  
2. その中に言語別サブフォルダ（`python/`、`javascript/`、`cpp/`）を追加。  
3. `solution.*`, `tests.*`, `README.md` を追加し、問題文と解法をまとめる。  
4. `articles/<problem-slug>.md` に対応する Zenn 記事を作成または更新。  

---

## ライセンス

本プロジェクトは MIT ライセンスの下で公開されています。
