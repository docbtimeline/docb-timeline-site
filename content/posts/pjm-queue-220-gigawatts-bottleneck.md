---
title: "811 Projects, 220 Gigawatts, One Bottleneck"
description: "PJM's reopened interconnection queue surfaces the constraint that's been hiding in plain sight: the wire, not the panel, not the battery, not the chip."
date: 2026-05-07
draft: false
tags: ["energy", "infrastructure", "manufacturing", "batteries"]
author: "DocB"
showToc: true
TocOpen: false
---

The solar farm has permits, financing, a signed land lease, and grid-tie equipment sitting in a Pennsylvania warehouse. The developer cannot break ground. PJM Interconnection — the grid operator covering thirteen states from Chicago to the Atlantic — closed its queue in 2022 and only reopened it on April 29, 2026. The developer's project is now one of 811 in the new cycle, behind hundreds of gigawatts of generation waiting for engineering studies under PJM's reformed cluster process.

The land lease meter is running. The interest rate on the construction loan is not.

## 220 Gigawatts Wait for a Wire

The reopened PJM queue contains roughly 220 gigawatts of nameplate capacity across 811 projects, according to JEPIC-USA's analysis of the operator's April 29 filing. Per Utility Dive's reporting on the same filing, gas-fired generation leads at 106 gigawatts — nearly half the total. Standalone storage adds another 67 gigawatts across 349 projects. Nuclear, improbably, makes up 18 gigawatts across 27 proposed units.

Maria Scheller, a vice president at ICF International, told industry press the reformed queue "promises to be smaller, stricter, and more actionable by design." The previous queue was none of those things. It was a four-year traffic jam of speculative applications that PJM eventually had to halt entirely.

The familiar story is that renewables are blocked by policy uncertainty or capital costs. The PJM numbers suggest something else: capital is queueing, technology is queueing, and the binding ceiling is the operator's ability to study, approve, and physically connect projects.

One practitioner, writing as @NeilWinward on X, put it directly: "Most models still treat interconnection as the primary constraint on grid expansion, but that assumption is increasingly outdated." His fuller argument is more challenging. In ERCOT, the Texas grid, projects connect quickly — suggesting interconnection itself is not the binding constraint. Transmission capacity is. If he is right, the PJM backlog reflects regional governance failure rather than a structural national pattern. The numbers remain either way: 220 gigawatts waiting, regardless of which label we attach to the holdup.

A skeptic could argue the reformed cluster process is precisely the fix. PJM has tightened readiness requirements, introduced AI-assisted screening, and filtered speculative applicants. If it works, the 220-gigawatt figure is a one-time backlog clearing rather than a structural ceiling. That is the optimistic reading. It assumes the reform converts a four-year queue into something closer to eighteen months. It also assumes the queue does not refill faster than it drains. Neither assumption has been tested.

Federal reform is reportedly in motion — FERC Order 2023 mandates cluster studies and ready-or-withdraw rules across regional grid operators. The unresolved question is whether these reforms resolve the constraint before its consequences harden, or merely redistribute the backlog across different stages of approval.

## Six Minutes, Three Megawatts

While developers wait years for a grid connection, the constraint they expected to face has quietly receded. CATL — Contemporary Amperex Technology, the Chinese battery maker that supplies roughly a third of the world's electric-vehicle cells — announced in spring 2026 that its third-generation Shenxing battery charges from 10% to 98% in six minutes and twenty-seven seconds. The chemistry is lithium iron phosphate, cheaper and more thermally stable than the nickel-based packs in most Western EVs. The new pack reaches an internal resistance of 0.25 milliohms, roughly half the industry average.

A six-minute charge is meaningful only if the station can deliver it. That requires power on the order of megawatts per stall — closer to a small factory's connection than a typical commercial service. A four-stall station pulls the equivalent of a 12-megawatt industrial customer. That class of connection requires the same interconnection study, transmission upgrade, and queue position as a small power plant.

One engineering workaround weakens this constraint: stations can install on-site stationary storage to deliver megawatt peaks from a much smaller grid connection. If battery-buffered charging becomes standard, the grid connection shrinks from "small power plant" to "large commercial customer." The constraint gets bypassed by deploying more of the battery technology that has just been improved.

A second practitioner, @cathode_daily, noted that CATL "conveniently forgot to publish thermal data" — no temperature curve at full rate, no cell health numbers after a thousand fast cycles. That skepticism has weight. CATL's own cold-weather demonstration (-30°C, nine minutes) was presented as eliminating cold-weather anxiety, though field performance under sustained use remains unproven. The honest reading is that the laboratory number is optimistic and the field number will be slower. Even at half the advertised speed, the power draw at the station does not change much. The constraint migrates from the cell to the wire either way.

## Safety Reviews Now Create Safety Risk

The interconnection study process exists to ensure new generation does not destabilize the grid. Engineers model load flows, fault currents, and transient stability before approving a connection. The job is necessary. It has also become so slow that it begins to defeat its own purpose.

When study timelines stretch to two or three years, renewable developers — facing land lease costs, equipment price escalation, and tax credit deadlines — withdraw. One hypothesis worth testing: the projects that survive the queue may skew toward gas plants, which carry fewer modeling complexities and clearer revenue paths. If renewable withdrawals concentrate the surviving queue around gas, and retiring units get extended to fill the gap, the study process could end up trading near-term reliability gains for longer-term reliability risk.

That pattern is not yet visible in official assessments. The North American Electric Reliability Corporation's 2026 Summer Reliability Assessment is, per @rtoinsider, "expected to present a pretty positive story" — a reassuring read, not evidence of degradation from queue delays. Watch how regulators frame the next reform: as a safety upgrade, or a safety compromise. The framing reveals which constraint they have decided is binding.

## The Queue Becomes the Multiplier

The same study process that gates the solar farm gates anything else that needs a megawatt-class grid connection. That is the projected mechanism: substation upgrades for fast-charging stations and data center power contracts enter the same cluster studies as new generation. Data center queue exposure is the most documented case so far — Dominion and AEP have both flagged hyperscaler load requests stalled behind generation studies — but the cross-sector chain remains a forecast, not yet a fully reported pattern.

MISO, the Midwest grid operator, has been derating roughly 78% of queued projects — discounting their nameplate capacity to reflect what the system can actually absorb. That is not a technology number. It is a bandwidth number. Maryland's 2025 renewable energy compliance report cited queue position as the primary reason for missing its 50% clean energy target, marking the first time a state formally blamed administrative throughput rather than project economics for a statutory shortfall.

CATL's GWh-scale Shenxing Gen3 LFP collapses much of the range/charging-time barrier, shifting the visible EV constraint from battery chemistry toward charging station density and grid peak capacity. Charging-speed chemistry is improving faster than grid connection timelines. The infrastructure problem now waits in the same queue as the solar farm. When the workaround — battery-buffered charging stations with smaller grid connections — requires the same multi-year interconnection study as the problem it was meant to bypass, the administrative constraint has become the structural one.

## If This Thesis Is Wrong

Three things would falsify this reading. First, if PJM's first reformed cluster completes studies on schedule and withdrawal rates stay below 25%, the queue was a one-time backlog, not a structural ceiling. Second, if transmission capacity rather than interconnection study throughput proves to be the binding constraint, queue reform addresses the wrong layer entirely — these are distinct problems, and conflating them obscures which fix matters. PJM's 220 GW queue tests interconnection bandwidth; whether transmission lines can deliver what interconnection approves is a separate question one step upstream. Third, if battery-buffered charging stations deploy fast enough to absorb the EV power problem before the megawatt-class connection becomes the norm, the consumer-facing edge of the thesis dissolves. Each falsifier is testable within eighteen months.

## What to Watch

PJM's reformed cycle is meant to deliver completed system impact studies for its first cluster within roughly eighteen months of the April 2026 opening. If withdrawal rates exceed 40% in the first cluster, expect calls for a fast-track process within twelve months.

Watch also for the first announced 350-kilowatt-or-higher public charging station that publishes its grid-connection contract terms. If the contract specifies on-site storage and a sub-megawatt utility feed, the workaround is winning. If it specifies a direct megawatt-class interconnection with a multi-year study window, the convergence is materializing on schedule.

Finally, watch state-level renewable target compliance reports through 2026 and 2027. If utilities begin citing queue position rather than project economics as the reason for shortfalls, the administrative constraint has formally entered the regulatory record.

The solar panels work. The batteries charge in six minutes. The wire takes four years.

## Sources

- *PJM's reformed queue draws 811 projects, 220 GW*, Power Magazine — https://www.powermag.com/pjms-first-reformed-queue-cycle-draws-811-projects-220-gw/
- *PJM interconnection queue: gas, solar, nuclear breakdown*, Utility Dive — https://www.utilitydive.com/news/pjm-interconnection-queue-gas-solar-nuclear/818824/
- *USA: over 800 new generation projects seek to connect under PJM's reformed process*, JEPIC-USA — https://www.jepic-usa.org/digests/2026/4/30/usa-over-800-new-generation-projects-seek-to-connect-under-pjms-reformed-interconnection-process
- *220 GW in PJM queue: what the record interconnection surge really means for the grid*, Construction Review Online — https://constructionreviewonline.com/220-gw-in-pjm-queue-what-the-record-interconnection-surge-really-means-for-the-grid/
- *Why the PJM queue is now mostly gas*, Heatmap News — https://heatmap.news/energy/pjm-queue-natural-gas
- *CATL Shenxing Gen3 LFP battery charging speed*, InsideEVs — https://insideevs.com/news/793596/catl-shenxing-gen3-lfp-battery-charging-speed/
- *CATL unveils six battery innovations including 350 Wh/kg condensed cells*, Charged EVs — https://chargedevs.com/newswire/catl-unveils-six-battery-innovations-including-350-wh-kg-condensed-cells/
- *CATL Shenxing third-generation announcement*, 36Kr — https://eu.36kr.com/en/p/3776717690423557
