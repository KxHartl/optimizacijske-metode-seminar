# Defense Q&A Package & Theoretical Justifications

> **Course:** Optimization Methods in Systems Development and Control (OMRiUS)  
> **Student:** Krešimir Hartl  
> **Mentor:** Prof. Dr. Sc. Andrej Jokić  

---

### Question 1: Why does switching between two Hurwitz (stable) linear modes cause instability in open loop?
**Detailed Defense Answer:**  
Hurwitz property of individual dynamic matrices $A_{\mathrm{even}}$ and $A_{\mathrm{odd}}$ guarantees asymptotic convergence to the origin if and only if the system resides indefinitely in one isolated mode. However, each mode defines a different vector field and a distinct set of elliptic Lyapunov level curves. 

Under periodic switching (every $\Delta t = 1\text{ s}$), the state transitions to a geometric configuration where the subsequent mode's vector field has a net outward expansion component before the oscillatory damping phase takes effect. By computing the **monodromy matrix** across one full periodic cycle ($T = 2\text{ s}$):
$$\Phi_{\mathrm{cycle}} = e^{A_{\mathrm{odd}} \cdot 1} e^{A_{\mathrm{even}} \cdot 1} = e^{-2}\begin{bmatrix} -9 & 0 \\ 0 & -\frac{1}{9} \end{bmatrix} \approx \begin{bmatrix} -1.2180 & 0.0000 \\ 0.0000 & -0.0150 \end{bmatrix},$$
its spectral radius is $\rho(\Phi_{\mathrm{cycle}}) = 1.2180 > 1$ (with $\det(\Phi_{\mathrm{cycle}}) = e^{-4} \approx 0.01832$). Because discrete stroboscopic state points satisfy $x(2(k+1)) = \Phi_{\mathrm{cycle}} x(2k)$, energy is pumped along the first principal axis in every cycle, resulting in exponential spiral divergence.

---

### Question 2: Why is the robust deterministic equivalent in Task 2 exact rather than a conservative inner approximation?
**Detailed Defense Answer:**  
The uncertainty sets $\mathcal{U}_1$ and $\mathcal{U}_2$ are rectangular boxes (hyper-rectangles in $\mathbb{R}^2$), which are convex polytopes defined by $2^2 = 4$ extreme vertices each. According to support function theory and the fundamental theorem of linear programming:
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = \max_{k \in \{1, \dots, 2^n\}} (v_i^{(k)})^T x.$$
Enforcing that a candidate solution $x$ satisfies the inequality for all 8 vertices ($4$ for each constraint) is both necessary and sufficient for the constraint to hold over the entire continuous uncertainty set. Consequently, there is zero conservatism/relaxation gap, making the resulting deterministic QP an exact equivalent of the semi-infinite robust formulation.

---

### Question 3: What is the physical and economic interpretation of the Lagrange multiplier $\mu_1^* = 12.2424$?
**Detailed Defense Answer:**  
By the sensitivity theorem in nonlinear programming:
$$\frac{\partial p^*}{\partial b_1} = -\mu_1^* = -12.242424.$$
The multiplier $\mu_1^*$ represents the **shadow price** or physical constraint reaction force. At the global optimum $x^* = (5.758, 4.242)$, the objective gradient $\nabla f(x^*)$ pushes the state toward the unconstrained minimum $x_0 = (-0.898, 0.683)$, but is countered by the normal boundary gradient $\nabla g_1(x^*) = [-1, -1]^T$ with magnitude $\mu_1^* = 12.2424$. Relaxing the constraint by $\Delta b_1 > 0$ decreases the optimal cost at an instantaneous rate of $12.2424 \cdot \Delta b_1$.

---

### Question 4: Why are congruence transformation and the substitution $Y = KQ$ necessary in LMI stabilization?
**Detailed Defense Answer:**  
The original Lyapunov derivative condition for the closed-loop system is:
$$(A_i + BK)^T P + P(A_i + BK) \prec 0, \quad P \succ 0.$$
This expression contains the product of two unknown variables $P$ and $K$ ($P B K$), forming a nonconvex Bilinear Matrix Inequality (BMI). 

By pre- and post-multiplying by the regular symmetric matrix $Q = P^{-1} \succ 0$ (congruence transformation), negative definiteness is preserved while transforming $P B K$ into $B K Q$. Introducing the linearizing change of variables $Y = K Q \in \mathbb{R}^{1 \times 2}$ yields:
$$A_i Q + Q A_i^T + B Y + Y^T B^T \prec 0,$$
which is strictly affine (LMI) in $(Q, Y)$. This enables global, polynomial-time numerical solution via semidefinite programming (SDP).
