# Design: Rahul's AI systems notebook

The profile leads with identity, then work, then supporting credentials and activity. It uses a dark engineering aesthetic with restrained color and legible project descriptions.

## Palette

| Role | Hex |
| --- | --- |
| Canvas | `#0B111B` |
| Panel | `#101B29` |
| Border | `#26374B` |
| Main text | `#F2F5FA` |
| Secondary text | `#9BAFC5` |
| Retrieval accent | `#8FE6CA` |
| Language-model accent | `#C6B5FF` |
| Vision accent | `#9CC8FF` |
| Automation accent | `#FFB78C` |

## Layout

1. Custom geometric hero with name, technical focus, university, and location.
2. Three social buttons and a small section navigation.
3. Two short introduction paragraphs.
4. Four linked project cards in a two-column GitHub-compatible table.
5. Expandable implementation details.
6. Six compact badges and a readable toolkit table.
7. Education, internships, and expandable credentials/research.
8. Actual GitHub stats plus an isometric contribution calendar after setup.
9. Contact invitation.

All SVG artwork is original and stored locally with the profile. The header mesh and card illustrations are decorative, not model architecture diagrams or performance charts. Core project descriptions remain selectable HTML text outside images.

## How the four requested resources are used

| Resource | Role in this package |
| --- | --- |
| VishwaGauravIn / GPRM | Component reference for social links, technology badges, and stats selection; hand-authored because the visual builder was inaccessible |
| anuraghazra / github-readme-stats | Actual stats and language cards fetched by the supplied workflow |
| lowlighter / metrics | Actual contribution-calendar Action configured in the supplied workflow |
| abhisheknaiidu / awesome-github-profile-readme | Layout inspiration from the minimalist, code, and Actions categories |

## Recreate the component choices in GPRM

- Username: `RahulAgarwal701`
- About: use the two introduction paragraphs in README.md.
- Socials: LinkedIn `rahul701`; email `agarwalrahul0100@gmail.com`.
- Core technologies: Python, PyTorch, FastAPI, PostgreSQL, Docker, AWS.
- Stats: general public stats plus compact languages.
- Theme target: dark canvas with mint titles and blue icons. The custom colors above are already applied by `scripts/update_stats.py`.
- Keep the custom hero/project SVGs and the metrics workflow; a stock GPRM export will not regenerate those assets.

The gallery is an inspiration resource, not a software dependency. The generator likewise does not run on your profile. The actual updating integrations are GitHub Readme Stats and lowlighter/metrics.
