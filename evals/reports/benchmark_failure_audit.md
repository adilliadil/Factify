# Benchmark Failure Audit

- Generated: 2026-04-26T23:27:16.333491+00:00
- Results timestamp: 2026-04-26T23:27:05.019163+00:00
- Model: gpt-5.4-nano
- Commit: 4de6b4e

This report expands failed benchmark rows into a reviewable format with inputs, outputs, and evidence.
Fields are marked as not captured only when the benchmark JSON does not contain them.

## Arm 0 - Bare LLM

Failures shown: 36

### 1. AVeriTeC / av_001 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Indian Railways has been completely privatized, and as a result, scores of people working in the Railways would lose their jobs.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `false`
- **Score:** `12`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `false`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Indian Railways is not fully privatized, so job losses from privatization are not inherent.
- **Explanation:** Indian Railways is a government-owned entity under the Ministry of Railways, and it has not been completely privatized. While some private participation exists in specific areas (e.g., certain operations, services, or infrastructure projects), that does not equate to full privatization of the rail system or an automatic loss of jobs for railway employees.
- **Confidence reason:** Indian Railways remains government-owned; full privatization is incorrect.
- **Claim verdicts:**
```json
[
  {
    "claim": "Indian Railways has been completely privatized, and as a result, scores of people working in the Railways would lose their jobs.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_002 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Donald Trump said: "Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children."
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Cannot verify whether Trump made this exact statement about Biden and charter schools.
- **Explanation:** The claim quotes a specific Trump statement, but no source, date, or transcript is provided to verify the wording. While Trump has criticized Biden and Democrats on school choice and charter schools in general, confirming this exact quote requires checking a reliable transcript or contemporaneous reporting.
- **Confidence reason:** Missing source; exact quote not verifiable from context.
- **Claim verdicts:**
```json
[
  {
    "claim": "Donald Trump said: \"Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_003 - Supported

#### Input
- **Claim:** At independence, Nigeria had a population of 45 million
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true, mostly_true`
- **TLDR:** Nigeria’s population at independence was far below 45 million.
- **Explanation:** Nigeria gained independence in 1960. Most historical estimates place Nigeria’s population around the mid- to high-30 millions at that time (roughly 35–40 million), not 45 million. While exact figures vary by source and method, 45 million appears too high for 1960.
- **Confidence reason:** Historical estimates vary, but 45M seems high for 1960.
- **Claim verdicts:**
```json
[
  {
    "claim": "At independence, Nigeria had a population of 45 million",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_006 - Not Enough Evidence

#### Input
- **Claim:** Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Nigeria was not the world’s third most terrorised country in 2020 after Afghanistan and Iraq.
- **Explanation:** There is no single universally accepted ranking of “most terrorised” countries for 2020, and commonly cited global terrorism datasets (e.g., Global Terrorism Index) do not place Nigeria consistently as third behind Afghanistan and Iraq. In many rankings, Nigeria is among the most affected but its exact position varies by metric (incidents, deaths, impact) and year, and it is not reliably the third most terrorised overall in 2020.
- **Confidence reason:** Rankings vary by dataset and metric; exact third-place claim unlikely.
- **Claim verdicts:**
```json
[
  {
    "claim": "Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** It’s unclear whether South Africa police staffing increased by 50% since 2002.
- **Explanation:** The claim depends on a specific baseline (police force size in 2002) and a specific endpoint (size in the most recent year), plus whether “police force” refers to sworn officers, total employees, or another measure. Without those figures or a cited source, the 50% growth cannot be verified from general knowledge alone.
- **Confidence reason:** Missing 2002 and latest police staffing data and definitions
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_009 - Supported

#### Input
- **Claim:** Today, Nigeria grapple has a population exceeding 200 million.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `false`
- **Score:** `18`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `true, mostly_true`
- **TLDR:** Nigeria’s population is far below 200 million.
- **Explanation:** Nigeria’s population is widely estimated to be around 200 million in recent years, but the claim says it is “exceeding 200 million” today. Depending on the source and year, Nigeria may be at or slightly above 200 million, but “exceeding” is not consistently supported without a specific reference date and dataset.
- **Confidence reason:** Population estimates vary by source and year.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today, Nigeria grapple has a population exceeding 200 million.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_012 - Not Enough Evidence

#### Input
- **Claim:** Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `?`
- **Score:** `-1`
- **Confidence:** `unknown`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `?`, expected one of `unverifiable, mixed`
- **TLDR:** _not captured in this benchmark result_
- **Explanation:** _not captured in this benchmark result_
- **Confidence reason:** _not captured in this benchmark result_
- **Claim verdicts:** _not captured in this benchmark result_
- **Source stances:** _not captured in this benchmark result_

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_016 - Not Enough Evidence

#### Input
- **Claim:** You see the number today? 33.1 GDP. The biggest in the history of our country by almost triple, right? Almost triple. Now it’s very much bigger than any GDP we’ve ever had. You have to go back to the 1950s, and then it’s less than half. This is the greatest number, 33.1 percent.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `22`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The claim about 33.1% GDP and it being the highest is not supported.
- **Explanation:** The statement appears to conflate a “33.1” figure with GDP and then makes sweeping historical comparisons (“biggest in history,” “almost triple,” “go back to the 1950s”). In general, GDP levels and shares depend on whether the figure is nominal vs real, per capita vs total, and what “33.1 percent” refers to; without those definitions, the historical comparison is not credible. Also, GDP is typically reported in dollars or growth rates, not as a single “33.1 GDP” number, making the claim likely misleading or incorrect.
- **Confidence reason:** Ambiguous metrics and no country/timeframe provided.
- **Claim verdicts:**
```json
[
  {
    "claim": "You see the number today? 33.1 GDP. The biggest in the history of our country by almost triple, right? Almost triple. Now it’s very much bigger than any GDP we’ve ever had. You have to go back to the 1950s, and then it’s less than half. This is the greatest number, 33.1 percent.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_017 - Supported

#### Input
- **Claim:** Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true, mostly_true`
- **TLDR:** The claim overstates and misattributes job losses to the China trade war.
- **Explanation:** US manufacturing employment has declined over the long term due to automation, productivity gains, offshoring, and broader economic cycles. While tariffs and trade disruptions may have affected some industries and regions, attributing a specific figure like 300,000 manufacturing jobs directly to the “trade war with China” is not supported as a clear, widely accepted causal total. Estimates of trade-war impacts vary and are generally smaller and more nuanced than the claim suggests.
- **Confidence reason:** Causal attribution and job-loss totals are disputed and not well-supported.
- **Claim verdicts:**
```json
[
  {
    "claim": "Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_019 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Cannot verify whether Twitter is adding warnings to unedited Biden fracking clips.
- **Explanation:** I can’t confirm from general knowledge whether Twitter currently adds specific warnings to tweets that are unedited clips of Biden about ending fracking. Twitter’s labeling policies and enforcement vary over time and depend on the exact content and context, and no specific example or timestamp is provided.
- **Confidence reason:** No verifiable details or sources provided
- **Claim verdicts:**
```json
[
  {
    "claim": "Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. AVeriTeC / av_020 - Supported

#### Input
- **Claim:** Edo State in Nigeria has a 19% unemployment rate.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** Edo State’s unemployment rate is claimed to be 19%, but this can’t be verified here.
- **Explanation:** Unemployment rates for Nigerian states vary by source, definition (ILO vs. national labor force surveys), and year. Without a specific dataset, year, or reference, it’s not possible to confirm whether Edo State’s unemployment rate was 19% at the time implied by the claim.
- **Confidence reason:** No source or year provided for the 19% figure
- **Claim verdicts:**
```json
[
  {
    "claim": "Edo State in Nigeria has a 19% unemployment rate.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. AVeriTeC / av_027 - Refuted

#### Input
- **Claim:** The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No reliable evidence confirms PLAAF shot down an Indian Su-30 in Tibet.
- **Explanation:** There is no widely corroborated, official, or independently verified public record that the PLAAF shot down an Indian Su-30 in Tibet. Claims of air-to-air shootdowns in contested regions are often disputed and require strong evidence (e.g., verified wreckage, credible radar/ATC data, or confirmed loss by both sides). Without such substantiation, the claim cannot be confirmed or reliably denied.
- **Confidence reason:** Lack of verifiable, independent sourcing for the specific incident
- **Claim verdicts:**
```json
[
  {
    "claim": "The PLAAF has shot down an Indian Sukhoi Su-30 fighter jet in Tibet.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 13. AVeriTeC / av_028 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** U.S. President Donald Trump has suspended all travel from China.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `false`
- **Score:** `12`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `false`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Trump did not suspend all travel from China.
- **Explanation:** The U.S. implemented travel restrictions related to COVID-19, including bans on certain travelers and entry rules that changed over time. However, the claim that Trump suspended all travel from China is not accurate—restrictions were not absolute and were subject to exceptions and phased adjustments.
- **Confidence reason:** Known travel rules were partial and time-varying
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. President Donald Trump has suspended all travel from China.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 14. AVeriTeC / av_030 - Supported

#### Input
- **Claim:** A Pakistani website was hacked by an Indian cyber group to wish Pawan Kalyan a Happy Birthday.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** No reliable evidence confirms a Pakistani site was hacked by an Indian group for Pawan Kalyan’s birthday.
- **Explanation:** The claim is very specific (a particular Pakistani website, a specific Indian cyber group, and a motive tied to Pawan Kalyan’s birthday), but no sources, screenshots, or credible reporting are provided. Without independent verification from reputable cybersecurity reporting or official statements, it’s not possible to confirm whether such a hack occurred or who was responsible.
- **Confidence reason:** Missing evidence and no verifiable sourcing provided
- **Claim verdicts:**
```json
[
  {
    "claim": "A Pakistani website was hacked by an Indian cyber group to wish Pawan Kalyan a Happy Birthday.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 15. PolitiFact / pf_002 - false

#### Input
- **Claim:** Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** A claim says a secret investigation is resolved and two judges declared it over.
- **Explanation:** The claim provides no verifiable details (jurisdiction, case name, dates, or the judges’ identities) and uses a placeholder name (“John Doe”). Without specific, checkable information, it’s not possible to confirm whether any criminal investigation related to a campaign was resolved or whether two judges said it was over.
- **Confidence reason:** No identifying details to verify against public records
- **Claim verdicts:**
```json
[
  {
    "claim": "Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 16. PolitiFact / pf_003 - true

#### Input
- **Claim:** Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `false`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `true`
- **TLDR:** Orrin Hatch did not co-sponsor a 1993 health care bill with an individual mandate.
- **Explanation:** The best-known early “individual mandate” proposals in the U.S. are associated with later health reform efforts (notably Massachusetts in the 2000s) and with federal proposals that emerged after 1993. In 1993, major federal health care legislation (e.g., the Clinton-era proposals) did not center on an individual mandate in the way later reforms did, and Hatch’s role is not typically documented as co-sponsoring such a bill.
- **Confidence reason:** Mandate details and co-sponsorship specifics are unclear without sources.
- **Claim verdicts:**
```json
[
  {
    "claim": "Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 17. PolitiFact / pf_004 - barely-true

#### Input
- **Claim:** Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** It’s unclear whether Mark Herring voted to shorten sentences for sex offenders.
- **Explanation:** The claim is specific about a particular vote and its scope (sex offenders, including rapists, receiving shorter sentences). Without details such as the bill name, year, jurisdiction, or the exact vote record, it’s not possible to verify whether Mark Herring supported such a change. General knowledge about his career is insufficient to confirm this exact allegation.
- **Confidence reason:** No bill/vote details provided to verify.
- **Claim verdicts:**
```json
[
  {
    "claim": "Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 18. PolitiFact / pf_007 - false

#### Input
- **Claim:** Unfortunately, since Mr. Fosters been mayor ... there are less people employed in the city of St. Petersburg than there were prior to his taking office.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The claim about St. Petersburg employment falling under Mayor Mr. Foster can’t be verified.
- **Explanation:** The statement provides no dates, full name, or employment figures, and “Mr. Foster” is ambiguous. Without knowing which St. Petersburg (city/state/country) and the relevant time period, it’s not possible to confirm whether employment decreased after he took office.
- **Confidence reason:** Missing identifiers and data to verify employment trends
- **Claim verdicts:**
```json
[
  {
    "claim": "Unfortunately, since Mr. Fosters been mayor ... there are less people employed in the city of St. Petersburg than there were prior to his taking office.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 19. PolitiFact / pf_008 - mostly-true

#### Input
- **Claim:** "There's only four senators senior to me ... there's still 44 older than me."
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** The statement about senators older than the speaker cannot be verified.
- **Explanation:** The claim is a specific, time-dependent statement about the ages and seniority of U.S. senators relative to the speaker. Without knowing who the speaker is, when it was said, and the relevant senators’ ages at that time, it cannot be checked against public records. Therefore, the accuracy of the “44 older than me” portion is not assessable from the claim alone.
- **Confidence reason:** Missing speaker identity and date; age data not provided.
- **Claim verdicts:**
```json
[
  {
    "claim": "\"There's only four senators senior to me ... there's still 44 older than me.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 20. PolitiFact / pf_009 - true

#### Input
- **Claim:** The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mixed`, expected one of `true`
- **TLDR:** Nazi propaganda used dehumanizing slurs, but this specific linkage to those exact words is unverified.
- **Explanation:** Nazi ideology and propaganda frequently used dehumanizing language about Jews to help justify persecution and genocide. However, the claim that the specific slurs “subhuman” and “mongrel” (as quoted from Ted Nugent about Obama) were used by Nazis for that purpose is not something that can be confirmed from general knowledge alone, and the exact wording may not match historical sources.
- **Confidence reason:** Exact Nazi wording and linkage are not verifiable here.
- **Claim verdicts:**
```json
[
  {
    "claim": "The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 21. PolitiFact / pf_010 - mostly-true

#### Input
- **Claim:** Marijuana is less toxic than alcohol.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `62`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `mostly_true, true`
- **TLDR:** Marijuana is generally less acutely toxic than alcohol, but not risk-free.
- **Explanation:** Alcohol is strongly associated with acute toxicity and high rates of fatal overdoses and poisoning. Cannabis is typically less likely to cause death from overdose, but it can still impair driving, worsen some mental health conditions, and carry risks from heavy or high-potency use. Overall, “less toxic” depends on what kind of toxicity (fatal overdose vs. health harms) is being compared.
- **Confidence reason:** General medical consensus, but “toxicity” is context-dependent.
- **Claim verdicts:**
```json
[
  {
    "claim": "Marijuana is less toxic than alcohol.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 22. PolitiFact / pf_011 - true

#### Input
- **Claim:** Says Donald Trump has changed his mind on abortion.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** It’s unclear whether Trump has changed his mind on abortion.
- **Explanation:** Whether Donald Trump has “changed his mind” on abortion depends on comparing his past and current statements and policy positions. Without specific dates, quotes, or the exact claim of what changed, it’s not possible to verify the assertion directly.
- **Confidence reason:** No specifics or evidence provided to compare positions.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Donald Trump has changed his mind on abortion.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 23. PolitiFact / pf_012 - false

#### Input
- **Claim:** A new ruling by the EPA would force dairy farmers to comply with the Spill Prevention, Control and Countermeasure Program when dealing with spilt milk -- the same regulations oil and natural gas producers must follow.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** EPA ruling would extend SPCC spill rules to dairy farms like oil and gas.
- **Explanation:** The claim hinges on a specific “new ruling” by the EPA and its scope, but no details (date, rule name, or regulatory citation) are provided. In general, the EPA’s Spill Prevention, Control, and Countermeasure (SPCC) requirements apply to certain facilities handling oil, and whether dairy operations fall under SPCC depends on factors like oil storage/handling and regulatory thresholds, not on a blanket category of “dairy.” Without the actual ruling text or citation, it’s not possible to confirm that dairy farmers are being newly required to comply in the way described.
- **Confidence reason:** No ruling details or citation to verify scope.
- **Claim verdicts:**
```json
[
  {
    "claim": "A new ruling by the EPA would force dairy farmers to comply with the Spill Prevention, Control and Countermeasure Program when dealing with spilt milk -- the same regulations oil and natural gas producers must follow.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 24. PolitiFact / pf_013 - mostly-true

#### Input
- **Claim:** Missouri is #1 in the nation for holding down tuition increases at public universities.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `mostly_true, true`
- **TLDR:** Missouri is not clearly #1 nationally for limiting public-university tuition increases.
- **Explanation:** There is no single, universally accepted national ranking that consistently places Missouri #1 for holding down tuition increases at public universities. Tuition growth varies by year, measure (percent vs dollar change), and whether rankings use in-state vs out-of-state, net vs sticker tuition, or specific time windows. Without a specific dataset and methodology, the “#1 in the nation” claim is not reliably supported.
- **Confidence reason:** No clear universal ranking; claim lacks methodology and timeframe
- **Claim verdicts:**
```json
[
  {
    "claim": "Missouri is #1 in the nation for holding down tuition increases at public universities.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 25. PolitiFact / pf_014 - half-true

#### Input
- **Claim:** Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** The claim about a 95% survey finding is not verifiable from general knowledge.
- **Explanation:** I’m not aware of a widely documented, credible survey showing that 95% of people caught crossing the U.S.-Mexico border said they came because they were promised amnesty. Without the survey source, methodology, date, and question wording, the figure cannot be checked for accuracy or context.
- **Confidence reason:** No survey details or source provided to verify.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 26. PolitiFact / pf_015 - false

#### Input
- **Claim:** When undocumented children are picked up at the border and told to appear later in court ... 90 percent do not then show up.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The claim’s “90% don’t show up” figure can’t be verified from general knowledge alone.
- **Explanation:** General reporting on immigration court attendance often cites that many people fail to appear, but the exact percentage for “undocumented children” picked up at the border and later told to appear varies by study, time period, and data source. Without a specific citation or methodology for the “90 percent” figure, it’s not possible to confirm whether it is accurate.
- **Confidence reason:** No source or methodology for the 90% figure
- **Claim verdicts:**
```json
[
  {
    "claim": "When undocumented children are picked up at the border and told to appear later in court ... 90 percent do not then show up.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 27. PolitiFact / pf_017 - true

#### Input
- **Claim:** In the last 10 years, Georgias middle class income has dropped $6,500.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true`
- **TLDR:** The claim can’t be verified without a specific data source and definition.
- **Explanation:** “Middle class income” and “dropped $6,500” depend on how middle class is defined (income percentile ranges, household vs. individual, inflation-adjusted or nominal) and which countrywide dataset is used. Without the underlying study or dataset for Georgia (state vs. country) and the time window, the $6,500 figure cannot be checked against known income statistics.
- **Confidence reason:** Missing definitions, geography, and source data.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the last 10 years, Georgias middle class income has dropped $6,500.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 28. PolitiFact / pf_018 - half-true

#### Input
- **Claim:** Oil production is down 14 percent this year on federal land.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Cannot verify whether federal-land oil production is down 14% this year.
- **Explanation:** The claim depends on a specific dataset (e.g., U.S. federal onshore oil production), a defined time window (“this year”), and the source used to compute the 14% figure. Without those details or a cited report, it’s not possible to confirm the magnitude or even the direction of change.
- **Confidence reason:** Missing source, timeframe, and definition of “federal land”
- **Claim verdicts:**
```json
[
  {
    "claim": "Oil production is down 14 percent this year on federal land.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 29. PolitiFact / pf_019 - barely-true

#### Input
- **Claim:** Onion Creeks highest flow rate on a recent night of flooding was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** The claim’s specific numbers can’t be verified from general knowledge alone.
- **Explanation:** “Onion Creeks” and its reported peak flood flow of 120,000 cubic feet per second is not a widely standardized, globally known figure, and the claim provides no date, location, or source. While Niagara Falls’ average flow is often cited around 85,000–90,000 cfs, whether 120,000 cfs is “nearly double” depends on the exact baseline and the Onion Creek measurement method.
- **Confidence reason:** No sources or identifiers for Onion Creek or the flood event.
- **Claim verdicts:**
```json
[
  {
    "claim": "Onion Creeks highest flow rate on a recent night of flooding was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 30. PolitiFact / pf_020 - pants-fire

#### Input
- **Claim:** U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence."
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false`
- **TLDR:** The claim about Langevin opposing a border fence for safety fears can’t be verified here.
- **Explanation:** I can’t verify whether Rep. Jim Langevin made this specific statement or held that exact rationale without the underlying source (e.g., a quote, interview, or transcript). In general, politicians’ positions on border fencing vary, but attributing a precise motive like “afraid someone will get hurt trying to go around the fence” requires direct evidence.
- **Confidence reason:** No source or quote provided to confirm motive.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration \"because he is afraid that someone will get hurt trying to go around the fence.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 31. PolitiFact / pf_021 - half-true

#### Input
- **Claim:** Says he brought 1,200 jobs to Texas by moving his factories here from China.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** The claim that 1,200 jobs were brought to Texas from China is not verifiable here.
- **Explanation:** Whether a specific person “brought 1,200 jobs to Texas” by moving factories from China depends on verifiable, sourced employment and investment records. Without the person’s identity, company details, dates, and documentation (e.g., official announcements, labor statistics, or filings), the number and causation cannot be confirmed or refuted from general knowledge alone.
- **Confidence reason:** Missing identity and sourcing for the job figure
- **Claim verdicts:**
```json
[
  {
    "claim": "Says he brought 1,200 jobs to Texas by moving his factories here from China.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 32. PolitiFact / pf_022 - mostly-true

#### Input
- **Claim:** Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** Cannot verify the alleged layoffs and Kasich super PAC donation tied to state tax breaks.
- **Explanation:** The claim references specific events (a company receiving state tax breaks, later laying off 100 Ohioans, and its CEO donating about $500,000 to Kasich’s super PAC) but provides no company name, dates, or sources. Without those details, it’s not possible to confirm whether the layoffs occurred, whether the company received tax breaks, or whether the CEO made the stated donation.
- **Confidence reason:** Missing identifying details and evidence to verify.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 33. PolitiFact / pf_025 - mostly-true

#### Input
- **Claim:** Federal spending on entitlements is projected to consume all revenue by 2045.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `62`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `mostly_true, true`
- **TLDR:** Entitlement spending is projected to consume most revenue by 2045, but not necessarily all.
- **Explanation:** Long-run budget projections from sources like the CBO and Social Security Trustees commonly show that by the mid-2040s, spending on major entitlements (especially Social Security and Medicare) would rise to levels that are roughly comparable to, or exceed, dedicated revenue streams and a large share of total federal revenues. However, the exact phrasing “consume all revenue by 2045” depends on the specific baseline, definition of “entitlements,” and whether it refers to total revenues or only certain categories. In many projections, total spending exceeds revenues well before or around that period, but “all revenue” is not a universal, unambiguous outcome across all assumptions.
- **Confidence reason:** Varies by projection source and definitions of revenue/entitlements.
- **Claim verdicts:**
```json
[
  {
    "claim": "Federal spending on entitlements is projected to consume all revenue by 2045.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 34. PolitiFact / pf_028 - barely-true

#### Input
- **Claim:** Says Tom Cottons vote in Congress to change Medicare will increase out-of-pocket expenses for every senior in Arkansas.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** Cotton’s Medicare vote would raise every Arkansas senior’s out-of-pocket costs.
- **Explanation:** The claim is very specific (“every senior in Arkansas”) and depends on the exact Medicare legislation, its provisions, and how out-of-pocket costs would change for different beneficiaries. Without details of the bill and cost estimates, it’s not possible to verify that all Arkansas seniors would necessarily face higher out-of-pocket expenses.
- **Confidence reason:** Missing bill details and beneficiary cost estimates
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Tom Cottons vote in Congress to change Medicare will increase out-of-pocket expenses for every senior in Arkansas.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 35. PolitiFact / pf_029 - mostly-true

#### Input
- **Claim:** Says Hillary Clinton called the Trans-Pacific Partnership the gold standard. You called it the gold standard of trade deals. You said its the finest deal youve ever seen.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_true, true`
- **TLDR:** The claim about Clinton calling TPP the “gold standard” can’t be verified here.
- **Explanation:** This is a specific attribution of quotes to Hillary Clinton and to “you,” but no sources, dates, or direct excerpts are provided. Without the original statements or a verifiable transcript/link, it’s not possible to confirm whether Clinton used that exact phrasing or whether the “you” quote is accurate.
- **Confidence reason:** No primary sources or transcripts provided
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Hillary Clinton called the Trans-Pacific Partnership the gold standard. You called it the gold standard of trade deals. You said its the finest deal youve ever seen.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 36. PolitiFact / pf_030 - true

#### Input
- **Claim:** Today California is kicking our butt, creating more jobs and more economic growth than Texas.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true`
- **TLDR:** California is not clearly outperforming Texas today in jobs and growth.
- **Explanation:** California’s economy is large, but recent years have not shown a consistent, clear lead over Texas in job creation and growth. Texas has generally been among the fastest-growing U.S. states for population and job growth, while California has faced higher costs and slower job growth in some periods. Without specific time frame and metrics, the claim is too broad and likely inaccurate.
- **Confidence reason:** Broad, time-unclear claim; general trends suggest Texas leads.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today California is kicking our butt, creating more jobs and more economic growth than Texas.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{}
```

#### Baseline Prompt
_No evidence sources are used for the bare LLM baseline._
#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

## Arm A - Gold Evidence

Failures shown: 9

### 1. AVeriTeC / av_002 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Donald Trump said: "Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children."
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources don’t provide evidence that Biden vowed to oppose school choice or close charter schools.
- **Explanation:** None of the sources directly quote or document the specific claim that Biden vowed to oppose school choice and close down charter schools. Source 3 says Biden supports “good charter schools” and allowing students to pick among public schools (school choice options), which conflicts with the “close down charter schools” and “oppose school choice” parts, but it does not address the exact “vowed” quote. Source 4 only mentions the Biden administration pushing for more oversight of charter school funding, not closing charter schools.
- **Confidence reason:** No direct evidence of the quoted vow; partial, indirect coverage only.
- **Claim verdicts:**
```json
[
  {
    "claim": "Donald Trump said: \"Biden also vowed to oppose school choice and close down charter schools, ripping away the ladder of opportunity for Black and Hispanic children.\"",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.edchoice.org/school-choice/what-is-school-choice/#:~:text=In%20a%20nutshell%3A%20School%20choice,other%20learning%20environment%20families%20choose.": "neutral",
  "https://en.wikipedia.org/wiki/Charter_schools_in_the_United_States#:~:text=Charter%20schools%20in%20the%20United%20States%20are%20primary%20or%20secondary,funded%20with%20public%20tax%20dollars.": "neutral",
  "https://web.archive.org/web/20210118102704/https://www.edchoice.org/school-choice/types-of-school-choice/": "contradicting",
  "https://www.edweek.org/policy-politics/federal-funding-and-charter-school-closures-what-the-latest-government-data-show/2022/10": "neutral"
}
```

#### Gold Evidence Input
1. **What is 'school choice'**
   URL: https://www.edchoice.org/school-choice/what-is-school-choice/#:~:text=In%20a%20nutshell%3A%20School%20choice,other%20learning%20environment%20families%20choose.
   Content: School choice allows public education funds to follow students to the schools or services that best fit their needs —whether that’s to a public school, private school, charter school, home school or any other learning environment families choose

2. **What are U.S charter schools?**
   URL: https://en.wikipedia.org/wiki/Charter_schools_in_the_United_States#:~:text=Charter%20schools%20in%20the%20United%20States%20are%20primary%20or%20secondary,funded%20with%20public%20tax%20dollars.
   Content: Charter schools in the United States are primary or secondary education institutions that are funded through taxation and operated by private organizations, rather than local school districts. They do not charge tuition, as they are funded with public tax dollars

3. **Did Joe Biden oppose school choice?**
   URL: https://web.archive.org/web/20210118102704/https://www.edchoice.org/school-choice/types-of-school-choice/
   Content: he supports good charter schools and allowing students to pick among public schools. Those also qualify as school choice options.

4. **Did Joe Biden want to close down charter schools?**
   URL: https://www.edweek.org/policy-politics/federal-funding-and-charter-school-closures-what-the-latest-government-data-show/2022/10
   Content: The Biden administration did controversially push for more oversight when it comes to charter school funding.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false, mostly_false`
- **TLDR:** Employment rose from 132,310 (2002/03) to 192,277 (2018/19), not 50% since 2002.
- **Explanation:** Source 1 reports 132,310 people employed in the SA police force in 2002/03, while Source 2 reports 192,277 employed in 2018/19. That increase is about 45% (192,277/132,310 ≈ 1.45), which is close to but not exactly the claimed 50% growth. Source 3’s 45.3% figure aligns with this calculation, but it does not directly establish “since 2002” as a precise 50% figure.
- **Confidence reason:** Only two employment datapoints; growth period and exact 50% not directly shown.
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20200918235056/https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/documents/2003/saps_annreport_0203_part3.pdf#page=5": "supporting",
  "https://web.archive.org/web/20210603081707/https://www.saps.gov.za/about/stratframework/annual_report/2018_2019/saps_annualreport2018_2019v2.pdf#page=41": "supporting",
  "https://www.calculator.net/": "supporting"
}
```

#### Gold Evidence Input
1. **How many people were employed in the SA police force in 2002/03**
   URL: https://web.archive.org/web/20200918235056/https://www.westerncape.gov.za/sites/www.westerncape.gov.za/files/documents/2003/saps_annreport_0203_part3.pdf#page=5
   Content: 132,310

2. **How many people were employed in SA police force in 2018/19**
   URL: https://web.archive.org/web/20210603081707/https://www.saps.gov.za/about/stratframework/annual_report/2018_2019/saps_annualreport2018_2019v2.pdf#page=41
   Content: 192,277

3. **What is the percentage growth in the SA police force between 2002 to 2019**
   URL: https://www.calculator.net/
   Content: 45.3%

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_010 - Refuted

#### Input
- **Claim:** UNESCO declared Nadar community as the most ancient race in the world.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The sources do not mention UNESCO or any declaration about Nadars being the oldest race.
- **Explanation:** Source 1 describes the Nadar community as a caste in Tamil Nadu and Kerala, but it does not mention UNESCO or any claim about being the most ancient race. Source 2 discusses a DNA study suggesting the San people may be the oldest human population, with no reference to UNESCO or Nadars.
- **Confidence reason:** No source addresses UNESCO or the specific claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "UNESCO declared Nadar community as the most ancient race in the world.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.familytreedna.com/groups/nadar/about/background": "neutral",
  "https://www.independent.co.uk/news/science/world-s-most-ancient-race-traced-in-dna-study-1677113.html": "neutral"
}
```

#### Gold Evidence Input
1. **What is Nadar?**
   URL: https://www.familytreedna.com/groups/nadar/about/background
   Content: Nadar (also referred as Nadan, Shanar) is a caste of Tamil Nadu & Kerala, South India. The Nadars are an entrepreneurial south Indian caste] and constitute 12% of Tamil Nadu's population. The Nadar community was not a singular caste, but an assortment of sub-castes and classes of different origins, which in course of time, came under the single banner Nadar. Nadars are predominant in the southern districts of Tuticorin, Kaniyakumari, Tirunelveli and Virudhunagar.

2. **What is the world's most ancient race?**
   URL: https://www.independent.co.uk/news/science/world-s-most-ancient-race-traced-in-dna-study-1677113.html
   Content: The San people of southern Africa, who have lived as hunter-gatherers for thousands of years, are likely to be the oldest population of humans on Earth, according to the biggest and most detailed analysis of African DNA.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_013 - Refuted

#### Input
- **Claim:** Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** Sources don’t verify the 21-times instruction; they only mention a related claim and general linkage.
- **Explanation:** Source 1 states that an article claims Ebeneezer is a medical doctor and herbal practitioner at Amuzu Hospital and that men must have sex at least 21 times a month to avoid prostate cancer, but it does not independently confirm the instruction. Source 2 only addresses whether sex/ejaculation amount is linked to prostate cancer, without validating the specific “21 times a month” guidance or attributing it to Dr. Ebeneezer.
- **Confidence reason:** Specific attribution and 21-times figure not confirmed.
- **Claim verdicts:**
```json
[
  {
    "claim": "Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210119165100/https://www.westafricareporters.com/men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer-expert/": "neutral",
  "https://web.archive.org/web/20201228105910/https://www.sciencedirect.com/science/article/abs/pii/S0302283816003778?via%3Dihub": "neutral"
}
```

#### Gold Evidence Input
1. **Who is Dr Ebeneezer?**
   URL: https://web.archive.org/web/20210119165100/https://www.westafricareporters.com/men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer-expert/
   Content: The original article claims Ebeneezer is a medical doctor and a herbal practitioner at the Amuzu Hospital

2. **Is amount of sex or ejaculation linked to prostate cancer?**
   URL: https://web.archive.org/web/20201228105910/https://www.sciencedirect.com/science/article/abs/pii/S0302283816003778?via%3Dihub
   Content: Yes

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_015 - Not Enough Evidence

#### Input
- **Claim:** In the US lockdowns are partly responsible for excess deaths not directly attributed to COVID-19 which were observed in 2020.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources don’t support lockdowns causing excess deaths; they only discuss excess deaths and missing lockdown mentions.
- **Explanation:** Source 1 (CDC MMWR) estimates excess deaths in 2020 and notes that excess deaths may include deaths directly or indirectly attributable to COVID-19, but it does not attribute the excess to lockdowns. Sources 2 and 3 explicitly state that the studies they refer to “do not mention lockdown factors in the excessive deaths,” which contradicts the claim that lockdowns are partly responsible.
- **Confidence reason:** CDC discusses excess deaths but not lockdown causation; other sources deny lockdown mention.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the US lockdowns are partly responsible for excess deaths not directly attributed to COVID-19 which were observed in 2020.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm": "neutral",
  "https://web.archive.org/web/20210310112506/https://jamanetwork.com/journals/jama/fullarticle/2771761": "contradicting",
  "https://web.archive.org/web/20210309181157/https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm": "contradicting"
}
```

#### Gold Evidence Input
1. **How is  lockdown partly responsible for excess deaths in the US ?**
   URL: https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm
   Content: As of October 15, 216,025 deaths from coronavirus disease 2019 (COVID-19) have been reported in the United States*; however, this number might underestimate the total impact of the pandemic on mortality. Measures of excess deaths have been used to estimate the impact of public health pandemics or disasters, particularly when there are questions about underascertainment of deaths directly attributable to a given event or cause (1–6).† Excess deaths are defined as the number of persons who have died from all causes, in excess of the expected number of deaths for a given place and time. This report describes trends and demographic patterns in excess deaths during January 26–October 3, [...]

2. **Do the studies used to make the claim include lockdowns relating to excessive deaths?**
   URL: https://web.archive.org/web/20210310112506/https://jamanetwork.com/journals/jama/fullarticle/2771761
   Content: they do not mention lockdown factors in the excessive deaths

3. **Do the studies used to make the claim include lockdowns relating to excessive deaths?**
   URL: https://web.archive.org/web/20210309181157/https://www.cdc.gov/mmwr/volumes/69/wr/mm6942e2.htm
   Content: they do not mention lockdown factors in the excessive deaths

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_018 - Not Enough Evidence

#### Input
- **Claim:** There was a 40% drop in the price of oil, Nigeria's main export.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources do not support a 40% oil-price drop; one cites a 73% fall.
- **Explanation:** Source 1 reports that Nigeria’s monthly average oil prices decreased 73% from January to April 2020, not 40%. Source 2 only discusses that oil prices fluctuate, without giving any specific percentage drop or linking it to a 40% decline.
- **Confidence reason:** Only one source gives a specific drop figure, and it differs.
- **Claim verdicts:**
```json
[
  {
    "claim": "There was a 40% drop in the price of oil, Nigeria's main export.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210405033525/https://nnpcgroup.com/NNPCDocuments/Performance%20Data/FullReports/NNPC%20Monthly%20Financial%20and%20Operations%20Report%20for%20the%20Month%20of%20July%202020.pdf": "supporting",
  "https://scialert.net/fulltext/?doi=aujss.2017.1.16#:~:text=The%20surplus%20of%20exporting%20value,great%20challenges%20for%20policy%20making.": "neutral"
}
```

#### Gold Evidence Input
1. **How much did Nigerian oil prices fall in 2020?**
   URL: https://web.archive.org/web/20210405033525/https://nnpcgroup.com/NNPCDocuments/Performance%20Data/FullReports/NNPC%20Monthly%20Financial%20and%20Operations%20Report%20for%20the%20Month%20of%20July%202020.pdf
   Content: According to data from July 2020 from the Nigerian National Petroleum Corporation, monthly average prices decreased 73% from January to April 2020.

2. **Are there frequent fluctuations in Nigeria's oil prices?**
   URL: https://scialert.net/fulltext/?doi=aujss.2017.1.16#:~:text=The%20surplus%20of%20exporting%20value,great%20challenges%20for%20policy%20making.
   Content: Oil prices have witnessed profound fluctuations and this has implications for the performance of macroeconomic variables, posing great challenges for policy making.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_019 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** The sources don’t provide evidence about Biden/fracking-specific warnings.
- **Explanation:** Source 1 discusses general Twitter election-related changes, including encouraging Quote Tweets and warning users to read content before retweeting. Source 2 is a generic “Yes” to a question about warnings on unedited Biden fracking tweets, but it does not provide underlying evidence or details beyond that single word. Because the sources don’t specifically document warnings on Biden fracking clips, the claim can’t be confirmed or refuted from the provided material.
- **Confidence reason:** Only one vague “Yes”; no specific documentation for Biden fracking warnings.
- **Claim verdicts:**
```json
[
  {
    "claim": "Twitter now putting warnings on tweets that are just unedited clips of Biden saying he would end fracking",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20201101032342/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html": "neutral",
  "https://web.archive.org/web/20201101024709/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html": "neutral"
}
```

#### Gold Evidence Input
1. **Have Twitter started putting warnings on tweets that are just unedited clips of Biden saying he would end fracking?**
   URL: https://web.archive.org/web/20201101032342/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html
   Content: Twitter automatically warns when the user has not opened and read the item to be re-tweeted. "Headlines don't tell the whole story," the Twitter message says. "You can read the article on Twitter before Retweeting." Twitter announced a set of changes to try to stem the spread of misinformation ahead of the November 3, 2020 presidential election. Among the most significant is a request that users add their own content before retweeting someone else's: (W)e will encourage people to add their own commentary prior to amplifying content by prompting them to Quote Tweet instead of Retweet. People who go to Retweet will be brought to the Quote Tweet composer where they'll be encouraged to [...]

2. **Had Twitter been putting warnings on un-edited tweets about Biden saying he would end fracking at the time of the claim (October 2020)?**
   URL: https://web.archive.org/web/20201101024709/https://blog.twitter.com/en_us/topics/company/2020/2020-election-changes.html
   Content: Yes

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_023 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** Even if your mail-in ballot is postmarked prior to the Election day but arrives after the Election day it will be thrown out.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** The sources don’t say what happens when a ballot is postmarked before Election Day but arrives after.
- **Explanation:** Source 2 only states that Wisconsin (and about 30 states) require absentee ballots to be received by Election Day to be counted, which does not specifically address the postmark-before/arrival-after scenario. Source 1 is about state deadline rules generally, and Source 3 contains no relevant information (“No”). None of the sources explicitly confirm that such ballots are always thrown out.
- **Confidence reason:** No source directly addresses postmark-before/arrive-after rule.
- **Claim verdicts:**
```json
[
  {
    "claim": "Even if your mail-in ballot is postmarked prior to the Election day but arrives after the Election day it will be thrown out.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.buzzfeednews.com/article/addybaird/vote-by-mail-state-deadlines": "neutral",
  "https://www.cbsnews.com/news/wisconsin-election-supreme-court-rules-againt-absentee-ballots-after-election-day/": "neutral",
  "https://www.facebook.com/GilbertLiz/photos/a.356148997800555/3549940058421417": "neutral"
}
```

#### Gold Evidence Input
1. **Do some states accept ballots that were postmarked before election day?**
   URL: https://www.buzzfeednews.com/article/addybaird/vote-by-mail-state-deadlines
   Content: There are 22 states plus the District of Columbia

2. **Are there states which do require votes to arrive by election day.**
   URL: https://www.cbsnews.com/news/wisconsin-election-supreme-court-rules-againt-absentee-ballots-after-election-day/
   Content: Wisconsin is one of about 30 states that require absentee ballots be received by Election Day to be counted.

3. **Does the original posterLiz Gilbert mention the state that does not allow voting after deadline?**
   URL: https://www.facebook.com/GilbertLiz/photos/a.356148997800555/3549940058421417
   Content: No

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_029 - Refuted

#### Input
- **Claim:** Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** Sources don’t confirm Trump suspended all China travel before the first U.S. case.
- **Explanation:** Source 1 only provides the date the first U.S. COVID-19 case was discovered (21 January 2020) and does not describe any presidential travel action. Source 2 discusses travel restrictions after the ban, but it does not state that Trump suspended all travel from China before the first U.S. case or characterize the action as “unprecedented.”
- **Confidence reason:** Sources lack direct evidence for timing and scope of the travel suspension.
- **Claim verdicts:**
```json
[
  {
    "claim": "Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://web.archive.org/web/20210502100658/https://www.cdc.gov/media/releases/2020/p0121-novel-coronavirus-travel-case.html": "neutral",
  "https://web.archive.org/web/20210503140609/https://www.nytimes.com/2020/04/04/us/coronavirus-china-travel-restrictions.html": "neutral"
}
```

#### Gold Evidence Input
1. **When was the first case of COVID-19 discovered in the US**
   URL: https://web.archive.org/web/20210502100658/https://www.cdc.gov/media/releases/2020/p0121-novel-coronavirus-travel-case.html
   Content: 21st January 2020

2. **How many people were still travelling after the travel ban on China after the discovery of the novel coronavirus in the US**
   URL: https://web.archive.org/web/20210503140609/https://www.nytimes.com/2020/04/04/us/coronavirus-china-travel-restrictions.html
   Content: There were 1,300 direct flights to 17 cities before President Trump’s travel restrictions. Since then, nearly 40,000 Americans and other authorized travelers have made the trip

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

## Arm B - Searched Evidence

Failures shown: 24

### 1. AVeriTeC / av_006 - Not Enough Evidence

#### Input
- **Claim:** Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `false`
- **Score:** `15`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say the 2020 ranking image used 2019 data, not a 2020 GTI release.
- **Explanation:** Source 3 (AFP) states the publisher (IEP) confirmed there was no 2020 terrorism index yet and that the viral screenshot showed 2019 data; it also notes Nigeria genuinely ranked third in 2019. Source 1 (HumAngle) similarly concludes it is false to claim Nigeria was ranked third most terrorised in 2020 because no such report had been released, and Source 2 (FactCheckHub) calls the infographic misleading because the 2020 GTI ranking had not been released and the graphic used older data.
- **Confidence reason:** Multiple fact-checks directly address and refute the 2020 ranking claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/": "contradicting",
  "https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/": "contradicting",
  "https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa": "contradicting",
  "https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism": "neutral",
  "https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf": "neutral"
}
```

#### Search Evidence Input
1. **Factcheck: Nigeria Not Ranked Third Most Terrorised Country In 2020 - HumAngle**
   URL: https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/
   Content: A Twitter account belonging to the leader of the Indigenous People of Biafra, Nnamdi Kanu, claimed on September 9 that Nigeria ranked second in the world, but this is not true. (The tweet was retweeted over 5,000 times and liked by over 4,200 users.) The report ranked Nigeria as the third-worst among a total of 163 countries, behind Afghanistan and Iraq. Trailing after the country were Syria, Pakistan, Somalia, India, Yemen, Philippines, and D.R. Congoㅡ as reported by TVC. Kanu quoted the GTI as stating that “the countries most heavily affected by terrorism are Iraq, Afghanistan, #Nigeria, Pakistan and Syria. Terrorism increased most significantly in Nigeria, where deaths increased by [...]

2. **Misleading 2020 global terrorism ranking resurfaces online - FactCheckHub**
   URL: https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/
   Content: However, when the 2020 list was released, Nigeria still ranked third and Afghanistan and Iraq ranked first and second respectively as shared in the image. Even though the countries on the list remained the same, the ranking for five of them had changed. The infographic has Afghanistan, Iraq, Nigeria, Syria, Pakistan, Somalia, India, Yemen, Philippines and DR Congo as the top ten, the actual ranking released differs in order; Afghanistan, Iraq, Nigeria, Syria, Somalia, Yemen, Pakistan, India, Democratic Republic of the Congo and Philippines. [...] # THE FINDINGS In 2020, The FactCheckHub verified the graphic which originated from TVC and found it to be misleading. The station on one of [...]

3. **Old data circulates claiming Nigeria is the most terrorised country in Africa | Fact Check**
   URL: https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa
   Content: Image A screenshot taken September 23, 2020, showing the TVC programme Nigerian channel TVC News first ran the story on September 10, 2020. It also shared its report on YouTube, with the caption “Nigeria Emerges Most Terrorised Country In Africa, Ranks Worse Than Syria, Yemen, Somalia”. The report has since popped up in Facebook and Twitter posts, and in various blogs and articles. The Daily Times newspaper shared a screenshot from TVC News's report on Facebook on September 13, 2020, with the caption “Nigeria now above Syria, Somalia, Yemen in terrorism index as the country climbs to third position”. Chidi Odinkalu, a professor and former chairman of the country’s National Human Rights [...]

4. **Global Terrorism Index 2020: Measuring the impact of terrorism - World | ReliefWeb**
   URL: https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism
   Content: ISIL’s shift to sub-Saharan Africa meant that the region recorded the second highest number of terrorism deaths, even after accounting for the substantial fall in Nigeria. Deaths attributed to ISIL affiliates in the region were recorded as far south as Mozambique and 41 per cent of all ISIL-related attacks in 2019 occurred in sub-Saharan Africa. [...] In 2019, deaths from terrorism fell for the fifth consecutive year, after peaking in 2014. The total number of deaths fell by 15.5 per cent to 13,826. The fall in deaths was mirrored by a reduction in the impact of terrorism, with 103 countries recording an improvement on their GTI score, compared to 35 that recorded a deterioration. The [...]

5. **[PDF] 2024 Global Terrorism Index - Institute for Economics & Peace**
   URL: https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf
   Content: Section 1 | RESULTS ­ 6 ­ | GLOBAL TERRORISM INDEX 2024 1 Burkina Faso 8.571 long-arrow-alt-up 1 2 Israel 8.143 long-arrow-alt-up 24 3 Mali 7.998 long-arrow-alt-up 1 4 Pakistan 7.916 long-arrow-alt-up 3 5 Syria 7.890 Arrows-alt-h 6 Afghanistan 7.825 LONG-ARROW-ALT-DOWN 5 7 Somalia 7.814 LONG-ARROW-ALT-DOWN 4 8 Nigeria 7.575 Arrows-alt-h 9 Myanmar 7.536 Arrows-alt-h 10 Niger 7.274 Arrows-alt-h 11 Iraq 7.078 LONG-ARROW-ALT-DOWN 5 12 Cameroon 6.98 LONG-ARROW-ALT-DOWN 1 13 Democratic Republic of the Congo 6.514 long-arrow-alt-up 1 14 India 6.324 LONG-ARROW-ALT-DOWN 1 15 Mozambique 6.267 LONG-ARROW-ALT-DOWN 3 16 Colombia 6.188 LONG-ARROW-ALT-DOWN 1 17 Chile 5.679 LONG-ARROW-ALT-DOWN 1 18 [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_007 - Not Enough Evidence

#### Input
- **Claim:** Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources mostly say increased enforcement and barriers can increase smuggling, not decrease it.
- **Explanation:** Source 1 explicitly argues that expanded border enforcement is more likely to increase human smuggling, citing increased smuggler usage rates and that enforcement fueled reliance on smugglers. Source 4 similarly finds enforcement can lead to marginally higher violent crime in a sector as border crossers resort to smugglers, linking enforcement dynamics to smuggling behavior. While Sources 3 and 2 discuss reduced unauthorized entries and barrier effectiveness, they do not provide evidence that illegal drug smuggling and human smuggling decreased specifically in areas where barriers were deployed.
- **Confidence reason:** Direct evidence against the claim appears in Source 1 and 4; other sources are indirect or incomplete.
- **Claim verdicts:**
```json
[
  {
    "claim": "Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf": "contradicting",
  "https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers": "supporting",
  "https://cmsny.org/publications/jmhs-is-border-enforcement-effective/": "supporting",
  "https://ccis.ucsd.edu/_files/wp131.pdf": "contradicting",
  "https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025": "neutral"
}
```

#### Search Evidence Input
1. **[PDF] nfap policy brief » may 2022 - human smuggling and us immigration ...**
   URL: https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf
   Content: Spener described how three Mexican men managed to smuggle 600 people into the United States in a year working part-time. He interviewed a U.S. federal judge who “had seen hundreds, if not thousands, of ‘alien smuggling’ defendants in his courtroom over the years.” When the judge asked defendants why they decided to smuggle people into the U.S. one of the most common answers he received was “Se me hizo fácil [it just seemed easy to me].”5 Given the low barriers to entry, it should be clear that it is impossible to end human smuggling through policies based solely or primarily on immigration enforcement. EXPANDED BORDER ENFORCEMENT HAS INCREASED HUMAN SMUGGLING Expanding immigration [...]

2. **The Border Wall System is Deployed, Effective, and Disrupting Criminals and Smugglers | Homeland Security**
   URL: https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers
   Content: [...]

3. **Is Border Enforcement Effective? What We Know and What it Means - The Center for Migration Studies of New York (CMS)**
   URL: https://cmsny.org/publications/jmhs-is-border-enforcement-effective/
   Content: The new evidence suggests that unauthorized migration across the southern border has plummeted, with successful illegal entries falling from roughly 1.8 million in 2000 to just 200,000 by 2015. Border enforcement has been a significant reason for the decline — in particular, the growing use of “consequences” such as jail time for illegal border crossers has had a powerful effect in deterring repeated border crossing efforts. The success of deterrence through enforcement has meant that attempted crossings have fallen dramatically even as the likelihood of a border crosser being apprehended by the Border Patrol has only risen slightly, to just over a 50-50 chance. [...] These research [...]

4. **[PDF] The Effect of Illegal Immigration and Border Enforcement on Crime ...**
   URL: https://ccis.ucsd.edu/_files/wp131.pdf
   Content: led to an increased use of professional smugglers which in turn has led to more violence on the border. JEL classification: J61, K42 Key words: crime, immigration policy, illegal immigration, human smuggling 2 The 1990s saw a remarkable decline in crime rates not only in the U.S. as a whole, but also along the U.S.-Mexico border. Between 1991 and 2000, the median border county crime rate fell 34 percent while the U.S. crime rate fell 30 percent. It is tempting to attribute the steeper decline in border crime to stepped-up border enforcement since over the same period, although the number of illegal immigrant apprehensions rose 121 percent, border patrol enforcement (as measured by [...]

5. **Border Crossings Once Again at a Record Low in November 2025 | Homeland Security**
   URL: https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025
   Content: [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The sources don’t provide police-force growth data since 2002, so the 50% claim can’t be checked.
- **Explanation:** None of the provided sources include figures for South Africa’s police force size in 2002 and a later year, nor do they state a 50% growth figure. Source 2 discusses police shortages and cross-country comparisons, but it does not quantify growth since 2002. Sources 1 and 4 are annual reports, yet the provided excerpts only list legislation and do not contain staffing-growth statistics.
- **Confidence reason:** No source excerpt contains the needed 2002-to-present police growth numbers.
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf": "neutral",
  "https://groundup.org.za/article/south-africas-police-shortage/": "neutral",
  "https://en.wikipedia.org/wiki/South_African_Police_Service": "neutral",
  "https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf": "neutral",
  "https://en.wikipedia.org/wiki/Crime_in_South_Africa": "neutral"
}
```

#### Search Evidence Input
1. **[PDF] south-african-police-service-annual-report-2024-2025.pdf**
   URL: https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf
   Content: ▪ Implementation of the Rome Statute of the International Criminal Court Act, 2002 (Act No 27 of 2002) ▪ International Co-operation in Criminal Matters Act, 1996 (Act No 75 of 1996) ▪ Liquor Act, 2003 (Act No 59 of 2003) and the various Provincial Liquor Acts 24 SOUTH AFRICAN POLICE SERVICE | ANNUAL REPORT 2024/2025 ▪ Marine Living Resources Act, 1998 (Act No 8 of 1998) ▪ Mental Healthcare Act, 2002 (Act No 17 of 2002) ▪ National Conventional Arms Control Act, 2002 (Act No 41 of 2002) ▪ National Environmental Management Act, 1998 (Act No 107 of 1998) ▪ National Road Traffic Act, 1996 (Act No 93 of 1996) ▪ National Strategic Intelligence Act, 1994 (Act No 39 of 1994) ▪ Non-proliferation [...]

2. **How the size of South Africa’s police force compares to other countries | GroundUp**
   URL: https://groundup.org.za/article/south-africas-police-shortage/
   Content: GroundUp Logo # How the size of South Africa’s police force compares to other countries ## The country has a growing shortage of detectives | By GroundUp and The Outlier Charts | South Africa Despite a much higher violent crime rate, South Africa has fewer police per 100,000 people than the US, UK, France, Italy and China. But we do have a higher police per person ratio than developing countries like Kenya, India and Nigeria. We also have more police per population than Canada and Japan, though they have extremely low violent crime rates. ## Growing shortage of detectives [...] Charts produced by The Outlier in partnership with GroundUp ### More about Policing Durban rape cover-up [...]

3. **South African Police Service - Wikipedia**
   URL: https://en.wikipedia.org/wiki/South_African_Police_Service
   Content: | v t e South Africa articles | [...] | v t e Law enforcement in South Africa | [...] | v t e Law enforcement in Africa |

4. **[PDF] South African Police Service Annual Report 2023/2024**
   URL: https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf
   Content: (Act No 58 of 1959) » Implementation of the Rome Statute of the International Criminal Court Act, 2002 (Act No 27 of 2002) » International Co-operation in Criminal Matters Act, 1996 (Act No 75 of 1996) » Liquor Act, 2003 (Act No 59 of 2003) and the various Provincial Liquor Acts » Marine Living Resources Act, 1998 (Act No 8 of 1998) » Mental Healthcare Act, 2002 (Act No 17 of 2002) » National Conventional Arms Control Act, 2002 (Act No 41 of 2002) » National Environmental Management Act, 1998 (Act No 107 of 1998) » National Road Traffic Act, 1996 (Act No 93 of 1996) » National Strategic Intelligence Act, 1994 (Act No 39 of 1994) » Non-proliferation of Weapons of Mass Destruction Act, [...]

5. **Crime in South Africa - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Crime_in_South_Africa
   Content: | 2001 | 16.1 | 30.2 | 29.6 | 54.8 | 54.1 | 34.2 | 57.0 | 76.2 | 55.2 | 47.8 | | 2002 | 13.2 | 30.7 | 33.1 | 52.7 | 53.3 | 35.2 | 56.5 | 79.5 | 52.1 | 47.4 | | 2003 | 12.9 | 25.9 | 30.4 | 40.4 | 48.8 | 30.5 | 53.9 | 63.1 | 48.6 | 42.7 | | 2004 | 13.8 | 23.9 | 31.9 | 38.1 | 41.6 | 30.7 | 51.1 | 58.7 | 48.6 | 40.3 | | 2005 | 12.9 | 22.8 | 25.4 | 36.4 | 38.8 | 29.5 | 49.9 | 59.2 | 53.2 | 39.6 | | 2006 | 13.9 | 24.4 | 24.8 | 38.1 | 40.8 | 32.2 | 50.4 | 60.7 | 52.6 | 40.5 | | 2007 | 12.9 | 24.3 | 23.6 | 38.3 | 38.9 | 29.7 | 47.0 | 58.6 | 51.1 | 38.6 | | 2008 | 14.2 | 25.5 | 23.3 | 37.5 | 34.6 | 33.3 | 46.9 | 43.3 | 50.2 | 36.4 | | 2009 | 14.3 | 21.8 | 22.2 | 33.8 | 29.3 | 33.1 | 41.3 | 41.1 [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_012 - Not Enough Evidence

#### Input
- **Claim:** Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `false`
- **Score:** `5`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say there’s no evidence for the “25,000 pics” child-torture/rape claim.
- **Explanation:** PolitiFact states there is no evidence that a laptop previously belonging to Hunter Biden contains child pornography, and that the specific allegation originated on an anonymous internet forum (Source 1). FactCheck.org similarly says the Facebook meme claiming “25,000 pics” provides no evidence (Source 3).
- **Confidence reason:** Multiple fact-checkers directly address and reject the exact allegation.
- **Claim verdicts:**
```json
[
  {
    "claim": "Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://dpaq.de/gXxW2": "contradicting",
  "https://www.politifact.com/article/2020/dec/30/10-most-popular-social-media-fact-checks-2020/": "contradicting",
  "https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/": "contradicting",
  "https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter": "neutral",
  "http://biggs.house.gov/media/in-the-news/hunter-biden-laptop-claims-5-fast-facts-you-need-know": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Fact-checking unproven claims about Hunter Biden and child pornography**
   URL: https://dpaq.de/gXxW2
   Content: #### If Your Time is short There is no evidence that a laptop previously belonging to Hunter Biden contains child pornography. The allegation originated on an anonymous internet forum that’s a known source of online disinformation. See the sources for this fact-check Two weeks until Election Day, social media is rife with attacks on Joe Biden’s son Hunter Biden. A New York Post story about a recovered computer hard drive led to attacks about the Biden son’s business dealings. Facebook and cable news have gone further to suggest new and unsupported theories about what’s on the hard drive. One text post says, "Hunter Biden had 25,000 pics of him torturing and raping children under age 10 [...]

2. **PolitiFact | 10 most popular social media fact-checks of 2020**
   URL: https://www.politifact.com/article/2020/dec/30/10-most-popular-social-media-fact-checks-2020/
   Content: (Screenshot from Prntly.com) Claim: Says President Barack Obama "waited six months to call swine flu an emergency after thousands died." Rating: False The Obama administration declared swine flu, or H1N1, a public health emergency six weeks before H1N1 was declared a pandemic. No H1N1 deaths had yet been recorded in the United States. ## 6. Fact-checking unproven claims about Hunter Biden and child pornography Claim: Says "Hunter Biden had 25,000 pics of him torturing and raping children under age 10 in China on his laptop." Rating: False There is no evidence that a laptop previously belonging to Hunter Biden contains child pornography. The allegation originated on an anonymous [...]

3. **Social Media Posts Dredge Up Baseless 'Child Trafficking' Conspiracy Theory - FactCheck.org**
   URL: https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/
   Content: Alex Jones, the conspiracy theorist behind InfoWars and the bogus notion that the Sandy Hook school shooting in 2012 was a hoax, posted a video Oct. 17 that carried the headline “Confirmed: Trump Has Footage Of Hunter Biden Raping And Torturing Little Girls — Set To Release.” The video quotes Rudy Giuliani, President Donald Trump’s personal attorney, claiming to have pictures of Hunter Biden “that I can’t describe, some of which are illegal.” The video has received more than 2.2 million views. Another Facebook post makes this graphic, baseless claim: “Hunter Biden had 25,000 pics of him torturing and raping children under 10 in China on his laptop!” This kind of nonsense is circulating [...]

4. **Hunter Biden laptop letter - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter
   Content: By May 2023, no evidence had publicly surfaced to support suspicions that the laptop was part of a Russian disinformation scheme. FBI investigators handling Hunter Biden's laptop quickly concluded in 2019 "that the laptop was genuinely his and did not seem to have been tampered with or manipulated". PolitiFact wrote in June 2021 that the laptop did belong to Hunter Biden, but did not demonstrate wrongdoing by Joe Biden. ## Details [edit] [...] 5. ^ Barrett, Devlin; Viser, Matt (June 23, 2023). "Whistleblower accounts show Hunter Biden's laptop had little role in IRS probe". The Washington Post.`{{cite news}}`: CS1 maint: deprecated archival service (link) 6. ^ Drobnic Holan, Angie; [...]

5. **Hunter Biden Laptop Claims: 5 Fast Facts You Need to Know | Congressman Andy Biggs**
   URL: http://biggs.house.gov/media/in-the-news/hunter-biden-laptop-claims-5-fast-facts-you-need-know
   Content: Who is Joshua Wilson? There is an FBI agent named Joshua Wilson who has been assigned to child pornography and abduction cases over the years. A sitting senator, Ron Johnson (R-Wisconsin), went on Fox News and speculated about what that mean for Hunter Biden. To be clear, though, it hasn't been definitively proven that the laptop belonged to Hunter Biden; it also hasn't been definitively proven that the subpoena relates to that laptop. Business Insider reported that the name on the back page of the subpoena appears to say Joshua Wilson and refer to the Wilmington Office. Although the Joshua Wilson who works for the FBI has worked on child pornography cases over the years, Mac Isaac [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_016 - Not Enough Evidence

#### Input
- **Claim:** You see the number today? 33.1 GDP. The biggest in the history of our country by almost triple, right? Almost triple. Now it’s very much bigger than any GDP we’ve ever had. You have to go back to the 1950s, and then it’s less than half. This is the greatest number, 33.1 percent.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources support the 33.1% figure but contradict the “almost triple” and “greatest ever” comparisons.
- **Explanation:** CNBC (Source 1) and the other news sources confirm a 33.1% annualized GDP growth rate in Q3 2020. However, the claim that this is “the biggest in the history of our country by almost triple” and that it is “very much bigger than any GDP we’ve ever had” is not supported by the provided sources; the LA Times (Source 2) explicitly says the 33.1% headline is misleading and that actual Q3 growth was 7.4%, and it does not substantiate the “almost triple”/“greatest ever” comparison. The “33.1 percent” part is supported, but the historical magnitude comparisons are contradicted or unsupported by the sources.
- **Confidence reason:** Multiple sources confirm 33.1% annualized growth; historical comparison claims are unsupported/contradicted.
- **Claim verdicts:**
```json
[
  {
    "claim": "You see the number today? 33.1 GDP.",
    "verdict": "supported"
  },
  {
    "claim": "The biggest in the history of our country by almost triple, right? Almost triple.",
    "verdict": "contradicted"
  },
  {
    "claim": "Now it’s very much bigger than any GDP we’ve ever had.",
    "verdict": "unverifiable"
  },
  {
    "claim": "You have to go back to the 1950s, and then it’s less than half.",
    "verdict": "unverifiable"
  },
  {
    "claim": "This is the greatest number, 33.1 percent.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html": "supporting",
  "https://enewspaper.latimes.com/infinity/article_share.aspx?guid=b4a6e8b2-c9dd-4f7f-9c93-08cf03222a7e": "contradicting",
  "https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068": "contradicting",
  "https://www.multpl.com/us-gdp-inflation-adjusted/table/by-year": "neutral",
  "https://www.macrotrends.net/3004/us-gdp": "neutral"
}
```

#### Search Evidence Input
1. **U.S. GDP booms at 33.1% rate in Q3 report, beating expectations**
   URL: https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html
   Content: "This is going to be seized upon by both ends of the political spectrum as either evidence of the strength of the post-lockdown economic rebound or a cursory warning that the gains could be short-lived," said James McCann, senior global economist at Aberdeen Standard Investments. "The reality is that the GDP numbers demonstrate that the U.S. economy did indeed rebound strongly as lockdown measures were lifted." In a tweet, Trump noted the "Biggest and Best in the History of our Country" GDP number and said growth in 2021 will be "FANTASTIC!!!" For his part, Biden noted that while the economy improved "visits to food banks haven't slowed, and poverty has grown." [...] CNBC Join IC Join [...]

2. **Record growth is no reason for Trump to brag**
   URL: https://enewspaper.latimes.com/infinity/article_share.aspx?guid=b4a6e8b2-c9dd-4f7f-9c93-08cf03222a7e
   Content: Trump took out advance advertisements on Facebook even before the release, according to the Financial Times, bragging that the GDP number would be “the highest in American history.” He should put a sock in it. Here’s why. First, the headline number of 33.1% is intrinsically misleading — it’s an annualized rate, meaning that it’s how fast the economy would grow if the actual third-quarter figures were extended out to a whole year. In truth, the economy grew by only 7.4% in the third quarter. Moreover, either way you take it — whether as an annualized rate or the actual GDP change for the quarter — it must be considered in the context of previous changes in the size of the economy. [...] [...]

3. **GDP rose at 33.1 percent annualized rate last quarter, but blowout figure is not what it seems**
   URL: https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068
   Content: Vice President Mike Pence echoed Trump’s self-congratulations in a tweet of his own, saying, “President @realDonaldTrump created the Greatest economy in the history of the world and we are well on our way back to that with today’s amazing Third Quarter GDP number!” In reality, a polarized electorate and worry about Trump’s handling of the pandemic make this bounceback less significant than it might otherwise have been, and market observers say the inability to contain Covid-19 makes this economic growth tenuous. “It’s easier to get big growth rates when you're coming off a lower base. That’s what a lot of this is,” said Dan North, senior economist at Euler Hermes North America. [...] [...]

4. **US Real GDP by Year - Multpl**
   URL: https://www.multpl.com/us-gdp-inflation-adjusted/table/by-year
   Content: | Dec 31, 1959 | 3.44 trillion | | Dec 31, 1958 | 3.29 trillion | | Dec 31, 1957 | 3.20 trillion | | Dec 31, 1956 | 3.19 trillion | | Dec 31, 1955 | 3.13 trillion | | Dec 31, 1954 | 2.94 trillion | | Dec 31, 1953 | 2.86 trillion | | Dec 31, 1952 | 2.84 trillion | | Dec 31, 1951 | 2.70 trillion | | Dec 31, 1950 | 2.56 trillion | | Dec 31, 1949 | 2.26 trillion | | Dec 31, 1948 | 2.29 trillion | | Dec 31, 1947 | 2.21 trillion | | Dec 31, 1946 | 2.21 trillion | | Dec 31, 1945 | 2.50 trillion | | Dec 31, 1944 | 2.52 trillion | | Dec 31, 1943 | 2.34 trillion | | Dec 31, 1942 | 2.00 trillion | | Dec 31, 1941 | 1.68 trillion | | Dec 31, 1940 | 1.43 trillion | | Dec 31, 1939 | 1.31 trillion | | [...]

5. **U.S. GDP (1947-2025)**
   URL: https://www.macrotrends.net/3004/us-gdp
   Content: ## U.S. GDP (1947-2025) Markets Metals Energy Commodities Interest Rates Exchange Rates Economy Inflation Rate Unemployment National Debt Debt/GDP Housing Starts Initial Claims Retail Sales Industrial Prod Durable Goods # U.S. GDP: $31.423T as of December 2025. ###### Units: Dollars ###### Frequency: Quarterly ###### Release: Gross Domestic Product ###### Source: U.S. Bureau of Economic Analysis ## Historical Chart | Related Charts | [...] ## Historical Chart | Related Charts | | U.S. Real GDP | | U.S. Real GDP Per Capita | | GDPNow Model Estimate | | U.S. Gross National Product | | U.S. Real GDP | | Real Potential GDP | | St. Louis Fed Real GDP Nowcast | | Real GNP | | GDP per Capita [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_017 - Supported

#### Input
- **Claim:** Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true, mostly_true`
- **TLDR:** Sources do not support the specific claim of 300,000 lost manufacturing jobs from the trade war.
- **Explanation:** Source 1 cites Moody’s estimating the trade conflict with China reduced U.S. employment by 300,000 jobs, but it does not specify that these were manufacturing jobs. Source 3 instead reports net negative effects on manufacturing jobs from the tariffs, with an Oxford Economics estimate of 245,000 total jobs lost, not 300,000 manufacturing jobs. Source 2 finds no evidence of net U.S. job losses overall from the “China shock,” further undermining the claim’s framing.
- **Confidence reason:** Job-loss magnitude is discussed, but manufacturing-specific and 300,000 figure are not consistently supported.
- **Claim verdicts:**
```json
[
  {
    "claim": "Because of a so-called trade war with China, America lost 300,000 manufacturing jobs.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.statesman.com/story/news/politics/elections/2020/07/01/fact-check-did-trump-lose-trade-war-that-he-started-per-biden-ad/113740186/": "supporting",
  "https://sccei.fsi.stanford.edu/china-briefs/did-china-shock-cause-widespread-job-losses-us": "contradicting",
  "https://econofact.org/factbrief/did-the-trump-tariffs-increase-us-manufacturing-jobs": "contradicting",
  "https://www.cato.org/blog/manufacturing-employment-data-confirms-concentrated-benefits-dispersed-costs-trumps-tariffs": "neutral",
  "https://www.progressivepolicy.org/u-s-manufacturing-employment-is-down-108000-in-2025/": "neutral"
}
```

#### Search Evidence Input
1. **Fact-check: Did Trump lose a trade war that he started, per Biden ad?**
   URL: https://www.statesman.com/story/news/politics/elections/2020/07/01/fact-check-did-trump-lose-trade-war-that-he-started-per-biden-ad/113740186/
   Content: "U.S. tariffs against Chinese manufactured imports disrupted U.S. supply chains, raising input costs to many U.S. firms that used these products," Jones said. Independent observers have projected a net economic hit to the United States from the trade friction with China. A 2019 study by the Organization for Economic Cooperation and Development estimated that the tariff hikes could cut U.S. and Chinese GDP by 0.9% and 1.1%, respectively, by 2021-22. In a December 2019 study, Federal Reserve researchers concluded that Trump's tariffs "have not boosted manufacturing employment or output, even as they increased producer prices." And the economic analysis firm Moody's concluded in September [...]

2. **Did the “China Shock” Cause Widespread Job Losses in the U.S.? | FSI**
   URL: https://sccei.fsi.stanford.edu/china-briefs/did-china-shock-cause-widespread-job-losses-us
   Content: No evidence of net U.S.job losses resulting from China shock. Increasing import competition from China reallocated jobs and earnings from manufacturing in the U.S. heartland to the service sector in coastal urban areas. Researchers do not find evidence of net job loss, however, in the U.S. as a whole between 1990 and 2014. One-third of manufacturing job losses were caused by existing businesses that repurposed their operations from manufacturing to services, particularly in research, management, and wholesale.Large multinational firms were the primary drivers of manufacturing job losses, switching into research, design, management, wholesale, and other service sectors. Plants operating [...]

3. **Fact Check: Did the Trump tariffs increase US manufacturing jobs? | Econofact**
   URL: https://econofact.org/factbrief/did-the-trump-tariffs-increase-us-manufacturing-jobs
   Content: Economy-wide, Oxford Economics estimated in 2021 that the tariffs and resulting trade war cost 245,000 jobs and 0.5% of GDP while reducing real incomes by $675 per household. This fact brief is responsive to conversations such as this one. ### Sources: EconoFact The U.S. and China: Trade and Trade Wars Federal Reserve Board Disentangling the Effects of the 2018-2019 Tariffs on a Globally Connected U.S. Manufacturing Sector FRED (Federal Reserve Bank Of St. Louis) All Employees, Manufacturing (MANEMP) Progressive Policy Institute Trade Fact of the Week: Trump-era tariffs raised prices but did not ‘bring manufacturing back’ Oxford Economics The US-China Economic Relationship [...] The [...]

4. **Manufacturing Employment Data Confirm the Concentrated Benefits—and Dispersed Costs—of Trump’s Tariffs | Cato at Liberty Blog**
   URL: https://www.cato.org/blog/manufacturing-employment-data-confirms-concentrated-benefits-dispersed-costs-trumps-tariffs
   Content: Survey evidence reinforces this conclusion. For instance, the December 2025 ISM Manufacturing Purchasing Manager’s Index, a widely watched measure of the US factory activity based on a monthly survey of supply chain executives, fell to 47.9—the lowest reading of the year and the sector’s tenth consecutive month of contraction. (Above 50 indicates expansion; below 50 indicates contraction.) In fact, the reading was the lowest of 2025. The PMI’s sub-indices tracking orders and prices, as well as testimonies offered by the surveyed executives, repeatedly point to higher input costs and trade policy uncertainty driven by the administration’s tariff regime as key headwinds.

5. **U.S. manufacturing employment is down 108,000 in 2025**
   URL: https://www.progressivepolicy.org/u-s-manufacturing-employment-is-down-108000-in-2025/
   Content: “Damage is done when a consumer who would have benefited from a $30 toaster chooses not to buy one for $33. A second cost appears as consumers switch to domestic options that are more expensive. The consumer who buys the $32 toaster made in America pays the extra $2, but the government collects no extra revenue. Still, the share of the $32 purchase price that would once have gone to a Chinese factory and its workers now goes to an American firm and its workers instead. It pays American taxes and supports American families in American communities.” [...] Ed Gresser Trade Fact | April 8, 2026 ### U.S. Customs blocks about $0.8 billion worth of goods a year on suspicion of ‘forced labor’ [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_018 - Not Enough Evidence

#### Input
- **Claim:** There was a 40% drop in the price of oil, Nigeria's main export.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources support a 40% export drop, not a 40% oil price drop.
- **Explanation:** Source 1 states Nigeria’s exports fell about 40.3% (2015 vs 2014) as crude prices plunged, but it does not say oil prices themselves dropped by 40%. Sources 2 and 3 discuss Brent falling below $40 (around $39/$37), which is not a clearly stated 40% drop. Therefore, the claim conflates a ~40% export decline with a ~40% oil price decline.
- **Confidence reason:** Only one source mentions ~40% and it refers to exports.
- **Claim verdicts:**
```json
[
  {
    "claim": "There was a 40% drop in the price of oil, Nigeria's main export.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.tralac.org/news/article/9314-nigerian-exports-slumped-40-last-year-as-oil-prices-plunged.html": "supporting",
  "https://cpeel.ui.edu.ng/news/oil-prices-below-40-what-it-means-nigeria-local-oil-companies-banks": "neutral",
  "https://www.arise.tv/fresh-concerns-in-nigeria-as-crude-oil-price-slumps-below-40/": "neutral",
  "https://assets.publishing.service.gov.uk/media/57a08a4b40f0b6497400051e/61062Case-Study-Nigeria.pdf": "neutral",
  "https://www.legit.ng/business-economy/money/1703251-new-data-shows-buying-50-crude-oil-nigeria/": "neutral"
}
```

#### Search Evidence Input
1. **Nigerian exports slumped 40% last year as oil prices plunged - tralac trade law centre**
   URL: https://www.tralac.org/news/article/9314-nigerian-exports-slumped-40-last-year-as-oil-prices-plunged.html
   Content: The value of the nation’s exports totalled N2,076.7 billion in Q4, 2015, showing a decrease of N256.5billion, or 11.0%, over the value recorded in the preceding quarter. On an annual basis total exports from Nigeria stood at N9,728.8 billion at the end of 2015, representing a drop of N6,575.2 billion or 40.3% over levels recorded in 2014. Notwithstanding a steep decline in crude oil exports by N4,945.9 billion or 41.6% in 2015, the structure of Nigeria’s exports is still dominated by crude oil exports. The contribution of crude oil to the value of total domestic export trade amounted to N6,945.3 billion or 71.4% in 2015 (estimate figures). [...] Exports by Section, revealed that the [...]

2. **Oil Prices Below $40: What it Means for Nigeria, Local Oil Companies, Banks | Centre for Petroleum, Energy Economics & Law**
   URL: https://cpeel.ui.edu.ng/news/oil-prices-below-40-what-it-means-nigeria-local-oil-companies-banks
   Content: Energy News 18 September 2020 The price of Brent, the benchmark of Nigeria’s crude oil has fallen to $39 as bearish factors mount and sentiment shifts add another wrench in the recovery for oil prices still reeling from the pandemic-driven blow to consumption. Brent futures dropped 4.1 percent to $38.95 a barrel as at 2 pm Nigerian Time, while US crude dropped by 1.10 percent, to $37.67. One major factor behind the fall in oil price is the concerns over rising exports from the Organisation of Petroleum Exporting Countries (OPEC) and allies’ in third quarter of 2020, with the possibility of a total breakdown of the OPEC+ agreement.

3. **Fresh Concerns in Nigeria as Crude Oil Price Slumps below $40**
   URL: https://www.arise.tv/fresh-concerns-in-nigeria-as-crude-oil-price-slumps-below-40/
   Content: “Nigerian exports to the United States are dominated by crude oil, which at $4.4 billion, accounted for 88% of US imports from Nigeria in 2019. According to US International Trade Commission data, Nigeria consistently ranks as the top source of exports to the United States under the African Growth and Opportunity Act,” it stated However, it noted that Nigeria also remains a major regional destination for US exports of motor vehicles and refined petroleum products (e.g., gasoline), which are among the fastest-growing U.S. exports to Africa. Agricultural products and machinery, the research group said, are other top US exports to the country, adding that Nigeria’s demand also has driven [...]

4. **[PDF] Oil Shock Vulnerabilities & Impacts: Nigeria Case Study - GOV.UK**
   URL: https://assets.publishing.service.gov.uk/media/57a08a4b40f0b6497400051e/61062Case-Study-Nigeria.pdf
   Content: top net exporters of crude oil, it is nonetheless heavily reliant on imports of refined fuels, which are essential to the functioning of its economy. This poses a risk to the domestic economy in the event of global oil and refined fuel shortages in the future. -40% -30% -20% -10% 0% 10% 20% 30% 1981 1983 1985 1987 1989 1991 1993 1995 1997 1999 2001 2003 2005 2007 2009 2011 production consumption 17 Figure 16: Nigeria’s net oil exports, 1986-2009 Source: EIA, 2012a. 3.4 Conflict over access to oil wealth Poverty and inequality in the distribution of oil wealth in Nigeria has led to widespread oil bunkering, which refers to the theft and trade in stolen oil. According to EIA (2012b), [...]

5. **New Data Shows US Buying 50% Less Crude Oil From Nigeria - Legit.ng**
   URL: https://www.legit.ng/business-economy/money/1703251-new-data-shows-buying-50-crude-oil-nigeria/
   Content: ## Another African country leads Despite the decline, crude oil remains Nigeria’s dominant export to the United States, accounting for about 63% to 65% of total US imports from the country in January. Total US imports from Nigeria fell to $183 million from $297 million in December, reflecting the broader contraction in trade flows. At the same time, the United States recorded a goods trade surplus of $419 million with Nigeria, widening sharply from $84 million in December as exports to Nigeria rose to $602 million. Across Africa, however, the US posted a trade deficit of $503 million, reversing a surplus recorded in the previous month. Nigeria’s crude export value to the US falls [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_020 - Supported

#### Input
- **Claim:** Edo State in Nigeria has a 19% unemployment rate.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `true, mostly_true`
- **TLDR:** One source reports 19% unemployment in Edo, but the provided evidence is indirect and not independently verified.
- **Explanation:** Source 1 (Dubawa) says Obaseki claimed Edo’s unemployment fell from 25% to about 19% and that this was “verifiable with” an NBS report, citing a The Nation report that referenced NBS data. However, none of the provided sources include the actual NBS state-level figure for Edo showing 19%, and Source 2 and Source 4 discuss different unemployment figures/timeframes without confirming 19% for Edo. Therefore, the claim is only partially supported by the excerpted reporting rather than directly evidenced.
- **Confidence reason:** Only one indirect source mentions the 19% figure; no direct NBS Edo value provided.
- **Claim verdicts:**
```json
[
  {
    "claim": "Edo State in Nigeria has a 19% unemployment rate.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/": "supporting",
  "https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf": "neutral",
  "https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/": "neutral",
  "https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria": "neutral",
  "https://www.nigerianstat.gov.ng/elibrary/read/929": "neutral"
}
```

#### Search Evidence Input
1. **Is Edo unemployment rate 19 percent as claimed by Obaseki? - Dubawa**
   URL: https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/
   Content: Excerpt of Obaseki’s statement. ### Verification A keyword search by Dubawa showed that in August 2020, a report by The Nation indicates that the unemployment rate in Edo state has reduced to 19%. The report which quoted a Nigeria Bureau of Statistics (NBS) report, noted Edo State has the lowest unemployment figure in the South-South region, compared to five other oil-rich states in the region. Is Edo unemployment rate 19 percent as claimed by Obaseki? [...] Channels Television had earlier conducted a poll which allowed the public to choose two candidates they would love to appear in the debate. The candidates of the APC and PDP emerged top of the poll. During the governorship debate [...]

2. **[PDF] perception of edo residents towards unemployment**
   URL: https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf
   Content: 10 Unemployment is one of the fundamental developmental challenges facing Nigeria at the moment. Research have shown that unemployment was rapid in the 1980s but the obtainable report from diverse local and international bodies and the glaring evidence of joblessness in these decades are clear evidences that there was no time in Nigeria’s checkered history where unemployment is as serious as now (Asaju et al, 2014) In previous days, the eventuality of unemployment though present, was not on a high rise where a high number of educated individuals roam the streets of the country, jobless. [...] 2.2.1 Unemployment in Nigeria “Educated and unemployed” is the raised placard in Nigeria as [...]

3. **How true are viral claims on Nigeria’s unemployment rate, extreme poverty and debt profile? | The ICIR- Latest News, Politics, Governance, Elections, Investigation, Factcheck, Covid-19**
   URL: https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/
   Content: The tweet read: “\ 28% unemployment rate, \ 49% in extreme poverty, \ $85.9Bn debt and counting, Buhari just approved N10 billion for census. Extreme irresponsible behavior is main crisis facing leadership in Nigeria.” THE CLAIMS: From the tweet, these claims were established: THE FINDINGS: Claim 1: The FactCheckHub first checked the National Bureau of Statistics (NBS) website for the data on Nigeria’s labour statistics to determine the total percentage of unemployment rate in the country. According to the statistics on Nigeria’s labour force released by the NBS for 2nd quarter (Q2) of 2020, Nigeria currently has 21,764,617 unemployed people. The data also stated that 27.1% people are [...]

4. **12 Unemployment Statistics in Nigeria for 2026 | MyJobMag**
   URL: https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria
   Content: A state-by-state breakdown was given, with Abia State recording the highest rate of unemployment at 18.7%, followed by the FCT and Rivers State with 14.1% and 13.4% respectively. Borno reported the least amount with 7.3% of the citizenry unemployed. The unemployment rate fell to 4.3% in Q2 2024, reversing a rising trend since Q2 2023. Also, the educational distribution of Nigerians played a major role in their employability. Persons with tertiary education had a higher employment rate compared to others in the educational subset. Despite the drop in unemployment, Nigeria's misery index (the sum of unemployment and inflation rate) rose to 38.3% in Q2 2024. This marks an increase from [...]

5. **Reports | National Bureau of Statistics**
   URL: https://www.nigerianstat.gov.ng/elibrary/read/929
   Content: Coat of Arm Nigeria Flag ## Labor Force Statistics - Volume 2: Unemployment and Underemployment by State (Q3 2018) ## Labor Force Statistics - Volume 2: Unemployment and Underemployment by State (Q3 2018) ### Summary - Unemployment and Underemployment rates vary across states according to the nature of economic activity predominant in each State. States with higher focus on seasonal agriculture tend to have higher rates of underemployment compared to unemployment. This may swing from high full-time employment during periods of planting and harvest, when they are fully engaged on their farms, to periods of high underemployment and even unemployment at other periods in between.

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_021 - Not Enough Evidence

#### Input
- **Claim:** Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `25`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources indicate Nigeria’s petrol was cheaper than Saudi Arabia in 2020, contradicting the claim.
- **Explanation:** Source 1 reports that Saudi Arabia’s petrol was more expensive than Nigeria’s after converting prices, stating Saudi petrol was 17.78% (octane 95) and 11.16% (octane 91) more expensive than Nigeria. This directly contradicts the claim that Nigeria’s 2020 fuel was not cheaper than Saudi Arabia. Sources 3 and 4 discuss comparisons and Saudi low prices generally, but Source 1 is the only one that directly addresses the relative price direction with calculations.
- **Confidence reason:** Only one source directly compares Nigeria vs Saudi prices with calculations.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/": "supporting",
  "https://www.facebook.com/groups/599563341561133/posts/1445300556987403/": "neutral",
  "https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/": "neutral",
  "https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf": "neutral",
  "https://tradingeconomics.com/country-list/gasoline-prices": "neutral"
}
```

#### Search Evidence Input
1. **FACT CHECK: Is petrol 40% cheaper in Nigeria than in Saudi Arabia as claimed by Dangote? - TheCable Fact Check**
   URL: https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/
   Content: On the other hand, on September 3, the Nigerian National Petroleum Company (NNPC) Limited increased thepetrol price across its retail outlets to N855 per litre. After converting the riyal value to naira, the naira denomination was used to determine the difference between petrol prices in both countries. As a result, Saudi Arabia’s petrol is 17.78 percent (for octane 95 petrol) and 11.16 percent (for octane 91 petrol), respectively, more expensive than that of Nigeria. Moreover, converting the petrol prices of both countries to dollars would lead to a similar result which is way less than the 40 percent Dangote claimed. Verdict: Partly false. The claim that petrol costs 40 percent less [...]

2. **Fuel price comparison between Saudi Arabia and Nigeria - Facebook**
   URL: https://www.facebook.com/groups/599563341561133/posts/1445300556987403/
   Content: Now, a Nigerian can only buy 73 Litres of fuel with his minimum wage, while a Saudi Arabian will buy about 1,717 Litres of fuel. The difference.

3. **FG justifies fuel price comparison with Saudi Arabia, others | Multiplatform Digital Information Technology**
   URL: https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/
   Content: President Buhari said in his Independence Day broadcast that: “we sell petrol at N161 per litre when same is sold at N168 per litre in Saudi Arabia; N211 per litre in Egypt; N362 per litre in Ghana; N362 per litre in Chad, and N346 per litre in Niger Republic. “It does not make sense for petrol to be cheaper in Nigeria than Saudi Arabia,’’ ## READ ALSO: ONDO DECIDES: APC accuses PDP, ZLP of creating tension ahead of polls A cross section of Nigerians, however, criticised the president for making such comparison without considering the minimum wage, standard of living and infrastructure in Saudi Arabia in particular. Responding to the critics, the minister said there was nothing wrong [...]

4. **[PDF] Fossil fuel subsidy swaps: A path towards accelerating the ...**
   URL: https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf
   Content: can be rightly ascribable to the decline in energy prices fueled by the rise in fossil fuel subsidies. Fuel prices in Saudi Arabia are amongst the lowest in the entire world: Gasoline, for example, costs only 62 cents per liter, while its global price is $2.54 per liter (Bloomberg, 2024). This relatively huge gap between domestic and international prices represents foregone revenue and could be viewed as an implicit subsidy (Aldubyan and Gasim, 2021). Hartley and Medlock III (2008) report that Saudi citizens believe they deserve low energy prices as a way to take advantage of their country's fossil fuel wealth. On account of the high, subsidy-driven energy consumption, population [...]

5. **Gasoline Prices - Countries - List**
   URL: https://tradingeconomics.com/country-list/gasoline-prices
   Content: | Country | Last | Previous | Reference | Unit | --- --- | Indonesia | 0.59 | 0.6 | Mar/26 | USD/Liter | | Saudi Arabia | 0.62 | 0.62 | Mar/26 | USD/Liter | | Russia | 0.83 | 0.87 | Mar/26 | USD/Liter | | United States | 0.96 | 0.77 | Mar/26 | USD/Liter | | India | 1.01 | 1.04 | Mar/26 | USD/Liter | | Japan | 1.11 | 1.01 | Mar/26 | USD/Liter | | Argentina | 1.19 | 1.11 | Mar/26 | USD/Liter | | South Africa | 1.2 | 1.26 | Mar/26 | USD/Liter | | South Korea | 1.23 | 1.18 | Mar/26 | USD/Liter | | Canada | 1.28 | 1.02 | Mar/26 | USD/Liter | | Brazil | 1.29 | 1.23 | Mar/26 | USD/Liter | | Mexico | 1.35 | 1.35 | Mar/26 | USD/Liter | | China | 1.37 | 1.03 | Mar/26 | USD/Liter | | Turkey | [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_022 - Refuted

#### Input
- **Claim:** The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** None of the sources show Nigeria donating $600M to Biden’s campaign.
- **Explanation:** Source 1 discusses $600 million in unemployment funds lost to Nigerian scammers in Washington state, and mentions Biden donors, but it does not say the Nigerian government donated $600 million to Joe Biden’s campaign. Sources 2, 3, 4, and 5 discuss other foreign-donation or U.S.-Nigeria assistance topics and do not provide evidence of a $600 million Nigerian government donation to Biden’s campaign.
- **Confidence reason:** No source directly addresses the specific donation claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/": "neutral",
  "https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues": "neutral",
  "https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-": "neutral",
  "https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/": "neutral",
  "https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf": "neutral"
}
```

#### Search Evidence Input
1. **Biden pick for unemployment program lost $600M to Nigerian scammers**
   URL: https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/
   Content: The Seattle Times described her as a “potent, behind-the-scenes force in Democratic politics” and said she had entertained a string of 2020 presidential candidates in salon-style fundraisers at her home. The newspaper’s analysis of federal campaign records found she and her husband Eric donated more than $400,000 to the Biden campaign and other Democratic causes in the past two years. The Department of Labor and the White House did not respond to requests for comment. ### Tag: # Magazine Magazine Covers # More from News [...] Logo Logo # Biden pick for unemployment program lost $600M to Nigerian scammers Biden pick for unemployment program lost $600M to Nigerian scammers President [...]

2. **Trump wants to investigate Democrats' fundraising, but his own campaign has issues | PBS News**
   URL: https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues
   Content: Regulators and watchdogs have also long been concerned about donations from individuals with ties to foreign interests. Trump has received many such contributions, including one in December from Nnenna Peters, the wife of Benedict Peters, a Nigerian billionaire who is the founder and CEO of oil and mining businesses. Nnenna Peters, who goes by Ella, gave $1 million to Trump's inaugural committee. A naturalized citizen, Nnenna Peters — who lives in Potomac, Maryland, a tony suburb of the capital — is allowed to make campaign donations. [...] Benedict Peters, as it turns out, has a lot to offer that could be of interest to Trump, who has made the extraction of natural resources a focus [...]

3. **FACT SHEET: U.S. Efforts to Assist the Nigerian Government in its Fight against Boko Haram | whitehouse.gov**
   URL: https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-
   Content: Jump to main content Jump to navigation Home ## Search form ## You are here ## Briefing Room # FACT SHEET: U.S. Efforts to Assist the Nigerian Government in its Fight against Boko Haram [...] Boko Haram is inflicting untold hardship on the people of Nigeria, with repercussions for men, women, girls, and boys throughout northeast Nigeria. The United States provides assistance to affected populations, including support to health, water, and sanitation services; the delivery of emergency relief supplies; and protection services, including psycho-social support for survivors of Boko Haram violence. The United States further invests in helping Nigeria to build security and increase [...]

4. **KOCO 5 News**
   URL: https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/
   Content: # KOCO 5 News - A report from the State Department lists... | Facebook Log In Log In Forgot Account? ## KOCO 5 News's Post []( ### KOCO 5 News January 29 · A report from the State Department lists tens of thousands of dollars in foreign gifts to former President Joe Biden and other officials in the last year of the Biden administration. Image 1: May be an image of text that says 'BIDEN'S FOREIGN GIFTS STATE DEPARTMENT REPORT DETAILS FOREIGN GIFTS GIVEN tO JOE BIDEN IN 2024' Image 2 Image 3 Image 4 All reactions: 665 956 comments 62 shares Like Comment Most relevant Taylor States Like a plane? 12w 356 Image 5 View all 46 replies Lydia C Willis And he sent them to the national archives. [...]

5. **[PDF] Congress Must Stop Biden's Misuse of U.S. Foreign Aid to Impose ...**
   URL: https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf
   Content: A review of the first 50 USAID employees, chosen alphabetically, who made political contributions during the 2020 federal election cycle shows that 48 of them donated to Democratic candidates and causes, with just two giving to Republicans, a 12 to 1 ratio. Of the estimated $48,000 donated, only $600 went to Republicans, less than 2 percent of the total.REF Following the slaying of George Floyd in late May 2020, an election year, over 1,000 USAID staff demanded that the agency “make a public statement affirming that Black Lives Matter,” accused USAID “of structural racism,” and insisted USAID design a plan to address “systemic injustice, racism, colonialism, and police brutality,” [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. PolitiFact / pf_002 - false

#### Input
- **Claim:** Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false, mostly_false`
- **TLDR:** Sources say the Wisconsin Supreme Court ended the John Doe investigation, but not “two judges said it’s over.”
- **Explanation:** WPR reports that the Wisconsin Supreme Court ended the long-running John Doe investigation and explicitly wrote that “this conclusion ends the John Doe investigation,” ordering return of seized property and destruction of evidence. EXPOSEDbyCMD sources also describe the court shutting down the John Doe investigation and ordering evidence destroyed/returned. However, none of the provided sources clearly identify “two judges” as saying it was over; they reference a 4-2 decision and specific justices, but not two judges making that statement in the way the claim specifies.
- **Confidence reason:** Court termination is clear; “two judges said” is not directly supported.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says the secret John Doe criminal investigation of his campaign has been resolved and two judges have said it is over.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.exposedbycmd.org/2016/09/22/leaked-documents-court-dismissal-john-doe-false-premise/": "supporting",
  "https://www.wpr.org/politics/state-supreme-court-ruling-blocks-john-doe-probe": "supporting",
  "https://www.theguardian.com/us-news/2016/sep/14/corporate-cash-john-doe-files-scott-walker-wisconsin": "neutral",
  "https://www.motherjones.com/politics/2007/07/search-john-doe-no-2-story-feds-never-told-about-oklahoma-city-bombing/": "neutral",
  "https://www.exposedbycmd.org/2016/06/23/cmd-urges-u-s-supreme-court-to-hear-prosecutors-appeal-in-john-doe-ii-corruption-case/": "supporting"
}
```

#### Search Evidence Input
1. **Leaked Documents Show Court's Dismissal of the John Doe Was Based on a False Premise - EXPOSEDbyCMD**
   URL: https://www.exposedbycmd.org/2016/09/22/leaked-documents-court-dismissal-john-doe-false-premise/
   Content: In a controversial ruling that July, the Court voted 4-2 to shut down the John Doe investigation into Scott Walker’s secret political fundraising scheme, arguing that coordination between Walker, his campaign consultants, and corporate lobby groups didn’t matter because it was all just “issue advocacy.” When the special prosecutor moved for reconsideration later that year, presenting evidence of express political advocacy, the court’s conservative majority, led by Justice Gableman, promptly fired him. It was Wisconsin’s version of the Saturday Night Massacre, when Richard Nixon had Archibald Cox canned (by Robert Bork) as the special prosecutor in the Watergate scandal. [...] The [...]

2. **State Supreme Court Ruling Blocks John Doe Probe - WPR**
   URL: https://www.wpr.org/politics/state-supreme-court-ruling-blocks-john-doe-probe
   Content: # State Supreme Court Ruling Blocks John Doe Probe Investigation Looked Into Allegations Of Coordination Between Candidates, Groups The Wisconsin Supreme Court has ended a long-running John Doe investigation into whether Gov. Scott Walker’s campaign illegally coordinated with conservative groups during his 2012 recall campaign. Writing for the court’s conservative majority in the 4-2 decision, Justice Michael Gableman minced no words. “To be clear,” Gableman wrote, “this conclusion ends the John Doe investigation.” ## Understanding Wisconsin, Together. WPR’s “Wisconsin Today” newsletter keeps you connected to the state you love without feeling overwhelmed. No paywall. No agenda. No [...]

3. **Leaked documents reveal secretive influence of corporate cash on politics | US political financing | The Guardian**
   URL: https://www.theguardian.com/us-news/2016/sep/14/corporate-cash-john-doe-files-scott-walker-wisconsin
   Content: Walker’s campaign told the Guardian that the John Doe investigation was “baseless” and had been shut down multiple times by the state courts. “There is absolutely no evidence of any wrongdoing,” a spokesman said. The third-party lobbying groups that were the subject of the investigation said the prosecutors had accused wholly innocent individuals of crimes that did not exist under state law. They insisted they had a right to comment about public officials and policy and to protect the confidentiality of their donors. ## Most viewed ## Most viewed [...] In 2015, Justice Prosser refused to recuse himself from a case in which the state supreme court sat in judgment over the John Doe [...]

4. **In Search of John Doe No. 2: The Story the Feds Never Told About ...**
   URL: https://www.motherjones.com/politics/2007/07/search-john-doe-no-2-story-feds-never-told-about-oklahoma-city-bombing/
   Content: After more than a year of proceedings, in August 1997, the grand jury (which, like all such panels, had heard only evidence selected by the government) concluded its investigation without issuing any criminal indictments. The doj held back the news for two months while staff in Washington met to devise a roll-out plan that a doj aide compared to “coordinating the invasion of Normandy.” The plan targeted the media as well as Senators Orrin Hatch (R-Utah) and Byron Dorgan (D-N.D.), who, thanks to Jesse Trentadue’s efforts, had taken an interest in the case. In a Senate Judiciary Committee hearing a few months earlier, Hatch had quizzed then-Attorney General Janet Reno about Kenney and [...]

5. **CMD Urges U.S. Supreme Court to Hear Prosecutors' Appeal in John Doe II Corruption Case - EXPOSEDbyCMD**
   URL: https://www.exposedbycmd.org/2016/06/23/cmd-urges-u-s-supreme-court-to-hear-prosecutors-appeal-in-john-doe-ii-corruption-case/
   Content: State Justices David Prosser and Michael Gableman denied a motion from the special prosecutor to step aside and then proceeded to help “cancel oral argument, issue sweeping secrecy orders, halt the investigation, fire the special prosecutor, order the evidence returned and copies destroyed, and dramatically curtail Wisconsin’s campaign finance law, rendering the longstanding limits and other restrictions the state places on contributions to candidates virtually meaningless.” They have even sought inappropriately to impede the prosecutors’ appeal to the U.S. Supreme Court. Specifically, the brief argues that: [...] Even more troubling, the special prosecutor may have unearthed documents [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. PolitiFact / pf_003 - true

#### Input
- **Claim:** Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources indicate Hatch co-sponsored a 1993 GOP health bill with an individual mandate.
- **Explanation:** PolitiFact directly states that Hatch was a co-sponsor of a 1993 Republican-backed bill that included an individual mandate (Source 1). Fox News and The New Yorker also say the individual mandate appeared in 1993 bills supported by Orrin Hatch (Sources 2 and 3). None of the provided sources contradict the claim; Source 5 is unrelated to the 1993 mandate question.
- **Confidence reason:** Multiple sources support, but details of the exact bill are not fully corroborated.
- **Claim verdicts:**
```json
[
  {
    "claim": "Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/": "supporting",
  "https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long": "supporting",
  "https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate": "supporting",
  "https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf": "neutral",
  "https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Hatch once supported an individual mandate, said Cenk Uygur**
   URL: https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/
   Content: We contacted Hatch's office to ask for an explanation for Hatch's change of position, but we didn't hear back. Last year, Kaiser Health News interviewed former Sen. Dave Durenberger, R-Minn., who had also co-sponsored the plan. Durenberger said that it was Republicans who had changed in the years since 1993, backing away from policies on health care they once supported. Uygur asked, "Did you know that Hatch co-sponsored the 1993 bill that had an individual mandate?" We didn't, but we checked the record. Hatch was the co-sponsor of a Republican-backed bill that included an individual mandate. We rate Uygur's statement True. [...] "Here's what I'm amazed by -- Orrin Hatch," Uygur said. [...]

2. **Individual health care insurance mandate has roots two decades long | Fox News**
   URL: https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long
   Content: The mandate, requiring every American to purchase health insurance, appeared in a 1989 published proposal by Stuart M. Butler of the conservative Heritage Foundation called "Assuring Affordable Health Care for All Americans," which included a provision to "mandate all households to obtain adequate insurance." The Heritage Foundation "substantially revised" its proposal four years later, according to a 1994 analysis by the Congressional Budget Office. But the idea of an individual health insurance mandate later appeared in two bills introduced by Republican lawmakers in 1993, according to the non-partisan research group ProCon.org. Among the supporters of the bills were senators Orrin [...]

3. **Unpopular Mandate | The New Yorker**
   URL: https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate
   Content: In February, 2012, Stuart Butler, the author of the Heritage Foundation brief that first proposed the mandate, wrote an op-ed for USA Today in which he recanted that support. “I’ve altered my views on many things,” he wrote. “The individual mandate in health care is one of them.” Senator Orrin Hatch, who had been a co-sponsor of the Chafee bill, emerged as one of the mandate’s most implacable opponents in 2010, writing in The Hill that to come to “any other conclusion” than that the mandate is unconstitutional “requires treating the Constitution as the servant, rather than the master, of Congress.” Mitt Romney, who had both passed an individual mandate as governor and supported Wyden- [...]

4. **[PDF] The New Bipartisan Consensus for an Individual Mandate**
   URL: https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf
   Content: Affordability, Responsibility, and Empowerment Act (PCARE) introduced by Republican Senators Orrin Hatch and Richard Burr, together with Congressman Fred Upton, it is now clear HEALTH POLICY CENTER The New Bipartisan Consensus for an Individual Mandate that there is at least some bipartisan agreement on the need for an individual mandate for health insurance. Although the official description of the PCARE proposal includes language indicating strong objection to the individual responsibility requirement of the Affordable Care Act (ACA), the proposal uses different types of penalties intended to bring most Americans into the health insurance pool and keep them there.1 According to the [...]

5. **How Sen. Orrin Hatch Changed America's Health Care - KFF Health News**
   URL: https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/
   Content: Some legislators and consumer advocacy groups wanted vitamins and other supplements to go through a tight approval process, akin to the testing the Food and Drug Administration requires of drugs. But DSHEA reined in the FDA, determining that supplements do not have to meet the same safety and efficacy standards as prescription drugs. That legislative clamp on regulation has led to ongoing questions about whether dietary supplements actually work and concerns about how they interact with other medications patients may be taking. DSHEA was co-sponsored by Democrat Tom Harkin, then a senator from Iowa. [...] “AIDS does not play favorites,” Hatch told other senators. “It affects rich and [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 13. PolitiFact / pf_004 - barely-true

#### Input
- **Claim:** Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** The sources don’t show Mark Herring voting on shorter sentences for sex offenders.
- **Explanation:** None of the provided sources mention Mark Herring or any vote by him on sentencing for sex offenders. Source 1 discusses sex-offender recidivism generally, Source 2 provides background on sexual offending prevalence, Source 3 is about Canada’s Bill C-14 bail/sentencing reforms without any Mark Herring vote details, and Source 4 is a dissenting report referencing the Supreme Court case Herring v. United States rather than a sentencing vote by Mark Herring.
- **Confidence reason:** No source addresses Mark Herring or the alleged vote.
- **Claim verdicts:**
```json
[
  {
    "claim": "Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf": "neutral",
  "https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf": "neutral",
  "https://openparliament.ca/bills/45-1/C-14/?singlepage=1": "neutral",
  "https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf": "neutral",
  "https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf": "neutral"
}
```

#### Search Evidence Input
1. **[PDF] Recidivism: The Great Lie of “Frightening and High” - Regulations.gov**
   URL: https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf
   Content: First of all, specialization is no more common for sex offenders than any other type of offender; thieves are more likely to steal, drug offenders are more likely to commit drug crimes, et cetera. Furthermore, strong evidence suggests people convicted of sexual offenses actually specialize at a lower rate than most other offenses. The 2000 Michigan Parole Board study shows people convicted of sexual offenses committed subsequent sexual offenses (2.46%) at a lower rate than forgers committing forgery (6.86%), burglars committing burglary (10.56%), robbers committing robbery (5.17%), drug offenders committing drug crimes (6.42%), and larcenists committing larceny (12.65%). "Langan and [...]

2. **[PDF] Sex Offender Management Assessment and Planning Initiative**
   URL: https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf
   Content: colleagues (2007) conducted a national telephone survey of 5,000 women aged 18–86, including approximately 3,000 who represented all women in the United States and 2,000 women attending college. The research results indicated that for women of all ages, an estimated 18 percent had been raped during their lifetime. This translates into an estimated 20 million victims of rape out of 112 million women in the United States. In looking at past-year victimization alone, the authors estimated that more than 1 million women had been raped. Of those who reported that they were raped, 16 percent indicated they had reported the crime to law enforcement. The study found that victims of drug- [...]

3. **Bill C-14 | openparliament.ca**
   URL: https://openparliament.ca/bills/45-1/C-14/?singlepage=1
   Content: Crime is a real concern throughout the country. Canadians are frustrated to see repeat violent offenders being released from prison. They are concerned about their safety. We see it every day: Car thefts and break-ins in the middle of the night are being caught on camera. People simply want to know that the system puts their safety first. [...] ## Debate Summary line drawing of robot This is a computer-generated summary of the speeches below. Usually it’s accurate, but every now and then it’ll contain inaccuracies or total fabrications. Bill C-14 proposes reforms to Canada's bail and sentencing laws, including changes to reverse onus provisions, bail conditions, sentencing factors, and [...]

4. **[PDF] DISSENTING REPORT - Supreme Court of Ohio**
   URL: https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf
   Content: by the police officer and the windfall afforded a guilty defendant by application of the rule is contrary to the idea of proportionality that is essential to the concept of justice.” It is well known that “[t]he principal cost of applying any exclusionary rule ‘is, of course, letting guilty and possibly dangerous criminals go free .’” Montejo v. Louisiana, 129 S.Ct. 2079, 2090 (2009) (quoting Herring v. United States, 555 U.S. 135, 141 (2009)). Letting the guilty go free is “something that ‘offends basic concepts of the criminal justice system.’” Herring, 129 S.Ct. at 701, quoting Leon, 468 U.S. at 908. “‘[T]he rule’s costly toll upon truth-seeking and law enforcement objectives [...]

5. **[PDF] Recommendations for SSOSA reforms; treatment alternatives for ...**
   URL: https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf
   Content: internet would be different from cases where someone was actually interacting with a child via the internet”. He further stated “this offense in part resembles 25 McWhorter, S., Stander, V., Merrill, L., Thomsen, S., & Milner, J. (200=9). Reports of rape reperpetration by newly enlisted male navy personnel. Violence and Victims, 24 (2), 209-224. doi: 10.1891/0886-6708.24.2.204 26 Dietz (2020). Denial and minimization among sex offenders. Behavior Sciences & the Law, 38, 571-585. doi: 10.1002/bsl.2493 27 Hernandez (2000). Self-reported contact sexual offenses by participants in the Federal Bureau of Prisons’ Sex Offender Treatment Program: Implications for internet sex offenses. Bureau [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 14. PolitiFact / pf_009 - true

#### Input
- **Claim:** The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `true`
- **TLDR:** Sources show the slur was used, but none link it to Nazi genocide justification.
- **Explanation:** Source 1 confirms Ted Nugent used the phrase “subhuman mongrel” for President Obama, but it does not connect that phrase to Nazi rhetoric or genocide justification. Source 3 discusses Nazi dehumanization and genocide in general via the Nuremberg Laws, and Source 2 mentions the slur in modern political context, but none of the sources state that Nazis used “subhuman mongrel” or that this specific wording was used to justify the Holocaust.
- **Confidence reason:** Slur usage is documented; Nazi linkage is absent.
- **Claim verdicts:**
```json
[
  {
    "claim": "The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.csmonitor.com/USA/Politics/Decoder/2014/0221/Ted-Nugent-apologizes-to-President-Obama.-Sincere": "supporting",
  "https://everytownresearch.org/report/extreme-right/": "neutral",
  "https://www.nationalww2museum.org/war/articles/nuremberg-laws": "neutral",
  "https://en.wikipedia.org/wiki/Holocaust_denial": "neutral",
  "https://www.adl.org/resources/backgrounder/debunking-holocaust-denial-claims": "neutral"
}
```

#### Search Evidence Input
1. **Ted Nugent apologizes to President Obama. Sincere? - CSMonitor.com**
   URL: https://www.csmonitor.com/USA/Politics/Decoder/2014/0221/Ted-Nugent-apologizes-to-President-Obama.-Sincere
   Content: By Peter Grier Staff writer @petergrier Ted Nugent has apologized for calling President Obama a “subhuman mongrel.” The shock rocker/political provocateur on Friday told conservative radio host and CNN commentator Ben Ferguson that he “did cross the line” with those words, uttered in an interview with Guns.com in January. At first Nugent did not apologize directly to Mr. Obama himself. Instead, his main regret seemed to be that the controversy over his unrestrained rhetoric was affecting the man he campaigned with in Texas this week, state Attorney General and presumptive GOP gubernatorial candidate Greg Abbott, as well as other top GOP figures such as Sen. Ted Cruz of Texas. [...] # [...]

2. **Armed and Dangerous: How the Gun Lobby Enshrines Guns as Tools of the Extreme Right | Everytown Research & Policy**
   URL: https://everytownresearch.org/report/extreme-right/
   Content: and Peter Finn, “Prospect of Ban Drives a Surge in Demand for Assault Weapons,” Washington Post, January 17, 2013, . NRA leaders also deployed racist rhetoric to denigrate President Obama, with one board member calling him a “subhuman mongrel” and LaPierre declaring that “eight years of one demographically-symbolic president is enough.”77)“Ted Nugent: Obama a ‘Subhuman Mongrel,’” Politico, February 21, 2014, ; Alexandra Jaffe, “NRA’s Wayne LaPierre: Obama, Clinton ‘Demographically-Symbolic,’” CNN, April 15, 2015, .

3. **The Nuremberg Race Laws | The National WWII Museum | New Orleans**
   URL: https://www.nationalww2museum.org/war/articles/nuremberg-laws
   Content: subjects” without rights creates the preconditions to justify dehumanization, deportation, and genocide—a process that began in earnest with the passage of the Nuremberg Laws. [...] landscape encouraged darker “solutions” to the “Jewish problem,” resulting in the mass murder by shooting of over 1.5 million Jews on the Eastern Front. From there, Nazi leaders decided to deport the millions trapped in ghettos to static death camps where they were gassed en masse. This so-called “Final Solution” saw 1.8 million Jews murdered at Bełżec, Sobibór, and Treblinka, and another 1.1 million murdered at Auschwitz. [...] Historian Thomas Childers writes, “it was also symptomatic of Hitler’s modus [...]

4. **Holocaust denial - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Holocaust_denial
   Content: Holocaust denial is the negationist and antisemitic claim that Nazi Germany and its collaborators did not commit genocide against European Jews during World War II, ignoring overwhelming historical evidence to the contrary. Theories assert that the genocide of Jews is a fabrication or exaggeration. Holocaust denial includes making one or more of the following false claims: that Nazi Germany's "Final Solution" was aimed only at deporting Jews from the territory of the Third Reich and did not include their extermination; that Nazi authorities did not use extermination camps and gas chambers for the mass murder of Jews; that the actual number of Jews murdered is significantly lower than [...]

5. **Debunking Holocaust Denial Claims | ADL**
   URL: https://www.adl.org/resources/backgrounder/debunking-holocaust-denial-claims
   Content: Deniers Debunked The lack of a “master document” does not mean that the genocide of European Jews did not occur. The “Final Solution” — the Nazis’ comprehensive plan to murder all European Jews — was, as the Encyclopedia of the Holocaust observes, “the culmination of a long evolution of Nazi Jewish policy.” The destruction process was shaped gradually: it consisted of many thousands of directives, some written and some verbal. [...] Subsequent testimony by the architects of the Holocaust corroborates this fact pattern. Eichmann, while awaiting trial in Israel in 1960, related that Heydrich had told him in August 1941 that “the Führer has ordered the physical extermination of the Jews.” [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 15. PolitiFact / pf_011 - true

#### Input
- **Claim:** Says Donald Trump has changed his mind on abortion.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources say Trump shifted from supporting a federal abortion ban to leaving it to states.
- **Explanation:** FactCheck.org reports Trump said during the 2024 campaign he would not sign a national abortion ban, describing it as a change from his 2016 support for a federal abortion ban after 20 weeks (Source 1) and noting he released a video saying he would leave abortion to the states (Source 3). Al Jazeera similarly describes Trump’s “let states decide” position as a change (Source 4).
- **Confidence reason:** Multiple sources describe a shift, but not all details are consistent across outlets.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says Donald Trump has changed his mind on abortion.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/": "supporting",
  "https://www.factcheck.org/2023/09/trump-walked-back-abortion-statement-misleadingly-used-in-biden-harris-ad/": "supporting",
  "https://www.factcheck.org/2024/05/biden-twists-trumps-comments-on-tracking-pregnancies-and-punishing-women-who-get-abortions/": "supporting",
  "https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed": "supporting",
  "https://www.aclu.org/trump-on-abortion": "neutral"
}
```

#### Search Evidence Input
1. **Trump's 'Like It or Not' Comment and Harris' Response - FactCheck.org**
   URL: https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/
   Content: Of course, we don’t know what Trump will do in the future, but as we’ve written, Trump during this campaign has said he won’t sign a national abortion ban, a change from his position in 2016, when Trump backed a federal abortion ban after 20 weeks of pregnancy. He says he’s against restrictions on birth control, and he supports IVF, or in vitro fertilization. Trump has said it’s up to states to decide if they want to monitor women’s pregnancies. [...] Harris also cited Project 2025. “And we know that what he has planned includes a national abortion ban, restricting access to birth control, putting IVF treatments at risk, and forcing states to monitor women’s pregnancies. You don’t have [...]

2. **Trump Walked Back Abortion Statement Misleadingly Used in Biden-Harris Ad - FactCheck.org**
   URL: https://www.factcheck.org/2023/09/trump-walked-back-abortion-statement-misleadingly-used-in-biden-harris-ad/
   Content: But the ad leaves out what Trump said later that evening, after his comments were roundly criticized by groups both for and against abortion rights. In a statement published on his website, Trump took back his town hall answer. > Trump statement, March 30, 2016: If Congress were to pass legislation making abortion illegal and the federal courts upheld this legislation, or any state were permitted to ban abortion under state and federal law, the doctor or any other person performing this illegal act upon a woman would be held legally responsible, not the woman. The woman is a victim in this case as is the life in her womb. My position has not changed — like Ronald Reagan, I am pro-life [...]

3. **Biden Twists Trump's Comments on Tracking Pregnancies and Punishing Women Who Get Abortions - FactCheck.org**
   URL: https://www.factcheck.org/2024/05/biden-twists-trumps-comments-on-tracking-pregnancies-and-punishing-women-who-get-abortions/
   Content: Other Democrats echoed Biden’s claim. For example, Michigan Gov. Gretchen Whitmer claimed Trump “said again that women should be punished for having abortions. And he’s okay with states monitoring pregnant women to stop them from having abortions.” New York Gov. Kathy Hochul cited Trump’s Time interview as evidence that he “endorses punishing women who get an abortion.” But again, those were not Trump’s words, and the Democrats’ claims twist his message. [...] In several campaign speeches, however, President Joe Biden has twisted Trump’s words, claiming that Trump said “states should monitor women’s pregnancies and prosecute those who violate abortion bans.” (Emphasis is ours.) In the [...]

4. **‘Let states decide’: How Donald Trump’s position on abortion has changed | Donald Trump News | Al Jazeera**
   URL: https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed
   Content: In a video posted on his social media platform, Truth Social, Trump said: “My view is now that we have abortion where everybody wanted it from a legal standpoint, the states will determine by vote or legislation or perhaps both. And whatever they decide must be the law of the land – in this case, the law of the state.” ## Recommended Stories He also took credit for the overturning of Roe v Wade by the US Supreme Court in 2022, a decision that led to 24 US states enacting laws banning nearly all abortions by January 2023. On the other hand, he voiced his support for abortion under three exceptions, in cases of rape, incest and when the life of the mother is at risk. Until now, Trump’s [...]

5. **Trump on Abortion | American Civil Liberties Union**
   URL: https://www.aclu.org/trump-on-abortion
   Content: The threats to people’s ability to control their bodies and their reproductive lives don’t stop with attempts to outlaw abortion. For example, Trump recently admitted that he was looking at ways to restrict access to contraception. While electoral realities forced him to attempt to walk back that statement, as one of the leading anti-reproductive-health members of Trump’s administration recently explained, Trump’s “track record is the best evidence, I think, you could have of what a second term might look like if Trump wins.” That track record includes, among other things, changing federal rules that decimated access to birth control for low-income people by forcing Planned Parenthood [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 16. PolitiFact / pf_014 - half-true

#### Input
- **Claim:** Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources don’t provide the claimed 95% survey result or the amnesty motivation.
- **Explanation:** None of the provided sources contain a survey stating that 95% of people caught crossing the U.S.-Mexico border said they were coming because they were promised amnesty. Source 1 discusses border apprehension declines and mentions an “amnesty plan,” but it does not provide the specific survey statistic or the quoted motivation. Source 2 and Source 3 discuss broader immigration/asylum context without the claimed 95% survey finding, and Source 5 is a congressional statement about expected effects of amnesty rather than a survey result.
- **Confidence reason:** No source reports the specific 95% survey claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says 95 percent of people caught crossing the U.S.-Mexico border said in a survey we are coming because weve been promised amnesty.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://cis.org/Arthur/Fact-Check-Illegal-Immigration-Down-90-Percent-Thanks-Biden": "neutral",
  "https://cis.org/Arthur/Who-FactChecks-FactCheckers": "neutral",
  "https://www.npr.org/2018/11/27/670807343/fact-check-whats-happening-on-the-u-s-mexico-border": "neutral",
  "https://azcir.org/news/2025/03/03/did-encounters-us-mexico-border-drop-by-95percent-in-first-week-of-trump-presidency-no/": "neutral",
  "https://www.congress.gov/event/113th-congress/house-event/LC29861/text": "neutral"
}
```

#### Search Evidence Input
1. **Fact Check: Illegal Immigration Down ‘90 Percent’ Thanks to Biden**
   URL: https://cis.org/Arthur/Fact-Check-Illegal-Immigration-Down-90-Percent-Thanks-Biden
   Content: In March, agents at the U.S.-Mexico line apprehended 3,811 nationals of those four countries, which is a 95 percent decline from December, when apprehensions of aliens from those countries totaled more than 84,000 — the highest figure for those four nationalities, again, ever. But the March figure was still a 235 percent increase over Southwest border apprehensions for nationals of those four countries in March 2020 (admittedly the month that the Covid-19 pandemic was declared), and a higher apprehension total than in any month when Joe Biden wasn’t president, in whole or part (4,410 Venezuelans, Nicaraguans, Haitians, and Cubans were caught entering illegally in January 2021). With a [...]

2. **Who Fact-Checks the Fact-Checkers?**
   URL: https://cis.org/Arthur/Who-FactChecks-FactCheckers
   Content: By contrast, according to CBP statistics, in FY 2019 CBP is now averaging 31,188 family units and UACs detained at and between the ports of entry a month, a 136 percent increase over FY 2017. In December 2018, in fact, almost 61 percent of all aliens deemed inadmissible at the ports of entry and apprehended entering between the ports were family units or UACs. Of those family units apprehended between the ports of entry, 95 percent are from El Salvador, Guatemala, or Honduras. Under the Flores settlement agreement and the 2008 Trafficking Victims Protection Reauthorization Act (TVPRA), the children in those family units must be released in 20 days, as I explained in my May 2018 [...]

3. **FACT CHECK: What's Happening On The U.S.-Mexico Border? : NPR**
   URL: https://www.npr.org/2018/11/27/670807343/fact-check-whats-happening-on-the-u-s-mexico-border
   Content: What is asylum? Seeking asylum means asking the U.S. to accept you — legally — because of persecution you are facing in your home country. Crossing the border illegally is a misdemeanor; for a person who has already been deported once, it's a felony. Seeking asylum at a port of entry, however, is not a crime at all. However, authorities at legal border crossings have been limiting the number of people who can request asylum. Only 40 to 100 people are allowed each day, Fredrick says. "People in the caravan who want to request asylum, they're looking at months to even be heard first by U.S. authorities, and then for that claim to be processed can take months or even years," Fredrick [...]

4. **FACT BRIEF: Did encounters at the U.S.-Mexico border decrease by 95% in the first week of Trump’s presidency?**
   URL: https://azcir.org/news/2025/03/03/did-encounters-us-mexico-border-drop-by-95percent-in-first-week-of-trump-presidency-no/
   Content: The Arizona Center for Investigative Reporting partners with Gigafact to produce fact briefs, or quick-response fact checks, about trending claims relating to Arizona. ## Sources Support AZCIR with a donation! Your support makes our work possible! Sign Up, Stay Informed The Arizona Center for Investigative Reporting is partnering with Gigafact to produce timely fact briefs, or quick-response fact checks, about trending claims relating to Arizona. gigafact logo for fact briefs azcir logo for fact briefs ### RELATED Avatar photo ## Carmela GuaglianoneAZCIR Fact Checker Carmela Guaglianone is a fact-checker for the Arizona Center for Investigative Reporting, working in partnership with [...]

5. **OPEN BORDERS: THE IMPACT OF PRESIDENTIAL AMNESTY ON BORDER SECURITY | Congress.gov | Library of Congress**
   URL: https://www.congress.gov/event/113th-congress/house-event/LC29861/text
   Content: Mexico and Central America, we are simply fooling ourselves. We will see a wave of illegal immigration because of the President's actions. At its core, the President's unilateral amnesty plan is deeply unfair to the millions who are waiting in line to become a part of our great Nation, and it demonstrates reckless disregard for America's security. We have a formal immigration process for a reason: To promote fairness in allowing people to enter the United States and to keep those who will seek to do us harm outside of our borders. Sadly, the Department of Homeland Security is unprepared to handle the coming surge that the President's policies will incite. The Border Patrol's resources [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 17. PolitiFact / pf_017 - true

#### Input
- **Claim:** In the last 10 years, Georgias middle class income has dropped $6,500.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact and GBPI both indicate Georgia middle-class income fell by about $6,500 in 10 years.
- **Explanation:** Source 2 (PolitiFact) states that Carter’s ad—claiming middle-class income dropped $6,500 in 10 years—was “on target” with Census Bureau data, citing an inflation-adjusted decline of $6,682 from 2002 to 2012. Source 1 (GBPI) also reports that Georgia’s median household income fell by nearly $8,000 from 2007 to 2011 and that as of 2016 middle-class Georgians bring home about 7% less income than in 2000, consistent with a substantial decline over roughly the last decade.
- **Confidence reason:** Two sources support the magnitude, but definitions/years differ slightly.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the last 10 years, Georgias middle class income has dropped $6,500.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.gbpi.org/wp-content/uploads/2018/02/Georgias-People-Hold-Untapped-Value.pdf": "supporting",
  "https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/": "supporting",
  "https://www.neilsberg.com/insights/georgia-median-household-income/": "neutral",
  "https://www.incomebyzipcode.com/georgia": "neutral",
  "https://www.census.gov/quickfacts/fact/table/GA/INC110224": "neutral"
}
```

#### Search Evidence Input
1. **Fact Sheet: Georgians Hold Untapped Potential**
   URL: https://www.gbpi.org/wp-content/uploads/2018/02/Georgias-People-Hold-Untapped-Value.pdf
   Content: brought home about as much in annual income as families in other states. But their earnings slipped soon after the millennium and crashed during the Great Recession. Georgia’s median household income fell by nearly $8,000 from 2007 to 2011, steeper than the nation as a whole. As of 2016, middle class Georgians bring home about 7 percent less income than in 2000. Economic struggle limits families’ ability to thrive, especially for groups historically excluded from opportunity. About 23 percent of children in Georgia, 14 percent of working-age adults and 10 percent of seniors in 2016 struggled to get by, as measured by people who live below the federal poverty line. That’s less than [...]

2. **PolitiFact | Carter claim about median household income on target**
   URL: https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/
   Content: "What we saw with the Great Recession, starting around 2007, was employment and income just really fell through the floor due to the collapse of the housing market, the collapse of the stock market," Tharpe said. "Those really hurt Georgia because of our reliance on the housing industry and construction jobs." Since that crash, the economy has been gradually moving in the right direction, he said. "But incomes and the ability for families to make a living and make ends meet is really lagging behind," Tharpe said. "We haven’t really seen that much growth since we hit that floor." In summary, Carter’s ad says middle-class income has dropped $6,500 in 10 years. [...] Nationally, in that [...]

3. **Georgia Median Household Income - 2025 Update | Neilsberg**
   URL: https://www.neilsberg.com/insights/georgia-median-household-income/
   Content: | Year | Median Household Income | YOY Change($) | YOY Change(%) | --- --- | | 2010 | 69,330 - | | 2011 | 67,716 | -1,614 | -2.33% | | 2012 | 66,153 | -1,563 | -2.31% | | 2013 | 64,609 | -1,544 | -2.33% | | 2014 | 63,760 | -849 | -1.31% | | 2015 | 64,009 | 249 | 0.39% | | 2016 | 64,997 | 988 | 1.54% | | 2017 | 66,063 | 1,066 | 1.64% | | 2018 | 67,777 | 1,714 | 2.59% | | 2019 | 70,181 | 2,404 | 3.55% | | 2020 | 72,237 | 2,056 | 2.93% | | 2021 | 73,191 | 954 | 1.32% | | 2022 | 74,298 | 1,107 | 1.51% | | 2023 | 74,664 | 366 | 0.49% | TABLE OF CONTENTS Georgia median household income trends: 2000 to 2023 Median household income in Georgia by household size Georgia income distribution and [...]

4. **Georgia Income Statistics | Current Census Data for Georgia Zip Codes**
   URL: https://www.incomebyzipcode.com/georgia
   Content: ### Georgia Income Levels or Income Distribution | | | | --- | Households | 4,074,366 | 100% | | Less than $10,000 | 219,526 | 5% | | $10,000 to $14,999 | 138,699 | 3% | | $15,000 to $19,999 | 128,174 | 3% | | $20,000 to $24,999 | 139,522 | 3% | | $25,000 to $29,999 | 135,539 | 3% | | $30,000 to $34,999 | 141,222 | 3% | | $35,000 to $39,999 | 146,930 | 4% | | $40,000 to $44,999 | 146,243 | 4% | | $45,000 to $49,999 | 141,769 | 3% | | $50,000 to $59,999 | 265,754 | 7% | | $60,000 to $74,999 | 380,471 | 9% | | $75,000 to $99,999 | 529,016 | 13% | | $100,000 to $124,999 | 411,252 | 10% | | $125,000 to $149,999 | 293,369 | 7% | | $150,000 to $199,999 | 373,457 | 9% | | $200,000 or more | [...]

5. **U.S. Census Bureau QuickFacts: Georgia**
   URL: https://www.census.gov/quickfacts/fact/table/GA/INC110224
   Content: | Total health care and social assistance receipts/revenue, 2022 ($1,000)(c) | 95,053,842 | | Total transportation and warehousing receipts/revenue, 2022 ($1,000)(c) | 55,684,552 | | Total retail sales, 2022 ($1,000)(c) | 216,836,912 | | Total retail sales per capita, 2022(c) | $19,869 | | Transportation | | --- | | Mean travel time to work (minutes), workers age 16 years+, 2020-2024 | 28.3 | | Income & Poverty | | --- | | Median households income (in 2024 dollars), 2020-2024 | $77,353 | | Per capita income in past 12 months (in 2024 dollars), 2020-2024 | $40,924 | | Persons in poverty, percent |  12.6% | [...] ### Table | All Topics Population Age and Sex Race and Hispanic Origin [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 18. PolitiFact / pf_018 - half-true

#### Input
- **Claim:** Oil production is down 14 percent this year on federal land.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources don’t provide federal-land oil output data needed to verify a 14% drop.
- **Explanation:** None of the provided sources state that oil production on federal land is down 14% this year. Source 5 (EIA) forecasts total U.S. crude production averaging 13.5 million b/d in 2026, about 100,000 b/d less than 2025, but it does not quantify a 14% federal-land decline. Source 1 discusses EIA STEO projections including Federal Gulf of America output, but it does not give a “down 14% this year on federal land” figure.
- **Confidence reason:** Federal-land 14% figure is not present in any source.
- **Claim verdicts:**
```json
[
  {
    "claim": "Oil production is down 14 percent this year on federal land.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/": "neutral",
  "https://www.factcheck.org/issue/oil-production/": "neutral",
  "https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/": "neutral",
  "https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/": "neutral",
  "https://www.eia.gov/todayinenergy/detail.php?id=66844": "neutral"
}
```

#### Search Evidence Input
1. **EIA Sees USA Crude Oil Production Dropping in 2026, 2027 | Rigzone**
   URL: https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/
   Content: In 2025, Lower 48 States production averaged 11.28 million barrels per day, Federal Gulf of America production came in at 1.91 million barrels per day, and Alaska output averaged 0.42 million barrels per day, the STEO showed. A quarterly breakdown included in the EIA’s latest STEO projected that U.S. crude oil production will come in at 13.73 million barrels per day in the first quarter of this year, 13.65 million barrels per day in the second quarter, 13.47 million barrels per day in the third quarter, 13.50 million barrels per day in the fourth quarter, 13.43 million barrels per day in the first quarter of 2027, 13.31 million barrels per day in the second quarter, and 13.13 million [...]

2. **oil production Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/oil-production/
   Content: FactCheck.org® A Project of The Annenberg Public Policy Center Become a Facebook fan Follow us on Twitter Get the RSS feed Follow on Insta Sign up for the email newsletter Help us hold politicians accountable. # Issues: oil production ### FactChecking Trump’s State of the Union Address FactChecking Trump’s State of the Union Address February 25, 2026 In the first State of the Union address of his second term, President Donald Trump proclaimed that “our nation is back, bigger, better, richer and stronger than ever before.” But our review of his speech found that he distorted a number of facts about the state of the economy, health care, immigration and other topics. ### Trump’s Numbers, [...]

3. **EIA sees 2026 oil production decline despite regional growth EIA sees 2026 oil production decline despite regional growth**
   URL: https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/
   Content: This marginal dip marks a turning point after steady expansion in US oil output driven primarily by shale plays and offshore developments. The EIA attributes the projected decline to a combination of weaker growth in key producing regions and lower oil prices, which may disincentivize new drilling. Production growth in 2025 was largely concentrated in the Permian Basin, with additional contributions from federal offshore areas in the Gulf of Mexico and new developments in Alaska. However, those gains are expected to taper or be outpaced by declines in other mature or cost-constrained regions across the Lower 48 states. Even with ongoing efficiencies, the pace of well completions is [...]

4. **U.S. energy agency forecasts a modest dip in domestic crude production in 2026**
   URL: https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/
   Content: March 24, 2026 BLM formal protest ### BLM initiates formal protest window ahead of Utah oil and gas lease auction scheduled for March 31, 2026 March 23, 2026 BLM lease, oil and gas rig ### BLM launches early stakeholder feedback process for August 2026 oil and gas lease auction in Montana and North Dakota March 22, 2026 The EIA has reported that US crude oil production will average approximately 13.5 million barrels per day (b/d) this year, which is roughly 100,000 b/d less than in 2025. The forecast follows four years of substantial crude oil production growth in the United States. ### The Permian Basin: A cornerstone of the United States oil and gas industries [...] Gastech The [...]

5. **EIA forecasts U.S. crude oil production will decrease slightly in 2026 - U.S. Energy Information Administration (EIA)**
   URL: https://www.eia.gov/todayinenergy/detail.php?id=66844
   Content: In our latest Short-Term Energy Outlook, we forecast U.S. crude oil production will average 13.5 million barrels per day (b/d) in 2026, about 100,000 b/d less than in 2025. This forecast decline in production follows four years of rising crude oil output. Production increased by 0.3 million b/d in 2024 and by 0.4 million b/d in 2025, mostly because of increased output in the Permian Basin in Texas and New Mexico. In 2026, we forecast modest production increases in Alaska, the Federal Gulf of America, and the Permian will be offset by declines in other parts of the United States. We forecast that the West Texas Intermediate crude oil price will average $65 per barrel (b) in 2025 and [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 19. PolitiFact / pf_019 - barely-true

#### Input
- **Claim:** Onion Creeks highest flow rate on a recent night of flooding was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `62`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `mostly_false, mixed`
- **TLDR:** 120,000 cfs is supported, but the Niagara Falls comparison is disputed and based on questionable references.
- **Explanation:** Sources 1 and 2 both state that Onion Creek’s highest flow rate on Oct. 31 was 120,000 cubic feet per second and that this was “nearly double” the average flow rate of Niagara Falls. However, Source 2 and Source 3 explain that the Niagara Falls “average” figure came from Wikipedia and that the city’s 120,000 cfs figure relied on older “provisional” USGS data (with later USGS readings higher than 120,000 cfs).
- **Confidence reason:** Flow-rate value is supported, but Niagara comparison methodology is contested.
- **Claim verdicts:**
```json
[
  {
    "claim": "Onion Creeks highest flow rate on a recent night of flooding was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://data.austintexas.gov/stories/s/2013-Halloween-Flood/fr92-dkxr/": "supporting",
  "https://www.politifact.com/factchecks/2013/nov/14/city-austin/during-flood-austins-onion-creek-flowed-34-percent/": "supporting",
  "https://www.statesman.com/story/news/2013/11/16/politifact-onion-creek-was-raging-but-niagara-falls-comparison-is-flawed/9987785007/": "contradicting",
  "https://www.austinchronicle.com/news/double-the-flow-rate-of-niagara-falls-12090015/": "supporting",
  "https://water.noaa.gov/gauges/atit2": "neutral"
}
```

#### Search Evidence Input
1. **2013 Halloween Flood | Open Data | City of Austin, Texas**
   URL: https://data.austintexas.gov/stories/s/2013-Halloween-Flood/fr92-dkxr/
   Content: The Onion Creek's highest flow rate on October 31 was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls. Link:

2. **PolitiFact | UPDATED: During flood, Austin's Onion Creek flowed up to 34 percent faster than Niagara Falls on average**
   URL: https://www.politifact.com/factchecks/2013/nov/14/city-austin/during-flood-austins-onion-creek-flowed-34-percent/
   Content: The city’s press release continued: "The Onion Creek’s highest flow rate during Oct. 31 was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls." Flow rate is the volume of fluid which passes through a given surface per unit of time, the release said. Do both ends of this flow-rate claim hold water? By telephone and email, officials later told us they based the reference to the Onion Creek flow rate on USGS information on the creek’s flow at U.S. 183 on Austin’s southeastern edge. They said the cited average flow rate of Niagara Falls, the international tourist site in New York state and Canada, came from Wikipedia, the collaboratively edited, [...]

3. **PolitiFact: Onion Creek was raging, but Niagara Falls comparison is flawed**
   URL: https://www.statesman.com/story/news/2013/11/16/politifact-onion-creek-was-raging-but-niagara-falls-comparison-is-flawed/9987785007/
   Content: # PolitiFact: Onion Creek was raging, but Niagara Falls comparison is flawed On a recent day of fatal flash floods, a Southeast Austin creek ran so quickly that it outpaced Niagara Falls in a way, the city of Austin said. A Nov. 6 city press release said that according to the U.S. Geological Survey, water levels at Onion Creek at U.S. 183 reached a record height of 41 feet. “The Onion Creek’s highest flow rate during Oct. 31 was 120,000 cubic feet per second, which is nearly double the average flow rate of Niagara Falls,” the press release said. Does this flow-rate claim hold water? Advertisement Article continues below this ad [...] Advertisement Article continues below this ad “It’s [...]

4. **Double The Flow Rate of Niagara Falls**
   URL: https://www.austinchronicle.com/news/double-the-flow-rate-of-niagara-falls-12090015/
   Content: The HSEM also released numbers from the U.S. Geological Survey on the extent of the flooding. Onion Creek had a staggering flow rate, doubling the average flow rate of Niagra Falls. At US 183, Onion Creek water levels reached a record height of 41 feet. In a 15 minute period, the water gauge rose 11 feet. According to available records, this was the first time water levels rose to to over 40 feet in that area. Only on three other years did the water level exceed 35 feet – in 1869, 1921, and 1869. [...] Tommorow, the Austin Police Department‘s Region 4 District representatives, the Austin Police Activities League, and Cops for Charities will be hosting soccer games and trick-or-treating [...]

5. **Onion Creek at US 183**
   URL: https://water.noaa.gov/gauges/atit2
   Content: Notice: The 2026 National Hydrologic Assessment has been released. Click here for more information. Flood Inundation Mapping services are now available for 60% of the U.S. population here. Additional NWPS resources are available here. Thank you for visiting a National Oceanic and Atmospheric Administration (NOAA) website. The link you have selected will take you to a non-U.S. Government website for additional information. NOAA is not responsible for the content of any linked website not operated by NOAA. This link is provided solely for your information and convenience, and does not imply any endorsement by NOAA or the U.S. Department of Commerce of the linked website or any [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 20. PolitiFact / pf_020 - pants-fire

#### Input
- **Claim:** U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence."
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `70`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false`
- **TLDR:** PolitiFact reports Langevin opposed the fence out of fear someone would get hurt.
- **Explanation:** Source 1 (PolitiFact) directly states the attributed reason: Langevin opposed the U.S.-Mexican border fence because he was afraid someone would get hurt trying to go around it. The other provided sources do not address this specific claim about Langevin’s stated motivation.
- **Confidence reason:** Only one source directly addresses the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration \"because he is afraid that someone will get hurt trying to go around the fence.\"",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/": "supporting",
  "https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm": "neutral",
  "https://www.congress.gov/event/110th-congress/house-event/LC8330/text": "neutral",
  "https://docs.house.gov/meetings/FA/FA00/20210930/114085/HMKP-117-FA00-20210930-SD002.pdf": "neutral",
  "https://www.dhs.gov/sites/default/files/publications/dhs-congressional-logs-2011_0.pdf": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Gardiner says Langevin opposed U.S.-Mexican border fence for fear someone will get hurt**
   URL: https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/
   Content: U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence.". # Gardiner says Langevin opposed U.S.-Mexican border fence for fear someone will get hurt. Gardiner, one of three Republicans hoping to unseat Democratic U.S. Rep. James Langevin in the 2nd District, devotes a lot of space to the issue on a web page called Illegal Immigration: Costly and Unfair to Citizens, Tax payers, and Legal Residents. He sent us to a website called OnTheIssues.org, which tracks voting records on a variety of issues, and a web page called "James Langevin on Immigration.". So regardless of the real reason [...]

2. **CONSTRUCTION OPTIONS AND STRATEGIC PLACEMENT**
   URL: https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm
   Content: In fact, I have testified, as my good friend mentioned, on issues of border security and border enforcement many times before Members of Congress. Over 11

3. **HOMELAND SECURITY FAILURES: TWIC EXAMINED**
   URL: https://www.congress.gov/event/110th-congress/house-event/LC8330/text
   Content: - [x] Aging (Special) (95th-119th) - [x] Aging (Special) (95th-119th) - [x] Agriculture, Nutrition, and Forestry (95th-119th) - [x] Agriculture, Nutrition, and Forestry (95th-119th) - [x] Appropriations (93rd-119th) - [x] Appropriations (93rd-119th) - [x] Armed Services (93rd-119th) - [x] Armed Services (93rd-119th) - [x] Banking, Housing, and Urban Affairs (93rd-119th) - [x] Banking, Housing, and Urban Affairs (93rd-119th) - [x] Budget (94th-119th) - [x] Budget (94th-119th) - [x] Caucus on International Narcotics Control (99th-119th) - [x] Caucus on International Narcotics Control (99th-119th) - [x] Commerce, Science, and Transportation (95th-119th) - [x] Commerce, Science, and [...]

4. **[PDF] Sexual assaults rise as the Peace Corps fails its volunteers**
   URL: https://docs.house.gov/meetings/FA/FA00/20210930/114085/HMKP-117-FA00-20210930-SD002.pdf
   Content: Dyan Mazurana, a Tufts University professor who has studied sexual violence in the international aid community, said the Peace Corps’ sexual assault statistics depict “an organization that can’t get its act together.” She said the agency should shut down programs if Peace Corps staff can’t ensure its volunteers will be safe. Fucci is one of six former Peace Corps volunteers interviewed by USA TODAY who said they were sexually assaulted by people they lived or worked with. Murray, who left the agency later that year, recently reviewed USA TODAY’s analysis of the most recent five years of Peace Corps crime data and said the data on rape and aggravated sexual assault still suggests [...]

5. **[PDF] WP# Receive Date Congressman Name Subject of Request 892621 ...**
   URL: https://www.dhs.gov/sites/default/files/publications/dhs-congressional-logs-2011_0.pdf
   Content: 893738 l/24/2011 Congressman Lloyd Doggett status of an 1-601 waiver 893739 1/24/2011 Congressman Michael Doyle Customer is requesting theat the I-90 application be expedited 892069 113/2011 Senator Richard J. 893612 l/21/201 1 Senator Tom Harkin Status of an I-290B 892575 1/10/2011 Congressman Doc Hastings Customer is requesting the status of an 1-130 petition for her husband. Dingell address a problem with a constituent 893779 1/24/2011 Congressman Kevin McCarthy Customer is requesting assistance with obtaining his certificate of citizenship 892380 1/6/2011 Senator Claire McCask.ilJ Re the status o~(bW 3 J jr-730 cases. 892584 1/10/2011 Senator Claire McCaskill Requests the status of [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 21. PolitiFact / pf_022 - mostly-true

#### Input
- **Claim:** Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `mostly_true, true`
- **TLDR:** PolitiFact supports the layoffs and tax-break context, but the CEO-to-Kasich super PAC link is not independently verified here.
- **Explanation:** Source 1 (PolitiFact) directly states that the company received state tax breaks and later laid off 100 Ohioans, and it also repeats the allegation that the CEO cut a half-million-dollar check to Kasich’s super PAC. However, the other provided sources do not corroborate the specific “half-million-dollar check to Kasich’s super PAC” detail, and they focus on broader JobsOhio/tax issues rather than that CEO donation. Therefore, the layoffs/tax-break portion is supported by the provided material, while the CEO donation portion is unverifiable from the remaining sources.
- **Confidence reason:** Only one source addresses the key donation and layoffs details.
- **Claim verdicts:**
```json
[
  {
    "claim": "Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/": "supporting",
  "https://www.urban.org/2016-analysis/kasich-cut-income-taxes-ohio-raised-sales-taxes": "neutral",
  "https://www.dispatch.com/story/news/politics/state/2026/03/19/osu-ted-carter-scandal-involved-jobsohio-podcast-spending-transparency/89120669007/": "neutral",
  "https://ohiocapitaljournal.com/2026/04/17/ohio-republican-bill-slammed-as-another-tax-giveaway-for-the-rich/": "neutral",
  "https://taxpolicycenter.org/taxvox/ohio-lawmakers-turn-surprise-surplus-huge-tax-cut": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Ted Cruz ad revisits a controversy from Kasich’s governorship of Ohio**
   URL: https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/
   Content: "Right before John Kasich was governor, he collected $611,000 from a Fortune 500 corporation," the ad says. "After Kasich became governor, that same company received $619 grand in state tax breaks for job creation. But last year, the company laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasich’s super PAC. John Kasich, not for us." To find out whether it’s fact or fiction, let’s take each allegation one at a time. Kasich took money from a Fortune 500 company [...] Last year, the company laid off 100 Ohioans In March 2015, Worthington announced it was cutting 555 jobs nationwide, which included 115 in Ohio. The company blamed the loss of these jobs [...]

2. **Kasich cut income taxes in Ohio but raised sales taxes | Urban Institute**
   URL: https://www.urban.org/2016-analysis/kasich-cut-income-taxes-ohio-raised-sales-taxes
   Content: Skip to main content The Urban.org Logo - Research and Evidence - What We Do - Events - About - Connect Urban is a trusted source for changemakers seeking to create a world where everyone has the opportunity and power to thrive. Learn more about us. - About Urban - Mission and Values - Our Story - Collaborate With Us - Our People - Careers - Support Urban - Organizational Principles - For the Media - Contact Us Urban values sharing our insights widely and connecting with partners across the country. Learn how you can stay informed and support us. - Collaborate With Us - Subscribe for Email Updates - Support Urban's Work - Attend an Event - Explore Careers - Get Involved - For the Media [...]

3. **OSU Ted Carter scandal puts spotlight on JobsOhio spending**
   URL: https://www.dispatch.com/story/news/politics/state/2026/03/19/osu-ted-carter-scandal-involved-jobsohio-podcast-spending-transparency/89120669007/
   Content: JobsOhio is a private nonprofit funded by the state's liquor profits. Former Gov. John Kasich created the organization in 2011 to help Ohio attract new businesses and development without the bureaucracy of government. But Kasich said he was disappointed by JobsOhio's decision to sponsor a podcast that struck him as a "misguided and weak attempt to deal with workforce issues." "What concerns me most is the possibility of mission drift," Kasich said in a Facebook post. "JobsOhio was created for one purpose and one purpose only: to create jobs for Ohio. I fully understand the importance of building a strong workforce, but this was clearly a failed attempt." Ohio Attorney General Dave [...]

4. **Ohio Republican bill slammed as another tax giveaway for the rich • Ohio Capital Journal**
   URL: https://ohiocapitaljournal.com/2026/04/17/ohio-republican-bill-slammed-as-another-tax-giveaway-for-the-rich/
   Content: The 2013 LLC tax break, which provides 40% of its benefits to the largest 7% of limited liability businesses and costs taxpayers about $1 billion a year. JobsOhio was created in 2011 under Kasich’s leadership. It has given more than $1 billion in what used to be public money to business interests, but it has struggled to show that it’s created a significant number of jobs. It did, however, give $60,000 to a woman with whom former Ohio State President Ted Carter had an “inappropriate relationship” to make four podcasts. She only made one. The “flat” state income tax passed in 2025. Policy Matters said it will cost $1 billion a year, with 40% of the benefit flowing to people making over [...]

5. **Ohio Lawmakers Turn A Surprise Surplus Into A Huge Tax Cut | Tax Policy Center**
   URL: https://taxpolicycenter.org/taxvox/ohio-lawmakers-turn-surprise-surplus-huge-tax-cut
   Content: without any of Kasich’s proposed offsets. According to the official numbers, it would reduce revenues by about $500 million in 2015 and $100 million after that. Among the legislature’s changes: [...] double the state earned income tax credit (EITC). At the same time, it would increase an already-generous business tax deduction. In February, Republican Kasich—who was something of a deficit hawk during his years in Congress--presented a revised budget that would reduce tax collections by about $100 million in 2015 and 2016. Kasich would have expanded previously-enacted income tax cuts for businesses and individuals. But because he proposed to partially offset them with a higher [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 22. PolitiFact / pf_025 - mostly-true

#### Input
- **Claim:** Federal spending on entitlements is projected to consume all revenue by 2045.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `20`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `mostly_true, true`
- **TLDR:** PolitiFact says CBO projections do not support entitlements consuming all federal revenue by 2045.
- **Explanation:** Source 1 directly evaluates the specific claim and concludes that using CBO current-law projections, entitlements would not consume every revenue dollar by 2045 (tax revenue would provide more money). Source 2 discusses rising entitlement spending and crowding out other spending, but it does not state that entitlements consume all revenue by 2045. Therefore, the provided sources mostly contradict the claim.
- **Confidence reason:** Source 1 directly tests the 2045 “all revenue” assertion using CBO projections.
- **Claim verdicts:**
```json
[
  {
    "claim": "Federal spending on entitlements is projected to consume all revenue by 2045.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/": "contradicting",
  "https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html": "neutral",
  "https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf": "neutral",
  "https://www.crfb.org/papers/explaining-federal-spending-and-revenue": "neutral",
  "https://budgetmodel.wharton.upenn.edu/t/Entitlements/": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Ohio Treasurer Josh Mandel says entitlement spending expected to consume all federal revenue by 2045**
   URL: https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/
   Content: The alternative projections were based on a realistic understanding of politics and policy -- and one such understanding was that Congress was almost certain to extend many if not all tax cuts. With a few exceptions, notably higher rates on families earning more than $450,000, that is close to what happened. So what did the alternative projections show about revenues and entitlements in 2045 -- that is, about Mandel’s claim? [...] Mandel’s debt figure was actually a tad low. The national debt, including money owed to investors and foreign governments as well as obligations owed from one federal account to another, was approaching $16.5 trillion -- and has since hit it -- the day he [...]

2. **Fiscal Challenges: Health Care, Taxes and Beyond**
   URL: https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html
   Content: Medicare spending is expected to rise from 2.3% of GDP currently to 7.0% of GDP in 2045, while federal spending on Medicaid (that is, excluding state contributions) will expand from 1.5% to 2.6% of national output. Much of the increase in Medicare spending is driven by per-beneficiary costs rising faster than inflation, even controlling for demographic trends. In sum, the costs to the federal government of the three most important entitlement programs are expected almost to double from 8.0% of GDP today to about 15.6% of GDP in 2045. In 2005, all other spending programs of the federal government, excluding interest payments on the national debt, amounted to 9.0% of GDP. Thus, if the [...]

3. **[PDF] Demographic Headwinds - Aspen Economic Strategy Group**
   URL: https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf
   Content: CBO projects that old-age dependency ratios will steadily rise from 34.2 percent in 2024 to 44.2 percent in 2055, as seen in figure 2. As a result, spending on the major old-age entitlement programs is also projected to continue to grow relative to GDP and is a key contributor to rising deficits and debt in CBO’s projections. The projected growth in old-age entitlement program spending can be attributed to (1) the size of cohorts expected to enter into retirement (due to past fertility rates and immigration), (2) CBO’s expectation that life expectancy will continue to rise, and (3) rising health costs. (Of note, projected future fertility rates do not play much of a role in this [...]

4. **Explaining Federal Spending and Revenue-Wed, 05/21/2025 - 12:00 | Committee for a Responsible Federal Budget**
   URL: https://www.crfb.org/papers/explaining-federal-spending-and-revenue
   Content: Individual taxes accounted for roughly half of all federal revenue, or $2.4 trillion. Payroll taxes, which fund Social Security and Medicare, accounted for about one-third and amounted to $1.7 trillion. Corporate income taxes totaled $530 billion (11 percent), and other sources, such as excise taxes, customs duties, estate taxes, fines and fees, made up 5 percent or $253 billion. Over the next decade, the Congressional Budget Office projects that under current law federal spending will increase from 23.4 percent of GDP in FY 2024 to 24.0 percent by 2035, while revenue will rise from 17.1 percent of GDP in FY 2024 to 18.3 percent by 2035. Over the past 50 years, spending has averaged [...]

5. **Entitlements | Penn Wharton Budget Model**
   URL: https://budgetmodel.wharton.upenn.edu/t/Entitlements/
   Content: Brendan Novak · · 55 min read Automatic Retirement Savings Plans for Low-Income Households Brief Entitlements Healthcare Social Security ## President Biden’s Proposal to Extend the Medicare Trust Fund PWBM estimates that President Biden’s new Medicare proposal would increase the solvency of the Medicare trust fund from the year 2028 to 2053. However, a significant share of that increase comes from redirecting existing (current law) revenue to the trust fund. Another portion comes from unspecific expenditure reductions that lack the details required to score. Counting only new income without unspecified expenditure reductions, we project, as an illustrative alternative, that the HI [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 23. PolitiFact / pf_027 - pants-fire

#### Input
- **Claim:** Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `false`
- **TLDR:** Sources say Canada restricts “false or misleading news,” but Fox wasn’t banned for that reason.
- **Explanation:** PolitiFact says the meme’s “banned for lying” rationale is not verifiable and that the claim “doesn’t” connect to Fox News being banned (Source 1). Snopes notes Canadian rules prohibit broadcasting “false or misleading news” and that these provisions helped keep Fox News out, but it does not support the specific claim that Fox News is banned because it violates a law preventing news channels from lying to viewers (Source 2). The provided legal/other sources do not substantiate the specific “banned in Canada” mechanism for Fox News (Sources 3-5).
- **Confidence reason:** Two fact-checks address it, but mechanism details conflict.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2014/jul/14/facebook-posts/fox-news-banned-canada/": "contradicting",
  "https://www.snopes.com/fact-check/canadian-fox/": "supporting",
  "https://www.justice.gc.ca/eng/csj-sjc/pl/charter-charte/c63.html": "neutral",
  "https://www.internetsociety.org/resources/internet-fragmentation/canadas-online-news-act/": "neutral",
  "https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/peace_security-paix_securite/combatt-disinformation-desinformation.aspx?lang=eng": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Is Fox News banned in Canada?**
   URL: https://www.politifact.com/factchecks/2014/jul/14/facebook-posts/fox-news-banned-canada/
   Content: "The (false news) provision has kept Fox News and right wing talk radio out of Canada and helped make Canada a model for liberal democracy and freedom," wrote Kennedy. "As a result of that law, Canadians enjoy high-quality news coverage including the kind of foreign affairs and investigative journalism that flourished in this country before Ronald Reagan abolished the ‘Fairness Doctrine’ in 1987." [...] What Kennedy is likely referring to are provisions in Canadian broadcast policy, include the Radio Act and other policies, that prohibit "any false or misleading news." These provisions against spreading misinformation used to be part of Canada’s criminal code, according to Canadian [...]

2. **Was the Fox News Channel Banned in Canada? | Snopes.com**
   URL: https://www.snopes.com/fact-check/canadian-fox/
   Content: It is true that various sections of CRTC regulations prohibit the broadcasting of "false or misleading news" by radio and television licensees, and that in 2011 the CRTC declined to narrow those regulations to apply only to "news that the licensee knows is false or misleading and that endangers or is likely to endanger the lives, health or safety of the public." [...] Canada's Radio Act requires that "a licenser may not broadcast ... any false or misleading news." The provision has kept Fox News and right-wing talk radio out of Canada and helped make Canada a model for liberal democracy and freedom. As a result of that law, Canadians enjoy high quality news coverage, including the kind [...]

3. **Bill C-63: An Act to enact the Online Harms Act, to amend the Criminal Code, the Canadian Human Rights Act and An Act respecting the mandatory reporting of Internet child pornography by persons who provide an Internet service and to make consequential and related amendments to other Acts**
   URL: https://www.justice.gc.ca/eng/csj-sjc/pl/charter-charte/c63.html
   Content: The following considerations support the consistency with the Charter of the duty to make certain content inaccessible to persons in Canada. Content that sexually victimizes a child or revictimizes a survivor and intimate content communicated without consent is expression that lies far from the core of the guarantee of free expression. Generally, expression that lies far from the core receives less protection under the Charter. Dissemination of some of this content already constitutes an offence under the Criminal Code. The objective of the duty to make this content inaccessible when it has been flagged or otherwise comes to an operator’s attention would be both to mitigate the risk of [...]

4. **Canada’s Online News Act - Internet Society**
   URL: https://www.internetsociety.org/resources/internet-fragmentation/canadas-online-news-act/
   Content: This is just one example of what reducing access to news can do in a crisis situation, but the impact is far greater. Services that aren’t even classified as ‘digital news intermediaries’ are affected. For example, it could make it harder for Canadian contributors to Wikipedia to do research and fact-checking, since this law hinders their ability to discover credible news content online in Canada. People in other countries have easier access to news. This law also poses a fragmentation threat because it centralizes management and restricts the use of links—a basic Internet function—by a centralized authority (CRTC) in Canada. This prevents people and businesses from contributing to the [...]

5. **Combatting foreign disinformation and information manipulation**
   URL: https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/peace_security-paix_securite/combatt-disinformation-desinformation.aspx?lang=eng
   Content: ### Sanctioning disinformation agents Canada has imposed sanctions against individuals and entities that are responsible for spreading false narratives and propaganda. Sanctions – Russian invasion of Ukraine tracks Canada's sanctions against disinformation and propaganda actors in the context of Russian invasion of Ukraine. ## Foreign disinformation and information manipulation Democracies rely on access to diverse, accurate and reliable information and news. This allows citizens and other members of society to develop informed opinions, take part in public debate, and hold governments to account. Information integrity, or the accuracy and reliability of content, enables democratic [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 24. PolitiFact / pf_030 - true

#### Input
- **Claim:** Today California is kicking our butt, creating more jobs and more economic growth than Texas.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `72`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact and Stanford evidence California’s job and income growth outpaced Texas in recent years.
- **Explanation:** PolitiFact’s fact checks on the exact “kicking our butt” claim rated it True, citing higher job growth rates for California than Texas (e.g., 2015 job growth 3% vs 1.5% and 2.8% vs 1.5% over May 2015–April 2016). Stanford’s SIEPR policy brief also reports California’s per-capita income growth outperformed Texas from 2000–2020 and that the gap widened from 2015 to 2020. None of the provided sources directly contradict California outperforming Texas on these measures; other sources (e.g., StatsPanda) are not needed to support the core claim and may be less authoritative.
- **Confidence reason:** Two PolitiFact checks directly address the claim; Stanford supports related growth metrics.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today California is kicking our butt, creating more jobs and more economic growth than Texas.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/": "supporting",
  "https://www.texasstandard.org/stories/__trashed-4/": "supporting",
  "https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/": "supporting",
  "https://siepr.stanford.edu/publications/policy-brief/tale-two-states-contrasting-economic-policy-california-and-texas": "supporting",
  "https://statspanda.com/blog/texas-vs-california-comparison": "neutral"
}
```

#### Search Evidence Input
1. **PolitiFact | Is California's economy 'growing a hell of a lot faster' than Texas?**
   URL: https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/
   Content: In August, PolitiFact Texas took a deep look at the economies of both California and Texas to evaluate a June claim by Julián Castro, the U.S. secretary of Housing and Urban Development, that "Today, California is kicking our butt, creating more jobs and more economic growth than Texas." It rated the claim True, citing greater jobs, per capita income and GDP growth rates in California. It noted Texas had a lower jobless rate. Building on that fact check, we looked at the most recent economic figures for both states to see if the assessment still holds. [...] California had one more economic bright spot in 2015: Per capita personal income grew at twice the rate as in Texas, 5.4 percent [...]

2. **Is Texas Trailing Behind California on Economic Growth? |  Texas Standard**
   URL: https://www.texasstandard.org/stories/__trashed-4/
   Content: Julián Castro, the U.S. secretary of Housing and Urban Development, brought up California during the Texas Democratic Party’s state convention after noting that as governor, Republican Rick Perry taunted the west coast state for its economy not matching his home state’s pace. “Today,” the former San Antonio mayor told reporters June 17, 2016, “California is kicking our butt, creating more jobs and more economic growth than Texas. Maybe what we need to do is trade in Gov. Jerry Brown,” of California, “for Gov. Greg Abbott and get better results.” Is that a fact? Gardner Selby of the PolitiFact Texas fact-checking team has the answer. [...] “Today,” the former San Antonio mayor told [...]

3. **PolitiFact | Julián Castro says California besting Texas in creating jobs, economic growth**
   URL: https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/
   Content: "Today," the former San Antonio mayor told reporters June 17, 2016, "California is kicking our butt, creating more jobs and more economic growth than Texas. Maybe what we need to do is trade in Gov. Jerry Brown," of California, "for Gov. Greg Abbott and get better results." Castro made a similar declaration in his evening keynote speech, telling delegates: "This is what happens when a party doesn’t believe in government in the first place but has absolute power over its people for decades. You know, they used to brag that Texas was doing so much better than big bad liberal California. But Texas Republicans managed to bungle that too. Because today California is kicking our butt in job [...]

4. **A tale of two states: Contrasting economic policy in California and Texas | Stanford Institute for Economic Policy Research (SIEPR)**
   URL: https://siepr.stanford.edu/publications/policy-brief/tale-two-states-contrasting-economic-policy-california-and-texas
   Content: In light of these population trends during the last decade or two, one might expect other measures of economic performance to show Texas as a rising force and California as a receding one. However, and as shown in Table 1 below, California’s performance stands out when considering the growth in per capita income (PCI) in recent years. Between 2000 and 2020, California’s PCI was significantly greater than both Texas and the U.S. as a whole (BEA, 2021). Both disparities grew substantially from 2015 to 2020. For example, while California’s per capita income was 20 percent higher than Texas’ in 2015, this gap surged to 30 percent just 5 years later. And this was not simply a COVID-induced [...]

5. **Texas vs California: America's Two Largest State Economies Compared by the Data | StatsPanda Blog | StatsPanda**
   URL: https://statspanda.com/blog/texas-vs-california-comparison
   Content: But the story changes when you factor in taxes and cost of living. Texas has no state income tax, while California's top rate of 13.3% is the highest in the nation. A tech worker earning $200,000 in California pays roughly $18,000 in state income tax; the same worker in Texas pays $0. This tax advantage has fueled massive corporate relocations — Tesla, Oracle, Hewlett Packard Enterprise, and Charles Schwab have all moved headquarters from California to Texas. Population growth is the clearest divergence: Texas grew 9.1% from 2020 to 2025, adding nearly 2.5 million people. California's population actually declined by 0.3%, a historic reversal. Texas is now projected to overtake [...]

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

## Arm C - Full Pipeline

Failures shown: 26

### 1. AVeriTeC / av_006 - Not Enough Evidence

#### Input
- **Claim:** Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `18`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources say the 2020 ranking image used 2019 data, not a released 2020 GTI ranking.
- **Explanation:** HumAngle and AFP report that the viral claim about Nigeria being third most terrorised in 2020 was misleading because the Global Terrorism Index 2020 ranking had not been released and the figures shown were from 2019. FactCheckHub similarly says the infographic was misleading and that the 2020 GTI ranking order differed from what was shared, with the TVC graphic using older data.
- **Confidence reason:** Multiple fact-checks directly address and refute the 2020 ranking claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Nigeria was the third most terrorised in the world in 2020, after Afghanistan and Iraq.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/": "contradicting",
  "https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/": "contradicting",
  "https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa": "contradicting",
  "https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism": "neutral",
  "https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **Factcheck: Nigeria Not Ranked Third Most Terrorised Country In 2020 - HumAngle**
   URL: https://humanglemedia.com/factcheck-nigeria-not-ranked-third-most-terrorised-country-in-2020/
   Stance: `contradicting`

2. **Misleading 2020 global terrorism ranking resurfaces online - FactCheckHub**
   URL: https://factcheckhub.com/misleading-2020-global-terrorism-ranking-resurfaces-online/
   Stance: `contradicting`

3. **Old data circulates claiming Nigeria is the most terrorised country in Africa | Fact Check**
   URL: https://factcheck.afp.com/old-data-circulates-claiming-nigeria-most-terrorised-country-africa
   Stance: `contradicting`

4. **Global Terrorism Index 2020: Measuring the impact of terrorism - World | ReliefWeb**
   URL: https://reliefweb.int/report/world/global-terrorism-index-2020-measuring-impact-terrorism
   Stance: `neutral`

5. **[PDF] 2024 Global Terrorism Index - Institute for Economics & Peace**
   URL: https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 2. AVeriTeC / av_007 - Not Enough Evidence

#### Input
- **Claim:** Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** Sources mostly argue enforcement and barriers increase smuggling, not decrease it.
- **Explanation:** Source 1 explicitly states that expanding border enforcement is more likely to increase human smuggling rather than decrease it, citing increased smuggler usage rates after enforcement. Source 4 similarly finds that increased enforcement can lead to more reliance on professional smugglers (and marginally higher violent crime in sectors), consistent with smuggling not decreasing. While Source 3 and DHS pages discuss reduced unauthorized entries, they do not provide evidence that illegal drug smuggling and human smuggling decreased specifically in areas where barriers were deployed; the drug/smuggling linkage is not established in the provided excerpts.
- **Confidence reason:** Direct evidence on smuggling effects is mostly negative; barrier-specific drug data absent.
- **Claim verdicts:**
```json
[
  {
    "claim": "Illegal drug, border crossings, and human smuggling activities have decreased in areas where barriers are deployed in the United States.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf": "contradicting",
  "https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers": "neutral",
  "https://cmsny.org/publications/jmhs-is-border-enforcement-effective/": "neutral",
  "https://ccis.ucsd.edu/_files/wp131.pdf": "contradicting",
  "https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025": "neutral"
}
```

#### Pipeline Sources Output
1. **[PDF] nfap policy brief » may 2022 - human smuggling and us immigration ...**
   URL: https://nfap.com/wp-content/uploads/2022/05/Human-Smuggling.NFAP-Policy-Brief.May-2022-1.pdf
   Stance: `contradicting`

2. **The Border Wall System is Deployed, Effective, and Disrupting Criminals and Smugglers | Homeland Security**
   URL: https://www.dhs.gov/archive/news/2020/10/29/border-wall-system-deployed-effective-and-disrupting-criminals-and-smugglers
   Stance: `neutral`

3. **Is Border Enforcement Effective? What We Know and What it Means - The Center for Migration Studies of New York (CMS)**
   URL: https://cmsny.org/publications/jmhs-is-border-enforcement-effective/
   Stance: `neutral`

4. **[PDF] The Effect of Illegal Immigration and Border Enforcement on Crime ...**
   URL: https://ccis.ucsd.edu/_files/wp131.pdf
   Stance: `contradicting`

5. **Border Crossings Once Again at a Record Low in November 2025 | Homeland Security**
   URL: https://www.dhs.gov/news/2025/12/04/border-crossings-once-again-record-low-november-2025
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 3. AVeriTeC / av_008 - Refuted

#### Input
- **Claim:** Since 2002, South Africa’s police force has grown by 50%.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** The sources don’t provide police-force growth data from 2002 to support the 50% claim.
- **Explanation:** None of the provided sources include figures for South Africa’s police force size in 2002 and a later year to calculate a 50% increase. Source 2 discusses police shortages and cross-country comparisons, but it does not state a 2002-to-present growth percentage. Sources 1 and 4 are annual reports, but the provided excerpts only list legislation and do not contain the needed staffing-growth statistics.
- **Confidence reason:** No source excerpt contains the required 2002-to-growth percentage data.
- **Claim verdicts:**
```json
[
  {
    "claim": "Since 2002, South Africa’s police force has grown by 50%.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf": "neutral",
  "https://groundup.org.za/article/south-africas-police-shortage/": "neutral",
  "https://en.wikipedia.org/wiki/South_African_Police_Service": "neutral",
  "https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf": "neutral",
  "https://en.wikipedia.org/wiki/Crime_in_South_Africa": "neutral"
}
```

#### Pipeline Sources Output
1. **[PDF] south-african-police-service-annual-report-2024-2025.pdf**
   URL: https://www.gov.za/sites/default/files/gcis_document/202511/south-african-police-service-annual-report-2024-2025.pdf
   Stance: `neutral`

2. **How the size of South Africa’s police force compares to other countries | GroundUp**
   URL: https://groundup.org.za/article/south-africas-police-shortage/
   Stance: `neutral`

3. **South African Police Service - Wikipedia**
   URL: https://en.wikipedia.org/wiki/South_African_Police_Service
   Stance: `neutral`

4. **[PDF] South African Police Service Annual Report 2023/2024**
   URL: https://www.gov.za/sites/default/files/gcis_document/202411/sapsannual-report2023-24.pdf
   Stance: `neutral`

5. **Crime in South Africa - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Crime_in_South_Africa
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 4. AVeriTeC / av_010 - Refuted

#### Input
- **Claim:** UNESCO declared Nadar community as the most ancient race in the world.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** No provided source shows UNESCO declaring Nadars the world’s most ancient race.
- **Explanation:** None of the sources mention UNESCO making any declaration about the Nadar community being the most ancient race in the world. Source 2 discusses UNESCO’s stance against racial doctrines, but it does not connect UNESCO to any specific community or claim about “most ancient race.” Sources 1, 3, and 4 discuss Nadar history/beliefs and social status, but they do not attribute any such declaration to UNESCO.
- **Confidence reason:** Claim about UNESCO is not addressed in any source.
- **Claim verdicts:**
```json
[
  {
    "claim": "UNESCO declared the Nadar community as the most ancient race in the world.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://en.wikipedia.org/wiki/Nadar_(caste)": "neutral",
  "https://www.filosoficas.unam.mx/docs/608/files/4statementsRACE.pdf": "neutral",
  "https://nadars.in/en/nadar-mahajana-sangam/": "neutral",
  "https://www.sanrorhistoricalresearch.com/en/nadar-history-misconceptions/nadar-19th-century-history-misconception/": "neutral",
  "https://courier.unesco.org/en/articles/fallacies-racism-exposed-unesco-publishes-declaration-worlds-scientists": "neutral"
}
```

#### Pipeline Sources Output
1. **Nadar (caste) - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Nadar_(caste)
   Stance: `neutral`

2. **[PDF] Four statements on the race question; UNESCO and its programme**
   URL: https://www.filosoficas.unam.mx/docs/608/files/4statementsRACE.pdf
   Stance: `neutral`

3. **Nadar community | Nadar sangam | Nadars of Tamilnad**
   URL: https://nadars.in/en/nadar-mahajana-sangam/
   Stance: `neutral`

4. **The Actual Social Standing of the 19th-Century Nadars.**
   URL: https://www.sanrorhistoricalresearch.com/en/nadar-history-misconceptions/nadar-19th-century-history-misconception/
   Stance: `neutral`

5. **Fallacies of racism exposed: UNESCO publishes Declaration by world's scientists | The UNESCO Courier**
   URL: https://courier.unesco.org/en/articles/fallacies-racism-exposed-unesco-publishes-declaration-worlds-scientists
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 5. AVeriTeC / av_011 - Supported

#### Input
- **Claim:** Fact Check: WHO has not approved home remedy for COVID-19, don’t fall for misinformation
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `unverifiable`, expected one of `true, mostly_true`
- **TLDR:** Sources don’t state WHO’s approval status for home remedies.
- **Explanation:** None of the provided sources explicitly say that WHO has not approved home remedies for COVID-19. Source 5 discusses WHO-approved therapeutics generally, but it does not address “home remedies” or WHO’s approval status for them. Sources 1–4 focus on debunking specific purported remedies and discussing FDA-approved treatments, not WHO approval of home remedies.
- **Confidence reason:** No source directly addresses WHO approval of home remedies.
- **Claim verdicts:**
```json
[
  {
    "claim": "WHO has not approved home remedies for COVID-19.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://factcheck.afp.com/debunks-novel-coronavirus-prevention-cures-treatments": "neutral",
  "https://www.factcheck.org/covid-misconceptions/": "neutral",
  "https://www.factcheck.org/issue/covid-19-drugs/": "neutral",
  "https://www.factcheck.org/2021/07/scicheck-no-new-revelation-on-hydroxychloroquine-and-covid-19/": "neutral",
  "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/treatments": "neutral"
}
```

#### Pipeline Sources Output
1. **Debunks of novel coronavirus prevention, cures, treatments | Fact Check**
   URL: https://factcheck.afp.com/debunks-novel-coronavirus-prevention-cures-treatments
   Stance: `neutral`

2. **COVID-19 Misconceptions - FactCheck.org**
   URL: https://www.factcheck.org/covid-misconceptions/
   Stance: `neutral`

3. **COVID-19 drugs Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/covid-19-drugs/
   Stance: `neutral`

4. **No New Revelation on Hydroxychloroquine and COVID-19 - FactCheck.org**
   URL: https://www.factcheck.org/2021/07/scicheck-no-new-revelation-on-hydroxychloroquine-and-covid-19/
   Stance: `neutral`

5. **Treatments**
   URL: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/treatments
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 6. AVeriTeC / av_012 - Not Enough Evidence

#### Input
- **Claim:** Hunter Biden (son of US president Joe Biden)  had 25,000 pics of him torturing and raping children under 10 in China on his laptop.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `false`
- **Score:** `10`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources say there’s no evidence for those specific child-abuse pictures on Hunter Biden’s laptop.
- **Explanation:** PolitiFact (via dpaq.de) and FactCheck.org both state that the “25,000 pics” claim is baseless and provides no evidence. CBS News and the Wikipedia summary discuss the laptop containing many types of data and being genuine, but they do not provide any support for the specific allegation about torturing/raping children under 10 in China.
- **Confidence reason:** Multiple fact-checks explicitly deny evidence for the claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Hunter Biden had 25,000 pictures of him torturing and raping children under 10 in China on his laptop.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://dpaq.de/gXxW2": "contradicting",
  "https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/": "contradicting",
  "https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter": "neutral",
  "https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/": "neutral",
  "https://www.nbcnews.com/tech/tech-news/inside-campaign-pizzagate-hunter-biden-n1244331": "neutral"
}
```

#### Pipeline Sources Output
1. **Fact-checking unproven claims about Hunter Biden and child ...**
   URL: https://dpaq.de/gXxW2
   Stance: `contradicting`

2. **Social Media Posts Dredge Up Baseless 'Child Trafficking ...**
   URL: https://www.factcheck.org/2020/10/social-media-posts-dredge-up-baseless-child-trafficking-conspiracy-theory/
   Stance: `contradicting`

3. **Hunter Biden laptop letter - Wikipedia**
   URL: https://en.wikipedia.org/wiki/Hunter_Biden_laptop_letter
   Stance: `neutral`

4. **Copy of what's believed to be Hunter Biden's laptop data turned over ...**
   URL: https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/
   Stance: `neutral`

5. **Inside the campaign to 'pizzagate' Hunter Biden - NBC News**
   URL: https://www.nbcnews.com/tech/tech-news/inside-campaign-pizzagate-hunter-biden-n1244331
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 7. AVeriTeC / av_013 - Refuted

#### Input
- **Claim:** Dr. Ebeneezer, a medical doctor and a herbal practitioner at the Amuzu Hospital has instructed men to have sex at least 21 times a month to avoid prostate cancer.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `false, mostly_false`
- **TLDR:** The 21-times claim is supported by some medical sources, but the “Dr. Ebeneezer” details are unverified.
- **Explanation:** Source 1 and Source 6 both state that the viral claim attributes to Dr. Ebeneezer advice to have sex at least 21 times a month to avoid prostate cancer, but Source 1 is itself a fact-check saying the underlying study does not conclude a strict “21 times” rule. Medical sources (Sources 7, 10, 12, 13) report that higher ejaculation frequency (including 21+ times/month) is associated with lower prostate cancer risk, though they also note it’s not definitive causation. However, none of the provided sources independently verify that “Dr. Ebeneezer is a medical doctor and a herbal practitioner at Amuzu Hospital,” so that part remains unverified.
- **Confidence reason:** Key identity/employment details aren’t independently corroborated.
- **Claim verdicts:**
```json
[
  {
    "claim": "Dr. Ebeneezer is a medical doctor and a herbal practitioner at Amuzu Hospital.",
    "verdict": "unverifiable"
  },
  {
    "claim": "Dr. Ebeneezer instructed men to have sex at least 21 times a month.",
    "verdict": "supported"
  },
  {
    "claim": "Having sex at least 21 times a month helps men avoid prostate cancer.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://leadstories.com/hoax-alert/2020/10/fact-check-study-did-not-say-men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer.html": "contradicting",
  "https://www.cui.edu/uploadedfiles/academicprograms/globalprograms/study-abroad/ghana-humanities.pdf": "neutral",
  "https://www.uwindsor.ca/secretariat/sites/uwindsor.ca.secretariat/files/s250530p_-_combined_may_30_2025_senate_package_compressed2.pdf": "neutral",
  "https://documents1.worldbank.org/curated/en/099050923113537780/txt/P1800600a10ae90009f25075bb8a4f8cf8.txt": "neutral",
  "https://www.ug.edu.gh/sites/default/files/manual_uploads/CBAS%20handbook%202017.pdf": "neutral",
  "https://punchng.com/fact-check-does-having-sex-21-times-a-month-prevent-cancer-in-40-years-and-above-men/": "contradicting",
  "https://www.health.harvard.edu/mens-health/ejaculation_frequency_and_prostate_cancer": "supporting",
  "https://howwelove.com/whats-a-healthy-frequency-for-a-couple-to-have-sex/": "neutral"
}
```

#### Pipeline Sources Output
1. **Fact Check: Study Did NOT Say Men Must Have Sex At Least 21 Times A Month To Avoid Prostate Cancer | Lead Stories**
   URL: https://leadstories.com/hoax-alert/2020/10/fact-check-study-did-not-say-men-must-have-sex-at-least-21-times-a-month-to-avoid-prostate-cancer.html
   Stance: `contradicting`

2. **UNIVERSITY OF GHANA HANDBOOK FOR THE BACHELOR'S**
   URL: https://www.cui.edu/uploadedfiles/academicprograms/globalprograms/study-abroad/ghana-humanities.pdf
   Stance: `neutral`

3. **[PDF] NOTICE OF MEETING AGENDA - University of Windsor**
   URL: https://www.uwindsor.ca/secretariat/sites/uwindsor.ca.secretariat/files/s250530p_-_combined_may_30_2025_senate_package_compressed2.pdf
   Stance: `neutral`

4. **P1800600a10ae90009f25075bb... - Documents & Reports**
   URL: https://documents1.worldbank.org/curated/en/099050923113537780/txt/P1800600a10ae90009f25075bb8a4f8cf8.txt
   Stance: `neutral`

5. **[PDF] CBAS handbook 2017.pdf - University of Ghana**
   URL: https://www.ug.edu.gh/sites/default/files/manual_uploads/CBAS%20handbook%202017.pdf
   Stance: `neutral`

6. **FACT CHECK: Does having sex 21 times a month prevent cancer in 40 years and above men?**
   URL: https://punchng.com/fact-check-does-having-sex-21-times-a-month-prevent-cancer-in-40-years-and-above-men/
   Stance: `contradicting`

7. **Ejaculation frequency and prostate cancer - Harvard Health**
   URL: https://www.health.harvard.edu/mens-health/ejaculation_frequency_and_prostate_cancer
   Stance: `supporting`

8. **What’s A Healthy Frequency for A Couple to Have Sex? – How We Love**
   URL: https://howwelove.com/whats-a-healthy-frequency-for-a-couple-to-have-sex/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 8. AVeriTeC / av_016 - Not Enough Evidence

#### Input
- **Claim:** You see the number today? 33.1 GDP. The biggest in the history of our country by almost triple, right? Almost triple. Now it’s very much bigger than any GDP we’ve ever had. You have to go back to the 1950s, and then it’s less than half. This is the greatest number, 33.1 percent.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `25`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** The sources only support the 33.1% growth rate, not the GDP-level and “greatest” comparisons.
- **Explanation:** Sources 1 and 2 discuss a 33.1% GDP growth rate (annualized) for a quarter, but they do not support claims that “the number today is 33.1 GDP” as a GDP level. Multiple sources (CNN Business, FactCheck/PolitiFact) explicitly dispute “biggest/best/greatest” GDP-in-history style assertions, noting record growth followed record declines and that the economy remained below pre-pandemic levels. The remaining claims about “almost triple,” “bigger than any GDP ever,” and “half the current one goes back to the 1950s” are not substantiated by the provided sources.
- **Confidence reason:** Most claims are not directly addressed; only 33.1% growth is clearly supported.
- **Claim verdicts:**
```json
[
  {
    "claim": "The number today is 33.1 GDP.",
    "verdict": "contradicted"
  },
  {
    "claim": "The GDP is the biggest in the history of the country by almost triple.",
    "verdict": "contradicted"
  },
  {
    "claim": "The current GDP is very much bigger than any GDP the country has ever had.",
    "verdict": "contradicted"
  },
  {
    "claim": "To find a GDP less than half of the current one, you have to go back to the 1950s.",
    "verdict": "unverifiable"
  },
  {
    "claim": "The greatest number is 33.1 percent.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html": "supporting",
  "https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068": "supporting",
  "https://www.factcheck.org/issue/gdp/": "neutral",
  "https://www.factcheck.org/2026/04/trumps-numbers-april-2026-update/": "neutral",
  "https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-4th": "neutral",
  "https://www.cnn.com/2020/10/29/economy/gdp-report-trump-biggest-best-factcheck": "contradicting",
  "https://www.politifact.com/factchecks/2021/oct/08/facebook-posts/no-donald-trump-didnt-lead-greatest-economy-histor/": "contradicting",
  "https://www.visualcapitalist.com/ranked-the-worlds-top-economies-in-1980-vs-2025/": "neutral"
}
```

#### Pipeline Sources Output
1. **U.S. GDP booms at 33.1% rate in Q3 report, beating expectations**
   URL: https://www.cnbc.com/2020/10/29/us-gdp-report-third-quarter-2020.html
   Stance: `supporting`

2. **GDP rose at 33.1 percent annualized rate last quarter, but blowout figure is not what it seems**
   URL: https://www.nbcnews.com/business/economy/gdp-rose-33-1-percent-last-quarter-blowout-figure-not-n1245068
   Stance: `supporting`

3. **GDP Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/gdp/
   Stance: `neutral`

4. **Trump's Numbers, April 2026 Update - FactCheck.org**
   URL: https://www.factcheck.org/2026/04/trumps-numbers-april-2026-update/
   Stance: `neutral`

5. **GDP (Third Estimate), Industries, Corporate Profits, State GDP, and State Personal Income, 4th Quarter and Year 2025 | U.S. Bureau of Economic Analysis (BEA)**
   URL: https://www.bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-4th
   Stance: `neutral`

6. **GDP Report: Trump is taking credit for the ‘biggest and best’ GDP in American history. Here are the facts | CNN Business**
   URL: https://www.cnn.com/2020/10/29/economy/gdp-report-trump-biggest-best-factcheck
   Stance: `contradicting`

7. **PolitiFact | No, Donald Trump didn’t lead ‘greatest economy in the history of the world’**
   URL: https://www.politifact.com/factchecks/2021/oct/08/facebook-posts/no-donald-trump-didnt-lead-greatest-economy-histor/
   Stance: `contradicting`

8. **Ranked: The World's Top Economies in 1980 vs. 2025**
   URL: https://www.visualcapitalist.com/ranked-the-worlds-top-economies-in-1980-vs-2025/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 9. AVeriTeC / av_020 - Supported

#### Input
- **Claim:** Edo State in Nigeria has a 19% unemployment rate.
- **Expected label:** Supported
- **Expected verdicts:** `true, mostly_true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `true, mostly_true`
- **TLDR:** Dubawa reports Obaseki citing NBS for 19%, but other sources don’t verify Edo’s rate.
- **Explanation:** Source 1 (Dubawa) says Obaseki claimed Edo’s unemployment fell from 25% to about 19% and that this was “verifiable with” an NBS report, but the source excerpt does not provide the NBS figure itself. The other provided sources do not give Edo’s unemployment rate as 19%, so they neither confirm nor clearly contradict it.
- **Confidence reason:** Only one source mentions the 19% figure; NBS data not shown.
- **Claim verdicts:**
```json
[
  {
    "claim": "Edo State in Nigeria has a 19% unemployment rate.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/": "supporting",
  "https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf": "neutral",
  "https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/": "neutral",
  "https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria": "neutral",
  "https://www.nigerianstat.gov.ng/elibrary/read/929": "neutral"
}
```

#### Pipeline Sources Output
1. **Is Edo unemployment rate 19 percent as claimed by Obaseki? - Dubawa**
   URL: https://dubawa.org/is-edo-unemployment-rate-19-percent-as-claimed-by-obaseki/
   Stance: `supporting`

2. **[PDF] perception of edo residents towards unemployment**
   URL: https://repository.uniben.edu/sites/default/files/2026-03/PEU.pdf
   Stance: `neutral`

3. **How true are viral claims on Nigeria’s unemployment rate, extreme poverty and debt profile? | The ICIR- Latest News, Politics, Governance, Elections, Investigation, Factcheck, Covid-19**
   URL: https://www.icirnigeria.org/how-true-are-viral-claims-on-nigerias-unemployment-rate-extreme-poverty-and-debt-profile/
   Stance: `neutral`

4. **12 Unemployment Statistics in Nigeria for 2026 | MyJobMag**
   URL: https://www.myjobmag.com/blog/unemployment-statistics-in-nigeria
   Stance: `neutral`

5. **Reports | National Bureau of Statistics**
   URL: https://www.nigerianstat.gov.ng/elibrary/read/929
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 10. AVeriTeC / av_021 - Not Enough Evidence

#### Input
- **Claim:** Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.
- **Expected label:** Not Enough Evidence
- **Expected verdicts:** `unverifiable, mixed`
- **Expected score range:** `[30, 60]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `25`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_false`, expected one of `unverifiable, mixed`
- **TLDR:** TheCable’s calculations show Saudi petrol was more expensive than Nigeria’s, contradicting the claim.
- **Explanation:** Source 1 directly evaluates the “40% cheaper in Nigeria than in Saudi Arabia” claim and concludes it is an exaggeration, stating Saudi petrol was 17.78% (octane 95) and 11.16% (octane 91) more expensive than Nigeria after currency conversion. The other sources do not provide a 2020 Nigeria-vs-Saudi price comparison that would support the “not cheaper” framing; Source 3 only quotes a Buhari comparison without providing the underlying 2020 data.
- **Confidence reason:** Only one source directly addresses the Nigeria–Saudi price comparison with calculations.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fuel in Nigeria in 2020 was not cheaper than that in Saudi Arabia.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/": "supporting",
  "https://www.facebook.com/groups/599563341561133/posts/1445300556987403/": "neutral",
  "https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/": "neutral",
  "https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf": "neutral",
  "https://tradingeconomics.com/country-list/gasoline-prices": "neutral"
}
```

#### Pipeline Sources Output
1. **FACT CHECK: Is petrol 40% cheaper in Nigeria than in Saudi Arabia as claimed by Dangote? - TheCable Fact Check**
   URL: https://factcheck.thecable.ng/fact-check-is-petrol-40-cheaper-in-nigeria-than-in-saudi-arabia-as-claimed-by-dangote/
   Stance: `supporting`

2. **Fuel price comparison between Saudi Arabia and Nigeria - Facebook**
   URL: https://www.facebook.com/groups/599563341561133/posts/1445300556987403/
   Stance: `neutral`

3. **FG justifies fuel price comparison with Saudi Arabia, others | Multiplatform Digital Information Technology**
   URL: https://multiplatforms.net/fg-justifies-fuel-price-comparison-with-saudi-arabia-others/
   Stance: `neutral`

4. **[PDF] Fossil fuel subsidy swaps: A path towards accelerating the ...**
   URL: https://thedocs.worldbank.org/en/doc/73c7b24d6ec4770fbe71ab358d0e42bf-0280032025/original/Siham-Matallah-Paper-for-the-fourth-RRN-Conference.pdf
   Stance: `neutral`

5. **Gasoline Prices - Countries - List**
   URL: https://tradingeconomics.com/country-list/gasoline-prices
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 11. AVeriTeC / av_022 - Refuted

#### Input
- **Claim:** The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `false, mostly_false`
- **TLDR:** None of the sources provide evidence of a $600M Nigerian donation to Biden.
- **Explanation:** The Washington Examiner article discusses a $600 million unemployment-funds fraud involving Nigerian scammers, but it does not state that the Nigerian government donated $600 million to Joe Biden’s campaign. The other sources discuss other Nigeria-related political donations or U.S. assistance to Nigeria against Boko Haram, none of which mention a $600 million Nigerian government donation to Biden’s campaign.
- **Confidence reason:** No source directly addresses the specific donation claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "The Nigerian government is donating $600 million to Democratic presidential nominee Joe Biden’s campaign.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/": "neutral",
  "https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues": "neutral",
  "https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-": "neutral",
  "https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/": "neutral",
  "https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **Biden pick for unemployment program lost $600M to Nigerian scammers**
   URL: https://www.washingtonexaminer.com/news/2605899/biden-pick-for-unemployment-program-lost-600m-to-nigerian-scammers/
   Stance: `neutral`

2. **Trump wants to investigate Democrats' fundraising, but his own campaign has issues | PBS News**
   URL: https://www.pbs.org/newshour/politics/trump-wants-to-investigate-democrats-fundraising-but-his-own-campaign-has-issues
   Stance: `neutral`

3. **FACT SHEET: U.S. Efforts to Assist the Nigerian Government in its Fight against Boko Haram | whitehouse.gov**
   URL: https://obamawhitehouse.archives.gov/the-press-office/2014/10/14/fact-sheet-us-efforts-assist-nigerian-government-its-fight-against-boko-
   Stance: `neutral`

4. **KOCO 5 News**
   URL: https://www.facebook.com/koco5/posts/a-report-from-the-state-department-lists-tens-of-thousands-of-dollars-in-foreign/1320927866731289/
   Stance: `neutral`

5. **[PDF] Congress Must Stop Biden's Misuse of U.S. Foreign Aid to Impose ...**
   URL: https://www.congress.gov/118/meeting/house/116508/documents/HHRG-118-GO06-20231025-SD004.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 12. AVeriTeC / av_028 - Conflicting Evidence/Cherrypicking

#### Input
- **Claim:** U.S. President Donald Trump has suspended all travel from China.
- **Expected label:** Conflicting Evidence/Cherrypicking
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[25, 75]`

#### Output
- **Actual verdict:** `false`
- **Score:** `10`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `false`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources say Trump did not suspend all travel from China.
- **Explanation:** FactCheck.org and AP both state Trump’s restrictions were not a total ban: there were exceptions (e.g., Americans and their family members) and the restrictions were “porous.” FactCheck.org also notes the policy was incremental and not “closed up” all travel, contradicting the claim of suspending all travel from China.
- **Confidence reason:** Multiple sources directly contradict the “all travel” claim
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. President Donald Trump has suspended all travel from China.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.factcheck.org/2020/03/the-facts-on-trumps-travel-restrictions/": "contradicting",
  "https://www.factcheck.org/2020/04/trump-biden-spin-china-travel-restrictions/": "contradicting",
  "https://www.voanews.com/a/usa_ap-fact-check-trumps-perfect-china-ban-death-toll-myths/6189080.html": "contradicting",
  "https://www.factcheck.org/2020/04/trumps-snowballing-china-travel-claim/": "neutral",
  "https://apnews.com/article/asia-pacific-anthony-fauci-pandemics-politics-ap-fact-check-d227b34b168e576bf5068b92a03c003d": "contradicting"
}
```

#### Pipeline Sources Output
1. **The Facts on Trump's Travel Restrictions - FactCheck.org**
   URL: https://www.factcheck.org/2020/03/the-facts-on-trumps-travel-restrictions/
   Stance: `contradicting`

2. **Trump, Biden Spin China Travel Restrictions - FactCheck.org**
   URL: https://www.factcheck.org/2020/04/trump-biden-spin-china-travel-restrictions/
   Stance: `contradicting`

3. **AP Fact Check: Trump's Perfect China 'Ban,' Death Toll Myths**
   URL: https://www.voanews.com/a/usa_ap-fact-check-trumps-perfect-china-ban-death-toll-myths/6189080.html
   Stance: `contradicting`

4. **Trump's Snowballing China Travel Claim - FactCheck.org**
   URL: https://www.factcheck.org/2020/04/trumps-snowballing-china-travel-claim/
   Stance: `neutral`

5. **AP FACT CHECK: Trump and the virus-era China ban that isn't | AP News**
   URL: https://apnews.com/article/asia-pacific-anthony-fauci-pandemics-politics-ap-fact-check-d227b34b168e576bf5068b92a03c003d
   Stance: `contradicting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 13. AVeriTeC / av_029 - Refuted

#### Input
- **Claim:** Before the first case of the coronavirus spread within the United States, the president Donald Trump took unprecedented action and suspended all travel from China.
- **Expected label:** Refuted
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `55`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `false, mostly_false`
- **TLDR:** Trump did suspend entry from China early, but sources don’t support “unprecedented” or “all travel.”
- **Explanation:** Source 5 (the Jan. 31, 2020 proclamation) states the U.S. confirmed person-to-person spread in the U.S. and describes the proclamation issued on Jan. 31, 2020, which aligns with a suspension of entry for certain travelers from China effective Feb. 2 (as described by Source 3). However, Source 6 (FactCheck.org) says Trump’s decision was not “way ahead of anybody else” and that many other countries imposed restrictions before or on the same day, undermining the “unprecedented” framing. None of the provided sources clearly support that Trump suspended “all travel” from China; Source 6 explicitly notes there were exceptions and that Trump mischaracterized it as a complete travel ban.
- **Confidence reason:** Multiple sources address timing and scope, but not “all travel” fully.
- **Claim verdicts:**
```json
[
  {
    "claim": "Before the first case of coronavirus spread within the United States, President Donald Trump suspended all travel from China.",
    "verdict": "mixed"
  },
  {
    "claim": "President Donald Trump took unprecedented action by suspending all travel from China.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.factcheck.org/2020/03/the-facts-on-trumps-travel-restrictions/": "neutral",
  "https://www.factcheck.org/2020/04/trumps-snowballing-china-travel-claim/": "neutral",
  "https://www.snopes.com/fact-check/trump-ban-travel-china-pandemic/": "supporting",
  "https://www.statesman.com/story/news/politics/elections/2020/04/13/fact-check-was-trump-slow-to-halt-travel-from-china/1361149007/": "neutral",
  "https://trumpwhitehouse.archives.gov/presidential-actions/proclamation-suspension-entry-immigrants-nonimmigrants-persons-pose-risk-transmitting-2019-novel-coronavirus/": "supporting",
  "https://www.factcheck.org/2020/04/trump-biden-spin-china-travel-restrictions/": "contradicting"
}
```

#### Pipeline Sources Output
1. **The Facts on Trump's Travel Restrictions - FactCheck.org**
   URL: https://www.factcheck.org/2020/03/the-facts-on-trumps-travel-restrictions/
   Stance: `neutral`

2. **Trump's Snowballing China Travel Claim - FactCheck.org**
   URL: https://www.factcheck.org/2020/04/trumps-snowballing-china-travel-claim/
   Stance: `neutral`

3. **Did Trump Ban All Travel From China at the Start of the Pandemic? | Snopes.com**
   URL: https://www.snopes.com/fact-check/trump-ban-travel-china-pandemic/
   Stance: `supporting`

4. **Fact-check: Was Trump slow to halt travel from China?**
   URL: https://www.statesman.com/story/news/politics/elections/2020/04/13/fact-check-was-trump-slow-to-halt-travel-from-china/1361149007/
   Stance: `neutral`

5. **Proclamation on Suspension of Entry as Immigrants and ...**
   URL: https://trumpwhitehouse.archives.gov/presidential-actions/proclamation-suspension-entry-immigrants-nonimmigrants-persons-pose-risk-transmitting-2019-novel-coronavirus/
   Stance: `supporting`

6. **Trump, Biden Spin China Travel Restrictions - FactCheck.org**
   URL: https://www.factcheck.org/2020/04/trump-biden-spin-china-travel-restrictions/
   Stance: `contradicting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 14. PolitiFact / pf_003 - true

#### Input
- **Claim:** Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources indicate Hatch co-sponsored a 1993 Republican health bill with an individual mandate.
- **Explanation:** PolitiFact directly states that Hatch was the co-sponsor of a 1993 Republican-backed bill that included an individual mandate (Source 1). Fox News and The New Yorker also say the individual mandate appeared in 1993 bills supported/co-sponsored by Orrin Hatch (Sources 2 and 3). None of the provided sources contradict the claim; they only discuss related context about later opposition.
- **Confidence reason:** Multiple sources directly link Hatch to 1993 mandate bills.
- **Claim verdicts:**
```json
[
  {
    "claim": "Orrin Hatch co-sponsored a 1993 health care bill that had an individual mandate.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/": "supporting",
  "https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long": "supporting",
  "https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate": "supporting",
  "https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf": "neutral",
  "https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Hatch once supported an individual mandate, said Cenk Uygur**
   URL: https://www.politifact.com/factchecks/2011/feb/14/cenk-uygur/hatch-once-supported-individual-mandate-said-cenk-/
   Stance: `supporting`

2. **Individual health care insurance mandate has roots two decades long | Fox News**
   URL: https://www.foxnews.com/politics/individual-health-care-insurance-mandate-has-roots-two-decades-long
   Stance: `supporting`

3. **Unpopular Mandate | The New Yorker**
   URL: https://www.newyorker.com/magazine/2012/06/25/unpopular-mandate
   Stance: `supporting`

4. **[PDF] The New Bipartisan Consensus for an Individual Mandate**
   URL: https://www.urban.org/sites/default/files/publication/48741/2000163-The-New-Bipartisan-Consensus-for-an-Individual-Mandate.pdf
   Stance: `neutral`

5. **How Sen. Orrin Hatch Changed America's Health Care - KFF Health News**
   URL: https://kffhealthnews.org/news/how-sen-orrin-hatch-changed-americas-health-care/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 15. PolitiFact / pf_004 - barely-true

#### Input
- **Claim:** Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.
- **Expected label:** barely-true
- **Expected verdicts:** `mostly_false, mixed`
- **Expected score range:** `[20, 50]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mostly_false, mixed`
- **TLDR:** The sources don’t mention Mark Herring or any vote on shorter sentences for sex offenders.
- **Explanation:** None of the provided sources contain information about Mark Herring voting to allow sex offenders (including rapists) to serve shorter sentences. Source 1 discusses sex-offender recidivism and studies, Source 2 provides general data on sexual offending, Source 3 summarizes Canadian bail/sentencing reforms without any Mark Herring vote, and Source 4 is about exclusionary-rule costs referencing a case name “Herring” unrelated to a voting record. Source 5 concerns Washington State SSOSA-related recommendations and voting results, but it does not identify Mark Herring or the specific claim about shorter sentences for sex offenders.
- **Confidence reason:** No source addresses the specific person, vote, or sentencing change.
- **Claim verdicts:**
```json
[
  {
    "claim": "Mark Herring voted to allow sex offenders, including rapists, to serve shorter sentences.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf": "neutral",
  "https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf": "neutral",
  "https://openparliament.ca/bills/45-1/C-14/?singlepage=1": "neutral",
  "https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf": "neutral",
  "https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **[PDF] Recidivism: The Great Lie of “Frightening and High” - Regulations.gov**
   URL: https://downloads.regulations.gov/DOJ-OAG-2020-0003-0283/attachment_7.pdf
   Stance: `neutral`

2. **[PDF] Sex Offender Management Assessment and Planning Initiative**
   URL: https://smart.ojp.gov/sites/g/files/xyckuh231/files/media/document/somapi_full_report.pdf
   Stance: `neutral`

3. **Bill C-14 | openparliament.ca**
   URL: https://openparliament.ca/bills/45-1/C-14/?singlepage=1
   Stance: `neutral`

4. **[PDF] DISSENTING REPORT - Supreme Court of Ohio**
   URL: https://www.supremecourt.ohio.gov/docs/Boards/deathPenalty/resources/dissentingReport.pdf
   Stance: `neutral`

5. **[PDF] Recommendations for SSOSA reforms; treatment alternatives for ...**
   URL: https://app.leg.wa.gov/ReportsToTheLegislature/Home/GetPDF?fileName=House%20Public%20Safety%20Committee%20Report%20-%20SOPB%202022%20-%20Final%20with%20Appendices_ee0ad910-1df2-435a-ac75-8a03f5684f46.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 16. PolitiFact / pf_009 - true

#### Input
- **Claim:** The words subhuman mongrel, which Ted Nugent called President Barack Obama, were used by the Nazis to justify the genocide of the Jewish community.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources support that Nazis used “untermensch/subhuman” and “mongrel” language for dehumanization; Nugent used the phrase for Obama.
- **Explanation:** PolitiFact (Source 1) and the RealClearPolitics transcript of Blitzer’s CNN remarks (Source 2) state that Nazis used “untermenschen/subhuman mongrels” to describe Jews in the build-up to the Holocaust, supporting the genocide-justification framing. Sources 5 and 6 show Ted Nugent used the phrase “subhuman mongrel” to attack Obama, supporting the second claim. However, the provided sources do not independently verify the exact Nazi phrase “subhuman mongrel” in English or that it was specifically used as a direct justification phrase for genocide, so the support is strong but not airtight.
- **Confidence reason:** Multiple sources support key points, but exact phrasing/justification linkage not fully evidenced.
- **Claim verdicts:**
```json
[
  {
    "claim": "The words \"subhuman\" and \"mongrel\" were used by the Nazis to justify the genocide of the Jewish community.",
    "verdict": "supported"
  },
  {
    "claim": "Ted Nugent called President Barack Obama by the words \"subhuman\" and \"mongrel\".",
    "verdict": "supported"
  },
  {
    "claim": "The Nazis used the words \"subhuman\" and \"mongrel\" to justify the genocide of the Jewish community.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2014/feb/19/wolf-blitzer/wolf-blitzer-ted-nugent-used-nazi-terminology-subh/": "supporting",
  "https://www.realclearpolitics.com/video/2014/02/19/cnns_wolf_blitzer_takes_on_ted_nugent_for_using_term_subhuman_mongrel_to_attack_obama.html": "neutral",
  "https://kymkemp.com/2025/11/21/humboldt-county-jail-reports-daily-booking-sheet-november-21-2025/": "neutral",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC9645591/": "supporting",
  "https://www.yahoo.com/entertainment/ted-nugent-takes-credit-piers-morgan-cancelation-got-180626523.html": "supporting",
  "https://www.newyorker.com/news/amy-davidson/ted-nugents-subhuman-mongrel-slur-in-translation": "supporting",
  "https://www.washingtonpost.com/news/post-politics/wp/2014/03/07/perry-nugents-subhuman-mongrel-comment-wasnt-racist/": "neutral",
  "https://www.clarionledger.com/story/news/2014/02/21/rocker-ted-nugent-apologizes-for-obama-racial-remark/5703459/": "supporting"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Wolf Blitzer: Ted Nugent used Nazi terminology, 'subhuman mongrel,' to describe President Barack Obama**
   URL: https://www.politifact.com/factchecks/2014/feb/19/wolf-blitzer/wolf-blitzer-ted-nugent-used-nazi-terminology-subh/
   Stance: `supporting`

2. **CNN's Wolf Blitzer Takes On Ted Nugent For Using Term "Subhuman Mongrel" To Attack Obama | Video | RealClearPolitics**
   URL: https://www.realclearpolitics.com/video/2014/02/19/cnns_wolf_blitzer_takes_on_ted_nugent_for_using_term_subhuman_mongrel_to_attack_obama.html
   Stance: `neutral`

3. **Humboldt County Jail Reports: Daily Booking Sheet - November 21, 2025 - Redheaded Blackbelt**
   URL: https://kymkemp.com/2025/11/21/humboldt-county-jail-reports-daily-booking-sheet-november-21-2025/
   Stance: `neutral`

4. **Dehumanization and mass violence: A study of mental state language in Nazi propaganda (1927–1945) - PMC**
   URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9645591/
   Stance: `supporting`

5. **Ted Nugent Takes Credit For Piers Morgan’s Cancelation: I Got His ‘A– Thrown Out’ (Video)**
   URL: https://www.yahoo.com/entertainment/ted-nugent-takes-credit-piers-morgan-cancelation-got-180626523.html
   Stance: `supporting`

6. **Ted Nugent’s “Subhuman Mongrel” Slur, in Translation | The New Yorker**
   URL: https://www.newyorker.com/news/amy-davidson/ted-nugents-subhuman-mongrel-slur-in-translation
   Stance: `supporting`

7. **Perry: Nugent’s ‘subhuman mongrel’ comment wasn’t racist - The Washington Post**
   URL: https://www.washingtonpost.com/news/post-politics/wp/2014/03/07/perry-nugents-subhuman-mongrel-comment-wasnt-racist/
   Stance: `neutral`

8. **The Clarion-Ledger**
   URL: https://www.clarionledger.com/story/news/2014/02/21/rocker-ted-nugent-apologizes-for-obama-racial-remark/5703459/
   Stance: `supporting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 17. PolitiFact / pf_011 - true

#### Input
- **Claim:** Says Donald Trump has changed his mind on abortion.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** Sources show Trump’s abortion position has shifted, including moving away from a national ban.
- **Explanation:** Axios and Al Jazeera describe multiple changes in Trump’s abortion stance over time, including recent statements that abortion limits should be left to states rather than a national ban. FactCheck.org also characterizes this as a change from his 2016 support for a federal abortion ban, while ACLU similarly notes his public position shifts with political conditions. None of the sources directly deny that he has changed his mind; they mainly document the shifting nature of his views.
- **Confidence reason:** Multiple sources document shifts, but not a single definitive “changed his mind” moment.
- **Claim verdicts:**
```json
[
  {
    "claim": "Donald Trump has changed his mind on abortion.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.axios.com/2024/04/08/trump-abortion-ban-rights-legislation-timeline": "supporting",
  "https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed": "supporting",
  "https://www.aclu.org/trump-on-abortion": "supporting",
  "https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/": "supporting",
  "https://www.congress.gov/118/meeting/house/117301/documents/HHRG-118-FD00-20240515-SD001.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **Trump abortion timeline: Trump changes stance on national abortion rights**
   URL: https://www.axios.com/2024/04/08/trump-abortion-ban-rights-legislation-timeline
   Stance: `supporting`

2. **'Let states decide': How Donald Trump's position on abortion has ...**
   URL: https://www.aljazeera.com/news/2024/4/9/let-states-decide-how-donald-trumps-position-on-abortion-has-changed
   Stance: `supporting`

3. **Trump on Abortion | American Civil Liberties Union**
   URL: https://www.aclu.org/trump-on-abortion
   Stance: `supporting`

4. **Trump's 'Like It or Not' Comment and Harris' Response**
   URL: https://www.factcheck.org/2024/11/trumps-like-it-or-not-comment-and-harris-response/
   Stance: `supporting`

5. **[PDF] Fact-checking 32 of his false claims to Time | CNN Politics**
   URL: https://www.congress.gov/118/meeting/house/117301/documents/HHRG-118-FD00-20240515-SD001.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 18. PolitiFact / pf_012 - false

#### Input
- **Claim:** A new ruling by the EPA would force dairy farmers to comply with the Spill Prevention, Control and Countermeasure Program when dealing with spilt milk -- the same regulations oil and natural gas producers must follow.
- **Expected label:** false
- **Expected verdicts:** `false, mostly_false`
- **Expected score range:** `[0, 40]`

#### Output
- **Actual verdict:** `mixed`
- **Score:** `35`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mixed`, expected one of `false, mostly_false`
- **TLDR:** Sources conflict: milk spills were proposed to be covered, but EPA later exempted milk containers; oil/natural gas SPCC is supported.
- **Explanation:** For the first claim, Source 1 states the allegation that a new EPA ruling would force dairy farmers to comply with SPCC for spilled milk, but Source 2 says EPA testimony indicated dairy containers would be exempted, and Source 4 says EPA exempted milk and milk product containers from SPCC (while fuel oil/other applicable oils remain covered). For the second claim, multiple sources support that SPCC applies to oil facilities: Source 3 describes SPCC requirements for facilities storing/using significant quantities of oil and notes oil includes milk due to animal fat, and Source 7 and Source 8 describe SPCC obligations for farms/facilities storing oil or oil products; none contradict that oil/natural gas producers must follow SPCC.
- **Confidence reason:** Milk-related coverage is contradicted by later exemption sources; oil/natural gas coverage is broadly supported.
- **Claim verdicts:**
```json
[
  {
    "claim": "A new ruling by the EPA would force dairy farmers to comply with the Spill Prevention, Control and Countermeasure Program when dealing with spilt milk.",
    "verdict": "mixed"
  },
  {
    "claim": "Oil and natural gas producers must follow the Spill Prevention, Control and Countermeasure Program.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2011/mar/11/morgan-griffith/morgan-griffith-says-epa-treats-milk-spills-same-w/": "supporting",
  "https://green.blogs.nytimes.com/2011/03/12/spilled-milk-regulations-a-myth-e-p-a-says/": "contradicting",
  "https://www.klobuchar.senate.gov/public/index.cfm/amy-in-the-news?ID=4ADE358E-D981-457E-BB25-35C90E059579": "supporting",
  "https://www.farmprogress.com/management/dairy-containers-excluded-from-spcc-regulations-in-updated-ruling": "contradicting",
  "https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/fact-sheet-proposed-exemption-milk-containers": "neutral",
  "https://www.govinfo.gov/content/pkg/CHRG-109shrg42267/html/CHRG-109shrg42267.htm": "neutral",
  "https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/spill-prevention-control-and-countermeasure-fact": "supporting",
  "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-112": "supporting"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Morgan Griffith says EPA treats milk spills same way as oil spills**
   URL: https://www.politifact.com/factchecks/2011/mar/11/morgan-griffith/morgan-griffith-says-epa-treats-milk-spills-same-w/
   Stance: `supporting`

2. **Spilled Milk Regulations a Myth, E.P.A. Says - The New York Times**
   URL: https://green.blogs.nytimes.com/2011/03/12/spilled-milk-regulations-a-myth-e-p-a-says/
   Stance: `contradicting`

3. **Klobuchar calls for EPA Exemption for Dairy Farmers - Amy in the News - U.S. Senator Amy Klobuchar**
   URL: https://www.klobuchar.senate.gov/public/index.cfm/amy-in-the-news?ID=4ADE358E-D981-457E-BB25-35C90E059579
   Stance: `supporting`

4. **Dairy containers excluded from SPCC regulations in updated ruling | Farm Progress**
   URL: https://www.farmprogress.com/management/dairy-containers-excluded-from-spcc-regulations-in-updated-ruling
   Stance: `contradicting`

5. **Fact Sheet: Proposed Exemption for Milk Containers and Associated Piping and Appurtenances | US EPA**
   URL: https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/fact-sheet-proposed-exemption-milk-containers
   Stance: `neutral`

6. **- THE ENVIRONMENTAL PROTECTION AGENCY'S SPILL PREVENTION CONTROL AND COUNTERMEASURE PROGRAM**
   URL: https://www.govinfo.gov/content/pkg/CHRG-109shrg42267/html/CHRG-109shrg42267.htm
   Stance: `neutral`

7. **Spill Prevention, Control, and Countermeasure Fact Sheet for Farms**
   URL: https://www.epa.gov/oil-spills-prevention-and-preparedness-regulations/spill-prevention-control-and-countermeasure-fact
   Stance: `supporting`

8. **40 CFR Part 112 -- Oil Pollution Prevention - eCFR**
   URL: https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-112
   Stance: `supporting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 19. PolitiFact / pf_016 - half-true

#### Input
- **Claim:** John McCain "has threatened extinction for North Korea and sung songs about bombing Iran."
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `true`
- **Score:** `92`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `true`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources directly report McCain warning North Korea with “extinction” and jokingly singing “Bomb Iran.”
- **Explanation:** Multiple sources (Presstv, Legal Reader, and CBS News) report McCain said aggressive actions by North Korea would lead to the country’s “extinction.” Multiple sources (NPR, CBS News, CNN, and NBC News) report McCain joked and briefly sang “Bomb Iran” to the tune of a Beach Boys song during a campaign appearance.
- **Confidence reason:** Independent sources directly document both quoted remarks.
- **Claim verdicts:**
```json
[
  {
    "claim": "John McCain has threatened extinction for North Korea.",
    "verdict": "supported"
  },
  {
    "claim": "John McCain has sung songs about bombing Iran.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.presstv.ir/Detail/2017/09/10/534708/US-McCain-North-Korea-nuclear-war-cancer-Kim": "supporting",
  "https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction/": "supporting",
  "https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction": "supporting",
  "https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction/": "supporting",
  "https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction": "supporting",
  "https://www.npr.org/2007/04/20/9688222/jesting-mccain-sings-bomb-bomb-bomb-iran": "supporting",
  "https://www.cbsnews.com/news/iran-laughs-off-mccains-bomb-iran-song/": "supporting",
  "https://www.cnn.com/POLITICS/blogs/politicalticker/2007/04/mccain-sings-bomb-bomb-iran.html": "supporting"
}
```

#### Pipeline Sources Output
1. **McCain threatens North Korea with ‘extinction’**
   URL: https://www.presstv.ir/Detail/2017/09/10/534708/US-McCain-North-Korea-nuclear-war-cancer-Kim
   Stance: `supporting`

2. **Senator John McCain Says North Korea Nuclear Tests Could Lead to Its 'Extintion' - Legal Reader**
   URL: https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction/
   Stance: `supporting`

3. **Senator John McCain Says North Korea Nuclear Tests Could Lead to Its 'Extintion' - Legal Reader**
   URL: https://www.legalreader.com/senator-mccain-north-korea-nuclear-extinction
   Stance: `supporting`

4. **McCain to North Korea: aggression will lead to "extinction" - CBS News**
   URL: https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction/
   Stance: `supporting`

5. **McCain to North Korea: aggression will lead to "extinction" - CBS News**
   URL: https://www.cbsnews.com/news/mccain-to-north-korea-aggression-will-lead-to-extinction
   Stance: `supporting`

6. **Jesting, McCain Sings: 'Bomb, Bomb, Bomb' Iran : NPR**
   URL: https://www.npr.org/2007/04/20/9688222/jesting-mccain-sings-bomb-bomb-bomb-iran
   Stance: `supporting`

7. **Iran Laughs Off McCain's "Bomb Iran" Song - CBS News**
   URL: https://www.cbsnews.com/news/iran-laughs-off-mccains-bomb-iran-song/
   Stance: `supporting`

8. **CNN.com - CNN Political Ticker**
   URL: https://www.cnn.com/POLITICS/blogs/politicalticker/2007/04/mccain-sings-bomb-bomb-iran.html
   Stance: `supporting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 20. PolitiFact / pf_017 - true

#### Input
- **Claim:** In the last 10 years, Georgias middle class income has dropped $6,500.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `70`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact and SaportaReport both indicate Georgia’s middle-class/median income fell by about $6,500 over ~10 years.
- **Explanation:** Source 1 (PolitiFact) directly addresses the claim and states Carter’s ad is “true,” citing Census Bureau data and noting a $6,500, 10-year drop in household income. Source 2 (SaportaReport) also reports Census data showing Georgia’s median household income fell from $54,803 (2002) to $47,829 (2013) in inflation-adjusted terms, which is a decline of about $6,974—consistent with the $6,500 figure given the different endpoints.
- **Confidence reason:** Two sources support the direction and magnitude; endpoints differ slightly.
- **Claim verdicts:**
```json
[
  {
    "claim": "In the last 10 years, Georgia's middle class income has dropped $6,500.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/": "supporting",
  "https://saportareport.com/georgias-middle-class-disappearing-gsu-report-cant-say-went/columnists/david/": "supporting",
  "https://thecurrentga.org/2025/10/11/analysis-how-georgias-drop-in-per-capita-income-presaged-its-rural-demographic-collapse-part-2/": "neutral",
  "https://www.incomebyzipcode.com/georgia": "neutral",
  "https://abc45.com/news/nation-world/middle-income-families-struggle-as-living-costs-outpace-dropping-prices-budget-groceries-rent-finances-united-states-economy-fact-check-team": "neutral"
}
```

#### Pipeline Sources Output
1. **Carter claim about median household income on target**
   URL: https://www.politifact.com/factchecks/2014/sep/29/jason-carter/carter-claim-about-median-household-income-target/
   Stance: `supporting`

2. **Georgia’s middle class is disappearing; GSU report can’t say where it's going, or why - SaportaReport**
   URL: https://saportareport.com/georgias-middle-class-disappearing-gsu-report-cant-say-went/columnists/david/
   Stance: `supporting`

3. **Analysis: How Georgia’s drop in per capita income presaged its rural demographic collapse – Part 2 - The Current**
   URL: https://thecurrentga.org/2025/10/11/analysis-how-georgias-drop-in-per-capita-income-presaged-its-rural-demographic-collapse-part-2/
   Stance: `neutral`

4. **Georgia Income Statistics for 2026**
   URL: https://www.incomebyzipcode.com/georgia
   Stance: `neutral`

5. **Fact Check Team: Middle-income families struggle as living costs outpace dropping prices**
   URL: https://abc45.com/news/nation-world/middle-income-families-struggle-as-living-costs-outpace-dropping-prices-budget-groceries-rent-finances-united-states-economy-fact-check-team
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 21. PolitiFact / pf_018 - half-true

#### Input
- **Claim:** Oil production is down 14 percent this year on federal land.
- **Expected label:** half-true
- **Expected verdicts:** `mixed, mostly_true, mostly_false`
- **Expected score range:** `[35, 70]`

#### Output
- **Actual verdict:** `unverifiable`
- **Score:** `50`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `unverifiable`, expected one of `mixed, mostly_true, mostly_false`
- **TLDR:** Sources don’t provide the specific “down 14% on federal land” figure.
- **Explanation:** None of the provided sources state that oil production on federal land is down 14% this year. Source 5 (EIA) forecasts total U.S. crude production averaging 13.5 million b/d in 2026, about 100,000 b/d less than 2025, and mentions Federal Gulf of America increases offset by declines elsewhere, but it does not quantify a 14% federal-land drop. Source 1 discusses EIA STEO projections for Federal Gulf of America and other regions, yet still does not give a “14 percent” federal-land figure for “this year.”
- **Confidence reason:** No source mentions the 14% federal-land figure.
- **Claim verdicts:**
```json
[
  {
    "claim": "Oil production is down 14 percent this year on federal land.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/": "neutral",
  "https://www.factcheck.org/issue/oil-production/": "neutral",
  "https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/": "neutral",
  "https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/": "neutral",
  "https://www.eia.gov/todayinenergy/detail.php?id=66844": "neutral"
}
```

#### Pipeline Sources Output
1. **EIA Sees USA Crude Oil Production Dropping in 2026, 2027 | Rigzone**
   URL: https://www.rigzone.com/news/eia_sees_usa_crude_oil_production_dropping_in_2026_2027-21-jan-2026-182820-article/
   Stance: `neutral`

2. **oil production Archives - FactCheck.org**
   URL: https://www.factcheck.org/issue/oil-production/
   Stance: `neutral`

3. **EIA sees 2026 oil production decline despite regional growth EIA sees 2026 oil production decline despite regional growth**
   URL: https://energy-oil-gas.com/news/eia-sees-2026-oil-production-decline-despite-regional-growth/
   Stance: `neutral`

4. **U.S. energy agency forecasts a modest dip in domestic crude production in 2026**
   URL: https://energiesmedia.com/us-energy-modest-dip-in-domestic-crude/
   Stance: `neutral`

5. **EIA forecasts U.S. crude oil production will decrease slightly in 2026 - U.S. Energy Information Administration (EIA)**
   URL: https://www.eia.gov/todayinenergy/detail.php?id=66844
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 22. PolitiFact / pf_020 - pants-fire

#### Input
- **Claim:** U.S. Rep. Jim Langevin didn't want a border fence to block illegal immigration "because he is afraid that someone will get hurt trying to go around the fence."
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `70`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false`
- **TLDR:** Sources support Langevin opposing a border fence and citing fear someone would get hurt.
- **Explanation:** PolitiFact reports that Michael J. Gardiner said Langevin opposed the U.S.-Mexican border fence because he was afraid someone would get hurt trying to go around it (Source 1). PolitiFact also indicates Langevin voted against the fence resolution, aligning with the claim that he opposed a border fence to block illegal immigration (Source 1). The OnTheIssues page states Langevin voted NO on building a fence along the Mexican border, supporting the opposition aspect but not the specific “afraid someone would get hurt” rationale (Source 2).
- **Confidence reason:** Opposition is supported by two sources; the specific fear rationale appears only in one.
- **Claim verdicts:**
```json
[
  {
    "claim": "U.S. Rep. Jim Langevin opposed a border fence to block illegal immigration.",
    "verdict": "supported"
  },
  {
    "claim": "Jim Langevin said he opposed the border fence because he was afraid someone would get hurt trying to go around it.",
    "verdict": "supported"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/": "supporting",
  "https://www.ontheissues.org/house/James_Langevin_Immigration.htm": "supporting",
  "https://www.congress.gov/109/crec/2005/02/15/CREC-2005-02-15-pt1-PgE247.pdf": "neutral",
  "https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm": "neutral",
  "https://www.politifact.com/factchecks/list/?category=immigration&ruling=barely-true": "neutral",
  "https://democrats-armedservices.house.gov/2018/11/smith-house-democrats-demand-answers-on-trump-border-deployment": "neutral",
  "https://nctr.ca/wp-content/uploads/2021/01/Volume_1_History_Part_1_English_Web.pdf": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Gardiner says Langevin opposed U.S.-Mexican border fence for fear someone will get hurt**
   URL: https://www.politifact.com/factchecks/2010/jun/25/michael-j-gardiner/gardiner-says-langevin-opposed-us-mexican-border-f/
   Stance: `supporting`

2. **James Langevin on Immigration**
   URL: https://www.ontheissues.org/house/James_Langevin_Immigration.htm
   Stance: `supporting`

3. **[PDF] CONGRESSIONAL RECORD— Extensions of ... - Congress.gov**
   URL: https://www.congress.gov/109/crec/2005/02/15/CREC-2005-02-15-pt1-PgE247.pdf
   Stance: `neutral`

4. **CONSTRUCTION OPTIONS AND STRATEGIC PLACEMENT**
   URL: https://www.govinfo.gov/content/pkg/CHRG-109hhrg41325/html/CHRG-109hhrg41325.htm
   Stance: `neutral`

5. **Fact-checks | PolitiFact**
   URL: https://www.politifact.com/factchecks/list/?category=immigration&ruling=barely-true
   Stance: `neutral`

6. **Smith, House Democrats Demand Answers on Trump Border Deployment - Press Releases - House Armed Services Committee - Democrats**
   URL: https://democrats-armedservices.house.gov/2018/11/smith-house-democrats-demand-answers-on-trump-border-deployment
   Stance: `neutral`

7. **[PDF] T he H istory, Part 1**
   URL: https://nctr.ca/wp-content/uploads/2021/01/Volume_1_History_Part_1_English_Web.pdf
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 23. PolitiFact / pf_022 - mostly-true

#### Input
- **Claim:** Says a company that got tax breaks from the state later laid off 100 Ohioans, even as its CEO cut a half-million-dollar check to Kasichs super PAC.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `35`
- **Confidence:** `low`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `mostly_true, true`
- **TLDR:** Sources don’t substantiate the specific layoffs and CEO check; only general incentive-noncompliance is supported.
- **Explanation:** Source 6 (PolitiFact) evaluates the exact combined statement and rates it “mostly-true,” but the provided excerpt does not include the underlying evidence for the “laid off 100 Ohioans” or the “half-million-dollar check” details. Sources 1, 2, 4, and 3 discuss Ohio job-creation tax credits/incentives failing to meet job or payroll benchmarks, but they do not identify the specific company, the “100 Ohioans” figure, or any CEO check to Kasich’s super PAC. Source 7 is only a list page and does not provide additional substantiation in the provided text; Sources 8–10 discuss Kasich super PAC fundraising generally, not the specific CEO check tied to the tax-break company.
- **Confidence reason:** Key specifics (company identity, 100 layoffs, $500k check) aren’t evidenced in provided excerpts.
- **Claim verdicts:**
```json
[
  {
    "claim": "A company that got tax breaks from the state later laid off 100 Ohioans.",
    "verdict": "unverifiable"
  },
  {
    "claim": "The CEO of that company cut a half-million-dollar check to Kasichs super PAC.",
    "verdict": "unverifiable"
  }
]
```
- **Source stances:**
```json
{
  "https://signalohio.org/most-job-creation-tax-credits-failed-to-create-ohio-jobs-as-promised-audit-says/": "neutral",
  "https://www.dispatch.com/story/business/employment/2025/12/04/ohio-business-loans-tax-breaks-jobs-report/87605321007/": "neutral",
  "https://www.bricker.com/DevelopOhio/After-receiving-a-tax-credit-to-create-85-new-jobs-in-Wilmington-TimberTech-eliminates-58-jobs-with-the-closing-of-its-Columbus-factory": "neutral",
  "https://www.statenews.org/government-politics/2026-01-13/nearly-two-thirds-of-companies-that-got-incentives-from-ohio-didnt-deliver-on-jobs-pay": "neutral",
  "https://ohiocapitaljournal.com/2025/12/03/hardworking-ohio-auto-workers-are-paying-the-price-for-ev-tax-credit-rollback/": "neutral",
  "https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/": "supporting",
  "https://www.politifact.com/factchecks/list/?target=john-kasich": "neutral",
  "https://www.dispatch.com/story/news/politics/2015/07/30/john-kasich-s-donor-list/24175365007/": "neutral"
}
```

#### Pipeline Sources Output
1. **State tax credits failed to create promised Ohio jobs, audit says**
   URL: https://signalohio.org/most-job-creation-tax-credits-failed-to-create-ohio-jobs-as-promised-audit-says/
   Stance: `neutral`

2. **Ohio gave business loans, tax breaks to create jobs. 65% didn't comply**
   URL: https://www.dispatch.com/story/business/employment/2025/12/04/ohio-business-loans-tax-breaks-jobs-report/87605321007/
   Stance: `neutral`

3. **After receiving a tax credit to create 85 new jobs in Wilmington, TimberTech eliminates 58 jobs with the closing of its Columbus factory**
   URL: https://www.bricker.com/DevelopOhio/After-receiving-a-tax-credit-to-create-85-new-jobs-in-Wilmington-TimberTech-eliminates-58-jobs-with-the-closing-of-its-Columbus-factory
   Stance: `neutral`

4. **Nearly two-thirds of companies that got incentives from Ohio didn't deliver on jobs, pay | The Statehouse News Bureau**
   URL: https://www.statenews.org/government-politics/2026-01-13/nearly-two-thirds-of-companies-that-got-incentives-from-ohio-didnt-deliver-on-jobs-pay
   Stance: `neutral`

5. **Hardworking Ohio auto workers are paying the price for EV tax credit rollback • Ohio Capital Journal**
   URL: https://ohiocapitaljournal.com/2025/12/03/hardworking-ohio-auto-workers-are-paying-the-price-for-ev-tax-credit-rollback/
   Stance: `neutral`

6. **PolitiFact | Ted Cruz ad revisits a controversy from Kasich’s governorship of Ohio**
   URL: https://www.politifact.com/factchecks/2016/apr/12/ted-cruz/ted-cruz-ad-revisits-controversy-kasichs-governors/
   Stance: `supporting`

7. **Fact-checks | PolitiFact**
   URL: https://www.politifact.com/factchecks/list/?target=john-kasich
   Stance: `neutral`

8. **John Kasich's donor list has Ohio all over it**
   URL: https://www.dispatch.com/story/news/politics/2015/07/30/john-kasich-s-donor-list/24175365007/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 24. PolitiFact / pf_025 - mostly-true

#### Input
- **Claim:** Federal spending on entitlements is projected to consume all revenue by 2045.
- **Expected label:** mostly-true
- **Expected verdicts:** `mostly_true, true`
- **Expected score range:** `[60, 100]`

#### Output
- **Actual verdict:** `mostly_false`
- **Score:** `20`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_false`, expected one of `mostly_true, true`
- **TLDR:** PolitiFact says CBO projections do not support entitlements consuming all federal revenue by 2045.
- **Explanation:** Source 1 (PolitiFact) directly evaluates the “consume all federal revenue by 2045” claim and concludes that using CBO’s current-law projections, entitlements would not consume every revenue dollar by 2045. While Source 2 and Source 3 discuss rising entitlement spending and crowding out other spending, they do not state that entitlements consume all revenue by 2045.
- **Confidence reason:** One source directly tests the exact 2045 “all revenue” claim.
- **Claim verdicts:**
```json
[
  {
    "claim": "Federal spending on entitlements is projected to consume all revenue by 2045.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/": "contradicting",
  "https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html": "neutral",
  "https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf": "neutral",
  "https://www.crfb.org/papers/explaining-federal-spending-and-revenue": "neutral",
  "https://budgetmodel.wharton.upenn.edu/t/Entitlements/": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Ohio Treasurer Josh Mandel says entitlement spending expected to consume all federal revenue by 2045**
   URL: https://www.politifact.com/factchecks/2013/feb/21/josh-mandel/ohio-treasurer-josh-mandel-says-entitlement-spendi/
   Stance: `contradicting`

2. **Fiscal Challenges: Health Care, Taxes and Beyond**
   URL: https://georgewbush-whitehouse.archives.gov/cea/cea-fc-20051201.html
   Stance: `neutral`

3. **[PDF] Demographic Headwinds - Aspen Economic Strategy Group**
   URL: https://www.economicstrategygroup.org/wp-content/uploads/2026/02/Dettling-Pardue-Low-Fertility-and-Fiscal-Sustainability.pdf
   Stance: `neutral`

4. **Explaining Federal Spending and Revenue-Wed, 05/21/2025 - 12:00 | Committee for a Responsible Federal Budget**
   URL: https://www.crfb.org/papers/explaining-federal-spending-and-revenue
   Stance: `neutral`

5. **Entitlements | Penn Wharton Budget Model**
   URL: https://budgetmodel.wharton.upenn.edu/t/Entitlements/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 25. PolitiFact / pf_027 - pants-fire

#### Input
- **Claim:** Fox News is banned in Canada because it violatesa law thatprevents news channels from lying to their viewers.
- **Expected label:** pants-fire
- **Expected verdicts:** `false`
- **Expected score range:** `[0, 20]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `90`
- **Confidence:** `high`
- **Correct:** `False`
- **Within one level:** `False`
- **Failure reason:** verdict got `mostly_true`, expected one of `false`
- **TLDR:** Sources say Fox News is not banned in Canada; the “lying law” reason is false.
- **Explanation:** Multiple sources (AP, Snopes, PolitiFact, and the Canadian fact-check) state Fox News is authorized/available in Canada, contradicting the claim that it is banned. PolitiFact and Snopes also specifically reject the explanation that a law preventing news channels from lying is the reason for any supposed ban.
- **Confidence reason:** Multiple independent fact-checkers directly address both parts of the claims.
- **Claim verdicts:**
```json
[
  {
    "claim": "Fox News is banned in Canada.",
    "verdict": "contradicted"
  },
  {
    "claim": "Fox News is banned in Canada because it violates a law that prevents news channels from lying to their viewers.",
    "verdict": "contradicted"
  }
]
```
- **Source stances:**
```json
{
  "https://www.thecanadianpressnews.ca/fact_checking/fox-news-isnt-banned-in-canada-despite-viral-posts-claiming-otherwise-but-it-could-be/article_3566ffe6-45a5-54bf-981a-51f72ba0eada.html": "contradicting",
  "https://www.berkshireeagle.com/ap/factcheck/not-real-news-fox-news-is-not-banned-in-canada-or-the-uk/article_7179bb60-5f74-11ec-81aa-8b5e01f382b8.html": "contradicting",
  "https://www.snopes.com/fact-check/canadian-fox/": "contradicting",
  "https://apnews.com/article/fact-checking-340810040961": "contradicting",
  "https://www.politifact.com/factchecks/2014/jul/14/facebook-posts/fox-news-banned-canada/": "contradicting",
  "https://factcheck.afp.com/fox-news-available-canada": "contradicting"
}
```

#### Pipeline Sources Output
1. **Fox News isn't banned in Canada, despite viral posts claiming otherwise – but it could be | Fact Checking | thecanadianpressnews.ca**
   URL: https://www.thecanadianpressnews.ca/fact_checking/fox-news-isnt-banned-in-canada-despite-viral-posts-claiming-otherwise-but-it-could-be/article_3566ffe6-45a5-54bf-981a-51f72ba0eada.html
   Stance: `contradicting`

2. **Not Real News: Fox News is not banned in Canada or the UK | Factcheck | The Berkshire Eagle**
   URL: https://www.berkshireeagle.com/ap/factcheck/not-real-news-fox-news-is-not-banned-in-canada-or-the-uk/article_7179bb60-5f74-11ec-81aa-8b5e01f382b8.html
   Stance: `contradicting`

3. **Was the Fox News Channel Banned in Canada? | Snopes.com**
   URL: https://www.snopes.com/fact-check/canadian-fox/
   Stance: `contradicting`

4. **Fox News is not banned in Canada or the UK | AP News**
   URL: https://apnews.com/article/fact-checking-340810040961
   Stance: `contradicting`

5. **PolitiFact | Is Fox News banned in Canada?**
   URL: https://www.politifact.com/factchecks/2014/jul/14/facebook-posts/fox-news-banned-canada/
   Stance: `contradicting`

6. **Fox News is available in Canada | Fact Check**
   URL: https://factcheck.afp.com/fox-news-available-canada
   Stance: `contradicting`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:

### 26. PolitiFact / pf_030 - true

#### Input
- **Claim:** Today California is kicking our butt, creating more jobs and more economic growth than Texas.
- **Expected label:** true
- **Expected verdicts:** `true`
- **Expected score range:** `[80, 100]`

#### Output
- **Actual verdict:** `mostly_true`
- **Score:** `78`
- **Confidence:** `medium`
- **Correct:** `False`
- **Within one level:** `True`
- **Failure reason:** verdict got `mostly_true`, expected one of `true`
- **TLDR:** PolitiFact’s data supports California outpacing Texas on jobs and growth, contradicting the “kicking our butt” framing.
- **Explanation:** Source 1 directly evaluates the June 2016 claim that “Today, California is kicking our butt, creating more jobs and more economic growth than Texas,” and rates it True, citing higher job growth in California than Texas. Source 2 also reports the same “kicking our butt” claim and includes supporting comparisons (jobs/income/GDP metrics) consistent with California doing better than Texas. Sources 3-5 are not directly tied to the “today” jobs/growth comparison in the provided PolitiFact fact-check context, and Source 6-10 are unrelated to the claims.
- **Confidence reason:** Only PolitiFact sources directly address the exact “today” jobs/growth comparison; other sources are tangential or unrelated.
- **Claim verdicts:**
```json
[
  {
    "claim": "Today California is creating more jobs and more economic growth than Texas.",
    "verdict": "supported"
  },
  {
    "claim": "Today California is kicking our butt.",
    "verdict": "mixed"
  }
]
```
- **Source stances:**
```json
{
  "https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/": "supporting",
  "https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/": "supporting",
  "https://businessintexas.com/blog/texas-vs-california-economy-which-state-is-best-for-business/": "neutral",
  "https://statspanda.com/blog/texas-vs-california-comparison": "neutral",
  "https://www.linkedin.com/posts/txedc_when-you-look-at-the-data-one-thing-becomes-activity-7424100550503493632-jZS0": "neutral",
  "https://www.usatoday.com/story/news/factcheck/2020/10/02/fact-check-clint-eastwood-did-not-author-pro-trumps-post/5885225002/": "neutral",
  "https://www.factcheck.org/": "neutral",
  "https://www.instagram.com/p/DTElWYDCQVS/": "neutral"
}
```

#### Pipeline Sources Output
1. **PolitiFact | Is California's economy 'growing a hell of a lot faster' than Texas?**
   URL: https://www.politifact.com/factchecks/2016/dec/19/jerry-brown/are-jobs-california-growing-hell-lot-faster-texas/
   Stance: `supporting`

2. **PolitiFact | Julián Castro says California besting Texas in creating jobs, economic growth**
   URL: https://www.politifact.com/factchecks/2016/aug/17/julian-castro/julian-castro-says-california-besting-texas-creati/
   Stance: `supporting`

3. **Texas vs. California Economy: Which State is Best for Business? | TxEDC**
   URL: https://businessintexas.com/blog/texas-vs-california-economy-which-state-is-best-for-business/
   Stance: `neutral`

4. **Texas vs California: America's Two Largest State Economies Compared by the Data | StatsPanda Blog | StatsPanda**
   URL: https://statspanda.com/blog/texas-vs-california-comparison
   Stance: `neutral`

5. **Texas Outpaces California in Job Growth and Unemployment Rate | Texas Economic Development Corporation posted on the topic | LinkedIn**
   URL: https://www.linkedin.com/posts/txedc_when-you-look-at-the-data-one-thing-becomes-activity-7424100550503493632-jZS0
   Stance: `neutral`

6. **Fact check: Clint Eastwood did not author pro-Trump social media post**
   URL: https://www.usatoday.com/story/news/factcheck/2020/10/02/fact-check-clint-eastwood-did-not-author-pro-trumps-post/5885225002/
   Stance: `neutral`

7. **FactCheck.org - A Project of The Annenberg Public Policy Center**
   URL: https://www.factcheck.org/
   Stance: `neutral`

8. **Instagram**
   URL: https://www.instagram.com/p/DTElWYDCQVS/
   Stance: `neutral`

#### Human Review Notes
- Evidence sufficient? yes / no / unclear
- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other
- Notes:
