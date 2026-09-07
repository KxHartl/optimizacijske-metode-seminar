# Codex Desktop Instructions (LiteRealm)

@AGENTS.md

## Codex-specific

1. **Strict proactive Git (self-enforced)**:
   - Codex has no project stop hook equivalent to Claude's configuration, so it
     must run the verification and create a commit after **every logical unit of
     work**.
   - Use precise Conventional Commits with a clear scope, for example
     `feat(latex): ...`, `fix(lmi): ...`, or `docs(kkt): ...`.
   - **`🤖 [AI]` marker**:
     - Add it only when Codex autonomously performs the work and creates the
       commit: `\.ai\scripts\helpers\checkpoint.ps1 "feat(scope): description"`.
     - Omit it when the user explicitly asks to commit their own or
       collaboratively assisted changes:
       `\.ai\scripts\helpers\checkpoint.ps1 -UserDriven "feat(scope): description"`.

2. **Required verification before responding**:
   - Before every final response, run `git status --porcelain`.
   - Commit all changes created for the completed logical unit before replying.
   - Preserve unrelated pre-existing user changes; never stage, modify, or
     discard them merely to obtain a clean status.

3. **Subagents and role orchestration**:
   - When available, delegate work to the specialists named in `AGENTS.md`
     (`latex_architect`, `data_fetcher`, `writer`, `qa_reviewer`,
     `latex_surgeon`, and `rag_indexer`) instead of doing specialist work in the
     primary context.
   - Follow their ownership boundaries and the required order:
     `data_fetcher` before `writer`.

4. **Engineering accuracy and RAG grounding**:
   - Ground every claim, quotation, and reference in PDFs under
     `data/sources/` via `rag query`.
   - Never invent a `\cite` key or state mathematical claims without checking
     the source.
   - Verify every numerical calculation and simulation by actually running its
     MATLAB or Python code.

5. **Codex workspace behaviour**:
   - Read `STATE.md` and `.ai/config/project.yaml` before project work; consult
     `.ai/config/REFERENCE.md` only when the task requires it.
   - Treat `data/raw/` as read-only and write derived data only below
     `data/processed/<source_ddmmyyyy_hhmmss>/`.
   - Use Croatian in the chat; use English in code, code comments, READMEs, and
     commit messages.
