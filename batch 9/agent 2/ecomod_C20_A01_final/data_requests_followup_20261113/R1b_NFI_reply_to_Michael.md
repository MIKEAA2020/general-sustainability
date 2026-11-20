# R1b — Reply to Michael (NFI Project Office) — ready to send

**Status:** draft. Nothing sent.
**Answers his single question, accepts the v1.3 hold, and closes the biomass-equation point.**

---

**Subject:** Re: NFI/MAGPlot data request — use in a boundary-matched biomass comparison (and yes, please hold MAGPlot to v1.3)

Dear Michael,

Thank you for the detail — it is genuinely useful, and it settles two things I would otherwise have had
to guess at. To your question, in two sentences:

> I use the plots as an **independent physical observation of forest aboveground biomass** to test
> whether improvements in national biological-supply accounts (the National Footprint and Biocapacity
> Accounts, in global hectares) are accompanied by measured biomass change at matched boundaries and
> periods — Canada being one of eight national cases. I aggregate plot-level tree records to the
> **national and ecozone level** (never publishing plot-level results), and the two things I need from
> the data are the **remeasured** stock change with its design-based uncertainty, and enough coverage
> information to say which parts of the national total are ground-sampled versus photo-plot-only or
> projected.

That last part is why I asked: the published Canada-wide change estimate is +17.639 Mt/yr with a
labelled interval of [−21.279, 56.557] Mt/yr, which spans zero, and the associated RSE and interval
do not reconcile under the ordinary definition. My interest is in whether that ambiguity is a sampling
property of a sparse, partly projected design — not in arguing the forest is declining.

**On MAGPlot — yes please, hold it to v1.3.** Your description makes the choice clear: v1.2 carries
tree data only, without compiled volume, biomass, age or the ecological plot layers, so using it for
this purpose would mean reimplementing biomass compilation across twelve contributing jurisdictions.
v1.3, compiled with an augmented version of the same compiler the NFI ground plot program uses, is both
less work and more comparable to the NFI ground plots — which is exactly what a boundary-matched
comparison needs. I would rather wait and use one compiler consistently than mix two. Please treat the
MAGPlot portion as deferred to v1.3, and keep the **NFI ground plot** portion moving now.

**On biomass equations — understood, and I am not asking for in-house material.** Published equations
are all I want to cite. Three modest asks, all about documentation rather than new content:

1. **The equation ID mapping**: which published equation (e.g. Lambert et al. 2005, Ung et al. 2008,
   as listed on p. 85 of the Compilation Procedures) applies to each biomass component, i.e. how the
   `BMEQ_*` IDs in the data resolve to published sources.
2. **Where in-house or modified equations enter**, if they do: whether the compiled biomass values for
   any species, region or component depend on equations that are unpublished, and if so roughly what
   share of records is affected. I do not need the equations themselves — I need to know which compiled
   values I can cite transparently and which I should treat as provider-compiled and not independently
   reproducible.
3. **Which data dictionary and compilation-procedures version** will accompany the extract (I see
   5.2.3, 5.3.2 and the 2.4 compilation procedures public; I will cite whatever version you send, and
   would rather not assume).

**Coordinates: still no exact coordinates.** Rounded ±10 km as originally requested. Two clarifying
notes so the DUA matches what I will actually do: I analyse at ecozone and national level using
province/territory and ecozone **attributes**, and I match remeasurements by plot and measurement
identifiers, so plot location precision does not enter my calculations at all. I also understand the
MAGPlot web services are randomized within 5 km, which is a different thing from the rounded release —
I will use the DUA'd data for v1.3 and not the WFS layer.

**Scope, unchanged otherwise:** NFI ground plots, all jurisdictions including Yukon, measurement years
through the 2022 release; no photo-plot data, no soil samples, no HILL or CASFRI layers.

**Agreement:** please send the data use agreement — I will sign and return promptly, and I am content
to complete any jurisdiction-specific form that the contributing jurisdiction requires for the v1.3
MAGPlot data when that time comes.

On the RSE/CI thread: understood that your team is investigating, and thank you for taking it on. I will
keep that question separate from this request and will not treat a resolved implementation as a change
to the published point estimate.

With thanks for the unusually clear handling of this,

Amin Abaee
Independent Researcher, Tehran, Iran — amin_abaee@ut.ac.ir
ORCID 0000-0002-0019-1842
