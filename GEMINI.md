# Gemini CLI / Antigravity Instructions (LiteRealm)

@AGENTS.md

# Gemini CLI / Antigravity Instructions (LiteRealm)

@AGENTS.md

## Antigravity / Gemini Agent Guidelines

1. **Strogi proaktivni Git (Samostalna disciplina)**:
   - Budući da nema automatskih vanjskih stop-hookova, agent samostalno provodi verifikaciju i commit nakon SVAKE logičke cjeline.
   - Commit poruke moraju biti inženjerski precizne (Conventional Commits s definiranim scope-om, npr. `feat(latex): ...`, `fix(lmi): ...`, `docs(kkt): ...`).
   - **Oznaka `🤖 [AI]`**:
     - Dodaje se **samo** kada agent samostalno/autonomno provodi zadatak i stvara commit (`.\.ai\scripts\helpers\checkpoint.ps1 "feat: ..."`).
     - **Ne dodaje se** ako korisnik zatraži commit vlastitog rada ili asistiranog rješenja (`.\.ai\scripts\helpers\checkpoint.ps1 -UserDriven "feat: ..."`).
2. **Obavezna verifikacija prije odgovora**:
   - Prije završetka svakog odgovora, agent OBAVEZNO provjerava `git status --porcelain`.
   - Ako izlaz nije prazan, sve promjene moraju biti committane prije slanja konačnog odgovora korisniku.
3. **Subagenti i orkestracija uloga**:
   - Antigravity podržava native subagente (`invoke_subagent`, `define_subagent`).
   - Glavni agent može definirati i pozivati specijaliste (`latex_architect`, `data_fetcher`, `writer`, `qa_reviewer`, `latex_surgeon`, `rag_indexer`) iz `~/.agentbrain/agents/` ili preuzimati njihovu ulogu uz strogo poštivanje `writes_to` i `never_touches` granica.
4. **Inženjerska točnost i RAG utemeljenost**:
   - Sve tvrdnje, citati i reference moraju biti utemeljeni u PDF izvorima u `data/sources/` preko `rag query`.
   - Zabranjeno je izmišljati `\cite` ključeve i matematičke tvrdnje bez provjere.
   - Svi numerički izračuni i simulacije (MATLAB/Python) moraju biti verificirani izvođenjem koda.
