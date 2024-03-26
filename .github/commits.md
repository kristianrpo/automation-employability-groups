# Conventional commits
Conventional Commit is a naming standard for commit messages in Git. This standard defines a structured format for commit messages that helps to clearly and concisely understand what has been changed in the repository.


## Types of commits
- **feat:** A new feature or functionality.
- **fix:** A bug fixed.
- **refactor:** A code change that neither corrects a bug nor adds a feature.
- **style:** Changes that do not affect the meaning of the code (blank spaces, formatting, missing semicolons, etc).
- **test:** Add missing tests or correct existing tests.
- **docs:** Changes in documentation.
- **reverts:** Reverts a previous commit
- **build:** Changes that affect the compilation system or external dependencies (e.g. changes in package.json).

## Write commits

- Is a mandatory part of the format
- Use the imperative, present tense: "change" not "changed" nor "changes"
    - Think of This commit will... or This commit should...
- Don't capitalize the first letter
- No dot (.) at the end

## Example

    feat: add support for TypeScript.