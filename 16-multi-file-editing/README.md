# Scenario 16: Multi-File Editing with Copilot Edits

Learn how to use Copilot Edits to make coordinated changes across multiple files.

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `user.model.ts` | TypeScript user model to refactor |
| `user.service.ts` | Service layer with user operations |
| `user.controller.ts` | API controller for user endpoints |
| `user.dto.ts` | Data transfer objects |

## 🎯 Learning Objectives

- Use Copilot Edits for multi-file changes
- Make consistent changes across related files
- Refactor code that spans multiple files
- Add features that require changes in multiple places

## 📝 How to Use Copilot Edits

### Opening Copilot Edits
1. Press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
2. Or click the Copilot Edits icon in the sidebar
3. Or use Command Palette: "GitHub Copilot: Open Copilot Edits"

### Adding Files to Edit
- Click "Add Files" or drag files into the Edits panel
- Use `#file:filename` to reference specific files
- Copilot can suggest relevant files based on your request

### Making Requests
Type natural language requests like:
- "Add a 'role' field to the User model and update all related files"
- "Implement soft delete across the user module"
- "Add input validation to all endpoints"

## 🏋️ Exercises

### Exercise 1: Add a New Field
Use Copilot Edits to add a `phoneNumber` field:

1. Open Copilot Edits
2. Add all files in this folder
3. Request: "Add an optional phoneNumber field to the User model and update all related DTOs, service methods, and controller endpoints"
4. Review the changes across all files
5. Accept or modify as needed

### Exercise 2: Implement a Feature
Add audit logging:

1. Add all files to Copilot Edits
2. Request: "Add createdAt and updatedAt timestamps to the User model and ensure they are set correctly in the service layer"
3. Review how Copilot updates multiple files consistently

### Exercise 3: Refactor Naming
Rename for consistency:

1. Add all files to Copilot Edits
2. Request: "Rename 'findById' to 'getUserById' in all files for consistency"
3. See how Copilot updates references across files

### Exercise 4: Add Validation
Add input validation:

1. Add all files to Copilot Edits
2. Request: "Add email format validation when creating and updating users"
3. Review how validation is added in DTOs, service, and controller

### Exercise 5: Error Handling
Improve error handling:

1. Add all files to Copilot Edits
2. Request: "Add custom error types for UserNotFoundError and UserAlreadyExistsError and use them in the service and controller"
3. See how Copilot creates and uses errors across files

## 💡 Tips for Multi-File Editing

### Be Specific About Scope
❌ "Add validation"
✅ "Add email validation that checks format in CreateUserDto and UpdateUserDto, and add corresponding error handling in UserService"

### Reference the Pattern
❌ "Add a new endpoint"
✅ "Add a DELETE /users/:id endpoint following the same pattern as the existing GET endpoint, including service method and controller action"

### Ask for Consistency
```
"Ensure all service methods follow the same error handling pattern"
```

### Preview Before Accepting
- Review each file's changes carefully
- Check that changes are consistent
- Verify no unintended modifications

## ⚠️ Things to Watch For

1. **Review all changes**: Don't accept blindly
2. **Check imports**: Verify new imports are correct
3. **Test after applying**: Run tests to verify functionality
4. **Commit often**: Make atomic commits for each logical change
5. **Undo if needed**: You can always undo changes

## 🔧 Keyboard Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Copilot Edits | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Accept all changes | `Ctrl+Enter` | `Cmd+Enter` |
| Discard changes | `Escape` | `Escape` |

## ✅ Key Takeaways

- Copilot Edits makes coordinated multi-file changes
- Add relevant files to get comprehensive updates
- Be specific about what you want changed
- Always review changes before accepting
- Use for refactoring, adding features, or fixing bugs across files
