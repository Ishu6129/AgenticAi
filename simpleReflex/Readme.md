# Reflex Agent Environment Simulation (Vacuum Cleaner Agent)

This project demonstrates a **simple reflex agent** operating in a **grid-based environment**, inspired by the classic **Vacuum Cleaner World** from Artificial Intelligence. The agent perceives the current room state (clean or dirty) and takes actions based solely on the current perception.

The environment and agent behavior are visualized using **Matplotlib**, showing step-by-step movement and cleaning actions.

---

## Overview

- Environment consists of **4 rooms** arranged in a 2×2 grid
- Each room can be **Clean (1)** or **Dirty (0)**
- The agent:
  - Cleans the room if dirty
  - Moves to the next room if clean
- Visualization updates dynamically for each step

---

## Environment Representation

- **Rooms:** Room1, Room2, Room3, Room4
- **State Encoding:**
  - `0` → Dirty
  - `1` → Clean
- **Color Coding:**
  - 🔴 Red → Dirty room
  - 🟢 Green → Clean room
  - 🔵 Blue → Agent position

---

## Agent Type

### Simple Reflex Agent

The agent follows a fixed rule-based policy:

- If the current room is **dirty**, clean it
- If the current room is **clean**, move to the next room

```python
def reflex_agent(state):
    if state == 0:
        return 1  # Clean
    return -1     # Move
````

This agent has **no memory** and **no model of the environment** beyond the current percept.

---

## Visualization

* Uses `matplotlib.pyplot` and `matplotlib.patches`
* Displays:

  * Room grid
  * Room state colors
  * Agent position
  * Step counter and current room
* Supports:

  * Frame-by-frame visualization
  * Continuous simulation mode

---

## Dependencies

Install required libraries using:

```bash
pip install matplotlib
```

Optional (for notebook animation):

```bash
pip install ipython
```

---

## How to Run

### Option 1: IPython / Jupyter (Frame-by-Frame)

This mode clears the output and redraws the environment at each step.

```python
from IPython.display import clear_output

steps = 8
agent_index = 0

for step in range(steps):
    current_room = rooms[agent_index]
    state = environment[current_room]
    action = reflex_agent(state)

    clear_output(wait=True)
    draw_environment(environment, agent_index, step)

    if action == 1:
        environment[current_room] = 1
    else:
        agent_index = (agent_index + 1) % len(rooms)

print("Simulation Completed")
```

---

### Option 2: Script Mode (Continuous Frames)

Best suited for running as a `.py` file.

```python
plt.ion()  # Enable interactive mode

steps = 9
agent_index = 0

for step in range(steps):
    current_room = rooms[agent_index]
    state = environment[current_room]
    action = reflex_agent(state)

    draw_environment(environment, agent_index, step)

    if action == 1:
        environment[current_room] = 1
    else:
        agent_index = (agent_index + 1) % len(rooms)

plt.ioff()
print("Simulation Completed")
```

---

## Key Concepts Demonstrated

* Simple reflex agents
* Perception-action rules
* Environment state representation
* Agent-environment interaction
* Step-wise visualization
* Matplotlib animation basics

---

## Learning Outcomes

* Understand how reflex agents operate
* Visualize agent decision-making
* Learn basic AI environment modeling
* Practice matplotlib-based animations

---

## Use Cases

* AI fundamentals demonstrations
* Introductory agent-based systems
* Educational simulations
* Visual explanation of reflex agents

---

## Author

Created as an educational demonstration of **simple reflex agents** and **environment interaction** in Artificial Intelligence.
