---
title: "Hyperscalers Reserved $450B in Chips Nobody Can Plug In"
description: "The constraint moved while everyone was buying chips — $450B in AI capex bottlenecks at five-year transformer queues, not silicon."
date: 2026-05-02
draft: false
tags: ["ai", "infrastructure", "energy", "manufacturing", "semiconductors"]
author: "DocB"
showToc: true
TocOpen: false
---



The procurement schedule on the project manager's screen has three columns that no longer line up. The high-bandwidth memory allocation, reserved with SK Hynix in early 2024, is firm for 2027 delivery. The transformer purchase order, placed later, has no committed date — the supplier is quoting roughly five years. The grid interconnection study queue, filed in parallel, stretches at least three years and often longer.

Behind these three lines sits a slice of the $602 billion that Google, Amazon, Meta, and Microsoft have committed to artificial intelligence infrastructure in 2026, according to Introl Blog's analysis of hyperscaler capital spending. Roughly three-quarters of that — about $450 billion — is aimed at AI buildouts. The chips will arrive on time. The site will not be able to energise them.

## The Bottleneck the Industry Already Solved

For two years, the visible scarcity in AI infrastructure was memory. Samsung and SK Hynix warned that AI-driven memory shortages could last until 2027 and beyond, and customers responded by reserving supply years in advance. SK Hynix posted a 71.8% operating margin in the first quarter of 2026, almost entirely from high-bandwidth memory — a stacked memory module bonded directly to AI accelerators, the only format fast enough to keep modern graphics processors fed, according to the company's first-quarter 2026 financial results. Quarterly revenue passed 50 trillion won for the first time, reaching 52.58 trillion, per Shacknews's coverage of those same earnings.

Procurement teams at hyperscalers and chip vendors did what rational buyers do when a critical input is scarce: they bought forward. Customers are locking in HBM allocation 2-3 years ahead via direct reservations to Samsung and SK Hynix, converting a temporary memory shortage into a durable two-tier AI infrastructure market where reserved buyers retain optionality and unreserved buyers face 12-24 month delays or 20-40% premiums. Allocation follows strategic customers. An infrastructure team standing up a new graphics-processor cluster cannot assume the memory is available on the spot market for at least the next eight quarters.

Forward reservation is what supply chains do under stress. Operators identified the binding input, paid premiums to lock supply, and built a two-tier market between the reserved and the unreserved. DDR5 spot prices rose from $6.84 in September 2025 to $27.20 in December 2025. NAND flash prices are up 246% since the start of 2025. High-bandwidth memory now consumes 23% of all standard memory wafers, and data centres absorb roughly 70% of memory chips produced globally. For hyperscalers that reserved early, chips are no longer the input most likely to delay a build.


## The Bottleneck Nobody Reserved Against

The input they did not reserve against is older, lower-tech, and harder to buy past. A high-power transformer is a precision-engineered cabinet of steel cores, copper windings, and mineral oil cooling that converts grid voltage to data centre voltage. There is no substitute. Switchgear — the cabinets that route and protect that power once it arrives — depends on the same overseas supply chains and faces the same queues. The United States has limited domestic manufacturing of large power transformers relative to current demand, and prices for Chinese electrical components have roughly doubled over four years.

Lead times tell the story. Before 2020, a high-power transformer took 24 to 30 months to deliver. By 2026 the same equipment quotes at five years. Demand for power transformers rose 116% between 2019 and 2025, driven by AI data centres, manufacturing reshoring, and broader electrification. Data centres now consume about 7% of US electricity against a baseline demand growth rate of nearly 2% per year, and the PJM grid operator's interconnection queue stretches roughly four years.

Power transformer lead times have extended from 24 months to 5+ years and PJM's 4-year interconnection queue means generation capacity sits stranded behind grid infrastructure, transferring the binding constraint on AI datacenter deployment from chips to electrical equipment manufacturing. Industry observer Kevin Walmsley reported that more than half of US AI data centre projects planned for 2026 have been delayed or cancelled while waiting on electrical equipment. Less than 50% of announced 2026 capacity is under construction, and none of it is online. Over two-thirds of announced 2027 capacity has not started as of April 2026. Roughly a third of what was supposed to be 2025 capacity is still offline, slipping forward year by year. Forecasters now project $3 trillion in AI infrastructure spending over five years, all of it gated by power delivery equipment.

The cheapest, lowest-tech components in the AI stack are blocking the most expensive ones from being plugged in.

## The Constraint Migrated While the Money Was Moving

The memory reservations mature in 2026 and 2027. Transformer deliveries quoted today arrive 2029 to 2031. The grid queue clears later still. Hyperscalers are already announcing nuclear power agreements, gas turbine deals, and on-site generation that route around the transformer and queue problem for new builds. Microsoft's Three Mile Island agreement, Google's Kairos Power partnership, and Amazon's nuclear investments are bets that behind-the-meter generation will scale faster than the grid queue clears. For marginal new capacity, the queue may not remain the gating step if co-located generation proves economical at scale.

For projects dependent on grid interconnection, the binding constraint on AI data centre deployment appears to have migrated from semiconductor supply to electrical equipment manufacturing over roughly the past eighteen to twenty-four months — the same window in which buyers were optimising for chips. Hyperscalers paid early to secure the input they understood. The input they could not pre-commit against is now what determines when grid-connected buildings turn on.

Data centre developers absorb the consequence because they have already committed capital to chips, land, and construction, and cannot bill customers from facilities that are not operational. The memory line on the procurement schedule, ordered confidently in 2024, becomes inventory waiting on a transformer line ordered later or not at all.

Eduardo Barbi at Giga Energy is selling against this gap directly, advertising a seven-week transformer delivery against the industry's five-year wait — a vertically integrated bypass for buyers willing to pay a premium and accept smaller equipment. Whether that bypass scales is the open question.

The firms with the most sophisticated supply chains on earth, advised by the most expensive consultants, optimised for the constraint that was loudest and missed the one built on 19th-century electrical engineering.

## If This Thesis Is Wrong

Three things would falsify the migration reading. First, the chip story might not be solved. If high-bandwidth memory yields slip, or if a new generation of accelerators raises memory intensity faster than packaging capacity grows, chips re-enter the binding position and transformers become a parallel rather than primary gate. Second, behind-the-meter generation might scale faster than argued here. If hyperscalers can stand up gigawatt-scale gas or nuclear capacity on-site within three years, the transformer and queue constraint applies only to the long tail of smaller operators, not to the firms doing most of the spending. Third, the lead-time figure may already be peaking. Transformer capacity does not need to match the 116% demand surge to begin easing the queue; even modest expansion from Hitachi Energy, GE Vernova, or Siemens Energy could pull quoted lead times down by 2028. The honest version of this thesis: power equipment is a major constraint on grid-connected AI capacity through 2027, not a permanent ceiling on the industry.

## What to Watch

Three signals would confirm or falsify the migration over the next eighteen months. Watch transformer lead times. If Hitachi Energy, GE Vernova, Siemens Energy, or a domestic entrant announces capacity that pulls large-power-transformer quotes below two years by the end of 2027, the constraint has eased rather than relocated. The falsifiable prediction: lead times will remain materially above the pre-2020 baseline of 24 to 30 months through year-end 2027, even if they begin trending down.

Watch the PJM interconnection queue. The Federal Energy Regulatory Commission's Order 2023 is meant to clear backlogs. If PJM publishes study completion timelines below three years for new data centre loads by mid-2027, the bottleneck is dissolving rather than relocating. If the queue holds at four years or extends, the migration thesis strengthens.

Watch behind-the-meter generation announcements. Each new hyperscaler power agreement structured to bypass the transmission queue is a vote that the queue will not clear in time. If five or more gigawatt-scale on-site generation deals close in 2026, the largest buyers have already concluded the public grid cannot deliver — and the constraint has migrated again, this time from equipment manufacturing to who owns their own power plant.

The firms that will operate AI at scale in 2028 are the ones buying copper and steel today, not the ones still buying silicon.
## Sources

- *SK Hynix and Samsung memory shortages, HBM demand*, Tom's Hardware — https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond-as-hbm-demand-explodes-customers-already-reserving-supply-years-ahead-while-the-wider-dram-market-begins-to-tighten
- *SK Hynix Q1 2026 announces 1Q26 financial results*, SK Hynix — https://news.skhynix.com/q1-2026-business-results/
- *Memory price tracking across recent quarters*, Sourceability — https://sourceability.com/post/tracking-memory-price-increases-across-the-last-several-quarters
- *Hyperscaler CapEx hits $600B in 2026*, Introl — https://introl.com/blog/hyperscaler-capex-600b-2026-ai-infrastructure-debt-january-2026
