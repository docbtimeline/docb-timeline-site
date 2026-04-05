---
title: "2,600 Gigawatts Are Waiting. The Transformers Aren't Coming."
description: "AI chip investment created 2,600 GW of queued power demand. The grid takes five years to say yes. The transformer takes two years to arrive."
date: 2026-03-30
draft: false
tags: ["energy", "ai", "infrastructure", "semiconductors"]
showToc: false
---

# 2,600 gigawatts are waiting. The transformers aren't coming.

A facilities engineer at a mid-tier cloud provider in central Texas has spent eleven months waiting for a grid interconnection agreement on a 150-megawatt data center expansion. The substation is visible from the parking lot. The fiber is lit. The servers are purchased. But the building sits half-empty because the local utility cannot schedule the transformer upgrade that would let the facility draw its full load.

## The Queue That Eats Compute

Those queues now hold between 2,300 and 2,600 gigawatts of proposed generation and load, according to Lawrence Berkeley National Laboratory's "Queued Up: 2024 Edition" study — roughly double the entire operating capacity of the American grid. Every solar farm, every battery installation, every data center that wants to plug into the transmission system must enter a sequential study process managed by regional grid operators. Median wait times have stretched to three to six years. Only about 13 percent of projects that enter the queue ever reach commercial operation.

According to Alisa Petersen, Katie Siegner, and John Coequyt at the Rocky Mountain Institute, the Department of Energy has urged FERC to accelerate load interconnection through federal rulemaking, but faster load connections alone are insufficient without new generation to support them. You can speed up the paperwork. The grid still needs physical copper and steel.

Could FERC reform compress those timelines? Pre-screening projects for financial viability could weed out speculative filings. But the backlog is not merely administrative. Transformer lead times have stretched past two years. High-voltage cable is on allocation. The physical equipment needed to connect a 200-megawatt data center simply does not exist in domestic inventory at the scale required.

One energy consultant noted on X that some colocation operators in Texas are quietly running diesel backup generators well past their permitted annual hours — a grey-market workaround that trades emissions compliance for revenue continuity.

Does the 2,600 GW figure overstate the real constraint? The skeptic's case — that speculative renewable projects inflate the queue — has merit regionally but misses the national picture. Transformers and substation components are shared resources. A solar project in Nevada and a data center in Virginia compete for the same manufacturer's production slot.

Grid access is now the price of admission nobody budgeted for.

## Intel's 18A Gamble Meets a Wall Socket

The grid bottleneck shapes who can use the chips Intel is racing to build. As reported by Digitimes, Intel CEO Lip-Bu Tan reversed his own initial strategy in early 2026 and opened the 18A process node — Intel's sub-3nm manufacturing technology — to external foundry customers. Tan had planned to keep 18A internal-only, then changed course after seeing yield progress. Intel's stock rose roughly 6 percent on the announcement. CFO David Zinsner explained the reversal candidly: yields had improved enough monthly that Tan recognized 18A could serve outside clients.

The celebration obscures a timing problem. Intel's Ohio fabrication complex has been delayed to 2030. Yields have surpassed 60 percent as of March 2026, but Intel projects reaching the consistency needed for high-volume external commitments only by 2027. A counterpoint from @kg_market noted that 18A yields have shown consistent monthly gains — a real achievement, but one that still leaves Intel roughly eighteen months from the consistency that would let hyperscale customers commit serious volume.

Intel's chip production success depends on yield improvements and manufacturing execution. Separately, a single large AI training cluster consumes 200 megawatts. If Intel succeeds at volume production, those chips will be deployed in facilities that must clear the same interconnection queue facing all new data center construction. Neither yield investment nor fab investment addresses the constraint between a finished wafer and a running data center.

Could Intel's chips simply ship to markets with better grid access? Hyperscalers are already pursuing this path — Microsoft in Sweden and UAE, Google in Finland, Amazon in Ireland. But CHIPS Act subsidy conditions explicitly aim to keep advanced compute on American soil — though those conditions apply to Intel's subsidized fabs, not to where hyperscalers deploy inference infrastructure.

Chips without outlets are inventory, not capability.

## The Feedback Loop Nobody Priced

AI infrastructure has reversed the normal sequence of technology scaling. Demand for compute is so intense that chip investment and facility investment are racing ahead simultaneously, both assuming the grid will accommodate them. The grid, governed by sequential study processes designed for a slower era, cannot.

AI hype drives capital into chip fabrication and data center construction. That capital creates energy demand that overwhelms the grid queue. The overwhelmed queue forces project abandonment or geographic concentration into regions with available capacity. Geographic concentration increases local grid strain, which lengthens queues further. Each actor is behaving rationally within their own planning horizon. The aggregate result is a system accelerating investment into a bottleneck it is simultaneously tightening.

The facilities engineer in Texas sees this loop from the inside. Her company pre-ordered servers built on next-generation silicon. The servers arrived. The power did not. She is managing a facility at 60 percent of designed capacity, paying full lease costs on a building that cannot earn full revenue. Her problem is a 150-megawatt gap between what the grid promised and what the grid can deliver.

The largest players are finding a different path. Microsoft, Amazon, and Google are investing in behind-the-meter generation — on-site natural gas turbines, small modular reactors, and direct power purchase agreements that bypass the interconnection queue entirely. If these solutions scale, the interconnection queue becomes a constraint primarily for smaller operators. The grid constraint may not block AI infrastructure so much as concentrate it further among the few companies with balance sheets large enough to build their own power plants.

## Convergence

Every successful Intel wafer adds demand for a grid connection that takes three to six years to secure. The chip breakthrough and the power bottleneck are not parallel problems but stacked ones — solving the first loads the second harder. Washington backed domestic foundry expansion to reduce reliance on Taiwan. Grid operators now face 3-6 year connection delays in Texas, Virginia, and Ohio—the same regions where new fabs are rising. Whether policymakers anticipated trading one constraint for another remains an open question.

## What to Watch

The first signal is FERC's response to the Department of Energy's push for interconnection reform. If FERC issues a final rule with binding timelines for large-load interconnection studies by September 2026, the queue begins to decompress. Watch for whether the rule includes pre-screening for financial commitment, which could meaningfully reduce effective queue depth.

The second signal is Intel's 18A yield disclosure at its next earnings call, expected in late April 2026. If yields have crossed 65 percent and Intel names at least one external foundry customer with a binding volume commitment, the chip-side constraint is genuinely easing. If the call repeats "improving monthly" without naming a customer, the foundry pivot remains aspirational.

The third signal is ERCOT's summer 2026 capacity reserve margin, published in May. If the reserve margin falls below 10 percent, expect at least two hyperscale data center projects in Texas to announce construction pauses by August 2026.

I predict ERCOT's summer 2026 reserve margin will fall below 12 percent. If it does, watch for whether any hyperscale operator publicly defers a Texas construction timeline — that would signal the grid constraint is binding corporate capital decisions, not just engineering schedules. If not, it means behind-the-meter generation has absorbed more demand than public filings suggest, and the constraint is migrating from interconnection to fuel supply.

## If This Thesis Is Wrong

The strongest competing explanation is that the interconnection queue overstates the real constraint. If the 2,600 GW backlog is dominated by speculative renewable projects that would never have competed for the same transmission corridors or transformer deliveries as data centers, then the binding queue for AI facilities is far shorter than the headline number implies. FERC reform that pre-screens for financial commitment could reveal the effective queue for serious projects is perhaps 400 to 600 GW — still large, but manageable within a three-year horizon.

The weakest link in this article's causal chain is the assumption that AI compute demand will continue accelerating at current rates. Inference cost reductions could reduce power demand per unit of useful AI output. If the cost of inference drops faster than demand for inference grows, the power constraint loosens.

The other vulnerability is the assumption that equipment shortages are national rather than regional. If behind-the-meter solutions scale without interconnection, the stacked constraint loosens from the bottom. If private generation bypasses the queue entirely, does the grid become more resilient — or does it fragment into a two-tier system where only the wealthiest operators can power their facilities?

The transformer doesn't care who designed the chip.


---

**Market Implication**

If this thesis holds, the grid bottleneck creates three tradeable expressions. Natural gas futures (12-month strip) capture demand from behind-the-meter generation as hyperscalers bypass the 3-6 year interconnection queue. A prediction market on whether ERCOT's summer 2026 reserve margin falls below 12 percent tests the article's explicit forecast that Texas grid strain will force construction deferrals by August. The sleeper trade is transformer manufacturers like ABB: with lead times exceeding two years and 2,600 GW competing for equipment slots, suppliers capture pricing power separate from the interconnection queue itself. Kill signals: FERC reform compressing queue times below 18 months by September 2026, ERCOT reserve margin above 12% in May, or two hyperscalers publicly deferring Texas builds without self-generation alternatives by August 2026.

*Analytical implication, not financial advice.*

---

## Sources

- [utilitydive.com: 815634](https://www.utilitydive.com/spons/redefining-data-center-power-strategies-in-the-ai-era/815634/)
- [tomorrowunveiled.com: the-grid-bottleneck-why-power-not-ai-is-becoming-t](https://tomorrowunveiled.com/the-grid-bottleneck-why-power-not-ai-is-becoming-the-real-bottleneck/)
- [macromashup.com: the-queue-where-ais-grid-constraint-gets-real](https://www.macromashup.com/p/the-queue-where-ais-grid-constraint-gets-real)
- [rmi.org: interconnection-reform-ai-data-centers-generator-q](https://rmi.org/interconnection-reform-ai-data-centers-generator-queues/)
- [datacenterdynamics.com: intel-announces-18a-node-success-says-production-i](https://www.datacenterdynamics.com/en/news/intel-announces-18a-node-success-says-production-is-on-track-for-2025/)
- [tomshardware.com: intel-chip-roadmap-2026-2028](https://www.tomshardware.com/tech-industry/semiconductors/intel-chip-roadmap-2026-2028)
- [tomshardware.com: intels-make-or-break-18a-process-node-debuts-for-d](https://www.tomshardware.com/pc-components/cpus/intels-make-or-break-18a-process-node-debuts-for-data-center-with-288-core-xeon-6-cpu-multi-chip-monster-sports-12-channels-of-ddr5-8000-foveros-direct-3d-packaging-tech)
- [manufacturingdive.com: 813634](https://www.manufacturingdive.com/news/intel-manufacturing-capacity-issues-may-take-years-to-fix-amd-nvidia-tsmc/813634/)
- [telecom.economictimes.indiatimes.com: 129065343](https://telecom.economictimes.indiatimes.com/news/devices/intel-ceo-tan-shifts-strategy-18a-manufacturing-technology-now-open-to-external-clients/129065343)
- [reglobal.org: us-ferc-to-widen-authority-doe-asks-regulator-to-m](https://reglobal.org/us-ferc-to-widen-authority-doe-asks-regulator-to-make-large-load-interconnection-rules/)
- [digitimes.com: intel-lip-bu-tan-semiconductor-foundry-technology.](https://www.digitimes.com/news/a20260305VL209/intel-lip-bu-tan-semiconductor-foundry-technology.html)
- [osti.gov: 2335720](https://www.osti.gov/biblio/2335720)
- [enkiai.com: grid-interconnection-delays-2026-a-threat-to-us-en](https://enkiai.com/ai-market-intelligence/grid-interconnection-delays-2026-a-threat-to-us-energy)
