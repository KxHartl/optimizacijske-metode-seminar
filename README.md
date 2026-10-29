# Optimization methods: QP, robust QP, LP road levelling and LMI stabilization

**Optimizacijske metode u razvoju i upravljanju sustava**

> Seminar paper, Optimization Methods in System Development and Control, MSc in Mechatronics and Robotics, 3rd semester, FSB, University of Zagreb, 2026
>
> Student: **Krešimir Hartl** · Mentor: Prof. dr. sc. Andrej Jokić

![MATLAB](https://img.shields.io/badge/MATLAB-R2025b-orange)
![YALMIP](https://img.shields.io/badge/SDP-YALMIP%20%C2%B7%20SDPT3-6a5acd)
![LaTeX](https://img.shields.io/badge/paper-LaTeX-008080)

A seminar paper that works through four optimization problems set in the course. Each one is
reduced to a finite-dimensional problem that can be checked directly: optimality through the KKT
conditions in the first two, an LP for the third, and a common quadratic Lyapunov function as the
stability certificate in the fourth. All computations are done in MATLAB, and every number in the
paper comes from the console output of the scripts in `src/`.

**Report:**
[`for_validator/02_REPORT_PDF/OMRiUS_seminar_Kresimir_Hartl.pdf`](for_validator/02_REPORT_PDF/OMRiUS_seminar_Kresimir_Hartl.pdf)
(Croatian, version 1.6)

---

## The four tasks

| Task | Problem | Method |
|---|---|---|
| 1 | Quadratic program with two inequality constraints | convexity from the Hessian, KKT conditions, graphical solution, `quadprog`, the Lagrange dual and the sensitivity of the optimum to the constraints |
| 2 | The same QP with ±15 % interval uncertainty in the constraint coefficients | robust (worst-case) counterpart reduced to a deterministic QP, compared with the nominal solution over Monte Carlo realizations |
| 3 | Levelling a longitudinal road profile at minimum earthwork cost | finite-difference discretization, absolute deviations turned into an LP with auxiliary variables, slope and curvature limits, `linprog` for four cases |
| 4 | Stabilizing a switched linear system | Hurwitz check of each mode, open-loop simulation under switching, state-feedback gain from an LMI with a common Lyapunov function (YALMIP with SDPT3), closed-loop simulation |

## What's inside

| Folder | Contents |
|---|---|
| [`src/`](src/) | MATLAB scripts `task1_qp_analysis.m` to `task4_lmi_switched_stabilization.m`, `run_all.m`, and Python scripts that build the study textbook |
| [`docs/`](docs/) | LaTeX source of the paper (`main.tex`, `chapters/`, `figures/`), the scripts' console output in `code/`, and a study textbook for the oral defence (`udzbenik/`, `textbook/`) |
| [`for_validator/`](for_validator/) | a self-contained package for independent checking: task, report PDF, LaTeX source, code and MATLAB output |
| [`TASK/`](TASK/) | the assignment, as a scan and as Markdown |
| [`data/`](data/) | course material and literature used while working |

## Run it

The scripts need MATLAB with the Optimization Toolbox, and YALMIP with SDPT3 for task 4.

```matlab
cd src
run_all
```

`run_all` runs the four scripts and saves each console log to `docs/code/taskN_output.txt`.

Build the paper with `.\.ai\scripts\helpers\build-docs.ps1` (Windows) or
`./.ai/scripts/helpers/build-docs.sh` (Linux/macOS). It needs
[Tectonic](https://tectonic-typesetting.github.io/).

---

The repository was set up with the owner's [LiteRealm](https://github.com/KxHartl/LiteRealm) template.

## License

[Apache-2.0](LICENSE). It covers the author's own work in this repository. Third-party sources are listed, not included.
