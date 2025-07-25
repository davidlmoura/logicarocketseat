# Tabelas Verdade

### 1. `p ∧ q`

| p | q | p ∧ q |
|---|---|--------|
| V | V |   V    |
| V | F |   F    |
| F | V |   F    |
| F | F |   F    |

---

### 2. `p ∨ q`

| p | q | p ∨ q |
|---|---|--------|
| V | V |   V    |
| V | F |   V    |
| F | V |   V    |
| F | F |   F    |

---

### 3. `p → q`

| p | q | p → q |
|---|---|--------|
| V | V |   V    |
| V | F |   F    |
| F | V |   V    |
| F | F |   V    |

---

### 4. `p → (q ∧ r)`

| p | q | r | q ∧ r | p → (q ∧ r) |
|---|---|---|--------|--------------|
| V | V | V |   V    |      V       |
| V | V | F |   F    |      F       |
| V | F | V |   F    |      F       |
| V | F | F |   F    |      F       |
| F | V | V |   V    |      V       |
| F | V | F |   F    |      V       |
| F | F | V |   F    |      V       |
| F | F | F |   F    |      V       |

---

### 5. `p ↔ q`

| p | q | p ↔ q |
|---|---|--------|
| V | V |   V    |
| V | F |   F    |
| F | V |   F    |
| F | F |   V    |

---

### 6. `p → (q ∨ r)`

| p | q | r | q ∨ r | p → (q ∨ r) |
|---|---|---|--------|--------------|
| V | V | V |   V    |      V       |
| V | V | F |   V    |      V       |
| V | F | V |   V    |      V       |
| V | F | F |   F    |      F       |
| F | V | V |   V    |      V       |
| F | V | F |   V    |      V       |
| F | F | V |   V    |      V       |
| F | F | F |   F    |      V       |
