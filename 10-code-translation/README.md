# Scenario 10: Code Translation

This scenario demonstrates how to use GitHub Copilot to convert code between different programming languages.

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `original_python.py` | Python source code to translate |
| `translated_javascript.js` | JavaScript translation (practice) |
| `translated_typescript.ts` | TypeScript translation (practice) |
| `translated_csharp.cs` | C# translation (practice) |

## 🎯 Learning Objectives

- Translate code between programming languages
- Understand language-specific idioms and patterns
- Maintain functionality while adapting to language conventions
- Handle differences in standard libraries

## 📝 Instructions

### Method 1: Using Copilot Chat

1. Open `original_python.py`
2. Select the code you want to translate
3. Open Copilot Chat (Ctrl+Alt+I)
4. Ask: "Convert this to JavaScript" (or any language)

### Method 2: Inline Chat

1. Select code in the source file
2. Press Ctrl+I (or Cmd+I on Mac)
3. Type: "translate to TypeScript"

### Method 3: Comment-Driven

1. Open the target file (e.g., `translated_javascript.js`)
2. Paste the original code as a comment
3. Let Copilot generate the translation

## 🏋️ Exercises

1. **Python → JavaScript**: Translate the data processing functions
2. **Python → TypeScript**: Add type annotations during translation
3. **Python → C#**: Convert to object-oriented C# style
4. **Compare Results**: Note how Copilot adapts to language conventions

## 💡 Tips

- Ask for idiomatic translations: "Convert to idiomatic JavaScript"
- Request explanations: "Explain the differences between these versions"
- Handle libraries: "Use lodash instead of Python's itertools"
- Preserve types: "Maintain type safety in the translation"

## ⚠️ Things to Watch For

- Different standard library functions
- Async/await patterns vary between languages
- Error handling conventions differ
- Null/undefined handling differences
