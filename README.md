# Slayer Agents

> 🇬🇧 **English** below · 🇮🇹 [**Italiano** più in basso](#slayer-agents--italiano)

Audit-first AI coding agents for Claude Code workflows.

Slayer Agents is a Claude Code-style plugin that gives you a small, opinionated squad of specialist agents for real software work: repo audits, scoped fixes, debugging, research, code review, verification, PR preparation, reporting, and git-safe delivery.

The roster is themed on Demon Slayer. The Demon Slayer Corps does the building, planning, and review; two demons — **Doma** and **Akaza** — form the adversarial red-team that hunts security holes and breaks weak code before users do. **Slayers build; demons break.** Every agent, demon or not, follows the same safety rules: read-only reviewers never mutate the worktree, secrets are never printed or logged, and nothing is pushed or published without explicit approval.

The workflow is simple:

1. Understand the real runtime path.
2. Plan before editing.
3. Make scoped changes.
4. Review and verify.
5. Commit only what was intended.

> Unofficial fan-themed project. This repository is not affiliated with, sponsored by, or endorsed by Koyoharu Gotouge, Shueisha, Aniplex, ufotable, or any related rights holder.

## Features

- Read-only audit command for tracing real code paths.
- Full gated feature lifecycle command for gather, research, plan, build, review plus test, and summary.
- Full gated bugfix lifecycle command for gather, investigate, fix plan, fix, verify, and summary.
- Planning command for implementation notes before edits.
- Research, explain, brainstorm, refactor, report, and PR commands.
- Scoped fix command for approved changes.
- Debug command for root-cause investigations.
- Review command with file and line findings.
- Test command for four-angle verification: unit/component, integration, E2E/user flow, and security.
- Commit command built around staged-diff safety.
- Project init command for generating local context.
- Natural routing skills for `kagaya`, `akaza`, and `tengen`.
- Yushiro internal support for activity logs, reports, memory, and artifact housekeeping.

## Agent Squad

| Agent | Role |
|---|---|
| Kagaya Ubuyashiki | Main orchestrator, planning, coordinates agents |
| Tanjiro Kamado | Implementation, architecture, automation, complex engineering |
| Mitsuri Kanroji | UI/UX, frontend, user flows |
| Tamayo | Deep debugging, unusual edge cases, hard investigations |
| Doma 🩸 | Security review, suspicious audit, auth and data leak checks (demon red-team) |
| Obanai Iguro | Code review, precise file and line findings |
| Akaza 🩸 | Stress testing, edge cases, performance pressure (demon red-team) |
| Zenitsu Agatsuma | Small scoped fixes, surgical changes |
| Gyomei Himejima | Data integrity, backend reliability, defensive design |
| Tengen Uzui | Git, release coordination, staged diff safety, final checklist |

Internal support:

| Agent | Role |
|---|---|
| Yushiro | Activity logging, reports, memory writes, artifact housekeeping |

## Installation

### Option 1: Install From GitHub In Claude Code

After this repository is available on GitHub:

```bash
/plugin marketplace add pappusinghadip/demonslayer
/plugin install slayer@slayer-agents
```

Then use the slash commands:

```text
/slayer:audit explain the auth flow
/slayer:feature add passkey login
/slayer:bugfix users cannot log in after password reset
/slayer:research auth flow
/slayer:explain checkout module
/slayer:plan add passkey login
/slayer:review staged changes
```

You can also use natural routing in Claude Code:

```text
kagaya, build a search bar
akaza, test the auth flow
tengen, prepare the commit
```

### Option 2: Run Locally From A Clone

Clone the repository:

```bash
git clone git@github.com:pappusinghadip/demonslayer.git
cd demonslayer
```

Run Claude Code with the plugin directory:

```bash
claude --plugin-dir "$PWD/plugins/slayer"
```

For the current local workspace:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/slayer-agents/plugins/slayer
```

## Quick Start

Initialize project context in any repo:

```text
/slayer:init
```

Audit before making changes:

```text
/slayer:audit why does /admin redirect to login
```

Create a plan before implementation:

```text
/slayer:plan add a manual passkey check after password login
```

Run a full feature lifecycle:

```text
/slayer:feature add a manual passkey check after password login
```

Run a full bugfix lifecycle:

```text
/slayer:bugfix login fails after password reset
```

Implement an approved scoped change:

```text
/slayer:fix implement the approved passkey plan
```

Review changed code:

```text
/slayer:review staged changes
```

Prepare a PR:

```text
/slayer:pr target main
```

Commit safely:

```text
/slayer:commit latest fix
```

## Commands

| Command | Purpose |
|---|---|
| `/slayer:audit` | Read-only repo audit and runtime path trace |
| `/slayer:brainstorm` | Compare options and tradeoffs before building |
| `/slayer:plan` | Create an implementation plan before editing |
| `/slayer:feature` | Gather -> research -> plan -> build -> review plus test -> summary |
| `/slayer:bugfix` | Gather -> investigate -> fix plan -> fix -> verify -> summary |
| `/slayer:fix` | Implement an approved scoped change |
| `/slayer:debug` | Root-cause debugging with approval before fixes |
| `/slayer:explain` | Layered codebase or feature explanation |
| `/slayer:research` | Deep read-only research from multiple angles |
| `/slayer:refactor` | Review-led refactoring with approval gate |
| `/slayer:review` | Code review and security-risk pass |
| `/slayer:test` | Four-angle verification, stress, and edge checks |
| `/slayer:commit` | Staged diff review and safe commit workflow |
| `/slayer:pr` | PR preparation with diff review and approval gate |
| `/slayer:report` | Activity summary from reports, memory, and artifacts |
| `/slayer:init` | Create project context for this workflow |

## Gated Lifecycles

Lifecycle state is written under `.slayer/.temp/`. If context is compacted or a terminal closes, restart by reading the task `status.md` and phase files. The commands check whether `.slayer/.temp/` is gitignored before writing artifacts.

### Feature Lifecycle

```text
/slayer:feature build a search bar

Phase 0  Gather         Requirements. Definition of done. Existing resources.
Phase 1  Research       Slayers explore the codebase from multiple angles in parallel.
          GATE          Confirm understanding before planning.
Phase 2  Plan           Architecture decisions, chunks, risks, and verification.
          GATE          Approve the plan before source edits.
Phase 3  Build          Slayers execute per the approved plan.
          GATE          Review what was built.
Phase 4  Review + Test  Obanai Iguro reviews. Doma audits sensitive paths. Akaza verifies from four angles.
          GATE          Decide which findings to fix, defer, or accept.
Phase 5  Summary        What was built, decisions made, test result, and reusable notes.
```

### Bugfix Lifecycle

```text
/slayer:bugfix users cannot log in after SSO

Phase 0  Gather         Bug details, logs, screenshots, impact, and timeline.
Phase 1  Investigate    Tamayo traces symptoms to root cause.
          GATE          Confirm the root cause before any fix is attempted.
Phase 2  Fix Plan       Proposed fix, blast radius, rollback, and verification.
          GATE          Approve the approach before source edits.
Phase 3  Fix            The right Slayer executes the fix.
          GATE          Review the fix.
Phase 4  Verify         Obanai Iguro reviews. Doma audits sensitive paths. Akaza confirms the bug is gone.
Phase 5  Summary        Root cause, fix, verification, and reusable decision rule.
```

Yushiro can log lifecycle output to `.slayer/reports/activity.log` and save reusable decision rules to `.slayer/memory/`.

## Recommended Workflow

### For New Features

```text
/slayer:feature build the new feature
/slayer:commit feature summary
```

### For Bugs

```text
/slayer:bugfix paste the error or describe the failing behavior
/slayer:commit bugfix summary
```

Use `/slayer:plan` plus `/slayer:fix` when you want to split the lifecycle manually. Use `/slayer:research`, `/slayer:explain`, or `/slayer:brainstorm` when you want understanding before any plan.

### For Git Handoff

```text
/slayer:review staged changes
/slayer:commit commit message or context
```

Tengen Uzui is intentionally staged-diff focused. The commit workflow should not use broad staging unless explicitly requested.

## How The Agents Route Work

- Kagaya Ubuyashiki coordinates larger work.
- Tanjiro Kamado handles complex implementation and automation.
- Mitsuri Kanroji handles frontend and user-facing flows.
- Tamayo handles difficult debugging.
- Gyomei Himejima handles backend reliability, persistence, and data safety.
- Zenitsu Agatsuma handles tiny low-risk patches.
- Obanai Iguro reviews code.
- Doma reviews security-sensitive paths.
- Akaza verifies edge cases, stress cases, and regressions.
- Tengen Uzui handles git, release checks, and final commit hygiene.
- Yushiro quietly handles `.slayer/` reports, memory, and activity logs.

## Repository Structure

```text
slayer-agents/
├── .claude-plugin/
│   └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── plugins/
│   └── slayer/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── agents/
│       ├── commands/
│       ├── hooks/
│       ├── knowledge/
│       └── skills/
├── scripts/
│   └── validate_slayer.py
├── skills/
│   └── slayer-agents/
│       └── SKILL.md
├── CLAUDE.md
└── README.md
```

## Validation

Run the structure validator:

```bash
python3 scripts/validate_slayer.py
```

Expected output:

```text
OK: Slayer Agents structure is valid
```

The validator checks:

- all 10 public agent files and internal Yushiro support agent exist;
- all command files exist;
- routing and shared-rule skills exist;
- hook files exist;
- required skills and knowledge files exist;
- agent skill references resolve;
- Claude plugin versions match;
- upstream reference identifiers are not present.

## Development

When editing the plugin:

1. Update agent, command, skill, or knowledge files under `plugins/slayer`.
2. Run validation.
3. Test locally with `claude --plugin-dir "$PWD/plugins/slayer"`.
4. Commit only intentional files.

Useful commands:

```bash
python3 scripts/validate_slayer.py
git status --short --branch
git diff --cached --name-status
```

## Git Safety Rules

Tengen Uzui follows these rules:

- start with `git status --short --branch`;
- inspect staged files with `git diff --cached --name-status`;
- inspect the actual staged diff before commit;
- never assume untracked files are included;
- never use `git add .` unless explicitly approved;
- remote writes follow `Remote Write Safety` in `plugins/slayer/knowledge/core-principles.md`;
- do not duplicate or weaken the core remote-write rule in command docs or agent docs.

## Generated State

Generated workflow state should stay out of normal commits:

```text
.slayer/.temp/
.claude/slayer/.temp/
```

Project context and memory may be created by `/slayer:init` inside a target repo.

## Versioning

Keep these versions in sync:

- `.claude-plugin/marketplace.json`
- `plugins/slayer/.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`

Run validation after version or metadata changes.

## License

No open-source license has been added yet. Unless a `LICENSE` file is added, all rights are reserved by the repository owner.

---

# Slayer Agents — Italiano

> 🇮🇹 **Italiano** · 🇬🇧 [**Back to English / torna all'inglese**](#slayer-agents)

Agenti di coding AI "audit-first" per i flussi di lavoro di Claude Code.

Slayer Agents è un plugin in stile Claude Code che mette a disposizione una piccola squadra, con una sua filosofia precisa, di agenti specializzati per il lavoro software reale: audit del repository, correzioni circoscritte, debugging, ricerca, revisione del codice, verifica, preparazione delle PR, reportistica e consegna sicura tramite git.

Il cast è ispirato a Demon Slayer. Il Corpo degli Ammazzademoni si occupa di costruire, pianificare e revisionare; due demoni — **Doma** e **Akaza** — formano il red-team avversario che cerca i buchi di sicurezza e rompe il codice debole prima che lo facciano gli utenti. **Gli Slayer costruiscono; i demoni rompono.** Ogni agente, demone o meno, segue le stesse regole di sicurezza: i revisori in sola lettura non modificano mai il worktree, i segreti non vengono mai stampati o registrati, e nulla viene pushato o pubblicato senza approvazione esplicita.

Il flusso di lavoro è semplice:

1. Capire il vero percorso di esecuzione.
2. Pianificare prima di modificare.
3. Apportare modifiche circoscritte.
4. Revisionare e verificare.
5. Committare solo ciò che era previsto.

> Progetto amatoriale a tema. Questo repository non è affiliato, sponsorizzato o approvato da Koyoharu Gotouge, Shueisha, Aniplex, ufotable o alcun titolare di diritti correlato.

## Funzionalità

- Comando di audit in sola lettura per tracciare i veri percorsi del codice.
- Comando per il ciclo di vita completo e con gate di una feature: raccolta, ricerca, piano, build, revisione più test e riepilogo.
- Comando per il ciclo di vita completo e con gate di un bugfix: raccolta, indagine, piano di fix, fix, verifica e riepilogo.
- Comando di pianificazione per le note di implementazione prima delle modifiche.
- Comandi di ricerca, spiegazione, brainstorming, refactoring, report e PR.
- Comando di fix circoscritto per le modifiche approvate.
- Comando di debug per indagini sulla causa radice.
- Comando di revisione con riscontri per file e riga.
- Comando di test con verifica a quattro angolazioni: unità/componente, integrazione, E2E/flusso utente e sicurezza.
- Comando di commit costruito attorno alla sicurezza del diff in stage.
- Comando di init del progetto per generare il contesto locale.
- Skill di routing naturale per `kagaya`, `akaza` e `tengen`.
- Supporto interno di Yushiro per log delle attività, report, memoria e gestione degli artefatti.

## La Squadra

| Agente | Ruolo |
|---|---|
| Kagaya Ubuyashiki | Orchestratore principale, pianificazione, coordina gli agenti |
| Tanjiro Kamado | Implementazione, architettura, automazione, ingegneria complessa |
| Mitsuri Kanroji | UI/UX, frontend, flussi utente |
| Tamayo | Debugging approfondito, casi limite insoliti, indagini difficili |
| Doma 🩸 | Revisione di sicurezza, audit sospetti, controlli su autenticazione e fughe di dati (red-team demone) |
| Obanai Iguro | Revisione del codice, riscontri precisi per file e riga |
| Akaza 🩸 | Stress test, casi limite, pressione sulle prestazioni (red-team demone) |
| Zenitsu Agatsuma | Correzioni piccole e circoscritte, modifiche chirurgiche |
| Gyomei Himejima | Integrità dei dati, affidabilità del backend, progettazione difensiva |
| Tengen Uzui | Git, coordinamento dei rilasci, sicurezza dei diff in stage, checklist finale |

Supporto interno:

| Agente | Ruolo |
|---|---|
| Yushiro | Registrazione delle attività, report, scritture in memoria, gestione degli artefatti |

## Installazione

### Opzione 1: Installazione da GitHub in Claude Code

Quando il repository è disponibile su GitHub:

```bash
/plugin marketplace add pappusinghadip/demonslayer
/plugin install slayer@slayer-agents
```

Poi usa gli slash command:

```text
/slayer:audit explain the auth flow
/slayer:feature add passkey login
/slayer:bugfix users cannot log in after password reset
/slayer:research auth flow
/slayer:explain checkout module
/slayer:plan add passkey login
/slayer:review staged changes
```

Puoi anche usare il routing naturale in Claude Code:

```text
kagaya, build a search bar
akaza, test the auth flow
tengen, prepare the commit
```

### Opzione 2: Esecuzione locale da un clone

Clona il repository:

```bash
git clone git@github.com:pappusinghadip/demonslayer.git
cd demonslayer
```

Avvia Claude Code con la directory del plugin:

```bash
claude --plugin-dir "$PWD/plugins/slayer"
```

Per l'attuale workspace locale:

```bash
claude --plugin-dir /Users/pappusingha/Documents/MyAgent/slayer-agents/plugins/slayer
```

## Avvio Rapido

Inizializza il contesto del progetto in qualsiasi repo:

```text
/slayer:init
```

Esegui un audit prima di apportare modifiche:

```text
/slayer:audit why does /admin redirect to login
```

Crea un piano prima dell'implementazione:

```text
/slayer:plan add a manual passkey check after password login
```

Esegui un ciclo di vita completo di feature:

```text
/slayer:feature add a manual passkey check after password login
```

Esegui un ciclo di vita completo di bugfix:

```text
/slayer:bugfix login fails after password reset
```

Implementa una modifica circoscritta approvata:

```text
/slayer:fix implement the approved passkey plan
```

Revisiona il codice modificato:

```text
/slayer:review staged changes
```

Prepara una PR:

```text
/slayer:pr target main
```

Committa in sicurezza:

```text
/slayer:commit latest fix
```

## Comandi

| Comando | Scopo |
|---|---|
| `/slayer:audit` | Audit del repository in sola lettura e tracciamento del percorso di esecuzione |
| `/slayer:brainstorm` | Confronta opzioni e compromessi prima di costruire |
| `/slayer:plan` | Crea un piano di implementazione prima di modificare |
| `/slayer:feature` | Raccolta -> ricerca -> piano -> build -> revisione più test -> riepilogo |
| `/slayer:bugfix` | Raccolta -> indagine -> piano di fix -> fix -> verifica -> riepilogo |
| `/slayer:fix` | Implementa una modifica circoscritta approvata |
| `/slayer:debug` | Debugging sulla causa radice con approvazione prima delle fix |
| `/slayer:explain` | Spiegazione a livelli del codice o della feature |
| `/slayer:research` | Ricerca approfondita in sola lettura da più angolazioni |
| `/slayer:refactor` | Refactoring guidato dalla revisione con gate di approvazione |
| `/slayer:review` | Revisione del codice e passaggio sui rischi di sicurezza |
| `/slayer:test` | Verifica a quattro angolazioni, stress e controlli sui casi limite |
| `/slayer:commit` | Revisione del diff in stage e flusso di commit sicuro |
| `/slayer:pr` | Preparazione della PR con revisione del diff e gate di approvazione |
| `/slayer:report` | Riepilogo delle attività da report, memoria e artefatti |
| `/slayer:init` | Crea il contesto di progetto per questo flusso di lavoro |

## Cicli di Vita con Gate

Lo stato del ciclo di vita viene scritto sotto `.slayer/.temp/`. Se il contesto viene compresso o un terminale viene chiuso, riprendi leggendo lo `status.md` del task e i file di fase. I comandi verificano che `.slayer/.temp/` sia nel gitignore prima di scrivere gli artefatti.

### Ciclo di Vita della Feature

```text
/slayer:feature build a search bar

Fase 0   Raccolta          Requisiti. Definizione di "fatto". Risorse esistenti.
Fase 1   Ricerca           Gli Slayer esplorano il codice da più angolazioni in parallelo.
          GATE             Conferma la comprensione prima di pianificare.
Fase 2   Piano             Decisioni di architettura, blocchi, rischi e verifica.
          GATE             Approva il piano prima delle modifiche al codice.
Fase 3   Build             Gli Slayer eseguono secondo il piano approvato.
          GATE             Revisiona ciò che è stato costruito.
Fase 4   Revisione + Test  Obanai Iguro revisiona. Doma controlla i percorsi sensibili. Akaza verifica da quattro angolazioni.
          GATE             Decidi quali riscontri correggere, rinviare o accettare.
Fase 5   Riepilogo         Cosa è stato costruito, decisioni prese, esito dei test e note riutilizzabili.
```

### Ciclo di Vita del Bugfix

```text
/slayer:bugfix users cannot log in after SSO

Fase 0   Raccolta          Dettagli del bug, log, screenshot, impatto e cronologia.
Fase 1   Indagine          Tamayo risale dai sintomi alla causa radice.
          GATE             Conferma la causa radice prima di qualsiasi tentativo di fix.
Fase 2   Piano di Fix      Fix proposta, raggio d'impatto, rollback e verifica.
          GATE             Approva l'approccio prima delle modifiche al codice.
Fase 3   Fix               Lo Slayer giusto esegue la fix.
          GATE             Revisiona la fix.
Fase 4   Verifica          Obanai Iguro revisiona. Doma controlla i percorsi sensibili. Akaza conferma che il bug è sparito.
Fase 5   Riepilogo         Causa radice, fix, verifica e regola decisionale riutilizzabile.
```

Yushiro può registrare l'output del ciclo di vita in `.slayer/reports/activity.log` e salvare regole decisionali riutilizzabili in `.slayer/memory/`.

## Flusso di Lavoro Consigliato

### Per Nuove Feature

```text
/slayer:feature build the new feature
/slayer:commit feature summary
```

### Per i Bug

```text
/slayer:bugfix paste the error or describe the failing behavior
/slayer:commit bugfix summary
```

Usa `/slayer:plan` più `/slayer:fix` quando vuoi suddividere il ciclo di vita manualmente. Usa `/slayer:research`, `/slayer:explain` o `/slayer:brainstorm` quando vuoi capire prima di qualsiasi piano.

### Per il Passaggio a Git

```text
/slayer:review staged changes
/slayer:commit commit message or context
```

Tengen Uzui è volutamente focalizzato sul diff in stage. Il flusso di commit non dovrebbe usare lo staging massivo a meno che non sia richiesto esplicitamente.

## Come gli Agenti Instradano il Lavoro

- Kagaya Ubuyashiki coordina il lavoro più ampio.
- Tanjiro Kamado gestisce implementazione complessa e automazione.
- Mitsuri Kanroji gestisce frontend e flussi rivolti all'utente.
- Tamayo gestisce il debugging difficile.
- Gyomei Himejima gestisce affidabilità del backend, persistenza e sicurezza dei dati.
- Zenitsu Agatsuma gestisce le piccole patch a basso rischio.
- Obanai Iguro revisiona il codice.
- Doma revisiona i percorsi sensibili alla sicurezza.
- Akaza verifica casi limite, casi di stress e regressioni.
- Tengen Uzui gestisce git, i controlli di rilascio e l'igiene finale dei commit.
- Yushiro gestisce in silenzio report, memoria e log delle attività in `.slayer/`.

## Struttura del Repository

```text
slayer-agents/
├── .claude-plugin/
│   └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── plugins/
│   └── slayer/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── agents/
│       ├── commands/
│       ├── hooks/
│       ├── knowledge/
│       └── skills/
├── scripts/
│   └── validate_slayer.py
├── skills/
│   └── slayer-agents/
│       └── SKILL.md
├── CLAUDE.md
└── README.md
```

## Validazione

Esegui il validatore della struttura:

```bash
python3 scripts/validate_slayer.py
```

Output atteso:

```text
OK: Slayer Agents structure is valid
```

Il validatore controlla che:

- esistano tutti i 10 file degli agenti pubblici e l'agente di supporto interno Yushiro;
- esistano tutti i file dei comandi;
- esistano le skill di routing e di regole condivise;
- esistano i file degli hook;
- esistano le skill e i file di conoscenza richiesti;
- i riferimenti alle skill negli agenti si risolvano;
- le versioni del plugin Claude coincidano;
- non siano presenti identificatori di riferimento upstream.

## Sviluppo

Quando modifichi il plugin:

1. Aggiorna i file di agenti, comandi, skill o conoscenza sotto `plugins/slayer`.
2. Esegui la validazione.
3. Testa in locale con `claude --plugin-dir "$PWD/plugins/slayer"`.
4. Committa solo i file voluti.

Comandi utili:

```bash
python3 scripts/validate_slayer.py
git status --short --branch
git diff --cached --name-status
```

## Regole di Sicurezza Git

Tengen Uzui segue queste regole:

- inizia con `git status --short --branch`;
- ispeziona i file in stage con `git diff --cached --name-status`;
- ispeziona il vero diff in stage prima del commit;
- non dare mai per scontato che i file non tracciati siano inclusi;
- non usare mai `git add .` se non esplicitamente approvato;
- le scritture remote seguono `Remote Write Safety` in `plugins/slayer/knowledge/core-principles.md`;
- non duplicare né indebolire la regola centrale sulle scritture remote nei documenti dei comandi o degli agenti.

## Stato Generato

Lo stato del flusso di lavoro generato dovrebbe restare fuori dai commit normali:

```text
.slayer/.temp/
.claude/slayer/.temp/
```

Il contesto di progetto e la memoria possono essere creati da `/slayer:init` dentro un repository target.

## Versionamento

Mantieni allineate queste versioni:

- `.claude-plugin/marketplace.json`
- `plugins/slayer/.claude-plugin/plugin.json`
- `.codex-plugin/plugin.json`

Esegui la validazione dopo modifiche a versione o metadati.

## Licenza

Non è ancora stata aggiunta alcuna licenza open-source. A meno che non venga aggiunto un file `LICENSE`, tutti i diritti sono riservati al proprietario del repository.
