# Codex_mini
## 為Chate GPT Codex 設製的練習場


 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index d7aab9c51f44945f454bd07d7a73b449e49317a0..907c4f524453401f6b076c51e7e2d19ea0a3a2f2 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,49 @@
 # Codex_mini
-## 為Chate GPT Codex 設製的練習場
\ No newline at end of file
+
+給 ChatGPT Codex 練習用的 Python 小專案（新手友善初始骨架）。
+
+## 專案結構
+
+```text
+.
+├── codex_mini/
+│   ├── __init__.py
+│   └── time_utils.py      # 時間工具函式
+├── main.py                # 執行入口
+├── tests/
+│   └── test_main.py       # pytest 測試範例
+└── requirements-dev.txt   # 開發/測試依賴
+```
+
+## 快速開始
+
+1. （可選）建立虛擬環境
+
+```bash
+python -m venv .venv
+source .venv/bin/activate
+```
+
+2. 安裝測試依賴
+
+```bash
+pip install -r requirements-dev.txt
+```
+
+3. 執行程式
+
+```bash
+python main.py
+```
+
+4. 執行測試
+
+```bash
+pytest
+```
+
+## 下一步建議
+
+- 練習加入命令列參數（例如 `--utc-only`）。
+- 導入 lint/format 工具（如 `ruff`、`black`）。
+- 增加更多函式與單元測試，熟悉 TDD 開發流程。
 
EOF
)