---
title: "Huawei Built the Processor. Henan Can't Plug It In."
description: "Export controls froze China at 7nm — and may have accidentally synchronised China's chip and grid timelines"
date: 2026-03-31
draft: false
tags: ["semiconductors", "china", "energy", "ai"]
showToc: false
---

# Huawei built the processor. Henan can't plug it in.

A datacenter site manager outside Zhengzhou would have the chips—if the scenario unfolding across China's AI infrastructure follows its current trajectory. Huawei's Ascend 910C processors are in production, though recent TechInsights teardown analysis reveals the Ascend 910C still contains CPU dies from TSMC dating to 2020, complicating claims of fully domestic fabrication. What facilities like hers don't have is 400 megawatts of grid interconnection. The substation upgrade that would connect her facility to Henan's provincial grid is, by the most optimistic internal estimate, thirty months away. The servers sit in a powered-down hall. The constraint she was told to worry about—semiconductors—resolved. The one nobody planned for is the one that binds.

## Shanghai's Second Fab Crosses 7 Nanometers

Hua Hong Group, China's second-largest chip manufacturer, is preparing 7nm production at its Fab 6 facility in Shanghai through its subsidiary Huali Microelectronics. Hua Hong's move matters because it breaks SMIC's monopoly as China's only domestic source of advanced-node chips. SMIC has already been producing 7nm processors, including Huawei's Kirin 9030 chip confirmed by TechInsights in December. According to reporting by Silicon UK, Hua Hong is targeting several thousand wafers per month by end of 2026, giving China two independent foundries at the node US export controls were designed to deny.

The yield penalties are real. Chinese 7nm production costs run roughly 30–50% above global benchmarks, partly because domestic equipment from firms like SiCarrier—backed by Huawei—hasn't matched the precision of ASML's lithography systems. Biren, a Chinese AI chip designer added to the US restricted entity list in 2023 and cut off from TSMC, is now prototyping on Huali's 7nm line. The restriction didn't eliminate demand. It rerouted fabrication.

Could China's 7nm chips simply be too expensive and too low-yield to matter at scale? That objection made sense in 2023. It makes less sense now. As Tom's Hardware reported, state-backed production targets call for scaling from roughly 20,000 chips per month to 100,000 by 2028 and 500,000 by 2030—a 25-fold increase. The chips are worse. They are also sufficient—at least for inference workloads and mid-scale training runs. Training LLMs at the scale of GPT-4 or Gemini requires memory bandwidth, interconnect speed, and power efficiency per FLOP that 7nm architectures struggle to match. But for the deployment China is currently pursuing, sufficiency breaks a supply constraint. Superiority doesn't have to.

The bottleneck didn't vanish. It packed its bags and left town.

## 2,300 Gigawatts in a Queue That Barely Moves

The chips flowing out of Shanghai and Wuhan need somewhere to compute. That somewhere requires electricity—and electricity requires standing in line. In the United States, 2,300 gigawatts of generation capacity now sit in interconnection queues, nearly double the country's entire operating grid capacity of roughly 1,200 GW. Median wait times approach five years in several regions. Only about 13% of projects entering the queue ever reach completion.

This isn't a generation problem. It's a transmission problem. Power exists—stranded behind bottlenecks where lines haven't been built to carry it. In Texas, ERCOT's demand for new connections exceeds available capacity by more than five times. The PJM Interconnection, managing the grid across thirteen eastern states, faces queue backlogs that industry observers estimate stretch three to eight years, with clearing rates reportedly in the range of 5–8 GW annually against a backlog exceeding 300 GW. For the first time since the Census Bureau started tracking it, America is spending more on datacenter construction ($3.57 billion) than on office buildings ($3.49 billion). The money is flowing. The electrons are not.

Google is reportedly financing a massive Texas datacenter project by Nexus, leased to Anthropic, using a "behind-the-meter" strategy—connecting natural gas generation directly to the facility to bypass grid interconnection entirely. This escape valve may be more available in the US than in China, where electricity markets are centrally regulated and behind-the-meter generation faces different regulatory barriers. That makes the grid constraint potentially more binding for Chinese operators.

Even if you halve the projections, 1,150 GW of backlogged capacity still dwarfs the grid's ability to process new connections. Reports suggest some coal plants scheduled for retirement in Virginia and Ohio are being kept online, with datacenter loads cited among the factors making their output necessary, though the specific causal link remains difficult to isolate from broader reliability concerns. The grid is running on equipment it planned to decommission.

Electricity doesn't care about your roadmap. It cares about the wire.

## The Accidental Gift of Arriving Early

Here is the counterintuitive truth: US export controls, by forcing China to stall at 7nm, may have done Beijing a strategic favor—though the durability of that advantage depends on whether China can execute grid infrastructure faster than US timelines suggest.

China's centralized grid planning and state-owned utility structure differ fundamentally from the fragmented US regulatory environment documented in PJM and ERCOT timelines. Whether Beijing has mobilized grid resources at the scale required for AI datacenter interconnection remains an open question—one that will determine whether the 3–8 year timeline borrowed from US experience applies to China's context. That track record demonstrates an ability to execute massive grid projects faster than any Western utility. China's centralized grid planning and eminent domain authority could compress those timelines considerably. If Beijing has recognized the grid bottleneck and mobilized State Grid resources at the scale of previous UHV campaigns, the 3–8 year timeline borrowed from PJM's experience may overestimate how long the constraint binds.

Had China's semiconductor industry progressed to 3nm—the cutting-edge node where TSMC and Samsung currently operate—before hitting the power constraint, the crisis would have been qualitatively different. While 3nm chips are more power-efficient per unit of computation, they enable denser configurations and higher total compute per rack, increasing aggregate datacenter power demand. The economic case for 3nm only works at massive scale, demanding even larger datacenter footprints, compounding the grid problem. A Chinese AI industry trying to scale 3nm datacenters into a grid that can't deliver interconnection would face a compounding crisis: more advanced chips demanding more power per rack, with yield penalties at 3nm far more punishing than at 7nm.

Instead, export controls froze China at 7nm—a node where yield penalties are manageable, power consumption per chip is lower, and the 30–50% cost premium is absorbable by state-backed enterprises. The controls didn't prevent China from building an AI chip industry. They may have inadvertently synchronized China's chip and grid timelines, though China's path to 3nm faced significant technical hurdles even without export controls, making the counterfactual less certain than a simple timeline comparison suggests.

The restriction was a wall. It functioned as a speed bump. Speed bumps, for a driver heading toward a cliff, are gifts.

## What to Watch

China's State Grid Corporation capital expenditure announcements for 2026–2027, expected by mid-year, will reveal whether Beijing has recognized the constraint migration. Watch specifically for datacenter-designated transmission projects in Henan, Guizhou, and Inner Mongolia—the three provinces where AI datacenter clusters are concentrating. If grid investment targeting datacenter interconnection rises above 15% of total State Grid capex, the constraint has been identified at the planning level.

In the US, PJM's interconnection queue processing rate is the leading indicator. PJM currently clears roughly 5–8 GW per year against a backlog exceeding 300 GW. If that rate doesn't double by September 2026, behind-the-meter bypass arrangements like Google's Texas project will proliferate—shifting the grid from a regulated utility model to a fragmented private-generation patchwork. The parallel to SWIFT sanctions in 2022 is instructive: when you block the main channel, traffic doesn't stop. It finds new pipes.

I predict first 7nm wafer output from Hua Hong's Fab 6 before December 31, 2026, based on the company's stated timeline and current facility preparation. But the facility will operate below 40% utilization through mid-2027 due to power interconnection delays. If not, it means China's grid buildout in the Yangtze Delta is faster than public queue data suggests—and the constraint migration described here has a shorter half-life than the 3–8 year timeline implies.

## If This Thesis Is Wrong

The strongest competing explanation is simpler: China's 7nm chips remain too low-yield and too expensive to substitute for Western alternatives at scale, and the chip constraint never actually resolved. ByteDance's recent purchase of 500 Nvidia Blackwell systems—despite Beijing's domestic push—suggests that even Chinese companies prefer Western silicon when they can get it. If domestic 7nm production capacity stays below datacenter chip demand through 2027, then chips remain the binding constraint and the migration this article describes is premature.

The weakest link in the chain is the production ramp itself. Hua Hong's "several thousand wafers per month" target is an announcement, not a shipment. The unresolved question is whether China's 7nm yield rates improve fast enough to make the 25-fold expansion plan physically achievable—or whether the controls bought more time than the timeline comparison suggests.

The wall moved. The wire didn't.


---

**Market Implication**

If this constraint migration holds, natural gas futures express the immediate bypass strategy as datacenters burn gas to avoid grid queues, while Chinese utility capex reveals whether Beijing has recognized the problem at the planning level. The prediction market question—'Will Hua Hong ship 7nm wafers before December 31, 2026?'—directly tests whether the chip constraint resolved on schedule. The thesis breaks if State Grid's 2026-2027 capex shows datacenter transmission below 10% of budget, or if PJM queue processing doubles above 16 GW/year by September 2026. The sleeper trade is copper: stranded generation needs wire, and 2,300 GW of backlog means years of transmission builds starting now.

*Analytical implication, not financial advice.*

---

## Sources

- [silicon.co.uk: hua-hong-7nm-629125](https://www.silicon.co.uk/e-innovation/artificial-intelligence/hua-hong-7nm-629125)
- [bits-chips.com: report-hua-hong-joins-smic-for-7nm-manufacturing](https://bits-chips.com/article/report-hua-hong-joins-smic-for-7nm-manufacturing/)
- [the-decoder.com: hua-hong-becomes-the-second-chinese-chipmaker-to-c](https://the-decoder.com/hua-hong-becomes-the-second-chinese-chipmaker-to-crack-7nm-manufacturing-as-beijing-pushes-for-ai-independence/)
- [macromashup.com: the-queue-where-ais-grid-constraint-gets-real](https://www.macromashup.com/p/the-queue-where-ais-grid-constraint-gets-real)
- [energycentral.com: news-as-data-centers-multiply-maryland-s-power-gri](https://www.energycentral.com/energy-management/post/news-as-data-centers-multiply-maryland-s-power-grid-struggles-to-keep-up-DHBAmhlVr9OHQRC)
- [utilitydive.com: 815934](https://www.utilitydive.com/news/interregional-transmission-winter-storm-fern-senate/815934/)
- [mintz.com: 2026-03-02-data-centers-close-2025-record-demand-r](https://www.mintz.com/insights-center/viewpoints/2896/2026-03-02-data-centers-close-2025-record-demand-rising-rents-and)
- [semiwiki.com: techinsights-teardown-huawei-ascend-910c-still-con](https://semiwiki.com/forum/threads/techinsights-teardown-huawei-ascend-910c-still-contains-cpu-dies-from-tsmc-from-2020.23737/)
- [tomshardware.com: china-to-increase-leading-edge-chip-output-by-5x-i](https://www.tomshardware.com/tech-industry/semiconductors/china-to-increase-leading-edge-chip-output-by-5x-in-two-years-report-claims-aims-to-lift-7nm-and-5nm-production-to-100-000-wafers-per-month-targeting-half-a-million-monthly-by-2030)
- [ourchinastory.com: China's-UHV-project:-The-world-leading-](https://www.ourchinastory.com/en/14967/China's-UHV-project:-The-world-leading-)
- [cudocompute.com: what-is-the-cost-of-training-large-language-models](https://www.cudocompute.com/blog/what-is-the-cost-of-training-large-language-models)
