# S2 — Digital / Product Translation

Status: PROVISIONAL / ACTIVE  
Date: 2026-10-07

## Purpose

Translate meaning into system behavior before designing screens, hardware or a final business.

The current goal is not to answer "what should we build?"

The goal is:

> If the seven meanings are true, how must a Plantupia system behave?

# Translation 01 — Context before advice

Derived from: Relational Life

A recommendation without context is weak.

Useful context may include:

- living entity
- place / zone
- light
- temperature / humidity
- substrate / container
- role of the planting
- care ownership
- prior interventions
- operational constraints

System rule:

> plant-in-context before generic species advice

# Translation 02 — Trajectory before snapshot

Derived from: Living Time

Current state is less useful than meaningful change.

Prefer questions such as:

- what changed?
- how quickly?
- compared with what baseline?
- did the intervention improve the condition?
- is this pattern repeating?

System rule:

> design for trajectories, not snapshots

# Translation 03 — Memory before intelligence

Derived from: Retained History

Intelligence should operate on retained context and causal history instead of raw data alone.

Core chain:

> Observation → Decision → Intervention → Result

System rule:

> memory before AI

# Translation 04 — Automate burden, preserve involvement

Derived from: Care Creates Relationship

Separate:

Burden:
- remembering everything
- scheduling large fleets
- repetitive documentation
- logistics
- searching history
- detecting exceptions too late

Meaningful involvement:
- observing
- touching
- pruning
- repotting
- learning
- choosing
- watching recovery / growth

System rule:

> automate the burden, not the relationship

Potential care modes may range between:

- Do it for me
- Help me do it
- Teach me to notice

These are not yet UI modes; they are relationship models.

# Translation 05 — Represent uncertainty

Derived from: Living Agency

A living system is not fully deterministic.

A system should distinguish:

- measured fact
- human observation
- rule-based estimate
- model inference
- uncertain recommendation

System rule:

> represent uncertainty instead of hiding it

# Translation 06 — Show meaning, not measurement

Derived from: Legibility

Raw sensor values are not inherently useful.

Working interaction hierarchy:

Normal state → quiet  
Meaningful change → visible  
Urgent exception → clear

System rule:

> show meaning, not measurement

The interface may be:

- screen
- timeline
- report
- subtle light
- sound
- physical cue
- message
- absence of notification

The interface is not assumed to be an app.

# Translation 07 — Evidence behind claims

Derived from: Accountable Living

Important outputs should retain provenance:

- source
- time
- method
- confidence
- observer / system where appropriate

System rule:

> every important claim should have a trail back to reality

## First abstract model

A deliberately simple first model:

Living Entity  
↕  
Context  
↕  
Observations over time  
↕  
Care / interventions  
↕  
Change / result  
↕  
Evidence / confidence

This is not a database schema.

It is a product-behavior model to test during exploration.
